from rgb import RGBThread
from ui import make_rgb_view

def exit_handler():
    print("exit handler called")
    rgb_thread.stop()
    ir_thread.stop()

    rgb_thread.join()
    ir_thread.join()

    cv2.destroyAllWindows()

def setup_display(display_addr):
    if os.environ.get("DISPLAY") is None:
        os.environ["DISPLAY"] = display_addr
    elif X_DISPLAY_ADDR:
        print("INFO: Using $DISPLAY from environment, not from config")

    cv2.namedWindow(VIS_WIN_NAME)
    cv2.namedWindow(IR_WIN_NAME)
    cv2.moveWindow(VIS_WIN_NAME, 0, 0)  # move RGB window to upper-left corner
    cv2.moveWindow(IR_WIN_NAME, IR_WIN_SIZE[0], 0)  # Align windows side by side
    print((IR_WIN_SIZE[0], 0))

    # @button press
    # start video recording
    # extra: write to screen "face detected" - if this is available in pyVHR
    # while (button is not pressed again):
	    # record 5s video
	    # feed the video to pyVHR
	    # show the result to screen


def mainloop():

    for i in itertools.count(start=0, step=1):

        time_start = time.monotonic()

        scores, boxes, landms = rgb_thread.get_detections()

        # only keep detections with confidence above 50%
        scores = np.array(scores)
        boxes = np.array(boxes)
        landms = np.array(landms)

        keep = scores > 0.5

        scores = scores[keep]
        boxes = boxes[keep]
        landms = landms[keep]

        boxes_ir = transform_boxes(boxes, 1.1, 1.1, 0, 0)

        if CALIBRATE:
            temp_arr, drift = calibration(temp_arr) 

        temps = get_bb_temps(temp_arr, boxes_ir)

        # Render UI views
        ir_view = make_ir_view(
            temp_arr,
            scores,
            boxes_ir,
            len(scores) * [None],  # don't feed landmarks
            # TODO: revisit this when we have improved homography-based transform
            temps,
            CALIB_BOX,
            IR_WIN_SIZE,
            CMAP_TEMP_MIN,
            CMAP_TEMP_MAX,
        )
        rgb_view = make_rgb_view(rgb_arr, scores, boxes, landms, VIS_WIN_SIZE)

        # Show rendered UI
        if SHOW_DISPLAY:
            cv2.imshow(VIS_WIN_NAME, rgb_view)
            cv2.imshow(IR_WIN_NAME, ir_view)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed in the cv2 window, we break from the loop and exit the program
            if key == ord("q"):
                break

        # Save images to filesystem
        if SAVE_FRAMES:
            if executor._work_queue.qsize() > MAX_FILE_QUEUE:
                print(
                    "Error: Too many files in file queue. Not saving frames from this iteration."
                )
            else:
                # TODO: catch writing errors due to full SD card
                # For examlple: libpng error: Write Error
                # The ret value of imwrite can be obtained from:
                # future = executor.submit(...)
                # future.result()

                # OPTIMIZE: we're saving frames with main loop frequency (up to 20Hz)
                # It would be more efficient to check if the frames changed between
                # iterations
                executor.submit(
                    cv2.imwrite,
                    f"{LOG_DIR}/frames/{session_id}-{i:05d}-rgb.jpg",
                    rgb_view,
                )
                executor.submit(
                    cv2.imwrite,
                    f"{LOG_DIR}/frames/{session_id}-{i:05d}-ir.png",
                    ir_view,
                )

        main_latency = time.monotonic() - time_start

        # Quick f-string format specifiers reference:
        # f'{value:{width}.{precision}}'
        print(
            f"INFO: Thread latencies   "
            f"Main={1000*main_latency:6.2f}ms   "
            f"RGB={rgb_thread._delay:6.2f}ms   "
            f"IR={ir_thread.latency:6.2f}ms"
        )

        time.sleep(max(0, 1 / HZ_CAP - main_latency))


if __name__ == "__main__":

    session_id = int(time.time())
    # For an unique id: session_id = uuid.uuid4()

    rgb_thread = RGBThread(model=FACE_DET_MODEL)
    rgb_thread.start()

    ir_thread = IRThread()
    ir_thread.start()

    if not CALIBRATE:
        CALIB_BOX = None

    if SAVE_FRAMES:
        executor = ThreadPoolExecutor(max_workers=4)

    if SHOW_DISPLAY:
        setup_display(X_DISPLAY_ADDR)

    while rgb_thread.frame is None:
        print("Waiting for RGB frames")
        time.sleep(1)

    while ir_thread.temps is None:
        print("Waiting for IR frames")
        time.sleep(1)

    try:
        mainloop()

    finally:
        exit_handler()
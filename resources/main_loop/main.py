# import RGBThread, make_rgb_view
import cv2, os
import RPi.GPIO as GPIO

def gstreamer_pipeline(
    camera_id=0,
    capture_width=3264,
    capture_height=2464,
    out_width=1024,
    out_height=768,
    framerate=10,
    flip_method=0,
):

    gst_string = f"""
    nvarguscamerasrc sensor_id={camera_id} ! 
    video/x-raw(memory:NVMM),
    width=(int){capture_width}, height=(int){capture_height},
    format=(string)NV12, framerate=(fraction){framerate}/1 !
    nvvidconv flip-method={flip_method} !
    video/x-raw, width=(int){out_width}, height=(int){out_height}, format=(string)BGRx !
    videoconvert !
    video/x-raw, format=(string)BGR !
    appsink max-buffers=1 drop=true
    """

    return gst_string



def record_video(camera_id, duration):

    gst_string = gstreamer_pipeline(
        camera_id=camera_id,
        framerate=30,
        flip_method=2,
    )

    capture = cv2.VideoCapture(gst_string, cv2.CAP_GSTREAMER)
    video_save = cv2.VideoWriter('videos/pulse5s.mp4', cv2.VideoWriter_fourcc(*'mp4v'), gstreamer_pipeline.framerate,(gstreamer_pipeline.out_width, gstreamer_pipeline.out_height))

    for frame_n in range(0, duration * gstreamer_pipeline.framerate):
        ret, frame = capture.read()
        cv2.imshow(str(frame_n), frame)
        video_save.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break
    capture.release()
    video_save.release()
    cv2.destroyAllWindows()


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


HZ_CAP = 20
LOG_DIR = "logs"
VIS_WIN_NAME = "RGB view"

VIS_BBOX_COLOR = (0, 0, 255)  # red
IR_BBOX_COLOR = (0, 255, 0)  # green

IR_WIN_SIZE = (960, 720)  # splits 1080p screen in half
VIS_WIN_SIZE = (960, 720)

SAVE_FRAMES = True
SHOW_DISPLAY = True
MAX_FILE_QUEUE = 10

X_DISPLAY_ADDR = ":0"

FACE_DET_MODEL = "retinaface"  # alternatively SSD

CALIBRATE = False # We default to false. Otherwise very large errors for users who deploy without a BB reference.
CALIB_T = 40 # temperature to which the blackbody reference is set to
CALIB_BOX = [8/160, 106/120, 20/160, 115/120]

CMAP_TEMP_MIN = 30
CMAP_TEMP_MAX = 40

    # on/of button press --> enter the loop of waiting for measurement button press
    # @button press
    # start video recording
    # extra: write to screen "face detected" - if this is available in pyVHR
    # while (button is not pressed again):
	    # record 5s video
	    # feed the video to pyVHR
	    # show the result to screen


def mainloop():

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15, GPIO.IN)
	button_state_old = 0
	while():
		# value is 1 when the butoon is idle
		button_state_upd = GPIO.input(15)

		# value is 0 when the button is pressed
		# enter the video recording/inference state when the button is pressed and exit the loop
		if (button_state_upd == 0 and button_state_old == 1) 
            # rgb_view = make_rgb_view(VIS_WIN_SIZE)
            # if SHOW_DISPLAY:
            #     cv2.imshow(VIS_WIN_NAME, rgb_view)
            #     # cv2.imshow(IR_WIN_NAME, ir_view)
            #     key = cv2.waitKey(1) & 0xFF

            #     # if the `q` key was pressed in the cv2 window, we break from the loop and exit the program
            #     if key == ord("q"):
            #         break          


			# do the video recording
            record_video(camera_id, 5)


            # feed the video to pyVHR


            # delete the video from disk
            os.remove('videos/pulse5s.mp4')

            button_state_old = 0
            
		button_state_old = button_state_upd
	GPIO.cleanup()

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

        # Render UI views
        rgb_view = make_rgb_view(rgb_arr, scores, boxes, landms, VIS_WIN_SIZE)

        # Show rendered UI
        if SHOW_DISPLAY:
            cv2.imshow(VIS_WIN_NAME, rgb_view)
            # cv2.imshow(IR_WIN_NAME, ir_view)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed in the cv2 window, we break from the loop and exit the program
            if key == ord("q"):
                break

        # Save images to filesystem  ----> make this saving of video
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

    while rgb_thread.frame is None:
        print("Waiting for RGB frames")
        time.sleep(1)

    try:
        mainloop()

    finally:
        exit_handler()
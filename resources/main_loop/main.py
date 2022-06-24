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

            # display the result

            # delete the video from disk
            os.remove('videos/pulse5s.mp4')

            button_state_old = 0

		button_state_old = button_state_upd
	
def exit_handler():
    GPIO.cleanup()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    session_id = int(time.time())
    # For an unique id: session_id = uuid.uuid4()

    try:
        mainloop()

    finally:
        exit_handler()
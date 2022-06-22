import cv2

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
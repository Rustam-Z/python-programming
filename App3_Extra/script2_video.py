import cv2
import time

camera_port = 0
video = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

while True:

    check, frame = video.read()

    print(check)
    print(frame)

    #time.sleep(3)
    cv2.imshow("Captured", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

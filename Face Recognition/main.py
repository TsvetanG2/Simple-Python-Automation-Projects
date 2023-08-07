import threading

import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

counter = 0

does_the_face_match = False

reference_img = cv2.imread('reference.jpg')


def check_face(frame):
    global does_the_face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            does_the_face_match = True
        else:
            does_the_face_match = False
    except ValueError:
        does_the_face_match = False


while True:
    ret, frame = camera.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter += 1

        if does_the_face_match:
            cv2.putText(frame, "The face match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "No match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()


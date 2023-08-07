import cv2
import pathlib

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path)) # Cast the path to string

camera = cv2.VideoCapture(0) #If you have 1 camera type 0, otherwise type 123 - depending on how many cameras you have
#Videos are being included into the folder, so you can test the app on them, otherwise use your own camera

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2) #Setting up the rectangle + colors(255, 255, 0)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    # Once we press q it will break out the loop


camera.release()
cv2.destroyAllWindows()

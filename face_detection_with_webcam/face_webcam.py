import cv2 
#import dlib
face_detector = cv2.CascadeClassifier('/Users/giammarcocellini/Desktop/haarcascade_frontalface_default.xml')
#face_detector_hog = dlib.get_frontal_face_detector()

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = face_detector.detectMultiScale(image_gray, minSize= (220,220))
    # detections_hog = face_detector_hog(image_gray,1)

    #for face in detections_hog:
    #    l, t ,r , b = face.left(), face.top(), face.right(), face.bottom()
    for (x,y,w,h) in detections:
        print(w,h)
        cv2.rectangle(frame , (x,y), (x + w,y + h), (0,255,0), 2)

    cv2.imshow('Video', frame)


    # using the wait key function to delay 
    # the closing of windows till any key is pressed 
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
video_capture.release()
cv2.destroyAllWindows()
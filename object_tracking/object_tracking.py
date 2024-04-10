import cv2

tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()
#import os
#print("file exists?", os.path.exists('/Users/giammarcocellini/Desktop/race.mp4'))
video = cv2.VideoCapture('/Users/giammarcocellini/Desktop/race.mp4')

ok, frame = video.read()

bbox = cv2.selectROI(frame) #select the object we want to track

ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()

    if not ok: # break when there no frames anymore
        break
    # update the bbox
    ok, bbox = tracker.update(frame)
    
    if ok:
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame , (x,y), (x+ w , y +h), (0,255,0) , 1)
    else:
        cv2.putText(frame, 'Error', (100,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1 , (0,0,255), 2)
    
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF ==27: #esc
        break


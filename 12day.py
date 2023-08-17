import cv2
ob=cv2.VideoCapture(0)
if not ob.isOpened():
    print("Error")
    exit()
background=None
accumlated_weight=0.5
gesture_flag=False
while True:
    ret, frame=ob.read()
    if not ret:
        print("Error:Could not read a frame.")
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray_frame,(21,21),0)
    if background is None:
            background=gray_frame.copy().astype("float")
            continue
    cv2.accumulateWeighted(gray_frame,background,accumlated_weight)
    frame_delta=cv2.absdiff(gray_frame,cv2.convertScaleAbs(background))
    thresh=cv2.threshold(frame_delta,25,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,iterations=2)
    contours,_=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        gesture_flag=True
    #Display frame in a window
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
         break
#close the window
ob.release()
cv2.destroyAllWindows()
import numpy as np
import  cv2
#Create a blank image with a white background
width, height=800,600
blank_image=np.ones((height, width,3),np.uint8)*255
#Draw a blue line
cv2.line(blank_image,(100,100),(400,500),(255,0,0),5)
#Draw a green rectangle
cv2.rectangle(blank_image,(200,200),(600,400),(0,255,0),3)
#Draw a red circle
cv2.circle(blank_image,(400,300),100,(0,0,255),-1)
#Put text on the image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_image,'OpenCV Image Generation',(50,50),font,1,(0,0,0))
#Display the generated image
cv2.imshow('Generated Image',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
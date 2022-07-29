

import cv2
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray , 100 , 0.01 , 150)

for corner in corners:
    x,y = corner[0]
    x=int(x)
    y=int(y)
    cv2.rectangle(img , (x-10,y-10) , (x+10,y+10) , (0,255,0),2)
    
cv2.imshow('CORNERS FOUND' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#cv2.cornerHarris


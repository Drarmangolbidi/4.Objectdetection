import cv2

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerMOSSE_create()

ret , frame = cap.read()

bbox = cv2.selectROI('Tracking' , frame , False)

tracker.init(frame,bbox)

def drawBox(img , bbox):
    x,y,w,h = int(bbox[0]) , int(bbox[1]) ,int(bbox[2]) ,int(bbox[3])
    cv2.rectangle(img , (x,y) , ((x+w),(y+h)) , (255,0,255) , 3)
    cv2.putText(img , "tracking" , (100,75), cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (0,255,0) , 2)
       
while True:
    ret , img = cap.read()
    ret , bbox = tracker.update(img)
    
    if ret:
        drawBox(img , bbox)
    else:
        cv2.putText(img , "LOST" , (100,75), cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (0,255,0) , 2)
        
    cv2.imshow('Tracking' , img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
                
cap.release()
cv2.destroyAllWindows()
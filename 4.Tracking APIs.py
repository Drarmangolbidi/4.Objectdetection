
import cv2
def ask_for_tracker():
    print("Choose The Tracker: ")
    print('Enter 0 For Boosting ')
    print('Enter 1 For MIL ')
    print('Enter 2 For KCF ')
    print('Enter 3 For TLD ')
    print('Enter 4 For MedianFlow ')
    choice = input("Please Select The Tracker: ")
    
    if choice== '0':
        tracker = cv2.TrackerBoosting_create()
    if choice== '1':
        tracker = cv2.TrackerMIL_create()
    if choice== '2':
        tracker = cv2.TrackerKCF_create()
    if choice== '3':
        tracker = cv2.TrackerTLD_create()   
    if choice== '4':
        tracker = cv2.TrackerMedianFlow_create()    
    return tracker    

tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)
while True:
    ret, frame = cap.read()  
    success, roi = tracker.update(frame) 
    (x,y,w,h) = tuple(map(int,roi))
    if success:
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else :
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3);
    cv2.imshow(tracker_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break        
cap.release()
cv2.destroyAllWindows()

# 4.Objectdetection
In this repository i try to detect object 
<br>

## :blush:Step One :( Detect Puzzel pieces ):blush:</b>

<br>

![1A](https://user-images.githubusercontent.com/109248678/181452436-8102b8b9-f651-4435-8111-d80ddef126f1.jpg)

<br>

download "the_guy.jpg","image.jpg" and "Template Matching.py" . 

<br>

I want to find this pieces :

<br>

![the_guy](https://user-images.githubusercontent.com/109248678/181450720-fb53d264-7448-4744-a805-b678f7b5ff41.jpg)

<br>

And the main image is :

<br>

![image](https://user-images.githubusercontent.com/109248678/181450848-c19598c7-9061-4d5b-8f32-303c2a53adf9.jpg)

<br>

<br>

Code is :👇

<br>

```python
import cv2

image = cv2.imread('image.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('the_guy.jpg' , 0)

w,h = template.shape[::-1]

result = cv2.matchTemplate(gray , template , cv2.TM_CCOEFF)

min_val , max_val , min_loc , max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_left = (top_left[0]+w , top_left[1]+h)

cv2.rectangle(image , top_left , bottom_left , (0,0,255), 2)

cv2.imshow('Object Found :' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
```
#### EX1_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!



<br>

## :blush:Step Two :( Detect with image feature ):blush:</b>

<br>

Download "2.Finding Corners.py" and "chess.JPG " . 

<br>

In this progtram we want detect the corner of the chessboard . 

<br>

![ae](https://user-images.githubusercontent.com/109248678/182014836-9b48a399-eb72-403e-b38d-47403783f298.jpg)

<br>

Code is :👇

<br>

```python


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
   
```
#### EX2_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!

<br>

## :blush:Step Three :( Kinds of algoritm of the image processing ):blush:</b>

<br>
1.Template Matching (weak)
<br>
2.Feature from accelerated segments (Fast)
<br>
3.Binary Robust independent elementary ( BRIEF)
<br>
4.Oriented Fast and Rotated BRIEF (ORB) 
<br>

After that you should know we have some way to object tracking 

<br>

## :blush:Step Four :( Object tracking Ways ):blush:</b>

<br>
1.boosting tracker
<br>
2.kernel and Scale Adaptation 
<br>
3. Tracking learning detection (TLD)
<br>

## :blush:Step Five :( Object tracking Ways with webcam ):blush:</b>

<br>

https://user-images.githubusercontent.com/109248678/182132260-8f7e5554-d3d3-41fc-952f-72f3a551e6ba.mp4

<br>

Install ( pip install opencv-contrib-python) for object tracking tools . 
<br>
```python
pip install opencv-contrib-python==3.4.13.47
```
<br>
Download "3.Object Tracking.py" and Play it :
<br>

```python
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
```

<br>

#### EX3_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!

<br>

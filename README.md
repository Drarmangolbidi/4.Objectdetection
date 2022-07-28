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

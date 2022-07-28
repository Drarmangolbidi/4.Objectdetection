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

# Motion-Detection-with-webcam
It is a motion detection program that detects movement if there is any.

I have used OpenCV2(Open Source Computer Vision Library) for this project.

OpenCV is a library of programming functions mainly aimed at real-time computer vision,it is easy to use.
# Working:

First I take the difference between the the consecutive frames .

As the difference in the frames also shows every boundary in the image, so to remove that boundary i blured the resultant difference of the image.

Then I used different morphological operations such as dilation and erosion on the resultant difference to get better boundaries in the image.

Then I found the resultant contours in the image and those contours were good enough to show only the movement in the frames then I ploted it.

I have commented every step with respective function used.

# Function used:
absdiff()-calculates the difference between the images
        
cvtColor()-coverting the image from BGR to gray scale
        
GaussianBlur()-application of gaussian blur
       
threshold()-to apply the thresholding in frame to get the particular difference above a value
    
dilate()-to apply dilation on image
        
erode( )-to apply erosion on image
        
findContours()-for finding the contours in the frames

drawContours()-for drawing the contours on the frames

# Result-

Left image shows still frame and Right frame shows with motion.

![img](https://github.com/ArjunSikhwal/Motion-Detection-with-webcam/blob/master/Screenshot%20(70).png)

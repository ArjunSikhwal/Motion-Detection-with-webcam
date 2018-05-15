# Motion-Detection-with-webcam
It is a motion detection program that detects movement if there is any.

I have used OpenCV2(Open Source Computer Vision Library) for this project.

OpenCV is a library of programming functions mainly aimed at real-time computer vision,it is easy to use.
# Working:

First i take the difference betweenthe the consecutive frames so that it shows the difference between the frames.

As the difference in the frames also shows every boundary in the image, so to remove that boundary i blured the resultant difference of the image.

Then I used different morphological operations such as dilation and erosion on the resultant difference to get better boundaries in the image.

Then i found the resultant contours in the image and those contours were good enough to show only the movement in the frames.then i ploted it.

# Function used:
absdiff()-calculates the difference between the images
        
cvtColor()-coverting the image from BGR to gray scale
        
GaussianBlur()-application of gaussian blur
       
threshold()-to apply the thresholding in frame to get the particular difference above a value
    
dilate()-to apply dilation on image
        
erode( )-to apply erosion on image
        
findContours()-for finding the contours in the frames

drawContours()-for drawing the contours on the frames

#importing OpenCV 2
import cv2 
import numpy as np

def main():
    
    #to set the resolution to the min. value so that even if the computing power of the PC is slow
    #the program will still work
    w = 800
    h = 600
    
    
    cap = cv2.VideoCapture(0)
    #setting the resolution
    cap.set(3, w)
    cap.set(4, h)
    

    #checking if the camera is open or not
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    #readin two frames for the difference
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()


    while ret:
        #absdifference is used so that even if the value is not positive ,it'll work.
        d = cv2.absdiff(frame1, frame2)
        
        #changing the difference(d) from RGB to gray map scale.
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        
        #applying Gaussian blur on the resultant.
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        
        #Applying binary threshold on the resultant.
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
        
        #Applying dilation on the resultant.
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=1 )
        
        #Applying erosion on the resultant.
        eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )
        
        #finding the contours in the frame.
        img, c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Drawing contours in the frames.
        cv2.drawContours(frame1, c, -1, (0, 0, 255), 2)


        cv2.imshow("Original", frame2)
        cv2.imshow("Output", frame1)
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()

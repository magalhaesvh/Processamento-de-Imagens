import numpy as np
import cv2

class Utils:
    def extractRegionOfInterest(self, image, xMin, xMax, yMin, yMax):
        return image[xMin:xMax, yMin:yMax]

    def blendingTwoImages(self, image1, image2, weightOfFirstImage):
        if image1.shape[0] != image2.shape[0] or image1.shape[1] != image2.shape[1]:
            image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]), interpolation = cv2.INTER_AREA)
        newImage = cv2.addWeighted(image1, weightOfFirstImage, image2, (1-weightOfFirstImage), 0)
        return newImage

    def trackingOfRegionOfInterest(self, video, minRGBColor, maxRGBColor):
        while True:
            ret, frame = video.read()
            min = np.array([minRGBColor[0],minRGBColor[1],minRGBColor[2]],dtype=np.uint8)
            max = np.array([maxRGBColor[0],maxRGBColor[1], maxRGBColor[2]],dtype=np.uint8)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv,min,max)

            result = cv2.bitwise_and(frame,frame,mask= mask)

            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('result', result)

            k = cv2.waitKey(30) & 0xFF == ord('q')
            if k == 27:
                break


        cv2.destroyAllWindows()

# min = [110,50,50]
# max = [130,255,255]



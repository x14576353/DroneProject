# Standard imports
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2

from time import sleep
from picamera import PiCamera



def getAlarm():
    for dweet in dweepy.listen_for_dweets_from('deanDronePI'):
        #grabbing the relevant data from dweet
        content1 = dweet["content"]
        cows = content1["cows"]
        content1 = dweet["content"]
        pic = content1["pic"]

        if pic = 10:
            cam = Picamera()
            camera.capture('/home/pi/Desktop/image.jpg')
            ap = argparse.ArgumentParser()
            ap.add_argument("-i", "--image", required=True,
            	help="/home/pi/Desktop")
            args = vars(ap.parse_args())

            image = cv2.imread(args["image.jpg"])
            smaller = imutils.resize(image, width=300)
            ratio = image.shape[0] / float(resized.shape[0])

            gray = cv2.cvtColor(smaller, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            sd = ShapeDetector()
            counted_cows = 0


            # loop over the contours
            for c in cnts:
            	# compute the center of the contour, then detect the name of the
            	# shape using only the contour
            	M = cv2.moments(c)
            	cX = int((M["m10"] / M["m00"]) * ratio)
            	cY = int((M["m01"] / M["m00"]) * ratio)
            	shape = sd.detect(c)

            	# multiply the contour (x, y)-coordinates by the resize ratio,
            	c = c.astype("float")
            	c *= ratio
            	c = c.astype("int")
            	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            	counted_cows = counted_cows + 1


            if counted_cows >= cows:
                alarm = "false"
                return alarm

            else:
                alarm = "true"
                return alarm
        else:
            alarm = "not yet time"
            return alarm

def post (statistics):
    thing = 'deanDronePI'


#pushing the alarm data to dweet
def publishing():
        statistics = {}
        statistics["alarm"] = getAlarm()
        return statistics
        time.sleep(60)

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

rospy.init_node('computer_vision_sample')

bridge = CvBridge()

color = 'undefined'
shape = 'undefined'
def image_colback_color(data):
    global color, shape

    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    img_hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV) #[118:119,158:159]

    #detected color
    #print(img_hsv[0][0])

    red_low1 = (0, 110, 150)
    red_high1= (7, 255, 255)

    red_low2 = (172, 110, 150)
    red_high2= (180, 255, 255)

    red_orange_low = (8, 110, 150)
    red_orange_high= (22, 110, 150)

    orange_low = (23, 110, 150)
    orange_high= (37, 110, 150)

    yellow_orange_low = (38, 110, 150)
    yellow_orange_high= (52, 110, 150)

    yellow_low = (53, 150, 150)
    yellow_high= (67, 255, 255)

    yellow_green_low = (68, 255, 255)
    yellow_green_high= (82, 255, 255)

    green_low = (83, 150, 150)
    green_high= (97, 255, 255)

    blue_green_low = (98, 150, 150)
    blue_green_high= (113, 255, 255)

    blue_low = (114, 150, 150)
    blue_high= (127, 255, 255)

    blue_violet_low = (128, 150, 150)
    blue_violet_high= (142, 255, 255)

    violet_low = (143, 150, 150)
    violet_high= (157, 255, 255)

    red_violet_low = (158, 150, 150)
    red_violet_hugh= (171, 255, 255)

    red_mask1 = cv2.inRange(img_hsv, red_low1, red_high1)
    red_mask2 = cv2.inRange(img_hsv, red_low2, red_high2)
    red_thresh = cv2.bitwise_or(red_mask1, red_mask2)
    red_orange_mask = cv2.inRange(img_hsv, red_orange_low, red_orange_high)
    orange_mask = cv2.inRange(img_hsv, orange_low, orange_high)
    yellow_orange_mask = cv2.inRange(img_hsv, yellow_orange_low, yellow_orange_high)
    yellow_mask = cv2.inRange(img_hsv, yellow_low, yellow_high)
    yellow_green_mask = cv2.inRange(img_hsv, yellow_green_low,  yellow_green_high)
    green_mask = cv2.inRange(img_hsv, green_low, green_high)
    blue_green_mask = cv2.inRange(img_hsv, blue_green_low, blue_green_high)
    blue_mask = cv2.inRange(img_hsv, blue_low, blue_high)
    blue_violet_mask = cv2.inRange(img_hsv, blue_violet_low, blue_violet_high)
    violet_mask = cv2.inRange(img_hsv,  violet_low, violet_high)
    red_violet_mask = cv2.inRange(img_hsv, red_violet_low, red_violet_hugh)

    if red_thresh[119][159] == 255:
        shape = shape_recog(red_thresh)
        color = 'red'
    elif red_orange_mask[119][159] == 255:
        shape = shape_recog(red_orange_mask)
        color = 'red_orange'
    elif orange_mask[119][159] == 255:
        shape = shape_recog(orange_mask)
        color = 'orange'
    elif yellow_orange_mask[119][159] == 255:
        shape = shape_recog(yellow_orange_mask)
        color = 'yellow_orange'
    elif yellow_mask[119][159] == 255:
        shape = shape_recog(yellow_mask)
        color = 'yellow'
    elif yellow_green_mask[119][159] == 255:
        shape = shape_recog(yellow_green_mask)
        color = 'yellow_green'
    elif blue_green_mask[119][159] == 255:
        shape = shape_recog(blue_green_mask)
        color = 'blue_green'
    elif blue_mask[119][159] == 255:
        shape = shape_recog(blue_mask)
        color = 'blue'
    elif blue_violet_mask[119][159] == 255:
        shape = shape_recog(blue_violet_mask)
        color = 'blue_violet'
    elif violet_mask[119][159] == 255:
        shape = shape_recog(violet_mask)
        color = 'violet'
    elif red_violet_mask[119][159] == 255:
        shape = shape_recog(red_violet_mask)
        color = 'red_violet'
    else:
        shape = 'undefined'
        color = 'undefined'


image_sub = rospy.Subscriber('main_camera/image_raw_throttled', Image, image_colback_color)

while not rospy.is_shutdown():
    print("color: {}".format(color))
    print("shape: {}".format(shape))
    rospy.sleep(0.2)
import base64
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
import time
import cv2 as cv
import numpy as np

driver = webdriver.Chrome()
try:
    driver.get("chrome://dino")
except BaseException :
    s = "dsd"

actions = ActionChains(driver)
def press_key(key):
    actions.send_keys(key)
    actions.perform()

press_key(" ")

canvas = driver.find_element_by_class_name("runner-canvas")

while True:
    # get the canvas as a PNG base64 string
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

    # decode
    canvas_png = base64.b64decode(canvas_base64)

    # save to a file
    with open(r"screens/canvas_png.png", 'wb') as file:
        file.write(canvas_png)

    #print canvas
    img = cv.imread('screens/canvas_png.png')

    template_cactus = cv.imread('template_cactus.PNG')

    result = cv.matchTemplate(img, template_cactus,cv.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(result)
    img.shape[1] - template_cactus.shape[1] + 1
    img.shape[0] - template_cactus.shape[0] + 1
    (startX, startY) = maxLoc
    endX = startX + template_cactus.shape[1]
    endY = startY + template_cactus.shape[0]
    cv.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)
    
    cv.imshow("Output", img)
    cv.waitKey(1)
    a = 0 + endX
    print(a)
 

driver.close
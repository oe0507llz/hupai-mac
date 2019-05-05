import time
import os
from PIL import Image
import pytesseract
import pyautogui
from selenium import webdriver
from datetime import datetime
from dateutil import tz
import cv2
import numpy as np

def template_matching(img_gray, template_image):

    # Read the template
    template = cv2.imread(template_image,0)
 
    # Store width and heigth of template in w and h
    w, h = template.shape[::-1]
 
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    #print(loc)
    if loc[0].size > 0:
        return loc[1][0], loc[0][0], w, h
    else:
        return 0, 0, w, h

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Shanghai')
utc = datetime.utcnow()
utc = utc.replace(tzinfo=from_zone)
local = utc.astimezone(to_zone)
initial_time = datetime.strftime(local, "%H:%M:%S")
print(initial_time)

today = str(datetime.today())

directory = today.replace(" ", "_")
print(directory)

my_dir = os.path.expanduser('~/{}/'.format(directory))

if not os.path.exists(my_dir):
    os.makedirs(my_dir)


url = 'http://moni.51hupai.com/'

browser = webdriver.Safari()
browser.get(url)
browser.maximize_window()
#browser.close()

# Specify a threshold
threshold = 0.8
i = 0

while i<900:
    fn = "screen_{}".format(i)
    new_dir = my_dir + fn
    pyautogui.screenshot("{}.png".format(new_dir))
    img_rgb = cv2.imread(new_dir + '.png')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('{}_gray.png'.format(new_dir),img_gray)
    loc1_x, loc1_y, w1, h1 = template_matching(img_gray, 'template1_11inch.png')
    if loc1_x > 0:
        crop_img1 = img_gray[loc1_y:loc1_y+h1, loc1_x+w1:int(loc1_x+w1*3/2)]
        cv2.imwrite('{}{}/{}_crop1.png'.format(my_dir, fn, fn), crop_img1)
        text1 = pytesseract.image_to_string(crop_img1, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
        if len(text1.replace(" ", "")) == 4:
            int_text1 = int(text1.replace(" ", ""))*10
        else:
            int_text1 = int(text1)
        print(int_text1)

    loc2_x, loc2_y, w2, h2 = template_matching(img_gray, 'template2_11inch.png')
#    if loc2_x > 0:
#        crop_img2 = img_gray[loc2_y:loc2_y+h2, loc2_x:loc2_x+w2]
#        cv2.imwrite('{}{}/{}_crop2.png'.format(my_dir, fn, fn), crop_img2)
    
    loc3_x, loc3_y, w3, h3 = template_matching(img_gray, 'template3_11inch.png')
#    if loc3_x > 0:
#        crop_img3 = img_gray[loc3_y:loc3_y+h3, loc3_x:loc3_x+w3]
#        cv2.imwrite('{}{}/{}_crop3.png'.format(my_dir, fn, fn), crop_img3)
    print("{}, {}, {}, {}".format(loc3_x, loc3_y, w3, h3))
    time.sleep(0.5)
    i +=1
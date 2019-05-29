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
import sys
firstarg=sys.argv[1]

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Shanghai')

def shanghai_time_now():
    utc = datetime.utcnow()
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    return datetime.strftime(local, "%H:%M:%S")

initial_time = shanghai_time_now()
print(initial_time)

today = str(datetime.today())

directory = today.replace(" ", "_")
print(directory)

my_dir = os.path.expanduser('~/{}/'.format(directory))

if not os.path.exists(my_dir):
    os.makedirs(my_dir)

# Specify a threshold
threshold = 0.75
i = 0

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

def price_recognition(img_gray, template_image, relative_h, relative_w):
    loc1_x, loc1_y, w1, h1 = template_matching(img_gray, template_image)
    print("{}, {}, {}, {}".format(loc1_x, loc1_y, w1, h1))
    if loc1_x > 0:
        crop_img1 = img_gray[int(loc1_y+h1-h1*relative_h):loc1_y+h1, loc1_x+w1:int(loc1_x+w1+w1*relative_w)]
        cv2.imwrite('{}{}/{}_crop_{}.png'.format(my_dir, fn, fn, str(datetime.today()).replace(" ", "")), crop_img1)
        text1 = pytesseract.image_to_string(crop_img1, lang='eng', config = '-c tessedit_char_whitelist=0123456789')
        print(text1)
        if text1:
            text1_s = ''.join(i for i in text1 if i.isdigit())
            text1_r = text1_s
            print(text1_s)
            for i in range(len(text1_s)):
                if text1_s[i] == "8" or text1_s[i] == "9":
                    #print(i)
                    text1_r = text1_s[i:]
                    break
                else:
                    text1_r = text1_s
            if len(text1_r) > 5:
                int_text1 = int(text1_r[0:5])
            elif len(text1_r) == 4:
                int_text1 = int(text1_r)*10
            elif len(text1_r) == 3:
                int_text1 = int(text1_r)*100
            else:
                int_text1 = int(text1_r)
            return int_text1
        else:
            return text1


url = 'http://moni.51hupai.com/'

browser = webdriver.Safari()
browser.get(url)
browser.maximize_window()
#browser.close()

ref = np.array(pyautogui.screenshot())

height, width = ref.shape[:2]

if height == 1600 and width == 2560:
    screen_size = "13inch_retina"
else:
    screen_size = "11inch" 

while i<1800:
    fn = "screen_{}".format(i)
    new_dir = my_dir + fn
    pyautogui.screenshot("{}.png".format(new_dir))
    img_rgb = cv2.imread(new_dir + '.png')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    print("Round {}".format(i))
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('{}_gray.png'.format(new_dir),img_gray)

    #time.sleep(0.2)

    int_text1 = price_recognition(img_gray, 'template1_{}.png'.format(screen_size), 1, 0.5)
    print(int_text1)

    int_text1a_pre = price_recognition(img_gray, 'template1a_{}.png'.format(screen_size), 1, 0.3)
    if int_text1a_pre:
        int_text1a = int_text1a_pre + 300
    else:
        int_text1a = int_text1a_pre
    print(int_text1a)

    int_text1b = price_recognition(img_gray, 'template1b_{}.png'.format(screen_size), 2.2, 1.5)
    print(int_text1b)

    if int_text1 == int_text1a or int_text1 == int_text1b:
        lowest_price = int_text1
    elif int_text1a == int_text1b:
        lowest_price = int_text1a
    elif int_text1:
        lowest_price = int_text1
    elif int_text1b:
        lowest_price = int_text1b
    else:
        lowest_price = int_text1a

    print("Lowest Transaction Pirce is {}".format(lowest_price))

    if firstarg == 'moni':
        loc4_x, loc4_y, w4, h4 = template_matching(img_gray, 'template4_{}.png'.format(screen_size))
        if loc4_x > 0:
            crop_img4 = img_gray[loc4_y:loc4_y+h4, loc4_x+w4:int(loc4_x+2*w4)]
            cv2.imwrite('{}{}/{}_crop4.png'.format(my_dir, fn, fn), crop_img4)
            text4 = pytesseract.image_to_string(crop_img4, lang='eng', config = '-c tessedit_char_whitelist=0123456789:')
        else:
            text4 = shanghai_time_now()  
    else:
        text4 = shanghai_time_now()
    print(text4)

    if text4 == "11:29:44" or text4 == "11:29:45":
        number_int = lowest_price +900
        number = str(number_int)
        loc2_x, loc2_y, w2, h2 = template_matching(img_gray, 'template2_{}.png'.format(screen_size))
#    if loc2_x > 0:
#        crop_img2 = img_gray[loc2_y:loc2_y+h2, loc2_x:loc2_x+w2]
#        cv2.imwrite('{}{}/{}_crop2.png'.format(my_dir, fn, fn), crop_img2)
        pyautogui.moveTo(loc2_x+w2, loc2_y+h2)
        pyautogui.click()
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.doubleClick()
        pyautogui.press('del')
        time.sleep(0.5)
        pyautogui.typewrite(number)


    
        loc3_x, loc3_y, w3, h3 = template_matching(img_gray, 'template3_{}.png'.format(screen_size))
#    if loc3_x > 0:
#        crop_img3 = img_gray[loc3_y:loc3_y+h3, loc3_x:loc3_x+w3]
#        cv2.imwrite('{}{}/{}_crop3.png'.format(my_dir, fn, fn), crop_img3)
        print("Location and size for submission: {}, {}, {}, {}".format(loc3_x, loc3_y, w3, h3))


    i +=1

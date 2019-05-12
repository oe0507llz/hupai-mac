# hupai-mac

Dependencies Boostrapping:
* Install [Python3 with Pip3](https://www.python.org/downloads/mac-osx/)
* ```pip3 install pyobjc-core pyobjc pyautogui pytesseract python-dateutil opencv-python```
* ```safaridriver --enable```
* Need to install Flash Player as Plugins in Safari

Installation of Tesseract:
* If brew is not installed (check by entering ```brew``` in the terminal)), run ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```
* ```brew install tesseract```
* ```brew install tesseract-lang```

How to get a floating Terminal console?
* Download [iTerm](https://www.iterm2.com/downloads.html), unzip it and add it in Apllications folder on your Mac
* iTerm2 -> Preferences -> Keys -> Create a Dedicated Hotkey Window -> click on the space after Hotkey: and enter your hotkey (such as Command + 1) after it turns recording -> Select Floating Windows -> Click Ok
* Click Profiles that is on the left side of Keys, select Hotkey Window -> switch the panel from General to Window -> Styple: Top of Screen -> Settings for New Windows with Columns of 100 and Rows of 5 -> Close Preferences
* Use Command + 1 to switch the new iTerm widows on and off

Historical data: <br>
http://www.yunpaiwang.net/jiagezoushi/

Remaining issues to solve:
* Differentiate between moni and real and pass a parameter through the command line as an arg; Moni will start counting for the first recognized 8xxxx Lowest Transaction Pirce if time recognition fails to work out while Real uses the computer system time.
* How to munual control at the same time when the safari is controlled by the selenium?
* How to identify the same template with various screen sizes? Maybe I can find a solution to do the template matching with a varying scaling factor
* How to use the same techniques on Windows?
* Attempt tesseract OCR on the Captcha images

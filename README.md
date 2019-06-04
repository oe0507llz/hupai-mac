# hupai-mac

Dependencies Boostrapping:
* ```bash install```
* Test by opening http://moni.51hupai.com/ in safari browser. If everything is displayed well, that is great. Otherwise, you need to follow the instruction from the webpage and install Flash Player as Plugins in Safari
* System Preferences -> Security & Privacy -> Privacy -> Accessibility -> Click the lock to make changes -> Allow iTerm to control your computer

How to get a floating iTerm console (iTerm should have been installed after ```bash install```)?
* iTerm2 -> Preferences -> Keys -> Create a Dedicated Hotkey Window -> click on the space after Hotkey: and enter your hotkey (such as Command + 1) after it turns recording -> Select Floating Windows -> Click Ok
* Click Profiles that is on the left side of Keys, select Hotkey Window -> switch the panel from General to Window -> Styple: Top of Screen -> Settings for New Windows with Columns of 100 and Rows of 5 -> Close Preferences
* Use Command + 1 to switch the new iTerm widows on and off

To run for the moni website: <br>
```
git clone https://github.com/oe0507llz/hupai-mac.git
cd hupai-mac
python3 hupai-mac.py moni
```

Historical data: <br>
http://www.yunpaiwang.net/jiagezoushi/

Remaining issues to solve:
* Differentiate between moni and real and pass a parameter through the command line as an arg; Moni will start counting for the first recognized 8xxxx Lowest Transaction Pirce if time recognition fails to work out while Real uses the computer system time.
* How to munual control at the same time when the safari is controlled by the selenium?
* How to identify the same template with various screen sizes? Maybe I can find a solution to do the template matching with a varying scaling factor
* How to use the same techniques on Windows?
* Attempt tesseract OCR on the Captcha images

Covered testcase examples of numbers after tesseract OCR recognition (RMB symbol can be recognized and removed; comma can be recognized as dot and removed):
<br>- 70859, 70901
<br>- 859, 901
<br>- 8590070, 9010070
<br>- 7085900, 7990100
<br>- 8590, 9010
<br>
<br>
How to make a fault-tolerable decision on which data to take as the lowest transaction price?
<br>- In case that all of three templates give the identical answer, it is simple and feel free to use it.
<br>- In case that two templates give the identical answer, feel free to use it.
<br>- In case that three templates give three different answers, use template1.
<br>- In case that three templates give three different answers and template1 give None, use template1b.
<br>- In case that three templates give three different answers and both template1 and template1b give None, use template1a.  


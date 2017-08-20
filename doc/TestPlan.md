# Selenium Test Automation Plan

[Test_Forum_update.py](src/Test_Forum_update.py)

1 This document is designed to show how I can use selenium webdriver with python for web app testing

2 This test scripts were written in Python

3 The script is doing this:
   - Launch Firefox browser
   - Open google search main page - http://www.google.com
   - Key in search keyword and click on Search button
      - make a validation via page source code to check wanted keywords are displaying in the search result,  if Not, it requires user to re-enter proper keyword until correct keyword is provided

   - Select website I want from search result - https://www.ranorex.com
     - Make a validation via getting current login website url, if user is in the page and proceed

     - Everything is ok, user enters into the website, and then clicks on Forum button to open Login page
   
   - Enter username & password on Login page (before script is running, user is required to provide username/password)
     	- if username / password are not provided, it requires to enter username / password 
   
   - User Click on Login button
    	- Make a validation via page source code to check user login successfully. If not, it prints error message and it requests to re-enter failed data till correct data is provided.
    	  - validation of username, password, maximum of wrong password, confirmation code
      - Finally all data are correct then print validation text (login successfully text)

   - Exit from browser    

4 Test tools / ENV
   - PyCharm
   - Python
   - Seleium webdrvier
   
5 Tested information:
   - Firefox browser   
   
   
   

# Selenium Test Automation Plan

1 This video is designed to show you how I can use selenium webdriver with python for web app testing

2 This test scripts were written in Python

3 The script is doing this:
   - Launch Firefox browser
   - Open google search main page - http://www.google.com
   - Key in search keyword and click on Search button
      - make a validation via page source code to check wanted keywords are displaying in the search result,  if Not, it requires user to re-enter proper keyword until correct keyword is provided

   - Select website I want from search result - https://www.ranorex.com
     - Make a validation via getting current login website url, if user is in the page and proceed

     - Everything is ok, user enters into the website, and then click on Forum button to open Login page
   
   - Enter username & password on Login page (before script is running, user is required to provide username/password)
     	- if username / password are not provided, it require to enter username / password 
   
   - User Click on Login button
    	- if Make a validation of username, it requires to re-enter username, then script proceed running
    	- esif Make a validation of password, it requires to re-enter password, then script proceed running
      - esif Make a maximum validation of wrong password, then script stops
      - else login successfully, make a validation ensure login successfully, and then print validation text

   - Exit from browser    

4 Test tools / ENV
   - PyCharm
   - Python
   - Seleium webdrvier
   
5 Tested information:
   - Firefox browser   
   
   
   

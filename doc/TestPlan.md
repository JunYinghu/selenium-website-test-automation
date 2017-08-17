# Selenium Test Automation Plan

1 This video is designed to show you how I can use selenium webdriver with python for web app testing.
2 This automation test scripts were written in Python.

3 The script is doing this:

   - Launch Firefox browser
   - Open google search main page - http://www.google.com
   - Key in search keyword and select website I want from search result - https://www.ranorex.com
   - Go to Forum Login page
   - Enter username & password (before script is running, user is required to provide username/password)
       -- If username / password are not provided, it require to enter username / password 
   - User Click on Login button
     -- If username is wrong, it requires to re-enter username
     -- If password is wrong, it requires to re-enter password
     -- If user types wrong password reaching the maximum of validation, then script quit
     -- If login successfully, make a validation ensure login successfully, and then print validation text
   - Exit from browser        

4 Test tools / ENV
   - PyCharm
   - Python
   - Seleium webdrvier      

5 Tested information:
   - Firefox browser   
   
   
   

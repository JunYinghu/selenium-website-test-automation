# Selenium Test Automation Plan3
[Test_Forum_Profile.py](src/Test_Forum_Profile.py)

https://www.linkedin.com/in/junyinghu/
https://github.com/JunYinghu


Please kindly watch related video:

- WebSite -  https://youtu.be/kvSdQnsxQYQ – finding element, checking keyword, checking error message
- WebSite -  https://youtu.be/qerJroOBeNg – finding element via configuration, checking radio button, read a session id from a text file , instantiate class , inherit class, constructor 

- Android(Samsung Note5) - https://youtu.be/Njdcjb3c-i8 – Sending text message / image, taking image / sending it, taking video / sending it, searching conversation and deleting it

1 This document is designed to show how to handle drop-down list in selenium webdriver with Python for web app testing
   - From technical , You will see
      - Get drop-down list options
      - Save all options into a csv file
      - Test all drop-down combination by using while

2 The script is doing this:
   - Launch Firefox browser
   - Open Form  - https://www.ranorex.com
      - Get a session id from a text file (in the previous video, user logged into Form already, I saved a session id for concurrent running)
             
   - Go to User Control Panel > Board preferences > Edit global settings
       - For drop-down list, you will see
          - Get drop-down list options
          - Save all options into a csv file
          - Test all drop-down combination by using while 
  
   - Exit from browser

3 Test tools / ENV
   - PyCharm
   - Python
   - Selenium webdrvier
   
4 Tested information:
   - Firefox browser
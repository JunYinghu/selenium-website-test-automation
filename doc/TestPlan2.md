# Selenium Test Automation Plan2

[Test_Forum_Profile.py](src/Test_Forum_Profile.py)

1 This document is designed to show how I can handle radio button, drop-down list in selenium webdriver with Python for web app testing
   - From technical , You will see
      - how to read a session id from a text file
      - how to instantiate class
      - how to inherit class
      - how to set constructor to initialize an instance of a class

   - In order to avoiding from changes of UI, this time a configuration file is introduced to save all of xpath / name / id of elements

3 The script is doing this:
   - Launch Firefox browser

   - Open Form  - https://www.ranorex.com
      - Get a session id from a text file
         - in the previous video, user logged into Form already, I saved a session id for concurrent running
           Please watch https://youtu.be/kvSdQnsxQYQ

   - Go to User Control Panel > Board preferences > Edit global settings
      - Check current radio status firstly, Then to enable the un-selected radio button
         - you will see how to instantiate class with constructor
      - For drop-down list, you will see
          - how to get drop-down list options counts
          - how to save drop-down list options into a csv file

   - Go to Edit posting defaults
     - Here to inherit class enabling radio button
   
   - Exit from browser

4 Test tools / ENV
   - PyCharm
   - Python
   - Selenium webdrvier
   
5 Tested information:
   - Firefox browser
   
   
   

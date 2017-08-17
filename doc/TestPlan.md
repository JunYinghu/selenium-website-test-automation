#  Selenium Test Automation Plan

1  This project is designed to make more practice on automation testing.

2  This automation test scripts were written in Python.

3  The script is doing this:

   - Launch Firefox browser
   - Open websit http://www.google.com
   - Key in search keyword and open the releated websit (https://www.ranorex.com)
   - Go to Forum, then go to Login page
   - Enter user_name & pass_word (before running, user is able to provide username/password)
   - User Click on Login button
     -- if username is wrong, it requires to re-enter username
     -- if password is wrong, it requires to re-enter password
     -- if user types wrong passwrod reaching the maximum of validation, then script quit
     -- if login successfully, print login successfully
   - Exit from browser     
   
4 Test tools / ENV
   - PyCharm
   - Python
   - Seleium webdrvier   
   
5 Tested information:
   - Firefox browser

   
   
   
   

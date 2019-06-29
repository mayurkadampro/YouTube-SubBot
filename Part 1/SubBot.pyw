'''
auther : mighty ghost hack - https://www.youtube.com/mightyghosthack
Note : this script works only on windows operating system.

'''

import socket # it helps to check Internet Coneection.
import pyautogui # its use for keyboard inputs.
import time # use for add delay in between inputs.
import subprocess # to run the cmd command.
from _thread import * # to run funtion in parallel.

class SubBot:
    # javascript code for click on subscribe and bell button
    subButton = 'var SubForLogin = document.getElementsByClassName("style-scope ytd-subscribe-button-renderer");'
    subButtonClick = "SubForLogin[1].click();"
    bellButton = 'var Bell = document.getElementsByClassName("style-scope ytd-toggle-button-renderer");'
    bellButtonClick = "Bell[1].click();"    

    # channel url 
    url = "https://www.youtube.com/mightyghosthack"
    
    # store command code list in order to perform.
    listOfBrowser = ['start chrome '+url,'start firefox '+url]

    # next we have to store key to open console in list.s
    listOfCommand = ['j','i']

    # you can change waitTime according to your pc speed bcoz some pc need more time to open and perform some action.
    waitTime = 1
    flag = True
    count = 0

    # first write function for internet connection checking...
    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    # this function is use for press enter we have to run its in thread so make another separate function
    def enter(self,val):
        time.sleep(self.waitTime)
        pyautogui.press('enter')
    
    # now write the main loop    
    def main(self):
        # write all code in loop and check for the internet connection avaliable or not
        # if internet connection is not avaliable then we loop and check for it again in 5sec of interval
        # once we get the internet connection set falg value to false so its not going to loop again
        while self.flag:
            
            # add 5sec of interval
            time.sleep(self.waitTime+4)
            
            # check for connection
            if self.is_connected() == True:
                # now iterate the list of browser
                for i in self.listOfBrowser:
                    # now call the enter function in thread
                    # it help to enter key when command not avlaible else just enter which have not affacts
                    start_new_thread(self.enter,(1,))

                    # now perform command operation over cmd
                    process = subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    process.communicate()

                    # in order to check command found or not we have to check for its return code
                    # if return code is 1 then the entering command is not avaliable
                    # if its 0 then its avlaible
                    if process.returncode == 1:
                        # once we now the command is not avaliable so there is not point to perform next operation
                        # so we skip those step by continue keyword.
                        # also increment the count variable by 1
                        # and check count is equal to len of listofbrowser length
                        # which means both command are not working on cmd
                        # not working in the sense both browser are not installed on his pc
                        # so we set flag value to false so it will quit from the loop
                        self.count = self.count + 1
                        if self.count == len(self.listOfBrowser):
                            self.flag = False;
                        continue

                    # if command is exit and return code is 0 then it automatically open the browser
                    # so it takes time to open in computer
                    # so add delay or wait for some time
                    time.sleep(self.waitTime+4)

                    # oce browser is open use key of combiniation to open the console
                    pyautogui.hotkey('ctrl','shift',self.listOfCommand[self.listOfBrowser.index(i)])

                    # and simply give an interval and past and enter the javascript code step by step
                    time.sleep(self.waitTime+2)
                    pyautogui.typewrite(self.subButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.subButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.bellButton)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                    pyautogui.typewrite(self.bellButtonClick)
                    pyautogui.press('enter')
                    time.sleep(self.waitTime)
                  
                    # for quitting.
                    pyautogui.hotkey('alt','f4')
                  
                    # extra enter option bcoz some browser show the confirm dialog box when there are more than one tab is open.
                    pyautogui.press('enter')

                    # once all code works then simply set flag value to false so it will not loop again.
                    self.flag = False;
                    break
            else:
                # else condition to print connect to internet
                print("Please Connect to Internet")

subBot = SubBot()
subBot.main()

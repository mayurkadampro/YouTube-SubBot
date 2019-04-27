import socket # it helps to check Internet Coneection.
import webbrowser as wb # its help to redirect into channel URL.
import pyautogui # its use for keyboard inputs.
import time # use for add delay in between inputs.
import subprocess # to run the cmd command.
from _thread import * 
#import pyspeedtest # pip install pyspeedtest

class SubBot:
    # javascript code for click on subscribe and bell button
    subButton = 'var SubForLogin = document.getElementsByClassName("style-scope ytd-subscribe-button-renderer");'
    subButtonClick = "SubForLogin[1].click();"
    bellButton = 'var Bell = document.getElementsByClassName("style-scope ytd-toggle-button-renderer");'
    bellButtonClick = "Bell[1].click();"

    url = "https://www.youtube.com/user/PewDiePie"
    listOfBrowser = ['start firefox '+url,'start chrome '+url]
    listOfCommand = ['i','j']

    # first write function for internet connection checking...
    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def enter(self,val):
        time.sleep(1)
        pyautogui.press('enter')

    def main(self):
        if self.is_connected() == True:
          for i in self.listOfBrowser:
              start_new_thread(self.enter,(1,))
              process = subprocess.Popen(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
              process.communicate()
              res  = process.returncode
              if res == 1:
                  continue
              time.sleep(5)
              #pyautogui.hotkey('ctrl','shift','i') # for mozilla and Edge
              pyautogui.hotkey('ctrl','shift',self.listOfCommand[self.listOfBrowser.index(i)])
              time.sleep(3)
              #pyautogui.click(button='right')
              pyautogui.typewrite(self.subButton)
              pyautogui.press('enter')
              time.sleep(1)
              pyautogui.typewrite(self.subButtonClick)
              pyautogui.press('enter')
              time.sleep(1)
              pyautogui.typewrite(self.bellButton)
              pyautogui.press('enter')
              time.sleep(1)
              pyautogui.typewrite(self.bellButtonClick)
              pyautogui.press('enter')
              time.sleep(1)
              # for quitting.
              pyautogui.hotkey('alt','f4')
              # extra enter option bcoz some browser show the confirm dialog box when there are more than one tab is open.
              pyautogui.press('enter')
              break
        else:
          print("Please Connect to Internet")

subBot = SubBot()
subBot.main()

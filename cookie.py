from ctypes.wintypes import RGB
import pyautogui as p
def cookieClick():
    location = p.locateOnScreen('assets/cok.png', confidence = 0.8)
    if location!=None:
        p.moveTo(location)
        while location!=None:
            p.click()
            if p.pixelMatchesColor(1237,296(102 ,255, 102)) or p.pixelMatchesColor(1237,296(97 ,231, 96)) or p.pixelMatchesColor(1237,296(97 ,241, 97)) or p.pixelMatchesColor(1237,296(112 ,218, 109)) or p.pixelMatchesColor(1237,296(98 ,242, 255)) or p.pixelMatchesColor(1237,291(97 ,231, 96)) or p.pixelMatchesColor(1237,291(97 ,241, 97)) or p.pixelMatchesColor(1237,291(112 ,218, 109)) or p.pixelMatchesColor(1237,291(98 ,242, 255)):
                autocursor()
                

            
    
def autocursor():
    location = p.locateOnScreen('assets/cur.png')
    p.moveTo(location)
    p.click()
    cookieClick()



def main():
    cookieClick()
    


main()

"""cookie=0
    green = p.pixelMatchesColor(1234,294)
    location = p.locateOnScreen('assets/cok.png', confidence = 0.8)
    if location!=None:
        p.moveTo(location)
        while location!=None:
            p.click()
            cookie+=click
            if :
                a = p.comfirm("Do you want to buy the cursor?")
                if a:
                    autocursor()
                    numCur+=1
                    curs=curs"""
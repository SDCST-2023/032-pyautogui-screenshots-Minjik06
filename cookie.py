from ctypes.wintypes import RGB
import random
import time
import pyautogui as p
def cookieClick():
    k=[autocursor(), Grandmother(), Farm()]
    location = p.locateOnScreen('assets/cok.png')
    p.moveTo(location)
    while True: 
        p.moveTo(location)
        if p.pixelMatchesColor(1218,333,(255,255,255)) and p.pixelMatchesColor(1218,277,(255,255,255)) and p.pixelMatchesColor(1220,391,(255,255,255)): 
            num=random.randint(0,2)
            k[num]
        p.click(location)
        if p.pixelMatchesColor(1220,391,(255,255,255)):
                Farm()
        p.click(location)
        if p.pixelMatchesColor(1218,333,(255,255,255)):
            Grandmother()
        p.click(location)
        if p.pixelMatchesColor(1218,277,(255,255,255)):
            autocursor()
        p.click(location)
            
    
def autocursor():
    location1 = p.locateOnScreen('assets/cur.png')
    p.click(location1)
    

def Grandmother():
    location2 = p.locateOnScreen('assets/gra.png')
    p.click(location2)
    

def Farm():
    location3 = p.locateOnScreen('assets/far.png')
    p.click(location3)

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
                    curs=curs
                    
                    
                    
                    def cookieClick():
    time.sleep(2)
    location = p.locateOnScreen('assets/cok.png', confidence = 0.8)
    if location!=None:
        p.moveTo(location)
        while location!=None:
            if p.pixelMatchesColor(1218,325,(255,255,255)):
                p.confirm("want to by cursor?")
                autocursor()
            p.click()"""
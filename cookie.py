from ctypes.wintypes import RGB
import random
import time
import pyautogui as p
from pyscreeze import pixel, pixelMatchesColor
debug = False
p.Pause = 0.001


def cookieClick():
    location = p.locateOnScreen('assets/cok.png')
    r,g,b=p.pixel(1194,168)
    print(r,g,b)
    p.moveTo(location)
    while True: 
        for i in range(20):
            p.click()
        #print(p.pixel(1220,391), p.pixel(1218,333) , p.pixel(1218,277))
            if p.pixelMatchesColor(1220,391,(255,255,255)):
                Farm()
                p.moveTo(location)
            if p.pixelMatchesColor(1218,333,(255,255,255)):
                Grandmother()
                p.moveTo(location)
            if p.pixelMatchesColor(1218,277,(255,255,255)):
                autocursor()
                p.moveTo(location)
        for k in range(40):
            if p.pixelMatchesColor(1194,168,(6,19,27)):
                Store()
                p.moveTo(location)
    
def autocursor():
    if debug: print("autocursor")
    location1 = p.locateOnScreen('assets/cur.png',confidence=0.9)
    while p.pixelMatchesColor(1218,277,(255,255,255)):
        p.click(location1)
    

def Grandmother():
    if debug: print("grandmother")
    location2 = p.locateOnScreen('assets/gra.png',confidence = 0.9)
    """mp = p.position()
    p.moveTo(location2)
    time.sleep(0.25)
    p.moveTo(mp)
    """
    while p.pixelMatchesColor(1218,333,(255,255,255)):
        p.click(location2)
    

def Farm():
    if debug: print("farm")
    location3 = p.locateOnScreen('assets/far.png',confidence=0.9)
    while p.pixelMatchesColor(1220,391,(255,255,255)):
        p.click(location3)

def Store():
    if debug: print("Store")
    location4 = p.locateOnScreen('assets/str.png',confidence=0.9)
    p.click(location4)


def main():
    cookieClick()
    


main()

"""def cookieClick():
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
        
        cookie=0




        def cookieClick():
    k=[autocursor(), Grandmother(), Farm()]
    location = p.locateOnScreen('assets/cok.png')
    p.moveTo(location)
    j=0
    while True: 
        p.moveTo(location)
        p.click()
        if p.pixelMatchesColor(1220,391,(255,255,255)):
            Farm()
        elif p.pixelMatchesColor(1218,333,(255,255,255)):
            Grandmother()
        elif p.pixelMatchesColor(1218,277,(255,255,255)):
            autocursor()



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
import pyautogui as p
def cookieClick():
    location = p.locateOnScreen('assets/cook.png', confidence = 0.8)
    if location!=None:
        p.moveTo(location)
        while location!=None:
            p.click()
    return
    
def autocursor():
    location = ('assets/cursor.png')
    location1 = ('assets/cursor1.png')
    if location1!=location:
        a=int(input("y or n"))
        if a=="y":
            p.moveTo(location)
            p.click()
        elif a=="n":
            cookieClick()

def main():
    cookieClick()
    


main()
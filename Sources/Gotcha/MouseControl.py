import pyautogui

def MousePosition() -> None:
    return pyautogui.position()

def MouseMove(x : int, y : int, t : int = 0) -> None:
    print("moved mouse", x, y, "while", t, "seconds")
    pyautogui.moveTo(x, y, t)

def MouseClickLeft(count : int = 1) -> None:
    print("clicked mouse", count)
    pyautogui.click(clicks=count)

def MouseClickRight() -> None:
    print("clicked mouse right")
    pyautogui.rightClick()

def MouseScroll(x : int) -> None:
    print("scrolled while", x)
    pyautogui.scroll(x)

def MouseDrag(x : int, y : int, t : int = 0) -> None:
    print("draged mouse", x, y, "while", t, "seconds")
    pyautogui.dragTo(x, y, t)
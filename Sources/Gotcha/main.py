import pyautogui

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

if __name__ == "__main__":
    # MouseMove(100, 200)
    # MouseClickLeft()
    # MouseClickRight()
    # MouseScroll(100)
    # MouseDrag(100, 100, 2)

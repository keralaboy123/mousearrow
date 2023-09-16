import winreg
import ctypes
import atexit


" a library for changing mouse pointer picture to user selected image"
ARROW = '%SYSTEMROOT%\\Cursors\\aero_arrow.cur' #default picture
HAND = '%SYSTEMROOT%\\Cursors\\aero_link.cur' #picture of hand
TEXT = ""

class Mousearrow:
    arrow = ARROW
    hand = HAND
    text = TEXT

    def __init__(self, arrow="",hand="",text=""):
        """
        this class is used for setting reseting mouse arrow image globaly in windows
        picture = file location to .cur formatted image

        """
        self.arrow = arrow or self.__class__.arrow
        self.hand = hand or self.__class__.hand
        self.text = text or self.__class__.text


    def setpicture(self):
        """" open registry key ,make changes and closes finaly updating ui"""
        self._setpicture(self.arrow)

    def setpicture_all(self):
        """" oopen registry key ,make changes and close. finaly update ui"""
        self._setpicture(self.arrow, "Arrow")
        self._setpicture(self.hand,"Hand")
        self._setpicture(self.text, "IBeam")

    @classmethod
    def reset(cls):
        " restore system defined picture when use of this module is over"
        cls._setpicture(cls.arrow)

    @classmethod
    def resetall(cls):
        " restore .system defined picture when use of this module is over"
        cls._setpicture(cls.arrow, key="Arrow")
        cls._setpicture(cls.hand, key="Hand")
        cls._setpicture(cls.text, key="IBeam")


    @staticmethod
    def _setpicture(picture,key="Arrow"):
        " real low level method for setting picture. key is registry key"
        regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Control Panel\Cursors', 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, key, 0, winreg.REG_SZ, picture)
        winreg.CloseKey(regkey)
        ctypes.windll.user32.SystemParametersInfoA(0x0057, 0, None, 0)


atexit.register(Mousearrow.resetall)  # restore system image if exited.

if __name__ == "__main__":
   import time

   test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"

   arrow = Mousearrow (test_image)
   arrow.setpicture_all()
   time.sleep(5)
   #arrow.resetall() # this is not need.atexit will handle it


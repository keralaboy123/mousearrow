import winreg
import ctypes,time

" a library for changing mouse pointer picture to user selected image"


class mousearrow:
    picture = '%SYSTEMROOT%\\Cursors\\aero_arrow.cur'
    def __init__(self,picture="" ):
        """
        this class is used for setting reseting mouse arrow image globaly in windows
        picture = file location to .cur formatted image

        """
        self.picture = picture or self.__class__.picture
    def setpicture(self):
        """" opense registry key and make changes and closes then updating ui"""
        regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Control Panel\Cursors', 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, 'Arrow', 0, winreg.REG_SZ, self.picture)
        winreg.CloseKey(regkey)
        ctypes.windll.user32.SystemParametersInfoA(0x0057, 0, None, 0)

    def reset(self):
        " restore static picture .system defined picture when use of this module is over"
        self.picture = self.__class__.picture
        self.setpicture()



if __name__ == "__main__":
   test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"
   arrow =mousearrow(test_image)
   arrow.setpicture()
   print (" picture setted ")
   time.sleep(5)
   arrow.reset()
   print(" picture resetted ")

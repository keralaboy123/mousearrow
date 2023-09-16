# mousearrow
change mouse arrow image to user selected image from python in windows
it uses winreg and ctypes


# install
download mousearrow.py into folder of your code 
   

# usage
  ```
    from mousearrow import Mousearrow

    test_image = "C:\\path\\example.cur"
    arrow = Mousearrow (test_image)
    arrow.setpicture()

    # to reset default image call
    arrow.reset()
  ```

   ### lowlevel method _setpicture
  ```
       from mousearrow import Mousearrow
       test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"
       arrow = Mousearrow()
       arrow._setpicture(test_image)
  ```
     
 we can set registry key like this."hand" means change picture of hand option. 
 its avaiable when moving mouse over hyperlinks
 same way we can blinking change cursor icon. just pass "Ibeam" as key
 
  ```
        arrow._setpicture(test_image,key="Hand")
  ```

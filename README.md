# mousearrow
change icon of mouse arrow to user selected image from python in windows.
it uses winreg and ctypes internaly


# install
download mousearrow.py into folder of your code 
   

# usage
  ```
    from mousearrow import Mousearrow

    test_image = "C:\\path\\example.cur"  #image must be in .cur format
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
     
 we can set registry key like this.
  ```
        arrow._setpicture(test_image,key="Hand")
  ```
"hand" means change icon of hand arrow
 its avaiable when moving mouse over hyperlinks
 same way we can change blinking  cursor icon. just pass "Ibeam" as key
 these keys are used by windows internaly.
 
 below is registry path to these settings.just browse it by registry editor 
   registry > hkey current user>controllpanel>cursors
 

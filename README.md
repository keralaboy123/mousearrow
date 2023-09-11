# mousearrow
change mouse arrow image to user selected image from python in windows
it uses winreg and ctypes


# install
download mousearrow.py into folder of your code 
   >import mousearrow

# usage
  ```
    import mousearrow

    test_image = "C:\\path\\example.cur"  #image must be in .cur format.try online .png to .cur converter
    arrow =mousearrow.Mousearrow(test_image)
    arrow.setpicture()

    # to reset default image call
    arrow.reset()
  ```

   ### lowlevel method _setpicture
  ```
       import mousearrow
       test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"
       arrow =mousearrow.Mousearrow()
       arrow._setpicture(test_image)
  ```
     
 we can set key name of registry key like this
 
  ```
        arrow._setpicture(test_image,key="Hand")
  ```

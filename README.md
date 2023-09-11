# mousearrow
change mouse arrow image to user selected image from python in windows

# install
download mousearrow.py into folder of your code 
   >import mousearrow

# usage
  ```
    import mousearrow

    test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"
    arrow =mousearrow.Mousearrow(test_image)
    arrow.setpicture()

    # to reset default image call
       ""arrow.reset()""
  ```

   ### lowlevel method _setpicture
     ```
       import mousearrow
       test_image = "%SYSTEMROOT%\\Cursors\\aero_helpsel.cur"
       arrow =mousearrow.Mousearrow()
       arrow._setpicture(test_image)
     ```

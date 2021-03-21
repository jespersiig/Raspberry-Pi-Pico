import time
import picoscroll as scroll

# Initialise the board
scroll.init()

while True:
    
    # Wait until the  button is pressed
    while scroll.is_pressed(scroll.BUTTON_A) == False and scroll.is_pressed(scroll.BUTTON_B) == False and scroll.is_pressed(scroll.BUTTON_X) == False and scroll.is_pressed(scroll.BUTTON_Y) == False :
        pass

    if scroll.is_pressed(scroll.BUTTON_A) == True:

        scroll.set_pixel(7, 0, 128)
        scroll.set_pixel(8, 0, 128)
        scroll.set_pixel(9, 0, 128)
        
        scroll.set_pixel(6, 1, 128)
        scroll.set_pixel(10, 1, 128)
        
        scroll.set_pixel(6, 2, 128)
        scroll.set_pixel(10, 2, 128)
        
        scroll.set_pixel(6, 3, 128)
        scroll.set_pixel(7, 3, 128)
        scroll.set_pixel(8, 3, 128)
        scroll.set_pixel(9, 3, 128)
        scroll.set_pixel(10, 3, 128)
        
        scroll.set_pixel(6, 4, 128)
        scroll.set_pixel(10, 4, 128)
        
        scroll.set_pixel(6, 5, 128)
        scroll.set_pixel(10, 5, 128)
        
        scroll.set_pixel(6, 6, 128)
        scroll.set_pixel(10, 6, 128)
        scroll.update()

    elif scroll.is_pressed(scroll.BUTTON_B) == True:
        brightness = 0

        # For each pixel in the matrix
        for y in range (0, scroll.get_height()):
            for x in range (0, scroll.get_width()):
            # Set that pixel to an increasing level of brightness
                scroll.set_pixel(x, y, brightness)
                brightness += 2
        scroll.update()

    elif scroll.is_pressed(scroll.BUTTON_Y) == True:
        i = 0
        loop = 18
        br_mult = 1
        br_pressed = 32
        tail = 12

        width = scroll.get_width()
        height = scroll.get_height()

        # RUN until the X button is pressed
        while scroll.is_pressed(scroll.BUTTON_X) == False:    
            for y in range(0, height):
                for x in range(0, width):
                    m = (x + (y * width)) % loop
                    for b in range(0, loop):
                        if m == (i + (loop - b)) % loop and b < tail:
                            scroll.set_pixel(x, y, br_mult * (tail - b))
            scroll.update()
            i += 1
            if i >= loop:
                i = 0
            time.sleep(0.02)

#    else:
#        print("Goodbye Cruel World")
        
    # Wait until the X button is pressed
    while scroll.is_pressed(scroll.BUTTON_X) == False:
        pass

    # Set the brightness of all pixels to 0
    scroll.clear()
    scroll.update()

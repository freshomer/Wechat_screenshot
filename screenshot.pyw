#!/usr/bin/env python
# #-*- coding:utf-8 -*-
'''
# prerequisite:
#   based on Python 3.x (32bit)
#   need Python pillow module
'''

import ctypes

def capture():
    '''
    Capture screenshot.
    '''
    try:
        dll = ctypes.cdll.LoadLibrary('PrScrn.dll')
    except Exception as dll_open_exception:
        print('DLL load error: {}'.format(dll_open_exception))
        return 0
    return dll.PrScrn(0)

def save_to_file():
    '''
    Save screenshot to local file.
    '''
    from PIL import Image
    from PIL import ImageGrab
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        print(image.format, image.size, image.mode)
        image.save("file.jpg", "JPEG")

def main():
    '''
    Main
    '''
    if capture() == 1:
        save_to_file()
    return

if __name__ == "__main__":
    main()

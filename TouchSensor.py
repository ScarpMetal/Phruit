# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import os, sys
import time

import Adafruit_MPR121.MPR121 as MPR121

class TouchSensor(object):

    DEBUG = True

    TOUCHED = 1
    RELEASED = -1
    UNCHANGED = 0

    def __init__(self):
        if self.DEBUG:
            print("Debug Mode Initialized")
            print("Use number keys. Press Ctrl-C to quit.")
            return
        print('Initializing TouchSensor...')
        
        self.cap = MPR121.MPR121()

        if not self.cap.begin():
            print('Error initializing MPR121.  Check your wiring!')
            sys.exit(1)

        print('Success! Press Ctrl-C to quit.')

        self.last_touched = self.cap.touched()

    def update(self):
        if self.DEBUG:
            return
        self.data = [0] * 12
        current_touched = self.cap.touched()
        # Check each pin's last and current state to see if it was pressed or released.
        for i in range(12):
            # Each pin is represented by a bit in the touched value.  A value of 1
            # means the pin is being touched, and 0 means it is not being touched.
            pin_bit = 1 << i
            # First check if transitioned from not touched to touched.
            if current_touched & pin_bit and not self.last_touched & pin_bit:
                print('{0} touched!'.format(i))
                self.data[i] = 1
            # Next check if transitioned from touched to not touched.
            if not current_touched & pin_bit and self.last_touched & pin_bit:
                print('{0} released!'.format(i))
                self.data[i] = -1
        # Update last state and wait a short period before repeating.
        self.last_touched = current_touched

    def status(self, pinNum):
        if self.DEBUG:
            return
        return self.data[pinNum]
        

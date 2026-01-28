## How to use this code:
1. Copy the folder "adafruit bus device" and the file "adafruit_vl53l0x.mpy" from the [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries) to the "lib" folder on your MakerPi.
2. Copy all .py files from the code/ directory to your MakerPi.
3. MakerPi NeoPixels will light up red. Hold the GP20 button and release it (NeoPixels will turn yellow when button is held and green when button is released).
4. You are now in sumo mode! Robot will seek out an opponent and attempt to shove it out of the ring. 

You can run `copy-code.ps1` on a Windows computer to copy the code files to your MakerPi, just remember to update 
the `copy-code.ps1` script with the correct path to the code directory and the correct drive letter for the MakerPi.
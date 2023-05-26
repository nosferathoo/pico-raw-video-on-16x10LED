# pico-raw-video-on-16x10LED

Wearable *cyberpunkish* video player done using Raspberry Pi Pico with LED 16x10 matrix display in the custom 3D printed case.

Result:

https://github.com/nosferathoo/pico-raw-video-on-16x9LED/assets/2834098/7fbb9744-5cb3-474c-91ce-1c2439cd7bbe

## Requirements

1. Raspberry Pi Pico with already soldered headers [ordered here](https://botland.com.pl/moduly-i-zestawy-do-raspberry-pi-pico/21573-raspberry-pi-pico-h-rp2040-arm-cortex-m0-ze-zlaczami-5056561803180.html)
2. 16x10 LED matrix display for Raspberry [I orderer it here](https://botland.com.pl/raspberry-pi-pico-hat-klawiatury-i-wyswietlacze/20116-matryca-led-rgb-16x10-do-raspberry-pi-pico-waveshare-20170-5904422350666.html)
3. 3D printer - I asked friend to print my model

## Video

The video has to be converted to a 16x10 raw RGB video. I wrote a simple converter (render/png2raw.py) that reads already prepared PNG files with 16x10 video frames from the current directory and outputs *output.raw* file. As a video source, I prepared and rendered animation using Blender. *video.blend* file contains the source Blender file, but you can use any video resized to 16x10 and dumped to separate png frames.

My video:

![render](https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/0b115801-619f-4c3e-bceb-01f170cb7b3f)

## Case

I've prepared a custom 3D printed case modeled in Blender based on [this](https://www.printables.com/pl/model/143745-](https://learn.adafruit.com/raspberry-pi-pico-case/3d-printing) model. The modification includes the possibility to rotate Pico, symmetrical USB cable entry, and back holes to thread a piece of cloth. In my first print, I noticed that Pico was not fitting very well because the USB port collided with supports for the Pico. I already modified it but probably you will still need to modify the USB entry holes to fit your cable. The source model (*case.blend*) is already print-friendly you just need to export it to STL. It is better to print the base in dark material and the cover in brighter, preferably white so it will not block LED lights.

<img width="300" alt="Case model" src="https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/081eb807-30a7-46da-bba5-80b51c940716">
<img width="300" alt="Case model" src="https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/95818014-5dcf-4eda-8868-5806d2291f0c">

## Program and installation

The program was written in Python using *Thonny IDE* based on an example program from 16x10 matrix LED grid SDK. Use Thonny IDE to install MicroPython on your Raspberry Pi Pico and then upload everything in the *Pico* folder. You can replace *output.raw* file with your raw video. Additionally, I've implemented BOOTSEL button handling so you can change video brightness on the fly.

This is how it works in daylight:

https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/ebdca11a-324c-4fbb-add0-3d9da3c1fe3a

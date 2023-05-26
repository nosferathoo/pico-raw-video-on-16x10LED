# pico-raw-video-on-16x10LED

Wearable *cyberpunkish* video player done using pico with LED 16x10 matrix display in custom 3D printed case.

Result:

https://github.com/nosferathoo/pico-raw-video-on-16x9LED/assets/2834098/7fbb9744-5cb3-474c-91ce-1c2439cd7bbe

## Requirements

1. Raspberry Pi Pico with already soldered headers [ordered here](https://botland.com.pl/moduly-i-zestawy-do-raspberry-pi-pico/21573-raspberry-pi-pico-h-rp2040-arm-cortex-m0-ze-zlaczami-5056561803180.html)
2. 16x10 LED matrix display for Raspberry [I orderer it here](https://botland.com.pl/raspberry-pi-pico-hat-klawiatury-i-wyswietlacze/20116-matryca-led-rgb-16x10-do-raspberry-pi-pico-waveshare-20170-5904422350666.html)
3. 3D printer - I asked friend to print my model

## Video

Video has to be converted to 16x10 raw RGB video. I wrote simple converter (render/png2raw.py) that reads already prepared PNG files with 16x10 video frames from the current directory and outputs *output.raw* file. As a video source I prepared and rendered animation using Blender. *video.blend* file contains source Blender file. But you can use any video resized to 16x10 and dumped to separate png frames.

My video:

![render](https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/0b115801-619f-4c3e-bceb-01f170cb7b3f)

## Case

I've prepared custom 3D printed case modeled in Blender:

<img width="690" alt="obraz" src="https://github.com/nosferathoo/pico-raw-video-on-16x10LED/assets/2834098/081eb807-30a7-46da-bba5-80b51c940716">

...

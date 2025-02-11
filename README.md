# Reverse Engineering: Hiroyasu IC-980 Pro VHF/UHF

## Introduction
This repository documents the reverse engineering process applied to the **Hiroyasu IC-980 Pro VHF/UHF** amateur radio, purchased from AliExpress.

The main objective is to analyze the hardware and firmware of the radio to understand its operation, identify possible improvements, and, if feasible, modify its software to expand its functionalities.
### Components
- STM32F101/103
- BoyaMicro 25D16AS
- TDA2003 Audio Amplifier
### Binaries
- BY25D16AS@40SOP8-208.BIN : Memory dump from backside SPI flash.
![200](images/photo_2025-01-08_11-24-25.jpg)
- openocd.py :config file to debug swd with openocd
- firmloader.py : loader for stm32 arm in IDA64 debugger
- Configuration for disssasembly binary in IDA

![](stm32%20ida%20v0_1/Captura1.PNG)
## Objectives

The main objectives of this project are:

1. Extract and analyze the radio's firmware.
2. Document the hardware and its operation.
3. Explore possible improvements in the radio's configuration and operation.

## Images
Opened Radio from top

![](images/Foto-radio-inside.jpg)

SPI FLASH

![400](images/photo_2025-01-08_11-24-25.jpg)


How has to be connected the SWD port

![400](images/prog_debug_ic980pro.jpg)


Debugg Interface after conect SWD port.

![500](images/Captura%20stm32f1xx.jpg)
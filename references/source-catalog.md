# Primary Source Catalog

Last curated: 2026-07-26. Always check the current official product page and document revision before making a part-specific claim.

## Competition and Historical Problems

- [NUEDC official history/news page](https://www.nuedc.cn/news/129.html)
- [NUEDC training system](https://www.nuedc-training.com.cn/)
- [chenshuo/nuedc historical material](https://github.com/chenshuo/nuedc)
- [CCBP/NUEDC_Topic historical problem repository](https://github.com/CCBP/NUEDC_Topic)

Use these to locate original statements and metadata. Confirm event level, year, clarification, and component list. Do not redistribute copyrighted PDFs without permission.

## Measurement and Uncertainty

- [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297)
- [BIPM/JCGM Guides in Metrology](https://www.bipm.org/en/publications/guides)
- [JCGM 100:2008 GUM](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e)

Use these for measurement models, Type A/Type B components, combined/expanded uncertainty, and reporting. Do not copy or rebrand copyrighted standards.

## STM32 and ARM

- [STM32G4 Reference Manual RM0440](https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)
- [STM32 ADC accuracy application note AN2834](https://www.st.com/resource/en/application_note/an2834-how-to-get-the-best-adc-accuracy-in-stm32-microcontrollers-stmicroelectronics.pdf)
- [ARM CMSIS-DSP documentation](https://arm-software.github.io/CMSIS-DSP/latest/)

Also retrieve the exact device datasheet, errata, board user guide/schematic, and current STM32Cube release notes.

## Texas Instruments MCU and DSP

- [MSPM0G3507 product page](https://www.ti.com/product/MSPM0G3507)
- [MSPM0 G-Series Technical Reference Manual SLAU846](https://www.ti.com/lit/pdf/slau846)
- [TMS320F28379D product page](https://www.ti.com/product/TMS320F28379D)
- [TMS320F2837xD Technical Reference Manual SPRUHM8](https://www.ti.com/lit/pdf/spruhm8)
- [TMS320F2837xD datasheet SPRS880](https://www.ti.com/lit/pdf/sprs880)
- [C2000 Academy](https://dev.ti.com/tirex/explore/node?node=A__AB9v29tV4.Nf78YEE5BfQQ__C2000-ACADEMY__3H1LnqB__LATEST)

Retrieve the exact device errata, LaunchPad/controlCARD schematic, C2000Ware/MSPM0 SDK release, and SysConfig-generated routing evidence.

## RP-series and Espressif

- [Raspberry Pi microcontroller documentation](https://www.raspberrypi.com/documentation/microcontrollers/)
- [RP2040 datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [Hardware design with RP2040](https://datasheets.raspberrypi.com/rp2040/hardware-design-with-rp2040.pdf)
- [ESP32-S3 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)
- [ESP32-S3 hardware design guidelines](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/index.html)

Verify the exact module/board because flash, PSRAM, antenna, regulator, USB, and pin exposure differ.

## NXP, GigaDevice, and Microchip

- [NXP i.MX RT1060 product and documentation page](https://www.nxp.com/products/i.MX-RT1060)
- [GD32F407VET6 official product page](https://www.gd32mcu.com/en/product/arm-cortex-m4/gd32f4xx-series/gd32f407vet6)
- [Microchip ATSAME54P20A product and documentation page](https://www.microchip.com/en-us/product/ATSAME54P20A)

Use the exact family reference manual, device datasheet, errata, package pinout, SDK release notes, and evaluation-board schematic. Similar peripheral names across vendors do not prove register, timing, electrical, or DMA compatibility.

## FPGA

- [AMD 7 Series SelectIO Resources UG471](https://docs.amd.com/v/u/en-US/ug471_7Series_SelectIO)
- [AMD 7 Series Clocking Resources UG472](https://docs.amd.com/v/u/en-US/ug472_7Series_Clocking)
- [AMD Vivado Design Suite User Guide: Using Constraints UG903](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints)
- [Intel Cyclone 10 LP device design guidelines](https://www.intel.com/content/www/us/en/docs/programmable/683777/current/cyclone-10-lp-device-design-guidelines.html)
- [Intel Quartus Prime Timing Analyzer documentation](https://www.intel.com/content/www/us/en/docs/programmable/683243/current/timing-analyzer.html)
- [Lattice ECP5 product and documentation page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5)

Retrieve exact device/package pinout, speed grade, errata/advisories, board schematic, and tool version support.

## Analog, ADC, Grounding, and Power Layout

- [Analog Devices MT-031: Grounding Data Converters](https://www.analog.com/media/en/training-seminars/tutorials/MT-031.pdf)
- [Analog Devices MT-101: Decoupling Techniques](https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf)
- [TI SBAA381: Why is finding an ADC's effective resolution bandwidth important?](https://www.ti.com/lit/pdf/sbaa381)
- [TI SNVA021C: Layout Guidelines for Switching Power Supplies](https://www.ti.com/lit/pdf/snva021)

Use the product datasheet and layout section for the exact op-amp, ADC, regulator, gate driver, MOSFET, sensor, and motor driver.

## Motor Drives, Current Sensing, and Fast Protection

- [TI DRV8323 three-phase gate-driver product page](https://www.ti.com/product/DRV8323)
- [TI INA240 current-sense amplifier product page](https://www.ti.com/product/INA240)
- [TI UCC21520 isolated gate-driver product page](https://www.ti.com/product/UCC21520)
- [ST STSPIN32G4 motor-controller product page](https://www.st.com/en/motor-drivers/stspin32g4.html)

Use these only as representative entry points. Recalculate shunt dissipation, amplifier range and common mode, gate charge/current, bootstrap behavior, dead time, desaturation or overcurrent response, propagation mismatch, thermal limits, regenerative bus rise, and safe-state behavior for the exact design.

## Precision Conversion, Sensors, and Physical-layer Interfaces

- [TI ADS131M04 simultaneous-sampling ADC product page](https://www.ti.com/product/ADS131M04)
- [TDK ICM-42688-P IMU product and datasheet page](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/)
- [ST VL53L1X time-of-flight sensor product page](https://www.st.com/en/imaging-and-photonics-solutions/vl53l1x.html)
- [TI DP83848 Ethernet PHY product page](https://www.ti.com/product/DP83848-EP)

Verify analog input drive, reference and clock requirements, digital-interface voltage, startup and calibration sequence, interrupt/data-ready timing, timestamp strategy, sensor bias/noise/temperature behavior, PHY magnetics and termination, and module-level deviations from the bare IC documentation.

## Control, Robotics, and Vision

- [MIT Underactuated Robotics notes](https://underactuated.mit.edu/)
- [MIT Underactuated notes: Acrobots, cart-poles, and swing-up](https://underactuated.mit.edu/acrobot.html)
- [Ascento: A Two-Wheeled Jumping Robot paper](https://arxiv.org/abs/1905.06334)
- [OpenCV camera calibration tutorial](https://docs.opencv.org/5.0/py_tutorials/py_calib3d/py_calibration/py_calibration.html)

Research papers provide models and methods, not guaranteed parameters for a team's hardware. Re-identify geometry, inertia, friction, delay, motor constants, and sensor behavior.

## Reference Project Inspiration

- [embedded-hardware-safety-review](https://github.com/016darling610/embedded-hardware-safety-review) - MIT-licensed hardware-safety review project that inspired the idea of making physical consequences explicit.

This project uses an independently written, broader contest workflow. If future contributions copy or adapt substantial material, preserve the source license and attribution.

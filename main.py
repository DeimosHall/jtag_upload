#!/bin/python3

import subprocess

# Ruta al archivo .sof que se programará en la FPGA Cyclone II
sof_file = "/home/deimos/Software dev/vhdl/blink/output_files/blink.sof"

# Comando de quartus_pgm para programar la FPGA Cyclone II mediante el USB-Blaster
quartus_pgm = "/home/deimos/altera/13.0sp1/quartus/bin/quartus_pgm"
cmd = f"{quartus_pgm} -m JTAG -c USB-Blaster -o 'p;{sof_file}'"

# Ejecutar el comando de quartus_pgm
subprocess.call(cmd, shell=True)

# Tengo este error pero si me aparece el usb blaster:

# ❯ ./main.py 
# Error (213013): Programming hardware cable not detected

# Software dev/python/jtag_uplaod via 🐍 v3.8.10 
# ❯ lsusb 
# Bus 001 Device 005: ID 0a5c:5800 Broadcom Corp. BCM5880 Secure Applications Processor
# Bus 001 Device 004: ID 1bcf:28ae Sunplus Innovation Technology Inc. Laptop Integrated Webcam HD
# Bus 001 Device 003: ID 8087:0a2a Intel Corp. 
# Bus 001 Device 002: ID 8087:8001 Intel Corp. 
# Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
# Bus 002 Device 003: ID 09fb:6001 Altera Blaster
# Bus 002 Device 002: ID 2563:0575 SHANWAN PS3/PC Gamepad
# Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

# ❯ /home/deimos/altera/13.0sp1/quartus/bin/quartus_pgm -a
# Info: *******************************************************************
# Info: Running Quartus II 32-bit Programmer
#     Info: Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Web Edition
#     Info: Copyright (C) 1991-2013 Altera Corporation. All rights reserved.
#     Info: Your use of Altera Corporation's design tools, logic functions 
#     Info: and other software and tools, and its AMPP partner logic 
#     Info: functions, and any output files from any of the foregoing 
#     Info: (including device programming or simulation files), and any 
#     Info: associated documentation or information are expressly subject 
#     Info: to the terms and conditions of the Altera Program License 
#     Info: Subscription Agreement, Altera MegaCore Function License 
#     Info: Agreement, or other applicable license agreement, including, 
#     Info: without limitation, that your use is for the sole purpose of 
#     Info: programming logic devices manufactured by Altera and sold by 
#     Info: Altera or its authorized distributors.  Please refer to the 
#     Info: applicable agreement for further details.
#     Info: Processing started: Tue Mar 21 22:03:24 2023
# Info: Command: quartus_pgm -a
# Info (213045): Using programming cable "USB-Blaster variant [2-2]"
# 1) USB-Blaster variant [2-2]
#   Unable to lock chain (Insufficient port permissions)

# Info: Quartus II 32-bit Programmer was successful. 0 errors, 0 warnings
#     Info: Peak virtual memory: 127 megabytes
#     Info: Processing ended: Tue Mar 21 22:03:25 2023
#     Info: Elapsed time: 00:00:01
#     Info: Total CPU time (on all processors): 00:00:00

# sudo usermod -aG plugdev tu_usuario

# Asegurarte de que el archivo /etc/udev/rules.d/51-usbblaster.rules exista y contenga lo siguiente:
# SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6001", MODE="0666"

# Después de hacer cualquier cambio en las reglas de udev, debes reiniciar el servicio udev para que los cambios tengan efecto:
# sudo service udev restart

# sudo chmod 777 /dev/bus/usb/002/003
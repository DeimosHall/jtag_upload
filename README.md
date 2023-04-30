# JTAG for Altera devices

This is a script to program Altera devices using the JTAG interface.

## Usage

If you run the script, you will get an error message

```
❯ ./main.py 
Error (213013): Programming hardware cable not detected
```

If we run `quartus_pgm -a`, we can see that the USB-Blaster is detected, but we don't have permission to access it.

```
❯ ./bin/quartus_pgm -a
Info: *******************************************************************
Info: Running Quartus II 32-bit Programmer
    Info: Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Web Edition
    Info: Copyright (C) 1991-2013 Altera Corporation. All rights reserved.
    Info: Your use of Altera Corporation's design tools, logic functions 
    Info: and other software and tools, and its AMPP partner logic 
    Info: functions, and any output files from any of the foregoing 
    Info: (including device programming or simulation files), and any 
    Info: associated documentation or information are expressly subject 
    Info: to the terms and conditions of the Altera Program License 
    Info: Subscription Agreement, Altera MegaCore Function License 
    Info: Agreement, or other applicable license agreement, including, 
    Info: without limitation, that your use is for the sole purpose of 
    Info: programming logic devices manufactured by Altera and sold by 
    Info: Altera or its authorized distributors.  Please refer to the 
    Info: applicable agreement for further details.
    Info: Processing started: Sun Apr 30 15:44:24 2023
Info: Command: quartus_pgm -a
Info (213045): Using programming cable "USB-Blaster variant [1-2]"
1) USB-Blaster variant [1-2]
  Unable to lock chain (Insufficient port permissions)

Info: Quartus II 32-bit Programmer was successful. 0 errors, 0 warnings
    Info: Peak virtual memory: 127 megabytes
    Info: Processing ended: Sun Apr 30 15:44:24 2023
    Info: Elapsed time: 00:00:00
    Info: Total CPU time (on all processors): 00:00:00
```

To fix this, we need to add a udev rule. Create a file called /etc/udev/rules.d/51-usbblaster.rules with the following content:

```
SUBSYSTEM=="usb", ATTR{idVendor}=="09fb", ATTR{idProduct}=="6001", MODE="0666"
```

Then, reload the udev rules:

```
sudo service udev restart
```

If the previous command doesn't work, try this one:

```
sudo service systemd-udevd restart
```

You will see something like this:

```
❯ sudo service systemd-udevd restart
Redirecting to /bin/systemctl restart systemd-udevd.service
```

We need to know the USB-Blaster device number. Run the following command:

```
lsusb
```

You will see something like this:

```
❯ lsusb
Bus 002 Device 005: ID 0a5c:5800 Broadcom Corp. BCM5880 Secure Applications Processor
Bus 002 Device 004: ID 1bcf:28ae Sunplus Innovation Technology Inc. Laptop Integrated Webcam HD
Bus 002 Device 003: ID 8087:0a2a Intel Corp. Bluetooth wireless interface
Bus 002 Device 002: ID 8087:8001 Intel Corp. Integrated Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 005: ID 0603:01fe Novatek Microelectronics Corp. Mechanical Keyboard
Bus 001 Device 004: ID 05e3:0606 Genesys Logic, Inc. USB 2.0 Hub / D-Link DUB-H4 USB 2.0 Hub
Bus 001 Device 006: ID 09fb:6001 Altera Blaster
Bus 001 Device 002: ID 046d:c08b Logitech, Inc. G502 SE HERO Gaming Mouse
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
````

What we are looking for is the device bus and device number. In this case, we have: Bus `001` Device `006`: ID 09fb:6001 Altera Blaster.

Now, we need to change the permissions of the USB-Blaster device:

```
sudo chmod 777 /dev/bus/usb/001/006
```

If we run quartus_pgm -a again, we will see that the device has permissions:

```
❯ ./bin/quartus_pgm -a
Info: *******************************************************************
Info: Running Quartus II 32-bit Programmer
    Info: Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Web Edition
    Info: Copyright (C) 1991-2013 Altera Corporation. All rights reserved.
    Info: Your use of Altera Corporation's design tools, logic functions 
    Info: and other software and tools, and its AMPP partner logic 
    Info: functions, and any output files from any of the foregoing 
    Info: (including device programming or simulation files), and any 
    Info: associated documentation or information are expressly subject 
    Info: to the terms and conditions of the Altera Program License 
    Info: Subscription Agreement, Altera MegaCore Function License 
    Info: Agreement, or other applicable license agreement, including, 
    Info: without limitation, that your use is for the sole purpose of 
    Info: programming logic devices manufactured by Altera and sold by 
    Info: Altera or its authorized distributors.  Please refer to the 
    Info: applicable agreement for further details.
    Info: Processing started: Sun Apr 30 16:53:58 2023
Info: Command: quartus_pgm -a
Info (213045): Using programming cable "USB-Blaster variant [1-2]"
1) USB-Blaster variant [1-2]
  020B10DD   EP2C5

Info: Quartus II 32-bit Programmer was successful. 0 errors, 0 warnings
    Info: Peak virtual memory: 127 megabytes
    Info: Processing ended: Sun Apr 30 16:53:58 2023
    Info: Elapsed time: 00:00:00
    Info: Total CPU time (on all processors): 00:00:00
```

Finally, we can run the script and program the device:

```
❯ ./main.py 
Warning (210120): Cyclone II information is incomplete. The ISP clamp functionality will be disabled.
Info: *******************************************************************
Info: Running Quartus II 32-bit Programmer
    Info: Version 13.0.1 Build 232 06/12/2013 Service Pack 1 SJ Web Edition
    Info: Copyright (C) 1991-2013 Altera Corporation. All rights reserved.
    Info: Your use of Altera Corporation's design tools, logic functions 
    Info: and other software and tools, and its AMPP partner logic 
    Info: functions, and any output files from any of the foregoing 
    Info: (including device programming or simulation files), and any 
    Info: associated documentation or information are expressly subject 
    Info: to the terms and conditions of the Altera Program License 
    Info: Subscription Agreement, Altera MegaCore Function License 
    Info: Agreement, or other applicable license agreement, including, 
    Info: without limitation, that your use is for the sole purpose of 
    Info: programming logic devices manufactured by Altera and sold by 
    Info: Altera or its authorized distributors.  Please refer to the 
    Info: applicable agreement for further details.
    Info: Processing started: Sun Apr 30 16:10:36 2023
Info: Command: quartus_pgm -m JTAG -c USB-Blaster -o p;/home/deimos/dev/vhdl/one_bit_comparator/output_files/comparator.sof
Info (213045): Using programming cable "USB-Blaster [1-2]"
Info (213011): Using programming file /home/deimos/dev/vhdl/one_bit_comparator/output_files/comparator.sof with checksum 0x00073B63 for device EP2C5T144@1
Info (209060): Started Programmer operation at Sun Apr 30 16:10:37 2023
Info (209016): Configuring device index 1
Info (209017): Device 1 contains JTAG ID code 0x020B10DD
Info (209007): Configuration succeeded -- 1 device(s) configured
Info (209011): Successfully performed operation(s)
Info (209061): Ended Programmer operation at Sun Apr 30 16:10:39 2023
Info: Quartus II 32-bit Programmer was successful. 0 errors, 1 warning
    Info: Peak virtual memory: 127 megabytes
    Info: Processing ended: Sun Apr 30 16:10:39 2023
    Info: Elapsed time: 00:00:03
Info: Total CPU time (on all processors): 00:00:00
```
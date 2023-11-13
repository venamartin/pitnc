# PiTNC

PiTNC provides a robust bluetooth and WIFI accessible TNC. When connected to a compatible mobile or base station full APRS and Winlink KISS interface is available on Bluetooth or a TCP/IP port.

The following APRS applications are supported: APRSDroid (Android), aprs.fi (iOS), YAAC (Windows and Mac), and Ham Tracks (Android).

# Required Components

| Item | Price (Aprox) | Purchase Link |
| ---- | ------------- | ------------- |
| Raspberry Pi W | $15.00 | https://www.pishop.us/product/raspberry-pi-zero-w/ |
| Micro USB Power Supply | $7.95 | https://www.pishop.us/product/wall-adapter-power-supply-micro-usb-2-4a-5-25v/ |
| 16Gb SD Card (larger okay) | $9.00 | https://a.co/d/7Zhavrw |
| Raspberry Pi Case | $9.99 | https://a.co/d/iUEp1YX |
| Micro USB to USB C cable | $6.00 | https://a.co/d/3dWxvo8 |
| Digirig | $50.00 | https://digirig.net/product/digirig-mobile/ |
| Digirig Interface Cable to Radio | ~$30.00 | Search for your radio and select the appropriate cable: https://digirig.net/store/ |
| Ferrites (Optional) | $9.99 | https://a.co/d/3dWxvo8 |

# Writing Raspberry Pi Image to SD Card using Win32 Disk Imager

## Steps

1. **Download and Install Win32 Disk Imager**
   - Visit the [official Win32 Disk Imager website](https://sourceforge.net/projects/win32diskimager/) to download the software.
   - Follow the installation instructions to install Win32 Disk Imager on your Windows computer.

2. **Insert SD Card**
   - Insert the blank SD card into your computer's SD card reader.

3. **Open Win32 Disk Imager**
   - Launch Win32 Disk Imager on your computer. You may need to run it as an administrator.

4. **Select Raspberry Pi Image File**
   - Click on the folder icon in the "Image File" field.
   - Navigate to and select your Raspberry Pi image file.

5. **Choose Target Device**
   - In the "Device" field, select the drive letter corresponding to your SD card. Be careful to choose the correct drive to avoid data loss.

6. **Write Image to SD Card**
   - Click the "Write" button to begin the writing process.
   - Confirm the action when prompted, as this will overwrite all data on the selected SD card.

7. **Wait for Completion**
   - Allow Win32 Disk Imager to complete the writing process. This may take some time, depending on the size of the image file.

8. **Verify Write Completion**
   - Once the process is complete, Win32 Disk Imager will display a confirmation message.
   - Safely eject the SD card from your computer.

9. **Insert SD Card into Raspberry Pi**
   - Insert the SD card into the Raspberry Pi's card slot.

10. **Power Up Raspberry Pi**
    - Power up your Raspberry Pi, and it should boot from the SD card with the flashed image.

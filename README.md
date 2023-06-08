# pitnc
Raspberry Pi TNC with Direwolf Configuration

Configuration
=============

1. Burn image to 16GB SD Card
2. Make the file system temporarily read/write
    ```
    sudo mount -o remount,rw /boot
    ```
4. Find your bluetooth MAC address
    ```
    hciconfig
    ```
3. Change the bluetooth name
    ```
    sudo nano /etc/machine-info   
    # add the following line
    PRETTY_HOSTNAME=pitnc <your BT MAC>
    ```
4. Change your callsign (not used but shoud do it anyway for future)
    ```
    nano ~/direwolf.conf
    
    # search for MYCALL=
    
    ```
6. Change WIFI 
    ```
    sudo raspi-config
    ```
    Choose System Options --> Wifi
    
    or Manually
    
    ```
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

    network={
    ssid="The SSID of your network (eg. Network name)"
    psk="Your Wifi Password"
    }
    ```
7. Reboot
    ```
    sudo reboot now
    ```
    
8. Make the system read only
    ```
    sudo raspi-config
    ```
   Select Performance Options --> Overlay File System
   

Monitor Direwolf
================

Log in to your raspberry pi first. Once logged in:
    ```
    sudo tmux attach -t direwolf
    ```
to exit
    ```
    CTRL-b d
    ```

To make file system read/write until reboot
============================================

    ```
    sudo mount -o remount,rw /boot
    ```

Service Method
==============

```
Install tmux

sudo apt install tmux
Code language: Bash (bash)
Now we can create our systemd unit: create the following file /etc/systemd/system/direwolf.service

You have to adapt the command line to fit your own needs i.e. path to your config file

[Unit]
Description=Direwolf
After=network.target

[Service]
Type=forking
#Modify the end of the line below to fit your own needs i.e path to your configuration file
ExecStart=/usr/bin/tmux new-session -d -s direwolf '/usr/local/bin/direwolf -c /home/pi/direwolf.conf'
Restart=always

[Install]
WantedBy=default.target
Code language: Makefile (makefile)
Next step enable the service

sudo systemctl enable direwolf.service
Code language: Bash (bash)
If everything went OK you can now start the service using

sudo systemctl start direwolf.service
Code language: Bash (bash)
To stop it

sudo systemctl stop direwolf.service
Code language: Bash (bash)
Request its status

sudo systemctl status direwolf.service
Code language: CSS (css)
To attach to the tmux terminal in order to watch direwolf do its thing

sudo tmux attach -t direwolf

```











Installation (incomplete)
=========================

Remove Pulse Audio
```
sudo apt-get remove --purge pulseaudio
sudo apt-get autoremove
rm -rf /home/pi/.pulse

sudo apt-get install cmake
sudo apt-get install libasound2-dev
sudo apt-get install libudev-dev

cd ~
git clone https://www.github.com/wb2osz/direwolf
cd direwolf
git checkout dev

mkdir build && cd build
cmake -DUNITTEST=1 ..
make -j4
make test
sudo make install

make install-conf


```

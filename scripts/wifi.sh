echo "Available WIFI networks:" 
sudo iwlist wlan0 scan | grep "ESSID" | sort -u

echo "To add the network: "
echo "     $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf"
echo ""
echo 'With the following format:
    network={
    ssid="The SSID of your network (eg. Network name)"
    psk="Your Wifi Password"
    }'

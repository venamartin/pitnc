#!/bin/bash
if [ -e /etc/machine-info ]
then
    echo "BT name is set"
else
    echo "BT name is being generated"
    sudo raspi-config nonint do_overlayfs 0
    echo -n 'PRETTY_HOSTNAME=pitnc ' > machine-info
    hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}" >> machine-info
    sudo mv ./machine-info /etc/machine-info
    sudo raspi-config nonint do_overlayfs 1
fi

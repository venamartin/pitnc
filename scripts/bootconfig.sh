#!/bin/bash
sleep 3

BOOT_CONF="/boot/pitnc.conf"
BOOT_CONF_LOCAL="/home/tnc/.pitnc/pitnc.conf"
PITNC="/home/tnc/dev/pitnc/pitnc.py"

#if df -h | grep 'overlay'; then
	# disable read only file system
	#echo "In read only mode."
#	sleep 1
#else

	if [ -e $BOOT_CONF ]
	then
		if cmp -s $BOOT_CONF $BOOT_CONF_LOCAL; then
			#echo "files match"
			sleep 1
		else
			# files dont match, do update
			sudo cp $BOOT_CONF $BOOT_CONF_LOCAL
			#echo "copied over to local"
			sudo python3 $PITNC --bootwifi 
			sudo wpa_cli -i wlan0 reconfigure
			sudo cat /etc/wpa_supplicant/wpa_supplicant.conf
			echo " "
			sleep 1
		fi
	fi
		
#fi


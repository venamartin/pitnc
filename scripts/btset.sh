#!/bin/bash
sleep 30

MACHINE_INFO_LOCAL="/home/tnc/dev/pitnc/scripts/machine-info"
MACHINE_INFO_SYSTEM="/etc/machine-info"


if df -h | grep 'overlay'; then
	# disable read only file system
	#echo "In read only mode."
	sleep 1
else

	sudo echo -n "PRETTY_HOSTNAME=pitnc " > $MACHINE_INFO_LOCAL
    hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}" >> $MACHINE_INFO_LOCAL
	if cat $MACHINE_INFO_LOCAL | grep ":" > /dev/null ; then 
		if [ -e $MACHINE_INFO_SYSTEM ]
		then
			if cmp -s $MACHINE_INFO_LOCAL $MACHINE_INFO_SYSTEM; then
				#echo "Bluetooth name matches MAC"
				sleep 1
			else
				sudo mv $MACHINE_INFO_LOCAL $MACHINE_INFO_SYSTEM
				service bluetooth restart
				#echo "Bluetooth name set."
				sleep 1
			fi
		else
			
			sudo mv $MACHINE_INFO_LOCAL $MACHINE_INFO_SYSTEM
			service bluetooth restart
			#echo "Bluetooth name set."
			 
		fi

		
	else
		sleep 1
		#echo "Bluetooth MAC not detected"
	fi
fi


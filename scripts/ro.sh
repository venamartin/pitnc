if df -h | grep 'overlay'>/dev/null; then
        echo -e "Already in read only mode."
else
	echo -e "Setting read only mode..."
	
	sudo raspi-config nonint do_overlayfs 0

	read -p "Reboot required. Reboot now? [Y/n]: " yn

	while true; do
		case $yn in 
			[yY] ) echo "Rebooting...";
			sudo reboot;
			break;;

			* ) echo "Reboot is required to enter read only mode. Type: sudo reboot";
			exit;;
		esac        
	done	
fi


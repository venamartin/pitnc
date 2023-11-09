
if df -h | grep 'overlay'>/dev/null; then
        echo "Setting read/write mode..."

	sudo raspi-config nonint do_overlayfs 1

        read -p "Reboot required. Reboot now? [Y/n]: " yn

        while true; do
                case $yn in
                        [yY] ) echo "Rebooting...";
                        sudo reboot;
                        break;;

                        * ) echo "Reboot is required to enter read/write mode. Type: sudo reboot";
                        exit;;
                esac
        done
else
        echo "Already in read/write mode."

fi


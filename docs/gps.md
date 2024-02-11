# Installation of gpsd

Run the following from the command prompt:

```console
sudo apt-get update
sudo apt-get install gpsd gpsd-clients
```


# configure gpsd

1. Edit the following file

```console
$ sudo micro /etc/default/gpsd
```

2. Edit as follows:

```console
# Devices gpsd should collect to at boot time.
# They need to be read/writeable, either by user gpsd or the group dialout.
DEVICES="/dev/ttyACM0"

# Other options you want to pass to gpsd
GPSD_OPTIONS=""

# Automatically hot add/remove USB GPS devices via gpsdctl
USBAUTO="false"
```

3. Restart

```console
$ sudo reboot
```


# To monitor

```console
$ cgps -s
```

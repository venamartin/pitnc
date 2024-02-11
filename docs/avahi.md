# Broadcast on Avahi

This will allow aprsdroid and aprs.fi to find the PiTNC without typing in the ip address. I believe YAAC will also do the same.

```console
$ cd /etc/avahi/services

$ sudo nano direwolf-agwpe.service
```

Insert the following

```
<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
<name replace-wildcards="yes">%h Direwolf AGWPE</name>
<service>
<type>_agwpe._tcp</type>
<port>8000</port>
</service>
</service-group>
```

Then add for KISS.

```console
$ sudo nano direwolf-kiss.service
```

Insert the following:

```
<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
<name replace-wildcards="yes">%h Direwolf KISS</name>
<service>
<type>_kiss-tnc._tcp</type>
<port>8001</port>
</service>
</service-group>
```

Then restart the service

```console
$ sudo systemctl restart avahi-daemon.service
```

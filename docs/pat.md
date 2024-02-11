# Pat Config

Modify the pat config file

```console
$ pat configure
```

Modify or add:

- mycall
- secure_login_password
- locator
- http_addr (to 0.0.0.0:8080)
- ax25 - engine to agwpe

Example config file:

```json

{
  "mycall": "KN6GWQ",
  "secure_login_password": "xxxxxxx",
  "auxiliary_addresses": [],
  "locator": "CM96dw",
  "service_codes": [
    "PUBLIC"
  ],
  "http_addr": "0.0.0.0:8080",
  "motd": [
    "Open source Winlink client - getpat.io"
  ],
  "connect_aliases": {
    "telnet": "telnet://{mycall}:CMSTelnet@cms.winlink.org:8772/wl2k"
  },
  "listen": [],
  "hamlib_rigs": {},
  "ax25": {
    "engine": "agwpe",
    "rig": "",
    "beacon": {
      "every": 3600,
      "message": "Winlink P2P",
      "destination": "IDENT"
    }
  },
  "ax25_linux": {
    "port": "wl2k"
  },
  "agwpe": {
    "addr": "localhost:8000",
    "radio_port": 0
  },
  "serial-tnc": {
    "path": "/dev/ttyUSB0",
    "serial_baud": 9600,
    "hbaud": 1200,
    "type": "Kenwood",
    "rig": ""
  },
  "ardop": {
    "addr": "localhost:8515",
    "arq_bandwidth": {
      "Forced": false,
      "Max": 500
    },
    "rig": "",
    "ptt_ctrl": false,
    "beacon_interval": 0,
    "cwid_enabled": true
  },
  "pactor": {
    "path": "/dev/ttyUSB0",
    "baudrate": 57600,
    "rig": "",
    "custom_init_script": ""
  },
  "telnet": {
    "listen_addr": ":8774",
    "password": ""
  },
  "varahf": {
    "addr": "localhost:8300",
    "bandwidth": 2300,
    "rig": "",
    "ptt_ctrl": false
  },
  "varafm": {
    "addr": "localhost:8300",
    "bandwidth": 0,
    "rig": "",
    "ptt_ctrl": false
  },
  "gpsd": {
    "enable_http": false,
    "allow_forms": false,
    "use_server_time": false,
    "addr": "localhost:2947"
  },
  "schedule": {},
  "version_reporting_disabled": false
}
```

# Running Pat HTTP

To start Pat as a http server in listening mode:

```console
$ pat --listen ax25 http
```

Or enable permanently through the configuration file:

```json
{
  ...
  "listen": ["ax25"],
  ...
}
```

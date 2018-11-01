## Raspberry

### IrDa configuration
https://hackernoon.com/make-your-tv-voice-controlled-through-amazon-alexa-and-raspberry-pi-a6373b7cf871
First install the librery in the raspberry
```
sudo apt-get install lirc
```

Then configure the modules and adding the IrDA

```
sudo nano /etc/modules
```
```
## /etc/modules
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
```
Add the reference to lirc
```
sudo nano /etc/lirc/hardware.conf
```

```
## /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"
# Don't start lircmd even if there seems to be a good config file
# START_LIRCMD=false
# Don't start irexec, even if a good config file seems to exist.
# START_IREXEC=false
# Try to load appropriate kernel modules
LOAD_MODULES=true
# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```
Change the boot file:
```
sudo nano /boot/config.txt
```

```
## /boot/config.txt 
dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
```
Change the boot file:
```
sudo nano /etc/lirc/lirc_options.conf
```
driver = devinput to default
```
## /etc/lirc/lirc_options.conf
driver          = default
```
Reset the service
```
sudo /etc/init.d/lircd restart
```
Next configure the lircd.conf (For generate that file check /etc/lirc/lircd.conf)

## install pip
```
sudo apt-get install python-pip
```
## install libffi and cryptography for flask-ask
```
sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
pip install 'cryptography<2.2'
```
## Create website
```
nano ~/www/website.py
```
## Create service
```
nano /lib/systemd/system/website.service 
```
```
[Unit]
Description=Flask Server
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/www/website.py
Restart=on-abort
User=pi

[Install]
WantedBy=multi-user.target
```
```
nano /lib/systemd/system/websitetunel.service 
```
```
[Unit]
Description=Tunel Server
After=multi-user.target

[Service]
Type=simple
ExecStart=/home/pi/www/ngrok http 4040
Restart=on-abort
User=pi

[Install]
WantedBy=multi-user.target
```
# CarPC

THANK YOU SO MUCH. This fixed my problem of the touch events not being
recognized when being run as a super user!

https://github.com/mrichardson23/rpi-kivy-screen

### Dependencies
1. Cython
2. kivy
3. Bibliopixel
4. decoder - http://www.brailleweb.com/cgi-bin/python.py?module=decoder.py#download
5. obd
6. pyserial - MUST BE NEWEST (pip install pyserial --upgrade)

### Bluetooth setup (Raspberry pi - Headless)
You must run bluetoothctl to pair to the bluetooth device
``` sudo bluetoothctl ```
Once you're in the CLI, type the following
```
power on
pairable on
discoverable on
agent on
default-agent
scan on
```
Once you see the device you're trying to connect to, type this
```
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
```
Your device should now be paired and trusted. 
You can also try to connect, but I've had problems with this. I normally just use rfcomm commands to bind to a /dev device
```
sudo rfcomm bind /dev/rfcomm0 XX:XX:XX:XX:XX:XX
```

### Copying service file to allow auto start up
In order for this script to be run as a service, you need to move the .service file to the system.
In order to do that, you need to copy the provided .service file to /etc/systemd/system
```
sudo cp ./CarPC.service /etc/systemd/system/
```
Then, you need to enable the script
```
sudo systemctl enable CarPC.service
```
Now, in order for your changed to take effect, two more commands need to be run
```
sudo systemctl daemon-reload
sudo systemctl start CarPC.service
```
The CarPC should now run on start up!

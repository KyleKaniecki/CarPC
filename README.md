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
1. You must run bluetoothctl to pair to the bluetooth device
``` sudo bluetoothctl ```
2. Once you're in the CLI, type the following
```
power on
pairable on
discoverable on
agent on
default-agent
scan on
```
3. Once you see the device you're trying to connect to, type this
```
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
```
4. Your device should now be paired and connected. 
5. You can also try to connect, but I've had problems with this. I normally just use rfcomm commands to bind to a /dev device
```
sudo rfcomm bind /dev/rfcomm0 XX:XX:XX:XX:XX:XX
```


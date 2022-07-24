from machine import Pin, UART, I2C
#Import utime library to implement delay
import utime, time

from micropyGPS import MicropyGPS
#https://github.com/inmcm/micropyGPS.py
#________________________________________________________
import tm1637
tm = tm1637.TM1637(clk=Pin(26), dio=Pin(27))

##########################################################
#GPS Module UART Connection
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
##########################################################
##########################################################
TIMEZONE = 3
my_gps = MicropyGPS(TIMEZONE)
##########################################################
##########################################################
while True:
    #_________________________________________________
    length = gps_module.any()
    if length>0:
        b = gps_module.read(length)
        for x in b:
            msg = my_gps.update(chr(x))
    #_________________________________________________
    t = my_gps.timestamp
    #t[0] => hours : t[1] => minutes : t[2] => seconds
    gpsTime = '{:02d}:{:02d}:{:02}'.format(t[0], t[1], t[2])
    gpsdate = my_gps.date_string('long')
    speed1 = my_gps.speed_string('kph') #'kph' or 'mph' or 'knot'
    speed = round(my_gps.speed[2])
    if speed<3: speed=0
    #_________________________________________________
    print('time:', gpsTime)
    print('Date:', gpsdate)
    print('speed:', speed1)
    #n = len(my_gps.satellites_visible())
    #print(n)
    #print(my_gps.satellites_visible())
    #_________________________________________________
    
    tm.number(speed)
    #_________________________________________________
    
##########################################################
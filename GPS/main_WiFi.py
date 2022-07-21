from machine import UART, Pin
import time
from esp8266 import ESP8266

esp01 = ESP8266()
esp8266_at_ver = None

led=Pin(25,Pin.OUT)
A=[['SAN','ZTE54','LEDE'],['37212628','121211119','121211119'],[0,0,0]]
#print("StartUP",esp01.startUP())
#print("ReStart",esp01.reStart())
print("Hello: ",esp01.startUP())
#print("Echo-Off",esp01.echoING())
#print("\r\n")

'''
Print ESP8266 AT comand version and SDK details
'''
#esp8266_at_var = esp01.getVersion()
#if(esp8266_at_var != None):
#    print(esp8266_at_var)

'''
set the current WiFi in SoftAP+STA
'''
#esp01.setCurrentWiFiMode()

apList = esp01.getAvailableAPs()
for items in apList:
    #print(items)
    for item in tuple(items):
        #print(item)
        for j in range(3):
            #print(item)
            #print(A[0][j])
            if item=='"'+A[0][j]+'"':
                #print(item)
                A[2][j]=1
                #print(A[0][j])
                      
#print("\r\n")

'''
Connect with the WiFi
'''
#print("Try to connect...")
conn=False
while (1):
    for i in range(3):
        for j in range(3):
            if A[2][i]==1:
                print("Try to connect...")
                print(A[0][i])
                #print(A[1][i])
                if "WIFI CONNECTED" in esp01.connectWiFi(A[0][i],A[1][i]):#esp01.connectWiFi("LEDE","121211119"):
                    print("Connected.")
                    conn=True
                    break
                else:
                    time.sleep(5)
            if conn:
                 break
        if conn:
            break        


#print("\r\n")
print("Start HTTP Operation")

while(1):    
    led.toggle()
    #time.sleep(1)
    
    '''
    Going to do HTTP Get Operation with www.httpbin.org/ip, It return the IP address of the connected device
    '''
    httpCode, httpRes = esp01.doHttpGet("lz42.ru","/ab.php","RaspberryPi-Pico", port=80)
    print("------------- ------------------Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n")
    break
    
    '''
    Going to do HTTP Post Operation with www.httpbin.org/post
    '''
    post_json="abcdefghijklmnopqrstuvwxyz"  #"{\"name\":\"Noyel\"}"
    httpCode, httpRes = esp01.doHttpPost("www.httpbin.org","/post", "application/json",post_json,"RPi-Pico",port=80)
    print("------------- www.httpbin.org/post Post Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n")
    break
    


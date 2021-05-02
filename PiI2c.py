mport smbus
import time

bus = smbus.SMBus(1)#I2C1 port


def getLightLevel():
    bus.write_byte(0x23,0x23)# sending byte to pi
    return bus.read_byte(0x23)# reading byte data

time.sleep(0.5)

while(True):
            print(getLightLevel())
                              
            if getLightLevel() < 1:
                print(" Too Dark")
               
            elif getLightLevel() >= 1 and getLightLevel() < 5:
                print("Dark")
               
            elif getLightLevel() >= 5 and getLightLevel() < 10:
                print("Medium")
                
            elif getLightLevel() >= 10 and getLightLevel() < 20:
                print("Bright")
                
            elif getLightLevel() >=20:
                print("Too Bright")
               
                
            time.sleep(0.5)
            



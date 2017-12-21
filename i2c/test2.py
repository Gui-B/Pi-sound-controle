from pcf8574 import PCF8574
import time

i2c_port_num = 1
pcf_address = 0x39
pcf = PCF8574(i2c_port_num, pcf_address)
print pcf.port
time.sleep(2)

pcf.port[7] = False
print pcf.port[7]
time.sleep(2)
pcf.port[7] = True
print pcf.port[7]
time.sleep(2)

pcf.port[7] = False
print pcf.port
time.sleep(2)



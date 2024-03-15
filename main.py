import serial

try:
    ser = serial.Serial()
    ser.port = "COM8"
    ser.baudrate = 115200
    ser.open()
    
    ser.write(b"config address 1.2.3.4.5.6.7.8\n")
    ser.write(b"config mode anchor\n")
    
except serial.SerialException as e:
    print("Error: ", e)
finally:
    ser.close()

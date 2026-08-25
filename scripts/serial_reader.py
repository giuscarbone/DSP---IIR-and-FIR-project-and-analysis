import serial 
import time

ser = serial.Serial("COM3", 115200) #reading from COM3 port at 115200 baud (synched with ESP32)

file = open("data.csv", "w") #opening data file in writing mode

time.sleep(2)

print("Reading data, CTRL + C to stop\n")

#tries to execute the while block
try: 
    while True:
        line = ser.readline().decode().strip() #reading the line

        #if line is not empty, save it
        if line != "":
            print(line)
            file.write(line + "\n")
            file.flush()

#if user executes CTRL + C, stop the reading of data
except KeyboardInterrupt:
        print("Reading stopped\n")

        file.close()
        ser.close()
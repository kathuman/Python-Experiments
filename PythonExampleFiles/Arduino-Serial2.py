import serial
ser = serial.Serial('COM3', 9600)
i = 0
while True:
    print ser.readline()
    
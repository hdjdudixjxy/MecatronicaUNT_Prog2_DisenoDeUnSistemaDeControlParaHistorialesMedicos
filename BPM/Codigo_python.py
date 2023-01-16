import time
import serial
serialArduino = serial.Serial('COM3', 115200)
time.sleep(1)
while True:
    val = serialArduino.readline().decode('ascii')
    A = "Su pulso cardiaco es:"
    print(A, val)
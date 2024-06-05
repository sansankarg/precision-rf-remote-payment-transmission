import serial
from update_server import sendToServer
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            payload = ser.readline().decode('utf-8').rstrip()
            print(payload)
            print(type(payload))
            sendToServer(payload)


import serial

from time import time
from time import strftime

def main():
	# configure the serial connections (the parameters differs on the device you are connecting to)

	# Choose ttyACM1 or ttyACM0 based on what usb is connected
	ser = init_serial('/dev/ttyACM1')
	# ser = init_serial('/dev/ttyACM0')
	f = init_print_to_file()

	start = False

	try:
		while True :
			data = ''
			while ser.inWaiting() > 0:
				data = str(ser.readline(1))
				if '\n' in str(data): start = True # Make sure to start at a new line
				if data != '' and start: f.write(data)

	except Exception, e:
		print 'Exeption in main:', e
		raise
	finally:
		ser.close()

def init_serial(port):

    ser = serial.Serial(
        port,
        # baudrate = 115200,
        baudrate=250000, # Make sure this correspond to the Arduino
        parity = serial.PARITY_ODD,
        stopbits = serial.STOPBITS_TWO,
        bytesize = serial.SEVENBITS
    )

    if(ser.isOpen() == False):
        ser.open()

    return ser

def init_print_to_file():
	# give the initial time of the program as input, the time is
	# given as microseconds after initialization, making it easier
	# to syncronize the clock with the arduino's.
	t0 = str(long(1000000 * time()));
	filename = 'raw-data/' + t0 +'.txt'

	print t0
    
	# filename = 'raw-data/' + 'test' +'.txt' # For debugging

	f = open(filename, 'w')    
	return f

if __name__ == '__main__':
    main()
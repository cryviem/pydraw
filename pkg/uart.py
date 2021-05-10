from serial import Serial
from serial.tools.list_ports import comports
from pkg.logger import log

VID_CP210X = 4292

class uart:
    def __init__(self):
        for myport in comports():
            if myport.vid == VID_CP210X:
                self.hdr = Serial(port= myport.name, baudrate=115200, timeout=1)
                log.info('connected to %s', myport.name)
                break
        else:
            raise Exception('COM port not found')

    def send(self, data):
        self.hdr.write(data.encode('utf-8'))

    def receive(self):
        return self.hdr.readline().decode('utf-8').strip()



import snap7
from snap7.util import get_real
from snap7.snap7types import areas

class S71200:
    def __init__(self, ip):
        self.ip = ip
        self.plc = snap7.client.Client()

    def connect(self):
        self.plc.connect(self.ip, 0, 1)
        if self.plc.get_connected():
            print("Connected to S7-1200: CPU 1215C AC/DC/RLY")
        else:
            print("Failed to connect to S7-1200")

    def read(self, db_number, start, size):
        if self.plc.get_connected():
            try:
                data = self.plc.read_area(areas['DB'], db_number, start, size)
                buffer = []
                for i in range(start, (start+13), 4):
                    buffer.append(get_real(data, i))
                temp1, temp2, hum1, hum2 = buffer
                return temp1, temp2, hum1, hum2
            except:
                print("Failed read Data Block S7-1200")
                return None
            # finally:
            #     self.plc.disconnect()
        else:
            return None

import pyserial as serial
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

class PM:
    def __init__(self, port, baudrate):
        self.client = ModbusClient(
            method='rtu', 
            port=port, 
            baudrate=baudrate,
            stopbits=1, 
            bytesize=8, 
            parity='N', 
            timeout=10)

    def connect(self):
        self.client.connect()
        if self.client.connect():
            print("Connected to powermeter via Modbus RTU")
        else:
            print("Failed to connect to powermeter")
    
    def disconnect(self):
        self.client.close()

    def validator(reg):
        if not reg.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(
                reg.registers, 
                byteorder=Endian.Big,
                wordorder=Endian.Little
            )
            return decoder.decode_32bit_float()
        else:
            return None
 
    def read(self, addr, length):
        result = self.client.read_input_registers(addr, length, unit=1)
        if not result.isError():
            return validator(result)
        else:
            print("Error reading from powermeter")
            return None

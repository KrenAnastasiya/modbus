#!/usr/bin/env python
'''
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

    with ModbusClient('127.0.0.1') as client:
        result = client.read_coils(1,10)
        print result
'''
#---------------------------------------------------------------------------# 
# import the various server implementations
#---------------------------------------------------------------------------# 
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.client.sync import ModbusUdpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#---------------------------------------------------------------------------# 
# configure the client logging
#---------------------------------------------------------------------------# 
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)


client = ModbusClient('localhost', port=5020)

client.connect()


#---------------------------------------------------------------------------#
log.debug("Reading Coils")
rr = client.read_coils(1, 1, unit=0x01)



log.debug("Write to a holding register and read back")
rq = client.write_register(1, 10, unit=1)
#rq = client.write_register(17, 2, unit=1)
rr = client.read_holding_registers(1, 1, unit=1)
#rr = client.read_holding_registers(1, 1, unit=1)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers[0] == 10)       # test the expected value
print(rr.registers[0])
#log.debug("Write to multiple holding registers and read back")
#rq = client.write_registers(1, [10]*8, unit=1)
#rr = client.read_holding_registers(1, 8, unit=1)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers == [10]*8)      # test the expected value

log.debug("Read input registers")
rr = client.read_input_registers(1, 8, unit=1)
assert(rq.function_code < 0x80)     # test that we are not an error

#arguments = {
#    'read_address':    1,
#    'read_count':      8,
#    'write_address':   1,
#    'write_registers': [20]*8,
#}
#log.debug("Read write registeres simulataneously")
#rq = client.readwrite_registers(unit=1, **arguments)
#rr = client.read_holding_registers(1, 8, unit=1)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rq.registers == [20]*8)      # test the expected value
#assert(rr.registers == [20]*8)      # test the expected value

#---------------------------------------------------------------------------# 
# close the client
#---------------------------------------------------------------------------# 
client.close()
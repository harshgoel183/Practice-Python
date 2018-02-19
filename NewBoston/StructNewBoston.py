from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)#here we are storing 2 intergers and 1 float
                            # hence ii and f
print(packed_data)#byte data

print(calcsize('i'))#how many bytes are needed to store a value
print(calcsize('f')) # 4
print(calcsize('iif'))# 4i + 4i + 4f = 12
#to get byte data to normal

original_data = unpack('iif', packed_data)#iif taken in same format
print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))

import socket
import struct
s = socket.socket()
s.connect(("vortex.labs.overthewire.org", 5842))

sum = 0
for i in range(4):
    data = struct.unpack("<I", s.recv(4))[0]
    sum += data
  
print (sum)
print (struct.pack("<I", sum))
s.send(struct.pack("<I", sum))
print (s.recv(1024))


# Username: vortex1 Password: Gq#qu3bF3
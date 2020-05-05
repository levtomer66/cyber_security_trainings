import socket
s = socket.socket()
s.connect(("127.0.0.1", 9007))

def ie_scale(start, end):
        expected = (end-start)*10
        print ("Expected %s, sending range %s to %s" % (expected,start,end))
        s.send(' '.join([str(i) for i in range(start,end)]))
        s.send("\x0a\x0d")
        result = int(s.recv(1024).decode('utf-8'))
        print ("Got result: %s" % (result))
        return result == expected

def solve(data):
        coins, tries = [int(i) for i in data.replace('N=', '').replace('C=','').split(' ')]
        print ("Coins: %s, Tries: %s" % (coins, tries))
        mid = coins / 2
        start = 0
        end = coins
        while tries > 0:
                if ie_scale(start, mid):
                        start = mid
                        mid = (mid+end)/2
                else:
                        end = mid
                        mid = (start+mid) / 2
                tries -= 1
        if mid == start or mid == end:
                print ("Found coin is %s" % (mid))
                s.send(str(mid) + "\x0a\x0d")
                data = s.recv(1024)
                print (data.decode('utf-8'))


while True:
        data = s.recv(1024)
        if not data:
                break
        sdata = data.decode('utf-8')
        if sdata.startswith('N'):
                solve(sdata)
        else:
                print (sdata)
                
                # b1NaRy_S34rch1nG_1s_3asy_p3asy
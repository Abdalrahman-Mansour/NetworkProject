from socket import *
serverPort = 9000 # port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) #use loacl host
serverSocket.listen(1)
d={} #dictinary
with open('Smart phones.txt') as fi: #read the file tat contains the Smart phones in dictionary
    for line in fi:
        (key, val) = line.split(';')
        val=str(val).split('$')
        d[key] = int(val[0])
Sorted_name = sorted(d.items(), key=lambda t: t[0])
sorted_price = sorted(d.items(), key=lambda t: t[1])
print "The server is ready to receive "
while True:
    connectionSocket, addr = serverSocket.accept() #accept connection
    sentence = connectionSocket.recv(4096).decode()# decode the reqested
    list=sentence.split(' ')
    request=list[1]
    print request
    ip   = addr[0]
    port = addr[1]
    print addr
    print sentence
    #if statmenst to check the reqests .
    if (request.lower()==('/Index.html'.lower()) ):
        #send the responce
      connectionSocket.send("HTTP/1.1 200 Ok \r \n")
      connectionSocket.send(' Content-Type: text/html   \r \n') #send the contennt type .
      connectionSocket.send('\r\n')
      f = open("index.html", "rb")
      connectionSocket.sendall(f.read())


    elif (request.lower()=='/Imagename.png'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/png  \r \n')
        connectionSocket.send('\r\n')
        f = open("NET.png", "rb")
        connectionSocket.send(f.read())

    elif (request.lower()=='/Imagename.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("Networks.jpg", "rb")
        connectionSocket.send(f.read())
    elif (request.lower()=='/SortName'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: text/html  \r \n')
        connectionSocket.send('\r\n')
        s='<html  ><head><style> * {margin: 0;padding: 0;font-family: monospace;}body {width: 75%;margin: 0 auto;' \
          'background-color: #eee;}h1 {text-align: center;font-size: 60;}</style><title> Sorted By Name </title> </head><body> <H1> <b> The Smart phones : </b> </H1><OL style="font-size:30px; Color:blue;"><LI> ' + str(Sorted_name.__getitem__(0) .__getitem__(0) )+'   ' + str(Sorted_name.__getitem__(0) .__getitem__(1) ) +'<LI> ' + str(Sorted_name.__getitem__(1) .__getitem__(0) )+'   ' + str(Sorted_name.__getitem__(1) .__getitem__(1) )+'<LI> ' + str(Sorted_name.__getitem__(2) .__getitem__(0) )+'   ' + str(Sorted_name.__getitem__(2) .__getitem__(1) )+'<LI> ' + str(Sorted_name.__getitem__(3) .__getitem__(0) )+'   ' + str(Sorted_name.__getitem__(3) .__getitem__(1) )+'<LI> ' + str(Sorted_name.__getitem__(4) .__getitem__(0) )+'   ' + str(Sorted_name.__getitem__(4) .__getitem__(1) )+'</OL></body> </html>'
        connectionSocket.send(s)
    elif(request.lower()=='/SortPrice'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: text/html  \r \n')
        connectionSocket.send('\r\n')
        s='<html  ><head ><style> * {margin: 0;padding: 0;font-family: monospace;}body {width: 75%;margin: 0 auto;' \
          'background-color: #eee;}h1 {text-align: center;font-size: 60;}</style><title> Sorted By Price </title> </head><body> <H1> <b> The Smart phones : </b> </H1><OL style="font-size:30px; Color:blue;"><LI> ' + str(sorted_price.__getitem__(0) .__getitem__(0) )+'     ' + str(sorted_price.__getitem__(0) .__getitem__(1) ) +'<LI> ' + str(sorted_price.__getitem__(1) .__getitem__(0) )+'   ' + str(sorted_price.__getitem__(1) .__getitem__(1) )+'<LI> ' + str(sorted_price.__getitem__(2) .__getitem__(0) )+'     ' + str(sorted_price.__getitem__(2) .__getitem__(1) )+'<LI> ' + str(sorted_price.__getitem__(3) .__getitem__(0) )+'     ' + str(sorted_price.__getitem__(3) .__getitem__(1) )+'<LI> ' + str(sorted_price.__getitem__(4) .__getitem__(0) )+'     ' + str(sorted_price.__getitem__(4) .__getitem__(1) )+'</OL></body> </html>'
        connectionSocket.send(s)
    elif(request.lower()=='/png-image.png'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/png  \r \n')
        connectionSocket.send('\r\n')
        f = open("png-image.png", "rb")
        connectionSocket.send(f.read())
    elif (request.lower() == '/jpg-image.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("jpg-image.jpg", "rb")
        connectionSocket.send(f.read())
    elif (request.lower() == '/backgroun.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("backgroun.jpg", "rb")
        connectionSocket.send(f.read())
    elif (request.lower() == '/xa.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("xa.jpg", "rb")
        connectionSocket.send(f.read())
    elif (request.lower() == '/abed.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n") #Send  status .
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("abed.jpg", "rb")
        connectionSocket.send(f.read())
    elif (request.lower() == '/ahmad.jpg'.lower()):
        connectionSocket.send("HTTP/1.1 200 Ok \r \n")
        connectionSocket.send('Content-Type: image/jpg  \r \n')
        connectionSocket.send('\r\n')
        f = open("ahmad.jpg", "rb")
        connectionSocket.send(f.read())
    else:
        connectionSocket.send("HTTP/1.1 404 Not Found \r \n")
        connectionSocket.send('Content-Type: text/html  \r \n')
        connectionSocket.send('\r\n')
        #HTML file contains the error and groub members and   ID and IP and port for cliner
        S='<html lang="en"><head><style> * {margin: 0;padding: 0;font-family: monospace;}body {width: 75%;margin: 0 auto;' \
          'background-color: #eee;}h1 {text-align: center;font-size: 60;}</style><title>Erorr</title><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">' \
          '<meta name="viewport" content="width=device-width, initial-scale=1.0"><style> body {   width: 75%; margin: 0 auto;  font-family: monospace; }' \
          '.a {height: 100vh;}h1 { margin: 1% 2%;font-size: 60px;text-align: center}h2 {margin: 1% 2%;margin-top: 5%;font-size: 35px;}' \
          'ul {margin-top: 3%;}ul li {margin: 1% 2%;font-size: 25px;}</style></head><body><div class="a"><h1> page not found</h1>' \
          '<section class ="page-content"><h2> Group members</h2><ul><b><li> Abdalrahman Mansour 1182955 </li><li> Ahmad Hamzah 1181751 </li><li>Mohamad abuzeina 1181965 </li></b></ul><footer class="page-footer"> ' \
          '<p style="font-size : 24px;color:red;"><b> IP: ' + str(ip)+"&nbsp;&nbsp;&nbsp; Port :"+str(port) + '</b></p></footer></section></div>'
        connectionSocket.send(S)
    connectionSocket.close()
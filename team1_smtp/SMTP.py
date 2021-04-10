from socket import *
import ssl
import base64
import getpass
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587) #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('HELO: 250 reply not received from server.')

# Issue a STARTTLS command
command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recvA = clientSocket.recv(1024).decode()
print(recvA)
if recvA[:3] != '220':
    print('STARTTLS: 220 reply not received from server.')

############# Authentication #############
scc = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

scc.send(('auth login\r\n').encode())
print(scc.recv(1024).decode())

# enter the email address
email = getpass.getpass("Email:")

scc.send((base64.b64encode(email.encode()))+('\r\n').encode())
print(scc.recv(1024).decode())

# enter the application password
password = getpass.getpass("Password:")

scc.send((base64.b64encode(password.encode()))+('\r\n').encode())
print(scc.recv(1024).decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailCommand = 'MAIL FROM: <teamNO1@gmail.com> \r\n'
print(mailCommand)
scc.send(mailCommand.encode())
recv2 = scc.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('MAIL FROM: 250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
RCPTCommand = 'RCPT TO: <userDest@gmail.com> \r\n'
print(RCPTCommand)
scc.send(RCPTCommand.encode())
recv3 = scc.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('RCPT TO: 250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
print(dataCommand)
scc.send(dataCommand.encode())
recv4 = scc.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('DATA: 354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
Subject= "Input: "
Text= "Hello from Team #1"
msgCommand = Subject+"\r\n\r\n"+Text+"\r\n"
scc.send(msgCommand.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
scc.send(endmsg.encode())
recv5 = scc.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('endmsg: 250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
scc.send(("QUIT\r\n").encode())
recv6 = scc.recv(1024).decode()
print(recv6)
scc.close()
if recv6[:3] != '221':
    print('Quit: 221 reply not received from server.')
# Fill in end
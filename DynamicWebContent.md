'''
Video Notes:

Video 1:
Getting Data from the Server:
1. Each time the user clicks on an anchor tag with an href = value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request - to GET the content of the page at specified URL. 
2. The server returns the HTML document to the browser, which formats and displays the document to the user.
3. A socket connection can be viewed as the way the brower app and web server are communcating. 

Video 2:
1. HTTP - Hypertext Transfer Protocol, is the protocol that browsers used to talk to servers.
2. HTTP was introduced in 1990.
3. Uniform Resources Locator can be split in three parts, protocol(example:http://), host(example:data.pr4e.org), and document(example: page1.htm).
4. Before HTTP protocol, which is before 1990, there were a lot of protocols.
5. As engineers, we need to question everything and not be satisfy with our designs.
6. The standards for all of the internet protocols(inner workings) are developed by an organization.
7. Internet Engineering Task Force(IETF)
8. www.ietf.org
9. Standards are called "RFCs"- "Request for Comments" 
Making an HTTP Request:
1. Connect to the server like data.pr4e.org
2. - a "handshake"
3. Request a document
 - Get http://data.pr4e.org/page1.htm HTTP/1.0
 - Get http://www.mlive.com/ann-arbor/HTTP/1.0
 - Get http://www.facebook.com HTTP/1.0
Accurate Hacking in the Movies
- Matric Reloaded
- Bourne Ultimatum 
- Die Hard 4
- ...

Video 3:
- Network Sockets are like phone calls for pairs of applications
TCP Connection/Sockets
- In computer networking, an internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Interent Protocol-based computer newtwork, such as the Internet."
APPLICATION PROCESS --> INTERNET --> APPLICATION PROCESS
- All computers have IP address, there are two kinds which are ipv4 and ipv6
- TCP port numbers are like phone call extention

Video 4:
Creating Socket:
- Import Socket Module - this is like getting your tools ready. I need to use Python's socket module to create a socket.
- Making a socket is like making a new phone, first you choose the type of socket, meaning IP address and TCP
- Input value in the AF_INET for internet(IPV4 addresses) and SOCK_STREAM for TCP
- Reciving and sending are parts of socket system

Video 5:
- Listen() could be explained as reciving calls
- Accept() is like blocking if you are already in communication or in a call with a server, it keeps waiting on you because you can not communicate with more than 1 server
- Accept and Handle Connection explaination: The server runs in an infinite loop, constantly accepting new connections. For each connection, it enters another loop to recieve and send data until the client disconnects(if not data: break). 
After communication is done, it closes the connection(close()) and waits for thenext client.

'''

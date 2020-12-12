# Client Server Calculator (CS 453 - Computer Networks)

This project has 2 parts 

# 1)Simple Client Server in a reliable environment, using TCP & UDP

The Server:
The server performs the Operation Code (OC) requested on the two integer numbers it receives from the sender and returns the result. 

The client:
The client sends an Operation Code (OC), and the two numbers it has acquired from the user. OC can be: Addition (+), Subtraction (-), Multiplication (*), and Division (/)
To make the problem simple, your client sends two numbers that are integers.


# 2) Simple Client Server in an unreliable environment, using UDP 

The client sends an Operation Code (OC), and two numbers. OC can be: Addition (+), Subtraction (-), Multiplication (*), and Division (/). To make the problem simple, your client sends two integer numbers.

We will simulate errors and how to handle them. When we use TCP, the transport protocol takes care of network unreliability, being dropped packets and/or erroneous transmission. But when you we UDP, our application should take care of reliability issues.
Because we are running on the same machine-> we will randomly drop packets at the server.

There is a possibility that the client does not receive a reply and it repeats sending the request. The client uses a technique known as exponential back off, where its attempts become less and less frequent. 
The client sends its initial request and waits for certain amount of time (in our case d=0.1 second). If it does not receive a reply within d seconds, it retransmits the request, but this time waits twice the previous amount, 2*d. It repeats this process, each time waiting for a time equal to twice the length of the previous cycle. This process is repeated until the wait time exceed 2 seconds. At which time, the client sends a warning that the server is “DEAD” and aborts for this request.) 

 


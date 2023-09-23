Readme TXT
(this is like a shittier version of the README.MD)
Please get started with the instructions in the README.MD file rather than this file if you can.

rawd0gger is a simple Multithreaded L4 Python DOS Attack.


To run the program, first open the rawd0gger directory in your terminal and then run

  sudo python3 rawd0gger.py <IP address> 

with your preferred arguments,

Arguments:

  -p The port the packets will be sent too (Defaults to port 80 if not specified)

  -a Amount of packets to send per thread (Will default to the maximum possible if not specified)



Example:

    sudo python3 rawd0gger.py <IP address> -p <port> -a <amount of packets to send>
                                         
Once the program starts it will ask you for how many threads to run, At Least one is required for the program to work.

Notices

  While this program randomises the IP in the packets you are not fully anonymous, If you do wish to protect yourself use a proxy and/or VPN while running this program.
  
  Don't be stupid, use it responsibly. We are not responsible for Malicious Use.
  
  "For educational purposes only."
  
  t0rkelSec 2023
  

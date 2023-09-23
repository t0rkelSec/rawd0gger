# rawd0gger
rawd0gger is a simple Multithreaded L4 Python DOS Attack.

## Usage

To run rawd0gger run, 
```
sudo python3 rawd0gger.py <IP Adress> -p <port> -a <amount of packets to send per thread>
```
*Once the program starts it will ask you for how many threads to run, Atleast one is required for the program to work.*

## Arguments

**-p**  the port to send packets too (Defaults to 80 if not specified)

**-a**  Amount of packets to send (Wil default to max if not specified)

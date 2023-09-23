# rawd0gger
**rawd0gger is a simple Multithreaded L4 Python DOS Attack.**

*v0.1*

## Usage

To download and use rawd0gger run the command,
```
git clone https://github.com/t0rkelSec/rawd0gger.git
```

To run the program, first open the rawd0gger directory in your terminal and then run: 

<sub>It is recomended that you learn the arguments before running the program.</sub>
```
sudo python3 rawd0gger.py <IP address> 
```

*Once the program starts it will ask you for how many threads to run, Atleast one is required for the program to work.*

**Please read the arguments section below to understand how to run the program with your prefered configuration**

## Arguments

**-p**  The port the packets will be sent too (Defaults to port 80 if not specified)


**-a**  Amount of packets to send ***per thread*** (Will default to the maximum possible if not specified)

### Example:

```
sudo python3 rawd0gger.py <IP address> -p <port> -a <amount of packets to send>
```

### Notices


**While this program randomizes the IP in the packets you are **not** fully anonymous, 
If you do wish to protect yourself use a proxy and/or VPN while running this program.**

*Dont be stupid, use responsibly. We are not responsible for Malicous Use.*

<sub>"*For educational purposes only.*"</sub>

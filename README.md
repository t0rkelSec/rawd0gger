# rawd0gger
**rawd0gger is a simple Multithreaded L4 Python Denial-of-service Attack.**

```
3d0g rawd0gger 2023 rawd0gger rawd0gger rawd0gger rawd0gger rawd0gger
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@x██▀███xxx▄▄▄xxxxxxx█xxxxx█░▓█████▄xxx▄████xxx▄████x▓█████xx██▀███xx@
@▓██x▒x██▒▒████▄xxxx▓█░x█x░█░▒██▀x██▌x██▒x▀█▒x██▒x▀█▒▓█xxx▀x▓██x▒x██▒@
@▓██x░▄█x▒▒██xx▀█▄xx▒█░x█x░█x░██xxx█▌▒██░▄▄▄░▒██░▄▄▄░▒███xxx▓██x░▄█x▒@
@▒██▀▀█▄xx░██▄▄▄▄██x░█░x█x░█x░▓█▄xxx▌░▓█xx██▓░▓█xx██▓▒▓█xx▄x▒██▀▀█▄xx@
@░██▓x▒██▒x▓█xxx▓██▒░░██▒██▓x░▒████▓x░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓x▒██▒@
@░x▒▓x░▒▓░x▒▒xxx▓▒█░░x▓░▒x▒xxx▒▒▓xx▒xx░▒xxx▒xx░▒xxx▒x░░x▒░x░░x▒▓x░▒▓░@
@xx░▒x░x▒░xx▒xxx▒▒x░xx▒x░x░xxx░x▒xx▒xxx░xxx░xxx░xxx░xx░x░xx░xx░▒x░x▒░@
@xx░░xxx░xxx░xxx▒xxxxx░xxx░xxx░x░xx░x░x░xxx░x░x░xxx░xxxx░xxxxx░░xxx░x@
@xxx░xxxxxxxxxxx░xx░xxxx░xxxxxxx░xxxxxxxxxx░xxxxxxx░xxxx░xx░xxx░xxxxx@
@xxxxxxxxxxxxxxxxxxxxxxxxxxxxx░xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
t0rkelSec rawd0gger rawd0gger rawd0gger rawd0gger rawd0gger rawd0gger
```

## Download
<sub>The commands in this document are for primarily Linux systems but it's pretty easy to figure out how to run this on other systems with a little bit of research.</sub>

<sub>*(and yes this does work on a linux enabled chromebook)*</sub>

## Requirments
*Requirments:*

**Python3** if you don't already have python3 you can get it with the commands,

```
sudo apt update
sudo apt install python3
```
Or
  https://www.python.org/downloads/


**Scapy for Python3**
  can be installed via the commands,
  ```
  sudo apt-get update
  sudo apt-get install python3-scapy
  ```

Now to download rawd0gger run the command,
```
git clone https://github.com/t0rkelSec/rawd0gger.git
```
Or you can get it at https://github.com/t0rkelSec/rawd0gger/releases

## Usage
Now to run the program, first open the rawd0gger directory in your terminal and then run the command: 

<sub>It is recomended that you learn the arguments before running the program.</sub>
```
sudo python3 rawd0gger.py <IP address> 
```

**Once the program starts it will ask you for how many threads to run, At least one is required for the program to work.**

***Please read the arguments section below to understand how to run the program with your prefered configuration***

## Arguments

**-p**  The port the packets will be sent to (Defaults to port 80 if not specified)


**-a**  Amount of packets to send ***per thread*** (Will default to the maximum possible if not specified)

### Example:

```
sudo python3 rawd0gger.py <IP address> -p <port> -a <amount of packets to send>
```

### Notices


**While this program randomises the IP in the packets you are **not** fully anonymous, 
If you do wish to protect yourself use a proxy and/or VPN while running this program.**

*Don't be stupid, use responsibly. We are not responsible for Malicious Use.*

Work in Progress, May still have bugs.

<sub>"*For educational purposes only.*"</sub>


<sub>t0rkelSec 2023</sub>

```
⠀⠀⢀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⣄⠀⠀⠀⠀⠀
⠀⣴⠊⠛⠦⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠈⠈⠳⡄⠀⠀⠀
⠸⣿⠀⠀⠀⠉⢹⣆⠀⠀⠀⠠⡶⠖⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠈⡆⠀⠀
⠀⠈⣧⠀⠀⠀⠀⠉⠓⠂⠐⠋⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡆⢀⢰⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡒⠀⣤⢀⠀⠈⡇⠀⠀⠀⢹⡂⠀
⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠞⠄⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠿⠁⠈⠁⠉⠻⢷⠶⠴⢭⡄⠤⡀⠀⠀⠀⠀⠀⢿⡇⠀⠈⢢⠀⣸⡇⠀⠀⠀⠐⠁⠀
⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⢐⡏⡀⠀⠀⠀⠀⠀⠀⣠⡚⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢮⡀⡀⠀⠀⠀⠉⢳⡄⠀⡘⠛⠋⠀⠀⠀⠀⠀⡄⠀
⠀⠀⠀⢀⣇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢀⣴⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣌⢂⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢰⣧⡅
⠀⠀⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣠⡾⠁⠀⠀⠀⠀⠀⣠⡴⠖⠤⠴⠤⠶⠀⢄⠀⠀⠀⠀⠀⠀⠈⠓⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢠⣤⠞⠵⠁
⠀⠀⠀⠀⠀⠻⣦⡀⠀⠀⠀⢰⡺⠀⠀⠀⢀⡾⠇⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⢹⣀⡀⠀⠀⠀⠀⠀⢱⠀⠀⠘⠛⢧⡀⠀⠀⣀⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠓⠖⠶⠶⠵⠃⠀⠀⠀⢺⢈⠀⠀⠀⢀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠙⢆⠀⠀⠀⠀⠀⠸⣄⠁⠀⠀⠈⠻⠒⠚⠏⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡀⠀⠀⠀⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣡⡀⠀⠀⠀⠀⢸⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⣠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⢻⡁⡀⠀⠀⢀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡔⠀⠀⡾⠀⠀⠀⠀⢀⡤⠞⠁⠀⠀⠀⠹⠄⠀⠀⠀⠈⢯⠀⠀⠀⣠⣼⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣧⠀⢸⡇⠀⠀⢠⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠸⡄⠀⢀⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⣸⡁⠀⢀⠾⡆⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢠⡣⠀⣸⡿⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣬⠛⠁⡆⠉⡆⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢧⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⣀⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢀⣸⣤⣿⠯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠘⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⠋⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠲⠖⠒⠒⠂⠒⠒⠒⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

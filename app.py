# Import Modules
import sys 
import socket
from pyfiglet import Figlet
from datetime import datetime
from time import sleep as sleep
from time import time as time
from threading import *


# Banner
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Port Scanner'))

# Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) 
else:
    target = socket.gethostbyname('localhost')

# Basic information for user    
for i in range(0,49):
    print('-',end='')
print()
sleep(1)
print(f'Scanning host: {target}')
sleep(1.5)
print(f'Started at {datetime.now()}')
for i in range(0,49):
    print('-',end='')
print()
start = time()

# Scanning port here

try :
    for port in range(1,65535):
        print(f'\rScanning Port {port}\r',end="")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result ==0:
            print(f"Port {port} is open\n")
        s.close()

except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()

for i in range(0,49):
    print('-',end='')
print()
endtime=time()
sleep(1)
print(f'Scanned successfully in {endtime-start}')

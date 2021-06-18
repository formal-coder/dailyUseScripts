import urllib3 as urllib
import sys
import time
from datetime import datetime

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END ,WARNING = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[93m'

def fancyDisplay(buffer, color = WHITE):
    sys.stdout.write(color)
    for i in buffer:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write(WHITE)
    return

while True:
    ntime = datetime.now()
    timenow = str(ntime)
    print(timenow[0:-7])
    fancyDisplay("\nENTER MAC ADDRESS >> ", GREEN)
    mac = input()
    if len(mac) == 0:
        fancyDisplay('\nOOPS! YOU FORGOT TO TYPE\n\n', MAGENTA)
        quit()
    url = "http://api.macvendors.com/" + str(mac)
    lib = urllib.PoolManager()
    response = lib.request('GET', url)
    strvendor = str(response.data)
    fancyDisplay("""


	"""+ strvendor[2:-1] +"""


	""", RED)
# Colors
NC='\033[0m' # No Color

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

# clear the screen
clear

# logo
echo -e "${BBlue}
=========================================${BRed}
                  _ __            
           ____  (_) /_____  _____
          / __ \/ / __/ __ \/ ___/
         / /_/ / / /_/ / / / /__  
        / .___/_/\__/_/ /_/\___/  
       /_/  ${BRed}Ham Tracks Offroad${BBlue}

=========================================${NC}\n"

BTMAC=$(hcitool dev | grep -o "[[:xdigit:]:]\{11,17\}")
BTNAME=$(sed -e 's#.*=\(\)#\1#' <<< cat /etc/machine-info 2>/dev/null)
IPADDR=$(ip addr show $(ip route | awk '/default/ { print $5 }') | grep "inet" | head -n 1 | awk '/inet/ {print $2}' | cut -d'/' -f1)
KISSPORT=$(cat direwolf.conf | grep 'KISSPORT' | sed 's/KISSPORT //')
WIFI=$(iwgetid --scheme)

echo -e "${BBlue}BLUETOOTH NAME: ${BGreen}${BTNAME}${NC}"
echo -e "${BBlue} BLUETOOTH MAC: ${BGreen}${BTMAC}${NC}"
echo -e "${BBlue}    IP ADDRESS: ${BGreen}${IPADDR}${NC}"
echo -e "${BBlue}     KISS PORT: ${BGreen}${KISSPORT}${NC}"
echo -e "${BBlue}          WIFI: ${BGreen}${WIFI}${NC}"

if df -h | grep 'overlay'>/dev/null; then
	echo -e "${BBlue}   FILE SYSTEM: ${BGreen}READ ONLY${NC}"
else
	echo -e "${BBlue}   FILE SYSTEM: ${BRed}READ/WRITE${NC}"
fi
echo ""
echo "    $ ro              # enter read only mode"
echo "    $ rw              # enter read/write mode"
#echo "    $ btset           # set the bluetooth name to match MAC"
echo "    $ wifi            # set the wifi to connecto to"
echo "    $ monitor         # monitor the APRS activity, ctrl-b d to exit"
echo ""

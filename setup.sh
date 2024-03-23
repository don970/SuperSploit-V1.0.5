#!/usr/bin/env bash
sudo apt-get install python3-prompt-toolkit -y
sudo apt-get install python3-pyfiglet -y
sudo apt-get install netcat-traditional adb fastboot pip -y
pip install --break-system-packages pure-python-adb pwn pybluez
bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )
sudo mv ./phoneinfoga /usr/local/bin/phoneinfoga
cd .data && git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng && pip install --break-system-packages -r REQUIREMENTS

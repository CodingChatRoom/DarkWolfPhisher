#!/bin/bash

# Colors for output
GREEN="\e[32m"
RED="\e[31m"
RESET="\e[0m"

echo -e "${GREEN}Starting installation...${RESET}"

# Check if running in Termux or Kali Linux
if [ -d "$HOME/../usr" ]; then
    echo -e "${GREEN}Detected Termux...${RESET}"
    pkg update -y && pkg upgrade -y
    pkg install python -y
    pkg install git -y
elif [ -f "/etc/debian_version" ]; then
    echo -e "${GREEN}Detected Kali Linux...${RESET}"
    sudo apt update -y && sudo apt upgrade -y
    sudo apt install python3 python3-pip git -y
else
    echo -e "${RED}Unsupported OS!${RESET}"
    exit 1
fi

# Give execution permission to darkwolf.py
chmod +x darkwolf.py

echo -e "${GREEN}Installation complete! Run with: python3 darkwolf.py${RESET}"

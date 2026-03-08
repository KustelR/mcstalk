# What is this
This project is aimed for monitoring online on minecraft servers? being as easy-to-use as possible
# Config
Program uses yaml for config file (`config.yaml`), currently supporting following attributes:
1. `target` - target ip address with port, or hostname (dns works kinda weird now tho)
2. `interval` - interval between checks in seconds
# Output
Gathered data goes in `reports` directory under "server_address.csv" names
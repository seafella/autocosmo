#!/bin/sh

wget https://cosmo.zip/pub/cosmos/bin/python
wget https://cosmo.zip/pub/cosmos/bin/unzip
wget https://raw.githubusercontent.com/seafella/autocosmo/main/autocosmo.sh
wget https://raw.githubusercontent.com/seafella/autocosmo/main/network_details.py

chmod +x ./python
chmod +x ./unzip
chmod +x ./autocosmo.sh

mkdir Lib
./python -m pip download requests beautifulsoup4 -d Lib
for whl in Lib/*.whl; do unzip "$whl" -d Lib/; done

./autocosmo.sh ./network_details.py
./network_details
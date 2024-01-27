#!/bin/sh
set -eux

# The first command line argument is the filename
FILENAME=$1

PREV="$(pwd)"
DIR="$(mktemp -d)"
# uncomment the following line and create a `./temp` folder to test
# DIR=./temp
cp "$FILENAME" "$DIR"

# Delete .args file if it exists and create a new one with specified content
if [ -f .args ]; then
  rm .args
fi
echo "$FILENAME" > .args
echo "..." >> .args

cp .args "$DIR"
# cp repl.html "$DIR"
# cp style.css "$DIR"
cd "$DIR"
wget https://cosmo.zip/pub/cosmos/bin/python
wget https://cosmo.zip/pub/cosmos/bin/zip
chmod +x python
chmod +x zip
./python -m compileall "$FILENAME"
mkdir Lib

# if [ -f Lib ]; then
  # echo "Found Lib folder. Copying it..."
cp -r "$PREV"/Lib ./Lib
# fi

# Extract the filename without the extension for use in the compiled filename
BASENAME=$(basename "$FILENAME" .py)
cp "__pycache__/${BASENAME}."*.pyc "Lib/${BASENAME}.pyc"
# cp style.css repl.html Lib
cp python "${BASENAME}.com"
./zip -r "${BASENAME}.com" Lib .args
cd "$PREV"
cp "$DIR/${BASENAME}.com" .
echo "Testing..."
./"${BASENAME}.com"

#!/bin/bash

psdrexafolder="$(dirname $0)/PSDRexa"
pyfile="$(dirname $0)/PSDRexa.py"
syncerfile="$(dirname $0)/PSDRexa_syncer.py"
dummyfile="$(dirname $0)/dummy,png"
base1="/Library/Application Support/Blackmagic Design/DaVinci Resolve"
base2="$HOME/Library/Application Support/Blackmagic Design/DaVinci Resolve"
base3="~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Support/Fusion/Settings"

if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. If you're seeing this error despite having Python installed, please ensure that the PYTHONHOME environment variable is set correctly."
    exit
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip is not installed. Please ensure that pip is installed correctly."
    exit
fi

echo "[start]Install PSDRexa"

if [ -d "$base1" ]; then
    module_folder="$base1/Fusion/Modules"
    script_folder="$base1/Fusion/Scripts/Utility"
elif [ -d "$base2" ]; then
    module_folder="$base2/Fusion/Modules"
    script_folder="$base2/Fusion/Scripts/Utility"
else
    echo "DaVinci Resolve folder is not exists."
    exit
fi

if [ -d "$module_folder/PSDRexa" ]; then
    echo "delete old PSDRexa Directory."
    rm -rf "$module_folder/PSDRexa"
fi
cp -R "$psdrexafolder" "$module_folder/PSDRexa"

cd "$module_folder/PSDRexa"
pip3 install -r requirements.txt --target module

if [ -f "$script_folder/PSDRexa.py" ]; then
    echo "delete old PSDRexa."
    rm "$script_folder/PSDRexa.py"
fi
cp "$pyfile" "$script_folder"

if [ -f "$script_folder/PSDRexa_syncer.py" ]; then
    echo "delete old PSDRexa_syncer."
    rm "$script_folder/PSDRexa_syncer.py"
fi
cp "$syncerfile" "$script_folder"

cp "$dummyfile" "$base3"



echo "[end]Install PSDRexa"

echo "Install PSDRexa Success!"

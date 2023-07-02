#!/bin/bash

# Get the directory of the script
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Set variables
zipfile="$script_dir/PSDRexa.zip"
pyfile="$script_dir/PSDRexa.py"

# Check if python is installed
if ! command -v python &> /dev/null; then
    osascript -e 'tell app "System Events" to display dialog "Python is not installed." with title "Error" buttons {"OK"} default button "OK" with icon caution'
    exit 1
fi

# Set DaVinci Resolve folder paths
base1="/Library/Application Support/Blackmagic Design/DaVinci Resolve"
base2="$HOME/Library/Application Support/Blackmagic Design/DaVinci Resolve"

# Check if DaVinci Resolve folders exist
if [ -d "$base1" ]; then
    module_folder="$base1/Fusion/Modules"
    script_folder="$base1/Fusion/Scripts/Utility"
elif [ -d "$base2" ]; then
    module_folder="$base2/Fusion/Modules"
    script_folder="$base2/Fusion/Scripts/Utility"
else
    osascript -e 'tell app "System Events" to display dialog "DaVinci Resolve folder does not exist." with title "Error" buttons {"OK"} default button "OK" with icon caution'
    exit 1
fi

# Clear module folder if exists
if [ -d "$module_folder/PSDCharacterExporter" ]; then
    rm -rf "$module_folder/PSDCharacterExporter/*"
fi
if [ -d "$module_folder/PSDRexa" ]; then
    rm -rf "$module_folder/PSDRexa/*"
fi

# Extract zipfile
unzip -o "$zipfile" -d "$module_folder"

# Navigate to module folder and install python requirements
cd "$module_folder/PSDRexa"
python -m pip install -r requirements.txt -t module

# Clear script folder if exists
if [ -f "$script_folder/PSDCharacterExporter.py" ]; then
    rm -f "$script_folder/PSDCharacterExporter.py"
fi
if [ -f "$script_folder/PSDRexa.py" ]; then
    rm -f "$script_folder/PSDRexa.py"
fi

# Copy python file to script folder
cp "$pyfile" "$script_folder"

# Notify user that installation was successful
osascript -e 'tell app "System Events" to display dialog "Install PSDRexa Success!" with title "Installation Complete" buttons {"OK"} default button "OK" with icon note'

# NIC Decoder LK

NIC Decoder LK is a Python desktop application that decodes Sri Lankan National Identity Card (NIC) numbers and extracts information such as date of birth and gender.

## Features
- Supports old NIC format (10 digits)
- Supports new NIC format (12 digits)
- Extracts:
  - Date of Birth
  - Gender (Male / Female)
- Simple GUI application
- Lightweight and fast

## How It Works
The application reads the NIC number and decodes embedded information based on Sri Lankan NIC structure rules.

## Requirements
- Python 3.x
- tkinter (built-in)

No external libraries required.

## Run Application
python nic_decoder.py

## Build EXE (Windows)
py -m PyInstaller --onefile --windowed --icon=NIC_Decoder.ico nic_decoder.py

Output file will be in:
dist/nic_decoder.exe

## Project Structure
NIC_Decoder/
├── nic_decoder.py
├── NIC_Decoder.ico
├── README.md
├── .gitignore

NOTE:
- build/ ignored by git
- dist/ ignored by git
- .spec ignored by git

## Git Commands (UPLOAD PROJECT)

git add .
git commit -m "Final NIC Decoder project"
git push origin main

If push fails:
git push --set-upstream origin main

## Author
Visal Weerakoon

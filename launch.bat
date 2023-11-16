@echo off
echo Creating virtual environment...
python -m venv boombot

echo Activating virtual environment...
call boombot\Scripts\activate

echo Installing required libraries...
pip install pyautogui opencv-python

echo Launching main.py...
python main.py

echo Deactivating virtual environment...
deactivate

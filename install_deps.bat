@echo OFF
echo Installing Dependencies...
winget install python
pip install typer
pip install -U pytest
echo Dependencies Installed!
pause
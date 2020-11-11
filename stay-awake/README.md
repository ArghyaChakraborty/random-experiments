## Steps
1. Install Python
2. `pip install pyautogui`
3. Copy the `stay-awake.py` in your desktop
4. `vi ~/.bash-aliases` (if you are using Windows, install `GitBash` first before executing this command)
5. Add this line at the end of the file: `alias sa='python <path to stay-awake.py>/stay-awake.py'`
6. Save the file and quit
7. `source ~/.bash-aliases`
8. Then execute `sa` in your command line and the python script will start
9. This script will move mouse from the top of your screen towards the bottom and then press `shift` key and then left click mouse key
10. It will be repeated forever
11. To stop the script, press `Alt` + `Tab` to go to the command line tool where `sa` command was executed
12. Then press `Ctrl` (or `Command`) + `C` to kill the script
13. Enjoy !!!!

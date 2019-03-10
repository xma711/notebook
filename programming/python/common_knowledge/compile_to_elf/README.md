python to elf
-------------------

reference: https://mborgerson.com/creating-an-executable-from-a-python-script


installation: sudo pip install pyinstaller

run: pyinstaller --onefile main.py

the elf executable can be found in dist/main


Limitation: if the self-written python scripts are in the same folder, 
there won't be problem combining them to one elf; 
but if they are in different folders, the elf doesn't contains the scripts from another folder.

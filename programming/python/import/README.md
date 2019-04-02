From .package_name impport xxx
----------------------------------------

The dot before the packge_name is a shortcut that tells python to search the current package before rest of the PYTHONPATH.

Reference: https://stackoverflow.com/questions/22511792/python-from-dotpackage-import-syntax

ultimately it is part of the relative imports.


Relative import
----------------------

Relative import means that the imported package's indicated path in the importing file (the file that imports this package) is relative to the importing file.  
It is not relative to where the command is started.

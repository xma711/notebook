how to import class from another folder
------------------------------------------

that folder needs to have an empty __init__.py ;
and then the folder will behave like a python file in the current directory.


if there are a series of folder and subfolders, then each level of folder has to have a __init__.py,
then we can do an import folder1.folder2.folder3.file ...


another way
----------------------

another way is to insert the path to this folder with __init__.py to the sys.path (a list object).  
this is illustrated in programming/python/common_knowledge/call_functions_from_another_directory/

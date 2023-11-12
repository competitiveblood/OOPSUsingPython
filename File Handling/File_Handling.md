**FILE HANDLING IN PYTHON**
Operations on File

1) Open a file
2) Read/write
3) Close the file

## FILE MODES IN PYTHON

f1=open('abc.txt')
File Modes(r,w,x,a,t,b,+)

"r" means open a file in read mode 

"w" means open a file in write mode(truncate/overwrite the previous content).
If file doesn't exits then create it

"x" means open a file for exclusive creation.
If file already exists then operation fails

"a" means open a file in appending mode at the end of the file without truncating. Create a new file if doesn't exists.

"b" open the file in binary

"+" open a file for updating mode in python 

#pragma once
#include <iostream>

std::string commands_instruction{
"\n\
Directory navigation: \n\
cd (directory) - to navigate directories.\n\
cd / - to navigate into the root directory.\n\
cd .. - to navigate back in the directories.\n\
ls - to display files in the current directory.\n\
\n\
File operations: \n\
mkdir - to create a new directory.\n\
touch - to create a new file.\n\
rm - to delete an existing file.\n\
rmdir - to delete an existing empty directory.\n\
mv - to move a file/directory or to rename it (i.e. cp file destination OR cp oldfile newfile)\n\
cp - to copy a file (i.e. cp oldfile destination/filename)\n\
open - to open up an existing file.\n\
\n\
System commands: \n\
clear - to clear the terminal.\n\
exit - to terminate application.\n"
};
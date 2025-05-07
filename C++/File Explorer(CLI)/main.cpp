#include <iostream>
#include <windows.h>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include "Header.h"

int main() {

	WIN32_FIND_DATAA findFileData{}; // Windows-specific structure that receives information about a found file or directory and can provide various details.
	SYSTEMTIME systemTime{};
	HANDLE hFind{}; // Windows-specific type that represents an open file search.

	std::string user_input{};
	std::string path{"C:/"};

	std::cout << "Welcome to the Linux-based File Explorer v2.0\n \nType \"help\" to get the list of all existing commands." << std::endl;

	while (true)
	{
		std::cout << "\n" << path << ">";

		getline(std::cin, user_input);

		// Directory navigation
		if (user_input == "cd /")
		{
			path = "C:/";
			continue;
		}
		else if (user_input == "cd ..")
		{
			size_t path_len{ path.length() - 1 };

			path.erase(path_len, 1);

			for (size_t n{ path_len }; n > 0; n--)
			{
				if (path.substr(n) != "/") path.erase(n);
				else break;
			}
			continue;
		}
		else if (user_input.substr(0, 2) == "cd")
		{
			path += user_input.erase(0, 3) + "/";

			hFind = FindFirstFileA((path + '*').c_str(), &findFileData);

			if (hFind == INVALID_HANDLE_VALUE)
			{
				size_t char_index{ path.find(user_input) };

				path.erase(char_index - 1, user_input.length() + 1);

				std::cout << "No such directory found!" << std::endl;
			}
			continue;
		}

		// File operations
		if (user_input == "ls") user_input = "*";
			
		// System commands
		else if (user_input == "help")
		{
			std::cout << commands_instruction;
			continue;
		}
		else if (user_input == "clear")
		{
			system("cls");
			continue;
		}
		else if (user_input == "exit")
		{
			break;
		}
		else
		{
			std::cout << "No such command!\n";
			continue;
		}

		hFind = FindFirstFileA((path + user_input).c_str(), &findFileData); // Find the first file and feed this data to the FindNextFile()

		// BOOL is a Windows-specific type that is defined as an int actually, created using typedef keyword. Windows library had this type before bool was introduced into C++.
		BOOL next_file{ FindNextFileA(hFind, &findFileData) };

		std::vector<std::string> files{};

		std::cout << std::string(40, ' ') << "LastWriteTime" << "\n\n";

		while (next_file != false)
		{
			FILETIME file_write_time{ findFileData.ftLastWriteTime };
			FileTimeToSystemTime(&file_write_time, &systemTime);

			std::string file_name{ findFileData.cFileName };
			std::size_t file_name_len{file_name.length()};
			std::ostringstream oss{};

			oss << std::setfill('0') << std::setw(2) << systemTime.wDay << '/' << std::setw(2) << systemTime.wMonth << '/' << systemTime.wYear;
			std::string date_string = oss.str();
			oss.str("");
			oss.clear();

			oss << std::setfill('0') << std::setw(2) << systemTime.wHour << ':' << std::setw(2) << systemTime.wMinute;
			std::string time_string = oss.str();
			oss.str("");
			oss.clear();

			file_name_len = std::abs(static_cast<int>(file_name_len) - 40); // absolute value (not negative)

			oss << file_name << std::string(file_name_len, ' ') << date_string << std::string(2, ' ') << time_string << "\n";

			if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
			{
				std::cout << oss.str();
			}
			else if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_SYSTEM) 
			{
				// System files are ignored
			}
			else files.push_back(oss.str());

			next_file = FindNextFileA(hFind, &findFileData);
		}
		for (size_t n{}; n < files.size(); n++) std::cout << files[n]; // Display all files at the end of the list

		FindClose(hFind);
	}
	
	return 0;
}
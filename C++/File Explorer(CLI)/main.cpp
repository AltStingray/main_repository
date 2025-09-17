#include <iostream>
#include <windows.h>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include "Header.h"

// ./ - to execute/run an executable file
// rm -r - to delete an existing directory and its contents.\n\
// EncryptFileA

int main() {

	WIN32_FIND_DATAA findFileData{}; // Windows-specific structure that receives information about a found file or directory and can provide various details.
	SYSTEMTIME systemTime{};
	HANDLE hFind{}; // Windows-specific type that represents an open file search.
	SECURITY_ATTRIBUTES securityAttributes{};
	// SHFILEOPSTRUCTA fileOp{};

	std::string user_input{};
	std::string path{"C:/"};

	std::cout << "Welcome to the Linux-based File Explorer v3.0\n \nType \"help\" to get the list of all existing commands." << std::endl;

	while (true)
	{
		std::cout << "\n" << path << ">";

		getline(std::cin, user_input);

		// Directory navigation
		if (user_input == "cd /")
		{
			path = path.erase(3, path.length());
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
				size_t user_input_len{ user_input.length() };

				path.erase(path.length() - user_input_len - 1, user_input_len + 1);

				std::cout << "Error: no such directory found!" << std::endl;
			}
			continue;
		}
		else if (user_input == "C:" || user_input == "D:" || user_input == "E:")
		{
			path = user_input + "/";
			continue;
		}


		// File operations
		if (user_input == "ls") user_input = "*";

		else if (user_input.substr(0, 5) == "mkdir")
		{
			std::string dir_name{ user_input.substr(6, user_input.length()) };

			BOOL create_dir{};
			create_dir = CreateDirectoryA((path + dir_name).c_str(), &securityAttributes);

			if (create_dir == 0)
			{
				(GetLastError() == 183) ? std::cout << "Error: specified directory already exists!\n" : std::cout << "Unknown error!";
			}
			else std::cout << "Directory created successfully!\n";

			continue;
		}
		else if (user_input.substr(0, 5) == "touch")
		{
			std::string file_name{ user_input.substr(6, user_input.length()) };

			HANDLE create_file{};
			create_file = CreateFileA(
				(path + file_name).c_str(), // File path and name
				(GENERIC_READ | GENERIC_WRITE), // Desired access
				(FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE), // Share mode
				&securityAttributes,
				CREATE_ALWAYS,  // Creates a new file
				FILE_ATTRIBUTE_NORMAL, // File attributes
				nullptr // Template file
			);

			if (create_file != INVALID_HANDLE_VALUE && GetLastError() == 0)
				std::cout << "File created successfully!\n";
			else
				std::cout << "Error: specified file already exists!\n";

			CloseHandle(create_file);

			continue;
		}
		else if (user_input.substr(0, 4) == "open")
		{
			HINSTANCE openfile{};
			std::string file_name{ user_input.substr(5, user_input.length()) };

			openfile = ShellExecuteA(nullptr, "open", (path + file_name).c_str(), nullptr, nullptr, SW_SHOWNORMAL);

			if (openfile == 0) std::cout << "Error: specified file is not found!\n";

			continue;
		}
		else if (user_input.substr(0, 5) == "rmdir")
		{
			BOOL delete_dir{};
			std::string dir_name{ user_input.substr(6, user_input.length()) };

			delete_dir = RemoveDirectoryA((path + dir_name).c_str());

			if (delete_dir != 0)
				std::cout << "Directory deleted successfully!\n";
			else if (GetLastError() == 2)
				std::cout << "Error: specified directory does not exist!\n";
			else
				std::cout << "Error: specified directory is not empty!\n";

			continue;
		}
		else if (user_input.substr(0, 5) == "rm -r")
		{
			// PCZZTSTR pFrom{};
			// LPSHFILEOPSTRUCTA lpFileOp{ &fileOp.wFunc() };
			// SHFileOperationA(lpFileOp);

			continue;
		}
		else if (user_input.substr(0, 2) == "rm")
		{
			BOOL delete_file{};
			std::string file_name{ user_input.substr(3, user_input.length()) };

			delete_file = DeleteFileA((path + file_name).c_str());

			(delete_file != 0) ? std::cout << "File deleted successfully!\n" : std::cout << "Error: specified file is not found!\n";

			continue;
		}
		else if (user_input.substr(0, 2) == "cp")
		{
			BOOL copy_file{};
			std::string oldfile{};
			std::string newfile{};

			for (size_t n{ 3 }; n < user_input.length(); n++)
			{
				std::string letter{ user_input.substr(n, 1) };

				if (letter != " ") oldfile += letter;
				else
				{
					user_input.erase(0, n + 1);

					size_t pos{ user_input.find("/") };

					// If no slashes found in the user input - copy file to the current directory
					if (pos == std::string::npos)
					{
						newfile = path + user_input;
					}
					else
					{
						newfile = user_input;
					}

					break;
				}
			}

			copy_file = CopyFileA((path + oldfile).c_str(), newfile.c_str(), FALSE);

			if (copy_file != 0) std::cout << "File copied successfully!\n";

			else if (GetLastError() == ERROR_FILE_NOT_FOUND) std::cout << "Error: specified file is not found!\n";

			else std::cout << "Error: No new file name is specified!\n";

			continue;
		}
		else if (user_input.substr(0, 2) == "mv")
		{
			BOOL move_file{};
			std::string oldfile{};
			std::string newfile{};
			std::vector<std::string> v{ oldfile, newfile };

			for (size_t n{ 3 }; n < user_input.length(); n++)
			{
				std::string letter{ user_input.substr(n, 1) };

				if (letter != " ") oldfile += letter;
				else
				{
					user_input.erase(0, n + 1);

					size_t pos{ user_input.find("/") };

					// If no slashes found in the user input - copy file to the current directory
					if (pos == std::string::npos)
					{
						newfile = path + user_input;
					}
					else
					{
						newfile = user_input;
					}

					break;
				}
			}
			
			move_file = MoveFileA((path + oldfile).c_str(), newfile.c_str());

			if (move_file != 0) std::cout << "File moved successfully!\n";

			else if (GetLastError() == ERROR_FILE_NOT_FOUND) std::cout << "Error: specified file is not found!\n";

			else std::cout << "Error: No new file name is specified!\n";

			continue;
		}

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

			file_name_len = std::abs(static_cast<int>(file_name_len) - 40); // abs - absolute value (not negative)

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
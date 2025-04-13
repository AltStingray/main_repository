#include <iostream>
#include <string>

int main() {

	std::string alphabet{ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" };
	std::string key{ "XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr" };
	std::string message{};
	std::string option{};
	char proceed{};

	do
	{
		system("cls");

		std::cout << "Encrypt/decrypt: ";
		getline(std::cin, option);

		if (option == "Encrypt" || option == "encrypt")
		{
			std::cout << "Type the message to encrypt: ";
			getline(std::cin, message);

			for (int n{}; n < message.length(); n++)
			{
				size_t index = alphabet.find(message[n]);
				message[n] = (index != std::string::npos) ? key[index] : ' ';

			}
			std::cout << "\nEnrypted message is: " << message << std::endl;
		}
		else if (option == "Decrypt" || option == "decrypt")
		{
			std::cout << "Type the message to decrypt: ";
			getline(std::cin, message);

			for (int n{}; n < message.length(); n++)
			{
				size_t index = key.find(message[n]);
				message[n] = (index != std::string::npos) ? alphabet[index] : ' ';
			}
			std::cout << "\nDecrypted message is: " << message << std::endl;
		}
		else
		{
			option = "wrong_input";
			std::cout << "\nWrong input, try again!" << std::endl;
		}

		std::cout << "\nContinue? (y/n) -> ";
		std::cin >> proceed;
		std::cin.ignore();

	} while (proceed == 'y' || option == "wrong_input");

	std::cout << std::endl;
	return 0;
}
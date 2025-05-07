// include string to be able to use getline() function
#include <string>
#include <iostream>
using namespace std;

int main() {

	string input_string{};
	cout << "What is the input string? ";

	// Storing the whole text line into an input_string, not just the first word.
	getline(cin, input_string);

	while (input_string.empty()) {
		cout << "You cannot pass an empty string! Try again: ";
		getline(cin, input_string);
	}

	cout << input_string << " has " << input_string.length() << " characters." << endl;

	return 0;
}

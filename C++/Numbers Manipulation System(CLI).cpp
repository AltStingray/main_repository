#include <iostream>
#include <vector>

// Passing vector to a function by value creates a copy of the original vector. Therefore, modifications done inside the function add_to_vec for example will not affect the original vector.
// The pass by reference method passes the reference of the vector to the function. It does not create the copy of vector therefore, all modifications done in the function will be reflected in the original array.


void display_menu() {

	std::cout << "Choose an option: \n"
		<< "P - Print numbers\n"
		<< "A - Add a number\n"
		<< "D - Delete numbers\n"
		<< "C - Clean the list\n"
		<< "M - Display mean of the numbers\n"
		<< "S - Display the smallest number\n"
		<< "L - Display the largest number\n"
		<< "Q - quit the program" << std::endl;
}

// Show numbers in the vector
void show_vec(std::vector<int> vec_numbers) {

	if (!vec_numbers.empty()) 
	{
		size_t n{};
		
		std::cout << "\nThe numbers in the list are:\n";
		while (n < vec_numbers.size()) 
		{
			std::cout << vec_numbers[n] << " ";
			n++;
		}
	}
	else std::cout << "\nThe list is empty!";

	std::cout << std::endl;
}


// Notice the reference method here
// Add numbers to the vector
void add_to_vec(std::vector<int>& vec_numbers) {

	int num{};

	std::cout << "\nEnter a number: ";
	std::cin >> num;
	std::cout << "Number " << num << " is added to the list.";

	vec_numbers.push_back(num);

	std::cout << std::endl;
}


// Delete numbers from the vector
void delete_from_vec(std::vector<int>& vec_numbers) {

	if (!vec_numbers.empty())
	{
		std::cout << "\nThe numbers in the list are:\n";
		for (int n : vec_numbers)
		{
			std::cout << n << " ";
		}

		int del_num{};

		std::cout << "\nWhich number do you want to delete? ";
		std::cin >> del_num;

		for (size_t n{}; n < vec_numbers.size(); n++)
		{
			if (del_num == vec_numbers[n])
			{
				vec_numbers.erase(vec_numbers.begin() + n);
			}
			else std::cout << "\nNo such number in the list!";
		}
		std::cout << "Number " << del_num << " deleted!";
	}
	else std::cout << "\nThe list is empty! Add some numbers first!";

	std::cout << std::endl;
}


// Clean the vector
void clean_vec(std::vector<int>& vec_numbers) {

	char proceed{};

	std::cout << "\nAre you sure? (y/n) -> ";
	std::cin >> proceed;

	if (proceed == 'y' || proceed == 'Y')
	{
		vec_numbers.clear();

		std::cout << "The list has been cleared!";
	}

	std::cout << std::endl;
}


// Determine the average number of the vector
void mean_vec(std::vector<int> vec_numbers) {

	if (!vec_numbers.empty())
	{
		int nums_sum{};

		for (int n{}; n < vec_numbers.size(); n++)
			nums_sum += vec_numbers[n];
		float mean_num {static_cast<float>(nums_sum) / vec_numbers.size()};

		std::cout << "\nThe average number is: " << mean_num;
	}
	else std::cout << "\nThe list is empty! Add some numbers first!";

	std::cout << std::endl;
}


// Determine the smallest number in the vector
void vec_min_num(std::vector<int> vec_numbers) {

	if (!vec_numbers.empty())
	{
		int min_number{vec_numbers[0]};

		for (int n{}; n < vec_numbers.size(); n++)
		{
			min_number = (vec_numbers[n] < min_number) ? vec_numbers[n] : min_number;
		}

		std::cout << "\nThe smallest number in the list is " << min_number;

	}else std::cout << "\nThe list is empty! Add some numbers first!";

	std::cout << std::endl;
}


// Determine the largest number in the vector
void vec_max_num(std::vector<int> vec_numbers) {

	if (!vec_numbers.empty())
	{
		int max_number{ vec_numbers[0] };

		for (int n{}; n < vec_numbers.size(); n++)
		{
			max_number = (vec_numbers[n] > max_number) ? vec_numbers[n] : max_number;
		}

		std::cout << "\nThe largest number in the list is " << max_number;

	}
	else std::cout << "\nThe list is empty! Add some numbers first!";

	std::cout << std::endl;
}


// A program that represets a menu with different options. User can enter different letters to select those options to manipulate with numbers and lists.
int main() {

	std::cout << "Welcome to the numbers manipulation program!\n\n";
	display_menu();

	char option{};
	std::vector<int> vec_numbers{};

	do
	{
		std::cout << "/";
		std::cin >> option; // Waiting for user input here before proceeding 

		system("cls");
		display_menu();

		switch (option) 
		{
		case 'P': case 'p': show_vec(vec_numbers); break;
		case 'A': case 'a': add_to_vec(vec_numbers); break;
		case 'D': case 'd': delete_from_vec(vec_numbers); break;
		case 'C': case 'c': clean_vec(vec_numbers); break;
		case 'M': case 'm': mean_vec(vec_numbers); break;
		case 'S': case 's': vec_min_num(vec_numbers); break;
		case 'L': case 'l': vec_max_num(vec_numbers); break;
		case 'Q': case 'q': break;

		default: std::cout << "\nWrong input, try again!" << std::endl;
		}

	} while (option != 'q' && option != 'Q');

	std::cout << "\nGoodbye...";

	std::cout << std::endl;
	return 0;
}
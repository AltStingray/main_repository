#include "Object.h"
#include <iostream>
using namespace std;




void Object::BeginPlay()
{
	cout << "Object BeginPlay() called!\n\n";
}
void Object::ObjectFunction()
{
	{
		cout << "ObjectFunction() called!\n\n";
	}
}
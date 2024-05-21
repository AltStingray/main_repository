#pragma once //allows not to include function below again and again in another files more than 1 time, instead it's cause error






class Object
{
public:
	virtual void BeginPlay(); // because this function have virtual, we can override child classes

	void ObjectFunction();
};
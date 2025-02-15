#include <iostream>
#include "Object.h"
#include "Actor.h"
#include "Pawn.h"
using namespace std;

void InheritanceFunction()
{
	Object* PtrToObject = new Object;
	Actor* PtrToActor = new Actor;
	Pawn* PtrToPawn = new Pawn;

	Object* ArrayObj[] = { PtrToObject, PtrToActor, PtrToPawn };

	for (int i = 2; i < 3; i++)
	{
		//ArrayObj[i]->BeginPlay(); leave it here for just in case


		Object* obj = ArrayObj[i];
		if (obj)
		{
			obj->ObjectFunction();
		}


		Actor* act = dynamic_cast<Actor*>(obj); //if this function won't succeed, then it will be a null
		if (act) //if it will be a null, then if and "act" not manage to proceed
		{
			act->ActorFunction();
		}


		Pawn* pwn = dynamic_cast<Pawn*>(act);
		if (pwn)
		{
			pwn->PawnFunction();
		}
	}


	delete PtrToObject;
	delete PtrToActor;
	delete PtrToPawn;
}



int main()
{

	InheritanceFunction();

	system("pause");
}
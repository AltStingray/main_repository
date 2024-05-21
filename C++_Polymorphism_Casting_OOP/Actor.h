#pragma once
#include "Object.h"





class Actor : public Object
{
public:
	virtual void BeginPlay() override;

	void ActorFunction();
};
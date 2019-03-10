#ifndef BANK1_ACCOUNT_H
#define BANK1_ACCOUNT_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "basic_account.h"

// this is a derived class from the basic account class;
// following LSP principle, 
// the reference of BasicAccount in any function can be substituted
// by the derived class without causing any trouble.
class Bank1_Account: public BasicAccount {

public:
	// just follow the constructor of the basic bank account
	Bank1_Account(double init_amt, double interest_r): BasicAccount(init_amt, interest_r) {};


	// different types of bank accounts have different ways of calculating;
	// this one has compound interest rate
	double calculate_amt_in_x_years(int years) {
		double rate = 1 + this->interest_rate;
		double amt_new = this->amount * pow(rate, years );
		return amt_new;
	};
};

#endif

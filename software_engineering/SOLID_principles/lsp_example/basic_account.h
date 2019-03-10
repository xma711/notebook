#ifndef BASIC_ACCOUNT_H
#define BASIC_ACCOUNT_H

#include <stdio.h>
#include <stdlib.h>

class BasicAccount {
// use protected instead of private
// to allow derived classes to use the attributes directly
protected:
	double amount;
	double interest_rate;

public:
	BasicAccount(double init_amt, double interest_r) {
		this->amount = init_amt;
		this->interest_rate = interest_r;
	};

	// all derived classes follow this function too;
	// with different implementation of calculate_amt_in_x_years,
	// this function still stands.
	double amount_in_x_years_based_on_interest(int years) {
		double amt_x = calculate_amt_in_x_years(years);
		return amt_x;
	};

	// different types of bank accounts have different ways of calculating;
	// for the basic one, use simple interests
	virtual double calculate_amt_in_x_years(int years) {
		double amt_new = this->amount + this->amount * this->interest_rate * years;
		return amt_new;
	};
};

#endif

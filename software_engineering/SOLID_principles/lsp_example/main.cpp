// a pratice to use the Liskov substitution principle (LSP)

#include <stdio.h>
#include <stdlib.h>
#include "basic_account.h"
#include "bank1_account.h"

// this function doesn't assume the account passed in must be BasicAccount;
// the account can be substituted by any account class that derive from the BasicAccount class.
// this follows the LSP!
void calculate_amt_in_10_years(BasicAccount* acc) {
	int yrs = 10;
	double amt = acc->calculate_amt_in_x_years(yrs);
	printf("amt in %d years = %f\n\n", yrs, amt);
};

int main() {
	// declare a basic account
	BasicAccount basic = BasicAccount(100, 0.02);
	printf("Using basic account:\n");
	calculate_amt_in_10_years(&basic);

	// declare a specific account from bank 1; use the same parameters for easier comparision
	Bank1_Account bank1_acc = Bank1_Account(100, 0.02);
	printf("Using Bank1 account:\n");
	calculate_amt_in_10_years(&bank1_acc);

	return 0;
}

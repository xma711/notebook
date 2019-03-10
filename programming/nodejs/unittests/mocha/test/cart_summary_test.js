// reference: https://www.codementor.io/nodejs/tutorial/unit-testing-nodejs-tdd-mocha-sinon

// run this test using: mocha ./cart_summary_test.js
// or, in one directory up, simply run 'mocha'

var chai = require('chai');

var expect = chai.expect;

var cartSummary = require('../cart_summary');

// how come i can use function 'describe' directly
describe('cartSummary', 
	function () {
		it ('getSubtotal() should return 0 if no items are passed in', 
			function () {
				var cartSummary1 = new cartSummary([]);
				expect(cartSummary1.getSubtotal()).to.equal(0); 
			} // end of callback function inside it 
		); // end of it function

		it('getSubtotal() should return the sum of the price * quantity for all items', function() {
  			var cartSummary2 = new cartSummary([{
    					id: 1,
    					quantity: 4,
    					price: 50
  				}, {
    					id: 2,
    					quantity: 2,
    					price: 30
  				}, {
    					id: 3,
    					quantity: 1,
    					price: 40
  				}
				]
			); // end of declaring cartSummary2

  			expect(cartSummary2.getSubtotal()).to.equal(300);
			} // end if cakkback function for it

		); // end of it function
	
	} // end of callback function inside describe
); // end describe

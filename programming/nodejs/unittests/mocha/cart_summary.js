function cartSummary(items) {
	this._items = items;
}

// each item in the array items should look something like this:
// {
//    id: 1,
//    quantity: 4,
//    price: 50
//  }

// return the total price
cartSummary.prototype.getSubtotal = function() {
	if (this._items.length) {
		return this._items.reduce(
			function(subtotal, item) {
				return subtotal += (item.quantity * item.price);
			},
			0
		); // end reduce function
	};

	return 0;	
};

module.exports = cartSummary;

const x = 1;

console.log(x);

x = 2; // no effect; but there won't be any warning..

console.log(x);


var exports = module.exports = {}
//const exports.x = x; // this line will lead to error; cannot use it this way
exports.x = x; // other module can still change the value of x; apparently exports.x is another memory location, its content just happens to be assigned as the local x


const y = 2; // this one cannot be imported
z=3;

exports.z = z;

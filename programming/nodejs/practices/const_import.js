var consts = require('./const');
console.log("original x = " + consts.x);
consts.x = 10;
console.log("x = " + consts.x);

console.log("z = " + z);

//console.log("y = " + y);

exports.z = 4;
console.log("exports.z = "+ exports.z + "; (global) z = " + z);

// import greeting_export from greeting_export.js
// then use the exported functions to do something

greeting = require('./greeting_export')

greeting.say_hello_in_english()

greeting.say_hello_in_spanish()

greeting.say_hello_in_english.longer_greeting()

greeting.say_hello_in_german()

// following will fail because the function is local to the greeting_export.js
//greeting.say_hello_in_german_implementation() 

console.log('\n try with a class:')

obj = new greeting.greetings_in_different_languages()

obj.say_hello_in_english()

obj.say_hello_in_german()

//console.log(num)  // this will failed
 
console.log(greeting.num) // but this is okay!

console.log(obj.number) // external module is able to see the variables inside the obj! the default behaviour is public!

obj.set_some_numbers(1 , 2, 5);
obj.set_some_numbers(100, 67);
console.log(greeting.num2);
console.log("in import: num22 = " + num22);
console.log("in import: num33 = " + num33);

num33 = 99
console.log("in import: num33 = " + num33);
num22 = 44
console.log("in import: num22 = " + num22);

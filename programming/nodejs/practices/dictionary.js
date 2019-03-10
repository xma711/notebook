
// like python, the key can be string (seems default) or other types like int
// cannot have a list like [1, 3] or tuple (1, 3) as the key or value
person = {gender:"male", age:23, job:"engineer", 10:'whatever', greet:function(){console.log("hello there!")}, }

console.log(person)
console.log("use int as key:")
console.log(person[10])
console.log("use string as key:")
console.log(person['gender'])

console.log("function header as the value:")
console.log(person['greet'])
console.log(person['greet']())

// an example shows how to start an external process and then kill it

var child_process = require('child_process')
var spawn = require('child_process').spawn;

console.log('start an external process and detach');

p1 = spawn('sleep', ['100'], {
    detached: true
});

//console.log(p1)


console.log('pid of the external process = ' + p1.pid)

console.log('now kill pid ' + p1.pid)

child_process.execSync("kill -9 " + p1.pid);

console.log("end of file");

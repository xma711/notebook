// an example shows how to start an external process and then kill it

var child_process = require('child_process')
var spawn = require('child_process').spawn;

console.log('start an external process and detach');

var run_linux_comand_sync = function(cmd, timeout_ms) {
	var timeout_set = timeout_ms;
	if (timeout_ms == undefined) {
		timeout_set = 5000;
	}
	child_process.execSync(cmd, timeout=timeout_set); // timeout is 5000 ms
}

var spawn_process = function(cmd) {
	cmd_list = cmd.split(' ');
	program_name = cmd_list[0]
	args_list = cmd_list.slice(1, 100)

	proc1 = child_process.spawn(program_name, args_list, {
    		detached: true
	});
	return proc1.pid;
}

var kill_process = function (pid) {
	cmd = "kill -9 " + pid
	run_linux_comand_sync(cmd);
}

cmd = "sleep 100"

pid = spawn_process(cmd);


console.log('pid of the external process = ' + pid)

console.log('now kill pid ' + pid)

kill_process(pid)

console.log("end of file");

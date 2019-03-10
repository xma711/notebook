 <html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php 
	echo '<p>Hello World</p>'; 
	echo "<p>Hello world again!</p>";
	// seems that every line needs to end with ;
	// variable assignment looks like bash script, but with $ in front
	$txt = "<p>hello world in a variable</p>";
	echo $txt;

	function myTest () {
		// note that from php's point of view, <p> is just some characters to print
		// it makes sense for html only
		echo "<p>echo from a function</p>";
	}
	myTest();
 ?> 
 </body>
</html>

About this example
-----------------

Follow https://itsfoss.com/use-swift-linux/

one outdated info in the reference is that empty Package.swift is no longer supported.

Need to use "swift package init" to create a nonempty Package.swift.

There has to be a Sources/ folder, in which the main code exists.

Then just "swift build" to build the program.
The resulant binary file can be found in .build/debug/Hello

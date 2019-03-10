about this example
-----------------

follow https://itsfoss.com/use-swift-linux/

one outdated info in the reference is that empty Package.swift is no longer supported.

need to use "swift package init" to create a nonempty Package.swift.

there has to be a Sources/ folder, in which the main code exists.

then just "swift build" to build the program.
the resulant binary file can be found in .build/debug/Hello

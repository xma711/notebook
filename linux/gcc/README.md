Options
--------------

-l (small L): to add shared libraries. e.g.  LDFLAGS=-lmosquitto

-L: let gcc/g++ know where the shared libraries are

-I (capital i): let gcc know where the .h file can be found. e.g. CFLAGS += -I$(MAIN_DIR)/lib/$(BOARD)/Mosquitto


name convention
------------------

Toolchains have a loose name convention like arch[-vendor][-os]-abi.

    arch is for architecture: arm, mips, x86, i686...

    vendor is tool chain supplier: apple,

    os is for operating system: linux, none (bare metal)

    abi is for application binary interface convention: eabi, gnueabi, gnueabihf

btw, the "sudo apt-get install gcc-arm-linux-gnueabihf" is actually installing the linaro arm cross toolchain. so it is similar to arm-linaro-linux-gnueabihf, but maybe with a different version numbers.

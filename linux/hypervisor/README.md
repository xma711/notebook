notes
----------------------

reference: https://www.networkworld.com/article/3243262/virtualization/what-is-a-hypervisor.html

a hypervisor is a process that separates a computer's operating system and applications 
from the underlying physical hardware.

hypervisor drives the concept of virtualization by allowing the physical host machine to operate multiple vms as guests.

there are 2 types of hypervisors: type 1 and type 2.  

type 1 hypervisors are sometimes called 'native' or 'bare metal' hypervisors,
run directly on the host's hardware to control the hardware and manage the guest VMs.
such hypervisors include Xen, Oracle VM Server for SPARC, Oracle VM Server for x86, Microsoft Hyper-V and VMware's ESX/ESXi.

type 2 hypervisors are sometimes called 'hosted hypervisors'.
they run on a conventional OS, just like other applications on the system.
in this case, a guest os runs as a process on the host, 
while hypervisors separate the guest os from the host os.  
examples of type 2 hypervisors include VMware Workstation, VMware Player, VirtualBox and Parallels Desktop for Mac.

in the enterprise center space, there are 3 major vendors on the hypervisors: VMware, Microsoft and Citrix Systems.

question: which type is qumu-system-x86_64? 
answer: type 2.


qemu
--------------------------

reference: https://en.wikipedia.org/wiki/QEMU

qumu is short for Quick Emulator.

it is a hosted hypervisor that performs hardware virtualization.

it emulates CPUs through dynamic binary translation and provides a set of device models,
enabling them to run a variety of unmodified guest operating systems.

it also can be used with kvm to run virtual machines at near-native speed.

operating modes:  
- user-mode emulation  
- system emulation: qemu emulates a full computer system including peripherals.
	it can be used to provide virtual hosting of several virtual computers on a single computer.
	qumu can boot many guest OS, including linux, windows, bsd etc.  
- kvm hosting: qemu deals with the setting up and migration of kvm images.
	it is still involved in the emulation of hardware, but the execution of the guest is done by kvm as requested by qemu.  
- xen hosting: qemu is involved only in the emulation of hardware;
	the execution of the guest is done within xen and is totally hidden from qemu.


kvm
-------------------

reference: https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine

kvm stands for kernel-based virtual machine.  
it is a virtualizatioin infrastructure for the linux kernel that turns it into a hypervisor

kvm requires a process with hardware virtualization extensions.  
kvm originally supported x86 processors and has been ported to s/390, powerpc and ia-64.

a wide variety of guest operating systems work with kvm, 
including many versions of linux, bsd, solaris, windows, os x, etc.

by itself, kvm does not perform any emulation.
it exposes the /dev/kvm interface, which userspace host (such as qemu) can then use to:  
- set up the guest vm's address space. the host must also supply a firmware image  
- feed the guest simulated i/o  
- map the guest's video display back onto the system host.

on linux, qemu is one such userpsace host. 
qemu uses kvm when available to virtualize guests at near-native speeds,
but otherwise falls back to software-only emulation.

there are some graphical management tools. one example is "virtual machine manager" - 
supports creating, editing, starting and stopping kvm-based virtual machines.


cloudstack
--------------------------

reference: https://en.wikipedia.org/wiki/Apache_CloudStack

cloudstack is cloud computing software for creating, managing and deploying infrastructure cloud services.  
it uses existing hypervisors such as kvm, VMware ESXi|VMware vcenter and XenServer/XCP for virtualization.  
in addition to its own API, cloudstack also supports the aws API and open cloud computing interface from the open grid forum.

deployment: the minimum production consists of one machine running the cloudstack management server,
and another machine to act as the cloud insfrastructure.
in its smallest deployment, a single machine can act as both the management server and the hypervisor host (using the kvm hypervisor).

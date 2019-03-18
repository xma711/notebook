Check cpu clock speed
----------------------
Dynamically watch the change: watch -n 1  cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq

in fact, ' cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq ' should be enough.

Another way is to use cpufreq-info from the cpufrequtils software (to install it in archlinux: pacman -S cpufrequtils).  
To check cpu clock speed, use: cpufreq-info -f

set cpu clock speed
-----------------------------

In bbb + archlinux, to run cpu at minimum clock speed:  
	echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

to run cpu at maximum clock speed, change "powersave" to "performance"

more about cpu frequency: https://wiki.archlinux.org/index.php/CPU_frequency_scaling

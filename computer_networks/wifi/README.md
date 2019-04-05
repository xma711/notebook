Find ssid from command line
------------------------------

Reference: https://askubuntu.com/questions/117065/how-do-i-find-out-the-name-of-the-ssid-im-connected-to-from-the-command-line

In short: use 'iwgetid' to get the ssid. 


Solve Ubuntu WiFi problem
----------------------

Just disable the power saving for WiFi:

/sbin/iwconfig wlan0 power off


Configure WiFi using command line.
------------------------------

In archlinux or Debian or Gentoo, using reference https://wiki.archlinux.org/index.php/Wireless_network_configuration

Command:

```
    wpa_supplicant -D nl80211,wext -i wlan0 -c <(wpa_passphrase "your_SSID" "your_key")
```

If this does not work, you may need to adjust the options.
If connected successfully, continue in a new terminal (or quit wpa_supplicant with Ctrl+c and add the -B switch to the above command to run it in the background).
WPA supplicant contains more information on options and on how to create a permanent configuration file for the wireless access point. 

In my case, the command is:

```
    wpa_supplicant -B -D nl80211,wext -i wlp6s0 -c <(wpa_passphrase "SSID" "the_key")
```

In Debian, also need to get an ip address:

```
    dhclient wlan0
```

In Gentoo, get and ip address using:

```
    dhcpcd
```

Note that NetworkManager is easier to manage WiFi or Ethernet.


Router
-----------------------

Router can be configured as a normal Ethernet router, or a repeater.

A repeater forwards all requests to the main router.

Issues and solutions
------------------------------------------

If after "systemctl restart NetworkManager" or suspend, the wifi ssid disappear from the dropdown list in the connection icon on the top right corner,
then it can be solved by "sudo systemctl restart network-manager.service"  
(wait... it seems NetworkManager and network-manager are the same thing...)

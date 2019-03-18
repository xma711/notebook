Iptables
--------------------

General reference: https://www.digitalocean.com/community/tutorials/how-to-list-and-delete-iptables-firewall-rules  
most frequently used iptables rules: http://www.thegeekstuff.com/2011/06/iptables-rules-examples  

list current rules in iptables: iptables -L

to add a rule: iptables -A INPUT(or other hooks) -j ACCEPT(or other actions)

possible places to hook: INPUT, OUTPUT, FORWARD, PREROUTING and POSTROUTING

possible actions: ACCEPT, DROP, REJECT.  
	- difference between DROP and REJECT is that DROP has no feedback to sender, but REJECT sends back a 'reject' msg.  DROP is more secured.

To delete a rule, list them first: iptables -L --line-numbers  
then: iptables -D INPUT(or other hooks) <number>

to save rules: sudo iptables-save > /tmp/iptables.txt (sudo is needed)

to restore rules: sudo iptables-restore < /tmp/iptables.txt

in fact, to modify the orderings of the rules, just save them to a file,
and then modify the file directly, 
and then restore the rules from the file.  
Reference: http://unix.stackexchange.com/questions/146349/move-iptables-rule-w-o-removing-and-adding

to enable ssh only:  
iptables -A INPUT -p tcp --dport 22 -j ACCEPT  
iptables -A INPUT -j DROP  
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT  # note that "-p tcp" is needed for --sport  
iptables -A OUTPUT -j DROP

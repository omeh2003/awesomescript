### Scan a single ip address ###
nmap 192.168.1.1

## Scan a host name ###
nmap server1.cyberciti.biz

## Scan a host name with more info###
nmap -v server1.cyberciti.biz

nmap 192.168.1.1 192.168.1.2 192.168.1.3
## works with same subnet i.e. 192.168.1.0/24
nmap 192.168.1.1,2,3

#Detect
nmap -A 192.168.1.254
nmap -v -A 192.168.1.1

#6. Find out if a host/network is protected by a firewall using namp command
## nmap command examples for your host ##
nmap -sA 192.168.1.254
nmap -sA server1.cyberciti.biz

#7. Scan a host when protected by the firewall
nmap -PN 192.168.1.1
nmap -PN server1.cyberciti.biz

#9. Scan a network and find out which servers and devices are up and running
nmap -sP 192.168.1.0/24

#10. How do I perform a fast scan using the namp?

nmap -F 192.168.1.1

#11. Display the reason a port is in a particular state
nmap --reason 192.168.1.1

#12. Only show open (or possibly open) ports using nmap command in Linux
nmap --open 192.168.1.1

#14. Show host interfaces and routes
nmap --iflist

nmap --iflist  | xargs echo | grep   -E  -o --regexp='((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'


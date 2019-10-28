# email_bruter
Quickly find email servers for a given domain via DNS brute forcing.  Limited Brute Force Scope.

Script "Brute Forces" through the following subdomains for a provided domain:
```email
webmail
mail
autodiscover
owa
owa2
outlook
exchange
smtp
smtp2
pop3
imap
```
These subdomains are just commonly found subdomains found for email servers I've found in on engagements.  I am open to accepting additional input.  If you know of additional subdomains, feel free to add more!

# Help Menu:
```
./email_bruter.py -h
usage: email_bruter.py [-h] -d DOMAIN

Email Server DNS Recon Tool

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain.com
```

# Example Usage:
```
./email_bruter.py -d secureworks.com
[+] webmail.secureworks.com : 206.55.101.90
[+] mail.secureworks.com : 206.55.100.43
[+] autodiscover.secureworks.com : 206.55.101.113
```

#!/usr/bin/python
import dns.resolver
import argparse
from colorama import Fore,Style

def get_args():
	p = argparse.ArgumentParser(description="Email Server DNS Recon Tool")
	p.add_argument('-d','--domain',type=str,help='domain.com',required=True)

	args = p.parse_args()

	return args

def a_lookup(record):
	ip = ""
	try:
		answers = dns.resolver.query(record,'A')
		for ip in answers:
			return ip
	except Exception as e:
		print(Fore.RED + "[!] No Record For %s" % record + Style.RESET_ALL)
		return "0.0.0.0"

def main():
	args = get_args()

	subdomains = ['email','webmail','mail','autodiscover','owa','owa2','outlook','exchange','smtp','smtp2','pop3','imap']

#	dnsServers = get_dnsServers(args)

	records = {}
	for subdomain in subdomains:
		hostname = subdomain+"."+args.domain
		records[hostname] = a_lookup(hostname)
	for k,v in records.iteritems():
		if "0.0.0.0" in str(v):
			continue
		else:
			print(Fore.GREEN+Style.BRIGHT+"[+] "+Style.RESET_ALL + "%s : %s" % (k,v))


if __name__ == '__main__':
	main()

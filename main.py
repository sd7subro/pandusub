from time import sleep
import telepot

def fetch_token():
	try:
		with open('token.txt') as obj:
			contents = obj.read()
	except FileNotFoundError:
		print("[!] File not found. Create a file named 'token.txt' with only BOT API in it.")
	except PermissionError:
		print("[!] File can't be read. Check for permissions.")
	else:
		return contents

def listen(BOT, offset = 0):
	updates = BOT.getUpdates(offset+1)
	if updates:
		offset = updates[-1]['update_id']
	return [updates, offset]


def main(BOT):
	offset = 0
	while(True):
		updates, offset = listen(BOT, offset)
		for update in updates:
			print("[+] New Message received. Update_ID :"+str(update['update_id']))
		sleep(1)
		
if __name__ == '__main__':
	token = fetch_token().strip()
	BOT = telepot.Bot(token)
	main(BOT)
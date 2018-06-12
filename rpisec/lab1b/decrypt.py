def decrypt(case_number):
	key = 'Q}|u`sfg~sf{}|a3'
	counter = 0
	plain_text = ''

	for i, _ in enumerate(key):
		x = ord(key[i]) ^ case_number
		plain_text += chr(x)
		
	return plain_text

if __name__=='__main__':
	for i in range(0, 22):
		if decrypt(i) == 'Congratulations!':
			print(i)

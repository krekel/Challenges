def serial_generator(username):
	seed = (ord(username[3]) ^ 0x1337) + 0x5EEDED

	for char in username:
		serial = ord(char) ^ seed
		temp = serial

		mult = hex(serial * 0x88233B2B)[0:8]
		serial = (serial - int(mult, 16))
		serial >>= 1
		serial += int(mult, 16)
		serial >>= 0x0A
		serial *= 0x539
		serial = temp - serial
		seed += serial 

	return seed

if __name__ == '__main__':
	username = input('username: ')
	serial = serial_generator(username)
	print('serial: {}'.format(serial))

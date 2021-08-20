def cipher_str(code_str:str, key_str:str):
	code_list = [str(bin(ord(i)))[2:] for i in code_str]
	key_list = [str(bin(ord(i)))[2:] for i in key_str]
	for i in range(len(code_list)):
		if len(code_list[i]) > len(key_list[i]):
			key_list[i] *= 2
	cipher_list = []
	for i in range(len(code_list)):
		temp_code_list = [int(s) for s in code_list[i]]
		temp_key_list = [int(s) for s in key_list[i]]
		for j in range(len(code_list[i])):
			cipher_list.append(temp_code_list[j] ^ temp_key_list[j])
		cipher_list.append("/")
	cipher_str = "".join(str(b) for b in cipher_list)
	return cipher_str
def decipher_str(code_str:str, key_str:str):
	code_list = code_str.split("/")
	code_list.pop()
	key_list = [str(bin(ord(i)))[2:] for i in key_str]
	for i in range(len(key_list)):
		if len(code_list[i]) > len(key_list[i]):
			key_list[i] *= 2
	decipher_list = []
	temp_decipher_list = []
	for i in range(len(key_list)):
		temp_code_list = [int(s) for s in code_list[i]]
		temp_key_list = [int(s) for s in key_list[i]]
		for j in range(len(code_list[i])):
			temp_decipher_list.append(str(temp_code_list[j] ^ temp_key_list[j]))
		decipher_list.append("".join(str(b) for b in temp_decipher_list))
		temp_decipher_list = []
	for i in range(len(decipher_list)):
		decipher_list[i] = chr(int(decipher_list[i],2))
	decipher_str = "".join(str(i) for i in decipher_list)
	return decipher_str
#print(decipher_str(cipher_str("123qwe", "123qwe"), "123qwe"))
print(cipher_str("123qwe", "123qwe"))
print(decipher_str("000000/001011/000001/0000011/0000011/0011100/", "1sdrty"))
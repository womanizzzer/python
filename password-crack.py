#!/usr/bin/python3

#SHA512 Dictionary Attack

import crypt

salt ="$6$7Es6.hsx$"
password_hash = "$6$7Es6.hsx$b0VBK7WB7BFg3t5AQky6KaY6vBcBR1nzjrHCwe2SpUfQCreD9bIpUKx203U7wrC1SCgznQ/4SPZLe54VC2QGE/"

with open("./password-crack-dictionary.txt") as file:
	for line in file:
		word = line.strip()
		if crypt.crypt(word, salt) == password_hash:
			print("Decrypted password:", word)




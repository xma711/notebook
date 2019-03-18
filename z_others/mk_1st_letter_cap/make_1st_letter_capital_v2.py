# have to run this with python3

import sys

print (f"sys.argv = {sys.argv}")

filename = sys.argv[1]
print (f"filename = {filename}")

outfile = sys.argv[2]
print (f"outfile = {outfile}")

letters = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# make it to dictionary for faster searching
letters_dict = {}
for l in letters:
	letters_dict[l] = l
letters = letters_dict

def sentence_start(data, i):
	if not data[i] in letters:
		return False

	if i == 0:
		return True

	j = i - 1

	# have to be a new line
	if data[j] != '\n':
		return False

	while j >= 0:
		if data[j] != ' ' and data[j] != '\t' and data[j] != '\n' and data[j] != '\r' and data[j] != '(' and data[j] != "'" and data[j] != '"' and data[j] != ')':
			break
		j -= 1

	if j < 0:
		return True

	if data[j] == '.' or data[j] == '?' or data[j] == '!':
		return True

	if data[j] == '-' and j > 8:
		all_dash = True
		for k in range(j-8, j):
			if data[k] != '-':
				all_dash = False
				break
		if all_dash == True:
			return True

	return False

with open(filename, 'r') as myfile:
	data = myfile.read()
	data2 = str(data)
	print (f"flen(data) = {len(data)}")
	for i in range(len(data)):
		if sentence_start(data, i):
			data2 = data2[:i] + data[i].upper() + data[i+1:]

assert (len(data2) == len(data))
with open(outfile, 'w') as f:
	f.write(data2)
	print (f"data is written to {outfile}")

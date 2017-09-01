

s = "30167b0eb4eef511ec82272b4b47a2d71471"
key = "1319057cb23c1dcbf616876372617fff8b48"

res = ""
for i in range(0, len(s), 2):
	s_num = int(s[i:i+2], 16)
	k_num = int(key[i:i+2], 16)
	xor = s_num ^ k_num
	res = res + "{:02X}".format(xor)

print res

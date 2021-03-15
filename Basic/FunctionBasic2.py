def phone(**data):
	count = 0
	for name,pirce in data.items():
		row = "{:20}{:10}" .format(name,pirce)
		print(row)
		count = count + pirce
	return count
t = phone(ip = 10000, nokia = 20000, samsung = 30000, mi = 90000)
print("-"*30)
print("{:20}{:10}" .format('Tong', t))
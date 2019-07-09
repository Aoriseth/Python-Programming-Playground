# 1.	Substitute for any subtractives to obtain:	CCCLXVIIII + DCCCXXXXV
# 2.	Catenate to obtain:	CCCLXVIIIIDCCCXXXXV
# 3.	Sort to obtain:	DCCCCCCLXXXXXVVIIII
# 4.	Combine groups to obtain:	DCCCCCCLXXXXXXIIII
# 									DCCCCCCLLXIIII
# 									DCCCCCCCXIIII
# 									DDCCXIIII
# 									MCCXIIII
# 5.	Substitute any subtractives to obtain:	MCCXIV


subs = {"IV":"IIII",
		"IX":"VIIII",}



def substituteSmall(num):
	substituted = num
	for code,replacement in subs.items():
		if code in num:
			substituted = substituted.replace(code,replacement)
	return substituted


print(substituteSmall("IXIV"))
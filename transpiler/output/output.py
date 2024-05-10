option = 0
nateeja = 0
pehla_num = 0
dosra_num = 0
# menu
print("1- jama krne kelie 1 dabaein  \n")
print("2- manfi krne kelie 2 dabaein\n")
print("3- zarb krne kelie 3 dabaein\n")
print("4- taqseem krne kelie 4 dabaein\n")
print("9- band krne kelie 9 dabaein\n")
# eek asaan calculator ki app:
while 9 != option:
	option = int(input("option (number) darj karein: "))
	pehla_num = int(input("pehla_num (number) darj karein: "))
	dosra_num = int(input("dosra_num (number) darj karein: "))
	if 1 == option:
		nateeja = pehla_num + dosra_num
		print(nateeja)
	elif 2 == option:
		nateeja = pehla_num - dosra_num
		print(nateeja)
	elif 3 == option:
		nateeja = pehla_num * dosra_num
		print(nateeja)
	elif 4 == option:
		nateeja = pehla_num / dosra_num
		print(nateeja)
	elif 9 == option:
		print("Asaan calculator istemaal krne ka shukriya!\n")

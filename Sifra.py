

veta = str(input("Zadajte text:"))
sifraKey = int(input("Zadajte o kolko pismen ma byt sifra posunuta (zaporne cisla dolava, kladne doprava):"))


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
length = len(veta)
sifra = ""
for i in range(length):
	
	if veta[i] == " ":
		sifra = sifra + " "
	else:
		letterPos = alphabet.index(veta[i])
		if letterPos+sifraKey > 25 and sifraKey>=0:
			sifra = sifra + alphabet[letterPos-26+sifraKey]
		elif letterPos+sifraKey < 0 and sifraKey<0:   
			sifra = sifra + alphabet[letterPos+26 +sifraKey]
		else:
			sifra = sifra + alphabet[letterPos+sifraKey]
	
print(sifra)
	
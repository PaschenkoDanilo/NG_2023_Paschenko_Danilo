import string

text ="Terrgvatf, arjpbzre! Jr ner tynq gb frr, gung lbh unir fhpprffshyyl cnffrq bhe vavgvny grfg. Qba'g or fb cebhq bs lbhefrys - vg'f whfg n grfg gb svygre zbfg hfryrff crbcyr, gung pna qb abguvat sbe bhe pbzzhavgl. Orsber jr jvyy cnff lbh fbzr erny gnfxf gb qb - chg lbhe rapelcgvba penpxre gb lbhe ercbfvgbel. Anzr sbyqre Jr xabj, naq chg vafvqr qhzo_qrpelcgbe.cl. Nyfb, va beqre gb cnff guvf gnfx - lbh fubhyq jevgr Dhvf phfgbqvrg vcfbf phfgbqrf? nf n pbzzrag. Guvf zrffntr va pbzzrag frpgvba vf lbhe npprcgnapr sbe gur fbzr arj wbo gb qb. Jr ner jnvgvat..."
upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase

dictKeys = string.ascii_letters
dictValues = lowerCase[13:] + lowerCase[:13] + upperCase[13:] + upperCase[:13]
index = 0
rot13Dict = {}
for keys in dictKeys:
    rot13Dict[keys] = dictValues[index]
    index +=1

decryptedText =""
for letters in text:
        if letters in rot13Dict.keys():
            decryptedText += rot13Dict.get(letters)   
        else:
            decryptedText += letters
print (decryptedText)
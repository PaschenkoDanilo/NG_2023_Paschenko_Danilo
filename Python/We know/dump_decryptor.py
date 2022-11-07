import string

text ="Terrgvatf, arjpbzre! Jr ner tynq gb frr, gung lbh unir fhpprffshyyl cnffrq bhe vavgvny grfg. Qba'g or fb cebhq bs lbhefrys - vg'f whfg n grfg gb svygre zbfg hfryrff crbcyr, gung pna qb abguvat sbe bhe pbzzhavgl. Orsber jr jvyy cnff lbh fbzr erny gnfxf gb qb - chg lbhe rapelcgvba penpxre gb lbhe ercbfvgbel. Anzr sbyqre Jr xabj, naq chg vafvqr qhzo_qrpelcgbe.cl. Nyfb, va beqre gb cnff guvf gnfx - lbh fubhyq jevgr Dhvf phfgbqvrg vcfbf phfgbqrf? nf n pbzzrag. Guvf zrffntr va pbzzrag frpgvba vf lbhe npprcgnapr sbe gur fbzr arj wbo gb qb. Jr ner jnvgvat..."
upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase

for encreptedLetters in text:
    if encreptedLetters in upperCase:
        decryptor = ord(encreptedLetters)
        if decryptor <= 77:
            decryptor += 13
            decryptor = chr(decryptor)
        else:
            decryptor -= 13
            decryptor = chr(decryptor)
    elif encreptedLetters in lowerCase:
        decryptor = ord(encreptedLetters)
        if decryptor >= 110:
            decryptor -= 13
            decryptor = chr(decryptor)
        else:
            decryptor += 13
            decryptor = chr(decryptor)
    else:
        decryptor = encreptedLetters
    print (decryptor, end = "")
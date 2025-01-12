def numara_vocale(sir):
    vocale = "aeiouAEIOU"
    contor = 0
    for caracter in sir:
        if caracter in vocale:
            contor += 1
    return contor
print(numara_vocale("12345"))

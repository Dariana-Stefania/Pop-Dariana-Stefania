import string
text=""" Stiri de ultima ora"""
jumatate=len(text)//2
text_1=text[0:jumatate]
text_1=text_1.upper()
# text_1=text_1.replace(_old:" ",_new:" ")
text_2=(text[jumatate:])
text_2=text_2[: :-1]
text_2=text_2[0]+text_2[1].upper()+text_2[2:]
text_2=text_2.translate(str.maketrans(" ", " ", string.punctuation))
text_mare=text_1+text_2
print(text_mare)

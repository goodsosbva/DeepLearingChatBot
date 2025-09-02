from konlpy.tag import Komoran

# komoran = Komoran()

# text = "나는 지금 비가 많이 오는 기분이다."

# morphs = komoran.morphs(text)
# print(morphs)

# pos = komoran.pos(text)
# print(pos)

# nouns = komoran.nouns(text)
# print(nouns)

komoran = Komoran(userdic='./Tokenizing/user_dic.tsv')
text = "엔펠피 나는 내일, 어제의 너와 만난다"
pos = komoran.pos(text)
print(pos)
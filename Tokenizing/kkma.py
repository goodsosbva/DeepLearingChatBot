from konlpy.tag import Kkma

kkma = Kkma()

text = "나는 지금 비가 많이 오는 기분이다."

morphs = kkma.morphs(text)
print(morphs)

pos = kkma.pos(text)
print(pos)

nouns = kkma.nouns(text)
print(nouns)

sentances = "오늘 날씨? 어떰? 더움?"
s = kkma.sentences(sentances)
print(s)
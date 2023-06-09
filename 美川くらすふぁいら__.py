#-*- encoding:shift-jis -*-
#クラス　美川さん
class mikawa_kenichi:
    def __init__(self,name,sign,gender,feel):
        self.name = name
        self.sign = sign
        self.gender = gender
        self.feel = feel
#美川さんの誕生(神秘)
mikawa = mikawa_kenichi("美川","さそり座",'女','普通')


#美川さんが何座の何なのかを聞いてみよう
sign_list = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
gender_list = ["男","女"]

def find_sign(mikawa,sign_list):
    for i in range(len(sign_list)):
        print(f"{sign_list[i]}座ですか？")
        if mikawa.sign == sign_list[i]:
            print("頷く")
            mikawa.feel = "上機嫌"
            return sign_list[i]
        else:
            print("首を振る")
            mikawa.feel = "不機嫌"
        mikawa.feel = "絶望"

def find_gender(mikawa,gender_list):
    for i in range(len(gender_list)):
        print(f"{mikawa.name}さんは{gender_list[i]}ですか？")
        if mikawa.gender == gender_list[i]:
            print("頷く")
            return gender_list[i]
        else:
            print("首を振る")
        mikawa.feel = "絶望"

sign = find_sign(mikawa,sign_list)
gender = find_gender(mikawa,gender_list)
print(f"そうよ私は{sign}の{gender}～♪")
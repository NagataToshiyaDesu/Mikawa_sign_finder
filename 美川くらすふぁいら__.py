#-*- encoding:shift-jis -*-
#�N���X�@���삳��
class mikawa_kenichi:
    def __init__(self,name,sign,gender,feel):
        self.name = name
        self.sign = sign
        self.gender = gender
        self.feel = feel
#���삳��̒a��(�_��)
mikawa = mikawa_kenichi("����","�������",'��','����')


#���삳�񂪉����̉��Ȃ̂��𕷂��Ă݂悤
sign_list = ["���Ђ���", "��������", "�ӂ�����", "���ɍ�", "������", "���Ƃߍ�", "�Ă�т��", "�������", "���č�", "�€��", "�݂����ߍ�", "������"]
gender_list = ["�j","��"]

def find_sign(mikawa,sign_list):
    for i in range(len(sign_list)):
        print(f"{sign_list[i]}���ł����H")
        if mikawa.sign == sign_list[i]:
            print("����")
            mikawa.feel = "��@��"
            return sign_list[i]
        else:
            print("���U��")
            mikawa.feel = "�s�@��"
        mikawa.feel = "��]"

def find_gender(mikawa,gender_list):
    for i in range(len(gender_list)):
        print(f"{mikawa.name}�����{gender_list[i]}�ł����H")
        if mikawa.gender == gender_list[i]:
            print("����")
            return gender_list[i]
        else:
            print("���U��")
        mikawa.feel = "��]"

sign = find_sign(mikawa,sign_list)
gender = find_gender(mikawa,gender_list)
print(f"�����掄��{sign}��{gender}�`��")
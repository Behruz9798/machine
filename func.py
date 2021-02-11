# def ism_familiya(ism,familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()}!\n"
#     f"Foydalanuvchi familiyasi: {familiya.title()}!")
# ism_familiya('Anvar','Narzullayev')
# ism_familiya('Behruz','Murotaliyev')
# ism_familiya(familiya='majidov',ism='hakim')


# def age_count(ism,tugulgan_yili):
#     """ism va tug'ilgan yilini xisoblovchi function"""
#     print(f"{ism.title()} {2020-tugulgan_yili} yoshda!")

# age_count('Olim aka',1890)

# def age_sum(familiya,tugulgan_yili):
#     print(f"{familiya.title()} {2020-tugulgan_yili} yoshdalar xojaka!")

# age_sum('Salimov',1987)

# def age_count(tugulgan_yil,joriy_yil=2021):
#     print(f"Siz {joriy_yil-tugulgan_yil} yoshga kirdingiz xojaka!")

# age_count(1987,2021)
# age_count(1898)


# amaliyot 1

# name = str(input("Ismingizni kiriting: "))
# age = int(input("Yoshingizni kiriting:"))

# def year_count(age,year=2021):
#     print(f"{name} siz {year-age} yilda tug'ulgansiz!")

# year_count(age,2021)


# amaliyot2
# import random
# number = random.randrange(1,60)
# print(number)

# def hisobla(kvadrat,kub):
#     print(f"sonning kvadrati = {number**2} \n sonning kubi = {number**3}") 

# hisobla('kvadrat','kub')


# amaliyot3

# import random

# num = random.randrange(1,90)

# def juft_toq(juft,toq):
#     if num % 2 == 0:
#         print(num,"juft son")
#     else:
#         print(num,"toq son")
    
# juft_toq('juft','toq')



# amaliyot4

# import random

# num = random.randrange(1,90)
# num2 = random.randrange(1,100)


# print("1-son = ",num)
# print("2-son = ",num2)


# def maximum(max):
#     if num > num2:
#         print(num)
#     else:
#         print(num2)

#     if num == num2:
#         print("Sonlar o'zaro teng!")

# maximum('max')



# amaliyot5


# import random

# x = random.randrange(1,90)
# y = random.randrange(1,10)

# print(x)
# print(y)

# def darajaga_kotar(daraja):
#     print(x**y)

# darajaga_kotar('daraja')





#Function sariq.dev lesson 2


# def toliq_ism_yasa(ism,familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa('Anvar','Olimov')
# talaba2 = toliq_ism_yasa('Xasan','Majidov')
# print(f"Darska kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darska kechikib keldi.")



# def avto_info(kompaniya,model,rangi,karobka,yili,narx=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rangi':rangi,
#         'karobka':karobka,
#         'yili':yili,
#         'narx':narx
#     }
#     return avto

# avto_1 = avto_info('GM','Tracker','Qora','Avtomat','2020')
# avto_2 = avto_info('BMW','X6','Oq','Turbo','2021','3500$')
# avtolar = [avto_1, avto_2]
# print('Onlayn bozordagi mavjud mashinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = 'nomalum'
#     print(f"{avto['kompaniya']} {avto['model']} {avto['rangi']} {avto['karobka']} {avto['yili']} Narhi:{narx}")



# amali mashgulot_1
def person_info(ismi,familiyasi,tugulgan_yili,tugulgan_joyi,email=None,tel_nomer=None):
    person = {
        'ismi':ismi,
        'familiyasi':familiyasi,
        'tugulgan_yili':tugulgan_yili,
        'tugulgan_joyi':tugulgan_joyi,
        'email':email,
        'tel_nomer':tel_nomer
    }
    return person

person_1 = person_info('Xasan','Majidov','1997','Andijon','xasan@gmail.com')
person_2 = person_info('Davron','Kabulov','1987','Toshkent','davronkabulov@gmail.com','+998917778388')
print(person_1)
print(person_2)




# def oraliq(min,max,qadam):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 5
#     return sonlar

# print(oraliq(0,10,2))
# print(oraliq(10,30,2))



# # salondagi avtomobillar royxatini shakllantrish

# def avto_info(kompaniya,rangi,modeli,yili,karobka,narhi):
#     avto = {
#         'kompaniya':kompaniya,
#         'rangi':rangi,
#         'modeli':modeli,
#         'yili':yili,
#         'karobka':karobka,
#         'narhi':narhi
#     }
#     return avto

# print("Salondagi avtomobillar ro'yxatini shakllantramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:")
#     kompaniya = input("Ishlab chiqaruvchi:")
#     rangi = input("Rangini kiriting:")
#     modeli = input("Mashina rusumini kiriting:")
#     yili = input("Ishlab chiqarilgan sanasini kiriting:")
#     karobka = input("Karobka:")
#     narhi = input("Mashinaning narhini kiriting:")

#     avtolar.append(avto_info(kompaniya,rangi,modeli,yili,karobka,narhi)) 

#     javob = input("Yana avto qo'shasizmi? (yes/no)")

#     if javob == 'no':
#         break

# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto ['narhi']:
#         narhi = ['narhi']
#     else:
#         print("Noma'lum")
#     print(f"{avto['kompaniya']} {avto['rangi']} {avto['modeli']} {avto['yili']} {avto['karobka']} {avto['narhi']}")



# def baxola(ismlar):
#     baxolar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baxo = input(f"Talaba {ism.title()}ning baxosini kiriting: ")
#         baxolar[ism] = int(baxo)
#     return baxolar

# talabalar = ['ali','vali','xasan','xusan']
# baxolar = baxola(talabalar[:])
# print(baxolar)
# print(talabalar)
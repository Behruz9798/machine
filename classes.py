class Car:
    def __init__(self,korxona,rusumi,rangi,yili,karobkasi,narhi):
        self.korxona = korxona
        self.rangi = rangi
        self.yili = yili
        self.karobkasi = karobkasi
        self.narhi = narhi
        self.rusumi = rusumi
    def __str__(self):
        return "Korxona\t" + self.korxona + "Rusumi\t" + self.rusumi + "Rangi:\t" + self.rangi + "Yili:\t"+self.yili + "Karobkasi:\t"+self.karobkasi + "Narhi\t" + narhi
    
avtolist = []
while True:
    print("1-mashina qo'shish\n2-ro'yxatni chiqarish\n3-yili bo'yicha tartiblash\n4-narhi bo'yicha tartiblash\nq-quit")
    cmd = input()
    if cmd == "1":
        korxona = input("Korxonani kiriting:")
        rangi = input("Rangini kiriting:")
        yili = input("yilini kiriting:")
        karobkasi = input("Karobkasini kiriting:")
        narhi = input("Narhini kiriting")
        rusumi = input("Mashina rusumini kiriting:")
        avto = Car(korxona,rangi,yili,karobkasi,narhi,rusumi)
        avtolist.append(avto)
    elif cmd == "2":
        print("____________MASHINA RO'YXATI_________")
        for avto in avtolist:
            print(avto)
        print("_____________________________________")
    elif cmd == "3":
        sortedList = avtolist
        sortedList.sort(key=lambda x:x.yili)
        for i in sortedList:
            print(i)

    elif cmd == "4":
        sortedList = avtolist
        sortedList.sort(key=lambda x:x.narhi)
        for i in sortedList:
            print(i)
    elif cmd == "q":
        break
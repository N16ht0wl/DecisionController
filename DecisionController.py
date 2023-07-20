import random
import time
movieList = ["Olağan Şüpheliler","Tanrılar Çıldırmış Olmalı 1,2,3", "Matrix 1,2,3", "Diktatör","Kuzuların Sessizliği","İnception","Bir Zamanlar Anadoluda","The Man From Earth","Otomatik Portakal","Tanrı Kent","Paramparça Aşklar ve Köpekler","Guguk Kuşu","Identity","Apocalypto","Sophie's Choice","Akıl Oyunları","American History X","25.Saat","Pulp Fiction","Kill Bill","Devlet Düşmanı","Hacivat Karagöz Niçin Öldürüldü","Entel Köy Efe Köye Karşı","1900","Dövüş Kulübü","Equilibrium","Azınlık Raporu","Memento","Kelebek Etkisi","21 Gram","Saatler","Ölü OzanlarDerneği","Uçurtmayı Vurmasınlar","2001:Uzay Macerası","Buz Devri","Sakıncalı Düşünceler","Rıhtımlar Üzerinde","Bülbülü Öldürmek","Esaretin Bedeli","Forrest Gump","The Tree of Life","My Sister's Keeper","V for Vendetta","Black Swan","The Others","Lucy","Contact","Uçurtma Avcıları","İbn-i Sina Hekim","Snowden"]
watchedMovie =[]
documentaryList = ["Cosmos","Mankind"]
watchedDocumentary =[]
bookList = ["Gılgameş Destanı","Akdeniz Mitologyasından Efsaneler","101 Felsefe Problemi","Tanrı Yanılgısı","İbrahim Peygamber","Antigone","Sapiens","İnsan Olmak","Vicdan Zorbalığa Karşı","Mantık Al-Tayr","Mukaddime","Felsefenin Evrimi","Bilim ve Şarlatanlık","Aşkın Metafiziği","Böyle Buyrdu Zerdüşt","Tüfek Mikrop ve Çelik","Devlet","Ütopya","Sofi'nin Dünyası","Cesur Yeni Dünya","İlahi Komedya","Siyasal Düşünceler Tarihi","Gülün Adı","Çavdar Tarlasında Çocuklar","Sahip Olmak ya da Olmak","Doğu'dan Uzakta","Doğu'nun Limanları","Alamut","İnsanın Anlam Arayışı","Özgürlükten Kaçış","Küçük Prens","Politik Psikiyatri","İnsanı Anlamak","İttihat ve Terakki","Aylak Adam","Sorgulayan Denemeler","Moby Dick","Hikayeler","Doğmamış Çocuğa Mektup","1984","Puslu Kıtalar Atlası","Sefiller","Martı","Genç Werther'in Acıları","Gülünesi Aşklar","Yabancı","Dava","Bütün Öyküler","Suç ve Ceza","Nietzche Ağladığında","Saatleri Ayarlama Enstitüsü","Söz ve Yazı","Öyküler","Sineklerin Tanrısı","Fareler ve İnsanlar","Bir Bİlim Adamının Romanı","Ana","Ölü Zaman Gezginleri","Alçaklığın Evrensel Tarihi","Tol","Cinayet Sanatı","Kızıla Boyalı Saçlar","Hamlet","Mülksüzler","Yüzyıllık Yalnızlık","Kara Kitap","Tutunamayanlar","Ses ve Öfke","Kabil","Cenk Hikayeleri","Ölümle Yüzleşmek"]
readBooks =[]
seiesList =["How I Met Your Mother"]
watchedSeries = []
yesChoices = ["yes","y"]
noChoices = ["no","n"]
print("===== Listenizdeki Seçenekler =====")
print("1)Film", "2)Belgesel", "3)Kitaplar", "4)Diziler", "5)Filmlere Ekleme Yapmak için Tercih edin", "6)Belgesellere Ekleme Yapmak için Tercih edin", "7)Kitaplara Ekleme Yapmak için Tercih edin", "8)Dizilere Ekleme Yapmak için Tercih edin", sep="\n")

while True:
    picker = input("Yapmak İstediğiniz Seçeneği Seçin:")
    if (picker == "1"):
        movie= random.choice(movieList)
        print("Seçilen Film........!")
        print(movie)
        time.sleep(2)
        watched = input("Bu Filmi izlediniz mi ?")
        if watched.lower() in yesChoices:
            watchedMovie.append(movie)
            movieList.remove(movie)
            print(watchedMovie)

        elif watched.lower() in noChoices:
            print(watchedMovie)

        else:
            print("Lütfen y/n yazın!")

        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")

    elif (picker=="2"):
        documentary = random.choice(documentaryList)
        print("Seçilen Belgesel........!")
        print(documentary)
        time.sleep(2)
        wDocumentary = input("Bu Belgeseli izlediniz mi ?")
        if wDocumentary.lower() in yesChoices:
            watchedDocumentary.append(documentary)
            documentaryList.remove(documentary)

        elif wDocumentary.lower() in noChoices:
            print(watchedDocumentary)
        else:
            print("Lütfen y/n yazın!")
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")

    elif (picker=="3"):
        books = random.choice(bookList)
        print("Seçilen Kitap........!")
        print(books)
        time.sleep(2)
        rBooks = input("Bu Kitabı Okudunuz mu ?")
        if rBooks.lower() in yesChoices:
            readBooks.append(books)
            bookList.remove(books)
        elif rBooks.lower() in noChoices:
            print(readBooks)

        else:
            print("Lütfen y/n yazın!")

        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")

    elif(picker=="4"):
        series = random.choice(seiesList)
        print("Seçilen Dizi........!")
        print(series)
        time.sleep(2)
        wSeries = input("Bu Diziyi izlediniz mi ?")
        if wSeries.lower() in yesChoices:
            watchedSeries.append(series)
            seiesList.remove(series)
        elif wSeries.lower() in noChoices:
            print(watchedSeries)
        else:
            print("lütfen y/n Yazın!")
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")
    elif (picker=="5"):
        yeniFilm=input("Eklemek İstediğiniz Filmin Adını Giriniz: ")
        movieList.append(yeniFilm)
        print(movieList)
        time.sleep(2)
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")
    elif(picker=="6"):
        yeniBelgesel=input("Eklemek İstediğiniz Belgeselin Adını Giriniz: ")
        documentaryList.append(yeniBelgesel)
        print(documentaryList)
        time.sleep(2)
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")
    elif(picker=="7"):
        yeniKitap=input("Eklemek İstediğiniz Kitabın Adını Giriniz: ")
        bookList.append(yeniKitap)
        time.sleep(2)
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")
    elif(picker=="8"):
        yeniDizi=input("Eklemek İstediğiniz Dizinin Adını Giriniz: ")
        seiesList.append(yeniDizi)
        print(seiesList)
        time.sleep(2)
        userInput = input("Yeni bir seçenek seçmek istiyor musunuz ? yes/no:")
        if userInput.lower() in yesChoices:
            print("user typed yes")
            continue
        elif userInput.lower() in noChoices:
            print("user typed no")
            time.sleep(2)
            break
        else:
            print("Lütfen y/n yazın!")

    else:
        print("Lütfen Yukarıdaki Seçeneklerden Birini Yazın!!")

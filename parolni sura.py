#ewmat = gumro kompyuter
#odam = programmani iwlatkon odam


#to'gri parolni oldindan aytib qoyish ewmatga
tugri_parol = "shakalakabum"

#urinishlar sonini aytish kerak gumro compga
urinish_soni = 0

#ewmatga aytib qoyish kerak toki notugri deb aytmagancha iwlaver 
iwlaver = True

#enni boshlash kerak
while (iwlaver): #iwlavergan paytda
    urinish_soni = urinish_soni + 1 #birinchi urinish bugani uchun, ewmat bitta quwib qoyadi urinishlar soni
    print("Agar  3tadan ziyod xato qilsang, surasan berdan") #tushintirish
    print(urinish_soni, "- urinish") #ewmat aytsin nechinchi urinish ekanligini 
    taxmin = input("parolni ter: ") #parolni surasin va taxmin deb nomlasin suraganini

    if taxmin == tugri_parol: #agar taxmin tugri parolga teng busa
        print("ahaa, topding!") #aha topding deb aytsin
        iwlaver = False #programma iwlaverishi noguri busin endi
    elif urinish_soni >=3: #yoki agar urinishlar soni 3dan utib ketsa
        print("ee ewmat topolmadingku, sur endi berdan") #bullie bezor bullim desin
        iwlaver = False #programma iwlaverishi notugri busin

        
    

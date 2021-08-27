from url_lib_7 import iphone_vcard
from url_lib import phone_book_name, phone_book_contacts, clinic_name


"""
Program do phone book for persons in each clinic separatly

"""

all_clinic = ['Sindikati', 'Strateško upravljanje in poslovno administrativne storitve', 'Diagnostične enote',
               'Uprava', 'Poliklinika', 'Samostojne klinike in klinični inštituti', 'Dejavnosti skupnega pomena',
               'Stomatološka klinika', 'Interna klinika', 'Pediatrična klinika', 'SPUKC - Sindikat zdravstva Slovenije',
               'Negovalni oddelek UKC Ljubljana', 'Nevrološka klinika', 'Ostale pomembne številke', 'Kirurška klinika',
               'Ginekološka klinika']


def through_all(iphone_vcard, clinic, phone_book_name, clinic_name):
    url = "http://tikc2.intranet.kclj.si/search/level/0"  # 81 ne dela
    file_name = clinic_name + ".vcf" #dodam pravo končnico
    for end_with in range(214):  # dela vse
        if end_with == 2:  # zato ker 3 ne dela
            url = "http://tikc2.intranet.kclj.si/search/level/3"  # izreže vn trojko ker dela same probleme
            pass
        else:
            print(url)
            url = url.replace(str(end_with), str(end_with + 1))
            print(str(end_with + 1))
            print(clinic(url))
            if clinic(url) == clinic_name:  # narediš for zanko da greš čez vse klinike; potrebno uslkaditi da je ime datoteke ime klinike; how to?
                iphone_vcard(url, file_name, phone_book_name)





for ime in all_clinic:
    through_all(iphone_vcard, clinic_name, phone_book_name, ime)


from vcf_format_maker import iphone_vcard
from scraper import phone_book_name, clinic_name


"""
Program do .vcf file for each clinic separatly

"""

all_clinic = ['Sindikati', 'Strateško upravljanje in poslovno administrativne storitve', 'Diagnostične enote',
               'Uprava', 'Poliklinika', 'Samostojne klinike in klinični inštituti', 'Dejavnosti skupnega pomena',
               'Stomatološka klinika', 'Interna klinika', 'Pediatrična klinika', 'SPUKC - Sindikat zdravstva Slovenije',
               'Negovalni oddelek UKC Ljubljana', 'Nevrološka klinika', 'Ostale pomembne številke', 'Kirurška klinika',
               'Ginekološka klinika']


def through_all(iphone_vcard, clinic, phone_book_name, clinic_name):
    url = "http://tikc2.intranet.kclj.si/search/level/0"
    file_name = clinic_name + ".vcf"
    for end_with in range(214):
        if end_with == 2:  # page no. 3 do not work
            url = "http://tikc2.intranet.kclj.si/search/level/3"
            pass
        else:
            print(url)
            url = url.replace(str(end_with), str(end_with + 1))
            print(str(end_with + 1))
            print(clinic(url))
            if clinic(url) == clinic_name:
                iphone_vcard(url, file_name, phone_book_name)







def main():
    for clinic in all_clinic:
        through_all(iphone_vcard, clinic_name, phone_book_name, clinic)


if __name__ == '__main__':
    main()


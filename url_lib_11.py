from url_lib_7 import iphone_vcard
from url_lib import phone_book_name, phone_book_contacts, clinic_name

# potrebno dati program v funkcijo da bo vleku določeno kliniko čez cel program
vse_klinike = ['Sindikati', 'Strateško upravljanje in poslovno administrativne storitve', 'Diagnostične enote',
               'Uprava', 'Poliklinika', 'Samostojne klinike in klinični inštituti', 'Dejavnosti skupnega pomena',
               'Stomatološka klinika', 'Interna klinika', 'Pediatrična klinika', 'SPUKC - Sindikat zdravstva Slovenije',
               'Negovalni oddelek UKC Ljubljana', 'Nevrološka klinika', 'Ostale pomembne številke', 'Kirurška klinika',
               'Ginekološka klinika']


# naredi eno funkcijo ki ge šeč vse strani potem pa naredi še eno funkcijo ki gre čez vse klinike

# ime_datoteke = "UKC_samo_Interna_01" #DODAJ .vcf
#napiši še ime klinike pri kateri preverjaš (v spodnjem primeru pediatrična klinika)

def cez_vse_strani(iphone_vcard, klinika, ime_imenika,ime):
    url = "http://tikc2.intranet.kclj.si/search/level/0"  # 81 ne dela
    ime_datoteke = ime + ".vcf" #dodam pravo končnico
    for koncnica in range(214):  # dela vse
        if koncnica == 2:  # zato ker 3 ne dela
            url = "http://tikc2.intranet.kclj.si/search/level/3"  # izreže vn trojko ker dela same probleme
            pass
        else:
            print(url)
            url = url.replace(str(koncnica), str(koncnica + 1))
            print(str(koncnica + 1))
            print(klinika(url))
            if klinika(url) == ime:  # narediš for zanko da greš čez vse klinike; potrebno uslkaditi da je ime datoteke ime klinike; how to?
                iphone_vcard(url, ime_datoteke, ime_imenika)

# for ime in vse_klinike:
#     ime = ime_datoteke
#     cez_vse_strani(url, iphone_vcard, klinika, ime_imenika, ime_datoteke, ime)




# napiši še opcijo da če gre šez vse da ti naredi po klinikah... Iz pediatrična klinika in gre samo čez tiste strani kjer je pek!
# potrebno dodati * if ime_imenika[:2] == "Pediatrična klinika" * (da izpiše samo tiste)
# naredi tako da za vsako kliniko naredi svoj imenik! ker je obstoječi prevelik ne morem ga uvoziti;
# naredi tako da nardi nov file z določenim imenom klinike... Najprej naredi za določeno kliniko.
# rad bi izdelal program ki bi naredil toliko filov kolikor je klinik

# potrebno dati program v funkcijo da bo vleku določeno kliniko čez cel program


for ime in vse_klinike:
    cez_vse_strani(iphone_vcard, clinic_name, phone_book_name, ime)


import urllib.request


def phone_book_scrape(url):
    socket = urllib.request.urlopen(url)
    phone_book_contacts = {}
    name_surname = ""
    phone_book_name = ""
    for line in socket:
        line = line.decode("utf-8")


        if line.startswith("        <span class='pn'>"):
            podatki = line.split(">")
            name_surname = podatki[1]
            name_surname = name_surname.split("<")[:-1]
            name_surname = "".join(name_surname)



        if line.startswith("     <td class='e'>"):
            opis = line.split("<")[1]
            opis = opis.replace("td class='e'>", " ")




        if line.startswith('    <div class="title">Imenik: '):
            phone_book_name = line.split(">")[1]
            phone_book_name = phone_book_name.replace("Imenik: ", "")
            phone_book_name = phone_book_name.replace("</div", "")


        if line.startswith("     <td class='n'>"):
            tel = line.split(">")[1]
            tel = tel.split("<")[:-1]
            tel = "".join(tel).replace("&nbsp;", " ")
            tel = tel.replace("int: ","")
            tel = tel.replace(" int: ","")
            tel = tel.replace("fax: ", "")
            tel = tel.replace("dect: ", "")
            tel = tel.replace("gsm: ", "")
            tel = tel.replace("multiton: ", "")
            tel = tel.replace("zunanja: ", "")
            tel = tel.split(",")
            if name_surname == opis:
                opis = ""



            phone_book_contacts[name_surname + opis] = tel
            name_surname = ""


    return phone_book_name, phone_book_contacts

def phone_book_name(url):
    return phone_book_scrape(url)[0]
def phone_book_contacts(url):
    return phone_book_scrape(url)[1]
def clinic_name(url):
    return phone_book_name(url).split("/")[0].strip() #samo klinko vrne brez končnega presledka

def department(url):
    return phone_book_name(url).split("/")[1].strip() #samo klinko vrne brez končnega presledka


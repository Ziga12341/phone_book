from scraper import phone_book_contacts


"""
Transfer data from dict format to iphone conntact import form which is  than used in .vcf

"""


def iphone_vcard(url, file_name, phone_book_name):
    file = open(file_name, "a", encoding="UTF-8")
    phone_book_name = phone_book_name(url)
    contacts = phone_book_contacts(url)
    for name,tel in contacts.items():
        if len(tel) == 1:
            tel1 = tel[0]
            if tel1:
                if tel1[0] == "0" or tel1[0] == "" or tel1[:2] == " 0":
                    pass
                else:
                    tel1 = str("01 522 ") + tel1
            file.write(
                f"BEGIN:VCARD\nVERSION:3.0\nN:{name };\nFN:{name };\nORG:{ phone_book_name};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{tel1}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2020B67//EN\nREV:2020-11-10T01:12:09Z\nEND:VCARD\n")
        if len(tel) == 2:
            tel1 = tel[0]
            if tel1:
                if tel1[0] == "0" or tel1[0] == "" or tel1[:2] == " 0":
                    pass
                else:
                    tel1 = str("01 522 ") + tel1
            tel2 = tel[1]
            if tel2:
                if tel2[0] == "0" or tel2[0] == "" or tel2[:2] == " 0":
                    pass
                else:
                    tel2 = str("01 522 ") + tel2
            file.write(
                f"BEGIN:VCARD\nVERSION:3.0\nN:{name};\nFN:{name};\nORG:{ phone_book_name};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{tel2}\nTEL;TYPE=HOME;TYPE=CELL;TYPE=VOICE:{tel1}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2020B67//EN\nREV:2020-11-10T01:12:09Z\nEND:VCARD\n")
        if len(tel) == 3:
            tel1 = tel[0]
            if tel1:
                if tel1[0] == "0" or tel1[0] == "" or tel1[:2] == " 0":
                    pass
                else:
                    tel1 = str("01 522 ") + tel1
            tel2 = tel[1]
            if tel2:
                if tel2[0] == "0" or tel2[0] == "" or tel2[:2] == " 0":
                    pass
                else:
                    tel2 = str("01 522 ") + tel2
            tel3 = tel[2]
            if tel3:
                if tel3[0] == "0" or tel3[0] == "" or tel3[:2] == " 0":
                    pass
                else:
                    tel3 = str("01 522 ") + tel3
            file.write(
                f"BEGIN:VCARD\nVERSION:3.0\nN:{name};\nFN:{name};\nORG:{ phone_book_name};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{tel2}\nTEL;TYPE=HOME;TYPE=CELL;TYPE=VOICE:{tel3}\nTEL;TYPE=WORK;TYPE=CELL;TYPE=VOICE:{tel1}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2020B67//EN\nREV:2020-11-10T01:12:09Z\nEND:VCARD\n")
        if len(tel) == 4:
            tel1 = tel[0]
            if tel1:
                if tel1[0] == "0" or tel1[0] == "" or tel1[:2] == " 0":
                    pass
                else:
                    tel1 = str("01 522 ") + tel1
            tel2 = tel[1]
            if tel2:
                if tel2[0] == "0" or tel2[0] == "" or tel2[:2] == " 0":
                    pass
                else:
                    tel2 = str("01 522 ") + tel2
            tel3 = tel[2]
            if tel3:
                if tel3[0] == "0" or tel3[0] == "" or tel3[:2] == " 0":
                    pass
                else:
                    tel3 = str("01 522 ") + tel3
            tel4 = tel[3]
            if tel4:
                if tel4[0] == "0" or tel4[0] == "" or tel4[:2] == " 0":
                    pass
                else:
                    tel4 = str("01 522 ") + tel4
            file.write(
                f"BEGIN:VCARD\nVERSION:3.0\nN:{name};\nFN:{name};\nORG:{ phone_book_name};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{tel2}\nTEL;TYPE=HOME;TYPE=CELL;TYPE=VOICE:{tel3}\nTEL;TYPE=WORK;TYPE=CELL;TYPE=VOICE:{tel4}\nTEL;TYPE=IPHONE;TYPE=CELL;TYPE=VOICE:{tel1}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2020B67//EN\nREV:2020-11-10T01:12:09Z\nEND:VCARD\n")
        if len(tel) == 5:
            tel1 = tel[0]
            if tel1:
                if tel1[0] == "0" or tel1[0] == "" or tel1[:2] == " 0":
                    pass
                else:
                    tel1 = str("01 522 ") + tel1
            tel2 = tel[1]
            if tel2:
                if tel2[0] == "0" or tel2[0] == "" or tel2[:2] == " 0":
                    pass
                else:
                    tel2 = str("01 522 ") + tel2
            tel3 = tel[2]
            if tel3:
                if tel3[0] == "0" or tel3[0] == "" or tel3[:2] == " 0":
                    pass
                else:
                    tel3 = str("01 522 ") + tel3
            tel4 = tel[3]
            if tel4:
                if tel4[0] == "0" or tel4[0] == "" or tel4[:2] == " 0":
                    pass
                else:
                    tel4 = str("01 522 ") + tel4
            tel5 = tel[4]
            if tel5:
                if tel5[0] == "0" or tel5[0] == "" or tel5[:2] == " 0":
                    pass
                else:
                    tel5 = str("01 522 ") + tel5
            file.write(
                f"BEGIN:VCARD\nVERSION:3.0\nN:{name};\nFN:{name};\nORG:{ phone_book_name};\nTEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:{tel2}\nTEL;TYPE=HOME;TYPE=CELL;TYPE=VOICE:{tel3}\nTEL;TYPE=WORK;TYPE=CELL;TYPE=VOICE:{tel4}\nTEL;TYPE=IPHONE;TYPE=CELL;TYPE=VOICE:{tel5}\nTEL;TYPE=MAIN;TYPE=CELL;TYPE=VOICE:{tel1}\nPRODID:-//Apple Inc.//iCloud Web Address Book 2020B67//EN\nREV:2020-11-10T01:12:09Z\nEND:VCARD\n")
    file.close()


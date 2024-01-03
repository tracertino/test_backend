import re

def sum_array(num):
    return sum(list(map(lambda x: int(x), re.findall("\d", str(num)))))

json = {"а": 1,"б" :2,"в": 3,"г": 4,"д": 5,"е" :6,"ё" :6,"ж" :7,"з" :8,"и": 9,"й" :1,"к": 2,"л": 3,
"м" :4,"н" :5,"о": 6,"п" :7,"р": 8,"с": 9,"т": 1,"у": 2,"ф": 3,"х" :4,"ц" :5,"ч" :6,"ш" :7,"щ" :8,
"ъ" :9,"ы" :1,"ь" :2,"э" :3,"ю" :4,"я" :5 }

json_gl = {"а": 1,"е" :6,"ё" :6,"и": 9,"о": 6,"у": 2,"ы" :1,"э" :3,"ю" :4,"я" :5 }

json_sogl = {"б" :2,"в": 3,"г": 4,"д": 5,"ж" :7,"з" :8,"й" :1,"к": 2,"л": 3,
"м" :4,"н" :5,"п" :7,"р": 8,"с": 9,"т": 1,"ф": 3,"х" :4,"ц" :5,"ч" :6,"ш" :7,"щ" :8,
"ъ" :9,"ь" :2}


def raschet_tlk_fio(fio, mission):
    result = re.findall(r"\w", fio.lower())
    fiasko = sum(list(map(lambda x: json.get(x), result)))
    while fiasko > 9:
        fiasko = sum_array(fiasko)

    missiya = fiasko*2
    while missiya > 9:
        missiya = sum_array(missiya)
    
    if mission == missiya:

        vibor_palach = sum(list(map(lambda x: json_gl.get(x, 0), result)))
        while vibor_palach > 9:
            vibor_palach = sum_array(vibor_palach)

        sut = sum(list(map(lambda x: json_sogl.get(x, 0), result)))
        while sut > 9:
            sut = sum_array(sut)

        if (missiya - sut) <= 0:
            vibor_zadacha = (missiya - sut) + 9
        else:
            vibor_zadacha = missiya - sut

        if vibor_zadacha%2 != 0:
            stremlenie = (vibor_zadacha+9)//2
        else:
            stremlenie = vibor_zadacha//2

        argument = sum_array(vibor_palach*2)
        while argument > 9:
            argument = sum_array(argument)

        antioblik = len(result)
        while antioblik > 9:
            antioblik = sum_array(antioblik)

        oblik = antioblik*2
        while oblik > 9:
            oblik = sum_array(oblik)
        
        return [missiya, vibor_zadacha, oblik]
    
    return False


def raschet(fio, date_rogd):

    result = re.findall(r"\w", fio.lower())
    fiasko = sum(list(map(lambda x: json.get(x), result)))
    while fiasko > 9:
        fiasko = sum_array(fiasko)

    missiya = fiasko*2
    while missiya > 9:
        missiya = sum_array(missiya)

    vibor_palach = sum(list(map(lambda x: json_gl.get(x, 0), result)))
    while vibor_palach > 9:
        vibor_palach = sum_array(vibor_palach)

    sut = sum(list(map(lambda x: json_sogl.get(x, 0), result)))
    while sut > 9:
        sut = sum_array(sut)

    if (missiya - sut) <= 0:
        vibor_zadacha = (missiya - sut) + 9
    else:
        vibor_zadacha = missiya - sut

    if vibor_zadacha%2 != 0:
        stremlenie = (vibor_zadacha+9)//2
    else:
        stremlenie = vibor_zadacha//2

    argument = sum_array(vibor_palach*2)
    while argument > 9:
        argument = sum_array(argument)

    antioblik = len(result)
    while antioblik > 9:
        antioblik = sum_array(antioblik)

    oblik = antioblik*2
    while oblik > 9:
        oblik = sum_array(oblik)


    result_date = re.findall(r"\d", date_rogd)

    resurs = sum_array(result_date)
    while resurs > 9:
        resurs = sum_array(resurs)

    bremya = resurs*2
    while bremya > 9:
        bremya = sum_array(bremya)

    vibor_energiya = resurs - sut
    if vibor_energiya <= 0:
        vibor_energiya = vibor_energiya + 9

    vibor_poterya = bremya - sut
    if vibor_poterya <= 0:
        vibor_poterya = vibor_poterya + 9

    antitelo = sut - resurs
    if antitelo <= 0:
        antitelo = antitelo + 9

    telo = antitelo * 2
    while telo > 9:
        telo = sum_array(telo)

    if sut%2 != 0:
        rutina = (sut+9)//2
    else:
        rutina = sut // 2

    smisl = fiasko + resurs
    while smisl > 9:
        smisl = sum_array(smisl)

    nevihod = vibor_zadacha * 2
    while nevihod > 9:
        nevihod = sum_array(nevihod)

    komfort = sut + nevihod
    while komfort > 9:
        komfort = sum_array(komfort)

    nepodarok = komfort * 2
    while nepodarok > 9:
        nepodarok = sum_array(nepodarok)

    zapas = nepodarok - sut
    if zapas <= 0:
        zapas = zapas + 9

    if vibor_palach%2 == 0:
        nevrag = vibor_palach // 2
    else:
        nevrag = (vibor_palach + 9) // 2

    kozir = sut + nevrag
    while kozir > 9:    
        kozir = sum_array(kozir)

    if kozir%2 == 0:
        oshibka = kozir // 2
    else:
        oshibka = (kozir + 9) // 2

    predatel = oshibka - sut
    if predatel <= 0:
        predatel = predatel + 9

    if antioblik%2 == 0:
        fars = antioblik // 2
    else:
        fars = (antioblik + 9) // 2

    antiyadro = stremlenie - sut
    if antiyadro <= 0:
        antiyadro = antiyadro + 9

    yadro = antiyadro * 2
    while yadro > 9:
        yadro = sum_array(yadro)

    antigrezi = sut + stremlenie
    while antigrezi > 9:
        antigrezi = sum_array(antigrezi)

    grezi = antigrezi * 2
    while grezi > 9:
        grezi = sum_array(grezi)

    result_json = {"1": fiasko,
                "2": missiya,
                "3": vibor_palach,
                "4": sut, 
                "5": vibor_zadacha, 
                "6": stremlenie,
                "7": argument,
                "8": antioblik,
                "9": oblik,
                "10": resurs,
                "11": bremya,
                "12": vibor_energiya, 
                "13": vibor_poterya,
                "14": antitelo,
                "15": telo,
                "16": rutina,
                "17": smisl, 
                "18": nevihod,
                "19": komfort,
                "20": nepodarok,
                "21": zapas,
                "22": nevrag,
                "23": kozir,
                "24": oshibka,
                "25": predatel,
                "26": fars,
                "27": antiyadro,
                "28": yadro,
                "29": antigrezi,
                "30": grezi}
    return result_json
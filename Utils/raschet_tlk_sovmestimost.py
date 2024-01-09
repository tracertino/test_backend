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

    telo_talant = antitelo * 2
    while telo_talant > 9:
        telo_talant = sum_array(telo_talant)

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
  #New calc      
    argument_n = vibor_energiya * 2
    while argument_n > 9:
        argument_n = sum_array(argument_n)
        
    if vibor_poterya % 2 == 0:
        stremlenie_n = vibor_poterya // 2
    else:
        stremlenie_n = (vibor_poterya + 9) // 2 
    
    nevihod_n = vibor_poterya * 2
    while nevihod_n > 9:
        nevihod_n = sum_array(nevihod_n)
        
    komfort_n = sut + nevihod_n
    while komfort_n > 9:
        komfort_n = sum_array(komfort_n)
        
    nepodarok_n = komfort_n * 2
    while nepodarok_n > 9:
        nepodarok_n = sum_array(nepodarok_n)
        
    zapas_n = nepodarok_n - sut
    if zapas_n <= 0:
        zapas_n += 9    
    
    if vibor_energiya % 2 == 0:
        nevrag_n = vibor_energiya // 2
    else:
        nevrag_n = (vibor_energiya + 9) // 2
        
    kozir_n = sut + nevrag_n
    while kozir_n > 9:
        kozir_n = sum_array(kozir_n)
        
    if kozir_n%2 == 0:    
        oshibka_n = kozir_n // 2
    else:
        oshibka_n = (kozir_n + 9) // 2
        
    predatel_n = oshibka_n - sut
    if predatel_n <= 0:
        predatel_n += 9
        
    uchitel = missiya * 2
    while uchitel > 9:
        uchitel = sum_array(uchitel)
    
    if resurs%2 == 0:
        muchitel = resurs // 2
    else:
        muchitel = (resurs + 9) // 2
        
    nuzhda = telo_talant * 2
    while nuzhda > 9:
        nuzhda = sum_array(nuzhda)

    result_json = [{"name": "fiasko",           "name_rus":"Фиаско",            "value": fiasko},
                    {"name": "missiya",         "name_rus":"Миссия",            "value": missiya},
                    {"name": "vibor_palach",    "name_rus":"Выбор (Палач)",     "value": vibor_palach},
                    {"name": "sut",             "name_rus":"Суть",              "value": sut}, 
                    {"name": "vibor_zadacha",   "name_rus":"Выбор (Задача)",    "value": vibor_zadacha}, 
                    {"name": "stremlenie",      "name_rus":"Стремление",        "value": stremlenie},
                    {"name": "argument",        "name_rus":"Аргумент",          "value": argument},
                    {"name": "antioblik",       "name_rus":"АнтиОблик",         "value": antioblik},
                    {"name": "oblik",           "name_rus":"Облик",             "value": oblik},
                    {"name": "resurs",          "name_rus":"Ресурс",            "value": resurs},
                    {"name": "bremya",          "name_rus":"Бремя",             "value": bremya},
                    {"name": "vibor_energiya",  "name_rus":"Выбор (Энергия)",   "value": vibor_energiya}, 
                    {"name": "vibor_poterya",   "name_rus":"Выбор (Потеря)",    "value": vibor_poterya},
                    {"name": "antitelo",        "name_rus":"АнтиТело",          "value": antitelo},
                    {"name": "telo_talant",     "name_rus":"Тело (Талант)",     "value": telo_talant},
                    {"name": "rutina",          "name_rus":"Рутина",            "value": rutina},
                    {"name": "smisl",           "name_rus":"Смысл",             "value": smisl}, 
                    {"name": "nevihod",         "name_rus":"НеВыход",           "value": nevihod},
                    {"name": "komfort",         "name_rus":"Комфорт",           "value": komfort},
                    {"name": "nepodarok",       "name_rus":"НеПодарок",         "value": nepodarok},
                    {"name": "zapas",           "name_rus":"Запас",             "value": zapas},
                    {"name": "nevrag",          "name_rus":"НеВраг",            "value": nevrag},
                    {"name": "kozir",           "name_rus":"Козырь",            "value": kozir},
                    {"name": "oshibka",         "name_rus":"Ошибка",            "value": oshibka},
                    {"name": "predatel",        "name_rus":"Предатель",         "value": predatel},
                    {"name": "fars",            "name_rus":"Фарс",              "value": fars},
                    {"name": "antiyadro",       "name_rus":"АнтиЯдро",          "value": antiyadro},
                    {"name": "yadro",           "name_rus":"Ядро",              "value": yadro},
                    {"name": "antigrezi",       "name_rus":"Антигрезы",         "value": antigrezi},
                    {"name": "fiasko",          "name_rus":"Грезы",             "value": grezi}]
    return result_json
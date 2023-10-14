from django.core.management.base import BaseCommand, CommandError
from bank.models import City, Department
from django.contrib.gis.geos import *
data = [
        {
            "id": 29000256,
            "Biskvit_id": "1203",
            "shortName": "ДО «На Краснознаменской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Щелково, ул. Краснознаменская, д. 6",
            "city": "Щелково",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.915437,
                "longitude": 37.996599
            }
        },
        {
            "id": 26000066,
            "Biskvit_id": "2436",
            "shortName": "ДО № 53 «Лесной, 63» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Лесной пр-т, д. 63, лит. А, комн. №№ 80-93, 96-120, 24-32, 36-49",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.98553,
                "longitude": 30.342431
            }
        },
        {
            "id": 26000077,
            "Biskvit_id": "4536",
            "shortName": "ДО № 62 «Чкаловский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Чкаловский пр-т, д. 15, лит. Г",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.962588,
                "longitude": 30.294192
            }
        },
        {
            "id": 21014005,
            "Biskvit_id": "5492",
            "shortName": "ОО в г. Костроме Филиала в г. Воронеже",
            "address": "Костромская область, г. Кострома, ул. Советская, д. 49",
            "city": "Кострома",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.763626,
                "longitude": 40.942049
            }
        },
        {
            "id": 17000002,
            "Biskvit_id": "5128",
            "shortName": "ДО «Воронцовский» Филиала в г. Москве",
            "address": "г. Москва, ул. Воронцовская, д. 43, стр. 1",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.733057,
                "longitude": 37.66495
            }
        },
        {
            "id": 26000015,
            "Biskvit_id": "0626",
            "shortName": "ДО № 23 «Московский, 220» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Московский пр., д. 220, лит. А, часть пом. 6-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.847982,
                "longitude": 30.322417
            }
        },
        {
            "id": 27007036,
            "Biskvit_id": "0656",
            "shortName": "ДО «Московская» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Московская, д. 7",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.48862,
                "longitude": 135.078331
            }
        },
        {
            "id": 21011141,
            "Biskvit_id": "6251",
            "shortName": "ОО «Канищево» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, ул. Интернациональная, д. 18",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.666775,
                "longitude": 39.665354
            }
        },
        {
            "id": 29000199,
            "Biskvit_id": "1303",
            "shortName": "ДО «Дедовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Истринский р-н, г. Дедовск, ул. Гагарина, д. 9",
            "city": "Дедовск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.859766,
                "longitude": 37.121325
            }
        },
        {
            "id": 29000296,
            "Biskvit_id": "0925",
            "shortName": "ДО «Авиамоторный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Авиамоторная, д. 10, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.754259,
                "longitude": 37.715246
            }
        },
        {
            "id": 22004005,
            "Biskvit_id": "5715",
            "shortName": "ДО «Салехардский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Салехард, ул. Матросова, д. 36б",
            "city": "Салехард",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.537135,
                "longitude": 66.628566
            }
        },
        {
            "id": 29000211,
            "Biskvit_id": "4610",
            "shortName": "ДО «Рязанский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Рязанский пр-т, д. 71, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.718633,
                "longitude": 37.78827
            }
        },
        {
            "id": 41000021,
            "Biskvit_id": "0690",
            "shortName": "Дополнительный офис «Красногвардейский» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Российская Федерация, г. Санкт-Петербург, Малоохтинский пр., д. 53, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.932383,
                "longitude": 30.401388
            }
        },
        {
            "id": 21014001,
            "Biskvit_id": "2651",
            "shortName": "ОО «Центральный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Костромская область, г. Кострома, ул. Советская, д. 79/73",
            "city": "Кострома",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.761221,
                "longitude": 40.953313
            }
        },
        {
            "id": 21008672,
            "Biskvit_id": "3816",
            "shortName": "ОО «Белый город» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, пр-т Белгородский, д. 54",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 50.602018,
                "longitude": 36.595927
            }
        },
        {
            "id": 27006004,
            "Biskvit_id": "2356",
            "shortName": "ОО «Петропавловский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Камчатский край, г. Петропавловск-Камчатский, ул. Ленинская, д. 59",
            "city": "Петропавловск-Камчатский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.018647,
                "longitude": 158.646989
            }
        },
        {
            "id": 27001002,
            "Biskvit_id": "2156",
            "shortName": "ОО «Театральный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Сахалинская область, г. Южно-Сахалинск, ул. Дзержинского, д. 36",
            "city": "Южно-Сахалинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.956602,
                "longitude": 142.738068
            }
        },
        {
            "id": 26000044,
            "Biskvit_id": "1706",
            "shortName": "ДО № 17 «Лиговский, 116» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр. Лиговский, д. 114, лит.В, д. 116-118, Лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.918647,
                "longitude": 30.353409
            }
        },
        {
            "id": 24010004,
            "Biskvit_id": "2024",
            "shortName": "ДО «Площадь Калинина» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Дуси Ковальчук, д. 179/5",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.060957,
                "longitude": 82.915121
            }
        },
        {
            "id": 21015004,
            "Biskvit_id": "1921",
            "shortName": "ОО «Советский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Орловская область, г. Орел, ул. Максима Горького, д. 47",
            "city": "Орел",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.978087,
                "longitude": 36.072838
            }
        },
        {
            "id": 21012000,
            "Biskvit_id": "1351",
            "shortName": "РОО «Тверской»",
            "address": "Тверская область, г. Тверь, ул. Новоторжская, д.12А",
            "city": "Тверь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.858302,
                "longitude": 35.909857
            }
        },
        {
            "id": 22005011,
            "Biskvit_id": "4615",
            "shortName": "ОО «Сибирский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, пр-т Мира, д. 1",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 61.262497,
                "longitude": 73.378668
            }
        },
        {
            "id": 24001006,
            "Biskvit_id": "1124",
            "shortName": "ОО «Шилкинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Шилка, ул. Балябина, 132в",
            "city": "Шилка",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.851485,
                "longitude": 116.031037
            }
        },
        {
            "id": 24002004,
            "Biskvit_id": "2314",
            "shortName": "ОО «Ракетчик» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, пос. ЗАТО Сибирский, ул. 40 лет РВСН, д. 4",
            "city": "ЗАТО Сибирский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.557893,
                "longitude": 83.838086
            }
        },
        {
            "id": 24006039,
            "Biskvit_id": "2813",
            "shortName": "ОО ЦИК «Кузбасский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, ул. Д. Бедного, д. 1",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.347551,
                "longitude": 86.076337
            }
        },
        {
            "id": 24009046,
            "Biskvit_id": "1746",
            "shortName": "ОО «На Авиаторов» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Авиаторов, д. 39",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.047419,
                "longitude": 92.913181
            }
        },
        {
            "id": 29000287,
            "Biskvit_id": "3110",
            "shortName": "ДО «Отрадное» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Декабристов, д. 20, корп. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.862343,
                "longitude": 37.608949
            }
        },
        {
            "id": 24003012,
            "Biskvit_id": "3043",
            "shortName": "ОО «Проспект Маркса» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, пр-т Карла Маркса угол ул. Съездовская, д. 15/29 корп. 1",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.976204,
                "longitude": 73.382127
            }
        },
        {
            "id": 25015007,
            "Biskvit_id": "0828",
            "shortName": "ДО «Прогресс» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Земеца, д. 18б, стр. 10",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.217424,
                "longitude": 50.294643
            }
        },
        {
            "id": 24001009,
            "Biskvit_id": "1324",
            "shortName": "ОО «Карымский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Карымский район, пгт. Карымское, ул. Шемелина, д. 1",
            "city": "пгт. Карымское",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.627823,
                "longitude": 114.35232
            }
        },
        {
            "id": 41017008,
            "Biskvit_id": "1339",
            "shortName": "ОО «Корабельный» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Северодвинск, ул. Ломоносова, д. 87/22",
            "city": "Северодвинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.549119,
                "longitude": 39.776754
            }
        },
        {
            "id": 24010038,
            "Biskvit_id": "3324",
            "shortName": "ДО «На Каменской» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Каменская, д. 30",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.029559,
                "longitude": 82.928973
            }
        },
        {
            "id": 27002003,
            "Biskvit_id": "3056",
            "shortName": "ОО «На Краснофлотской» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Благовещенск, ул. Краснофлотская, д. 135",
            "city": "Благовещенск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.256737,
                "longitude": 127.525341
            }
        },
        {
            "id": 21008024,
            "Biskvit_id": "1216",
            "shortName": "ОО «На Попова» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, ул. Попова, д. 18",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.594831,
                "longitude": 36.588408
            }
        },
        {
            "id": 25011014,
            "Biskvit_id": "2962",
            "shortName": "ОО «Александровский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Кирова, д. 5",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 54.731908,
                "longitude": 55.947426
            }
        },
        {
            "id": 27007029,
            "Biskvit_id": "1723",
            "shortName": "ДО «Платинум» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Дикопольцева, д. 26",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.484201,
                "longitude": 135.083775
            }
        },
        {
            "id": 21006040,
            "Biskvit_id": "3045",
            "shortName": "РОО «Тульский»",
            "address": "Тульская область, г. Тула, пр-т Ленина, д. 77",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.179898,
                "longitude": 37.6039
            }
        },
        {
            "id": 25008007,
            "Biskvit_id": "1853",
            "shortName": "ОО «Волжский» в г. Чебоксары Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Чебоксары, ул. Нижег.ская, д. 4",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 56.140851,
                "longitude": 47.245913
            }
        },
        {
            "id": 25013030,
            "Biskvit_id": "3742",
            "shortName": "ОО «На Машинистов» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Машинистов/ ул. Лепешинской, д. 49/9",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.04189,
                "longitude": 56.103176
            }
        },
        {
            "id": 21009003,
            "Biskvit_id": "1266",
            "shortName": "ОО «Фокинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Брянск, пр-т Московский, д. 15",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.217985,
                "longitude": 34.400238
            }
        },
        {
            "id": 21006032,
            "Biskvit_id": "1645",
            "shortName": "ОО «На Красноармейском» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, пр-т Красноармейский, д. 38",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.198463,
                "longitude": 37.58782
            }
        },
        {
            "id": 26000102,
            "Biskvit_id": "0338",
            "shortName": "ДО №52 «Оптиков, 34» Филиала № 7806 Банка ВТБ",
            "address": "г. Санкт-Петербург, ул. Оптиков, д. 34, корп.1, лит А. пом. 9-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.999764,
                "longitude": 30.216236
            }
        },
        {
            "id": 25007000,
            "Biskvit_id": "1052",
            "shortName": "РОО «Саратовский»",
            "address": "Саратовская область, г. Саратов, ул. Советская, д. 51, литер А",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.529646,
                "longitude": 46.018195
            }
        },
        {
            "id": 22002012,
            "Biskvit_id": "3049",
            "shortName": "ОО «Миасский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Миасс, пр-т Автозаводцев, д. 20",
            "city": "Миасс",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.058858,
                "longitude": 60.107138
            }
        },
        {
            "id": 27004006,
            "Biskvit_id": "2656",
            "shortName": "ОО «На Дзержинского» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Якутск, ул. Дзержинского, д. 23",
            "city": "Якутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.045137,
                "longitude": 129.739778
            }
        },
        {
            "id": 25015004,
            "Biskvit_id": "4718",
            "shortName": "ДО «На Агибалова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Агибалова, д. 48",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.190413,
                "longitude": 50.119992
            }
        },
        {
            "id": 21010000,
            "Biskvit_id": "1068",
            "shortName": "РОО «Ярославский»",
            "address": "Ярославская область, г. Ярославль, ул. Кирова, д. 10/25",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.626275,
                "longitude": 39.889277
            }
        },
        {
            "id": 0,
            "Biskvit_id": "0096",
            "shortName": "ДОПЗП в Ленинградской области",
            "address": "Ленинградская область, г. Гатчина, проспект 25 Октября, д.38",
            "city": "Гатчина",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.573227,
                "longitude": 30.125443
            }
        },
        {
            "id": 27003000,
            "Biskvit_id": "1054",
            "shortName": "РОО «Владивостокский»",
            "address": "Приморский край, г. Владивосток, ул. Светланская, д. 13",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.116529,
                "longitude": 131.882898
            }
        },
        {
            "id": 29000178,
            "Biskvit_id": "3900",
            "shortName": "ДО ЦИК «Павелецкий» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Бахрушина, д. 32, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.731952,
                "longitude": 37.637084
            }
        },
        {
            "id": 24009033,
            "Biskvit_id": "2546",
            "shortName": "ОО «Северный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Шумяцкого, д. 6",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.068268,
                "longitude": 92.93598
            }
        },
        {
            "id": 25015014,
            "Biskvit_id": "1719",
            "shortName": "ОО «Старый город» в г. Тольятти Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. Голосова, д. 30А",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.508452,
                "longitude": 49.431703
            }
        },
        {
            "id": 41017007,
            "Biskvit_id": "1039",
            "shortName": "ОО «На Набережной» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Архангельск, наб. Северной Двины, д. 55",
            "city": "Архангельск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.530993,
                "longitude": 40.527018
            }
        },
        {
            "id": 29000079,
            "Biskvit_id": "3510",
            "shortName": "ДО «Свиблово» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Снежная, д. 26",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.854997,
                "longitude": 37.653388
            }
        },
        {
            "id": 24010030,
            "Biskvit_id": "3840",
            "shortName": "ДО «Золотая Нива» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Бориса Богаткова, д. 221",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.037252,
                "longitude": 82.976251
            }
        },
        {
            "id": 21008028,
            "Biskvit_id": "2116",
            "shortName": "ОО «Трубецкого» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, пр-т Гражданский, д. 36",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.594259,
                "longitude": 36.596942
            }
        },
        {
            "id": 24006038,
            "Biskvit_id": "2713",
            "shortName": "ОО «Кемеровский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, ул. Ноградская, д. 5г",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.354778,
                "longitude": 86.076642
            }
        },
        {
            "id": 23008030,
            "Biskvit_id": "2855",
            "shortName": "ДО «Екатеринодарский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. Красная, д. 145/1",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.047609,
                "longitude": 38.977721
            }
        },
        {
            "id": 21007006,
            "Biskvit_id": "3441",
            "shortName": "ОО «Елецкий» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Елец, ул. Орджоникидзе, д. 6",
            "city": "Елец",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.612151,
                "longitude": 38.528446
            }
        },
        {
            "id": 25015001,
            "Biskvit_id": "1619",
            "shortName": "ОО «Жигулевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Жигулевск, ул. Победы, д. 8",
            "city": "Жигулевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.403749,
                "longitude": 49.486365
            }
        },
        {
            "id": 25003005,
            "Biskvit_id": "5118",
            "shortName": "ОО «На Карла Маркса» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Кировская область, г. Киров, ул. Карла Маркса, д. 101, по 1002/А",
            "city": "Киров",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.594621,
                "longitude": 49.667717
            }
        },
        {
            "id": 22006022,
            "Biskvit_id": "2402",
            "shortName": "ДО «Персональный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Бориса Ельцина, д. 1А",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 56.846169,
                "longitude": 60.589354
            }
        },
        {
            "id": 22006025,
            "Biskvit_id": "1322",
            "shortName": "ДО «Локомотивный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Техническая, д. 63",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.869004,
                "longitude": 60.522977
            }
        },
        {
            "id": 21003000,
            "Biskvit_id": "0851",
            "shortName": "РОО «Владимирский»",
            "address": "Владимирская область, г. Владимир, ул. Разина, д. 21",
            "city": "Владимир",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.117542,
                "longitude": 40.367109
            }
        },
        {
            "id": 22005008,
            "Biskvit_id": "2815",
            "shortName": "ОО «Когалымский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Когалым, ул. Ленинградская, д. 19/1",
            "city": "Когалым",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.260606,
                "longitude": 74.473706
            }
        },
        {
            "id": 24002016,
            "Biskvit_id": "1314",
            "shortName": "ОО «Рубцовский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Рубцовск, ул. Ленина, д. 141",
            "city": "Рубцовск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.502586,
                "longitude": 81.208492
            }
        },
        {
            "id": 24001003,
            "Biskvit_id": "2040",
            "shortName": "ОО «Шатры» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Чита, ул. Бутина, 115",
            "city": "Чита",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.044898,
                "longitude": 113.510104
            }
        },
        {
            "id": 24001005,
            "Biskvit_id": "1824",
            "shortName": "ОО «На Амурской» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Чита, ул. Амурская д. 41",
            "city": "Чита",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.025756,
                "longitude": 113.509035
            }
        },
        {
            "id": 25006289,
            "Biskvit_id": "2968",
            "shortName": "ОО «Богородский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, Богородский район, г. Богородск, ул. Ленина, д.204, пом.47",
            "city": "Богородск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.103256,
                "longitude": 43.513162
            }
        },
        {
            "id": 29000031,
            "Biskvit_id": "1603",
            "shortName": "ДО «Жуковский Центральный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Жуковский, ул. Ломоносова, д. 4",
            "city": "Жуковский",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.589992,
                "longitude": 38.123306
            }
        },
        {
            "id": 41019041,
            "Biskvit_id": "2590",
            "shortName": "ОО «Ленинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Мурманск, пр-т Героев Североморцев, д. 33А",
            "city": "Мурманск",
            "scheduleFl": "пн-пт: 11:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.002507,
                "longitude": 33.098696
            }
        },
        {
            "id": 23006021,
            "Biskvit_id": "2905",
            "shortName": "ОО «В Новочеркасске» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Новочеркасск, ул. Комитетская, д. 56/64",
            "city": "Новочеркасск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.416498,
                "longitude": 40.106031
            }
        },
        {
            "id": 21016009,
            "Biskvit_id": "0451",
            "shortName": "ДО «Россошанский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Россошь, ул. Пролетарская, д. 75",
            "city": "Россошь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.197201,
                "longitude": 39.565398
            }
        },
        {
            "id": 22002022,
            "Biskvit_id": "4002",
            "shortName": "ОО «Шадринский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Курганская область, г. Шадринск, ул. Февральская, д. 54",
            "city": "Шадринск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.084872,
                "longitude": 63.628597
            }
        },
        {
            "id": 25002000,
            "Biskvit_id": "1009",
            "shortName": "РОО «Йошкар-Олинский»",
            "address": "Республика Марий Эл, г. Йошкар-Ола, ул. Вашская, д. 8",
            "city": "Йошкар-Ола",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.628911,
                "longitude": 47.889179
            }
        },
        {
            "id": 22006321,
            "Biskvit_id": "1132",
            "shortName": "ДО «Полевской» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Россия , Свердловская область, г. Полевской, ул. Ленина, д. 15",
            "city": "Полевской",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.496319,
                "longitude": 60.23584
            }
        },
        {
            "id": 41018001,
            "Biskvit_id": "1338",
            "shortName": "ОО «Прегольский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Калининград, Ленинский пр-т, д. № 87-91",
            "city": "Калининград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.703806,
                "longitude": 20.507002
            }
        },
        {
            "id": 24007061,
            "Biskvit_id": "1911",
            "shortName": "ОО «Железногорск-Илимский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, Нижнеилимский район, г. Железногорск-илимский, 8 квартал, д. 22, пом. 2",
            "city": "Железногорск-Илимский",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.583599,
                "longitude": 104.113951
            }
        },
        {
            "id": 24007000,
            "Biskvit_id": "2011",
            "shortName": "РОО «Иркутский»",
            "address": "Иркутская область, г. Иркутск, ул. Российская, д. 10",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.28496,
                "longitude": 104.275522
            }
        },
        {
            "id": 21001004,
            "Biskvit_id": "2121",
            "shortName": "ОО «На Достоевского» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Калужская область, г. Калуга, ул. Достоевского, д. 20",
            "city": "Калуга",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.511875,
                "longitude": 36.251756
            }
        },
        {
            "id": 24002010,
            "Biskvit_id": "2214",
            "shortName": "ОО «Энтузиаст» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, ул. Попова, д. 114, пом. Н3",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.358217,
                "longitude": 83.673263
            }
        },
        {
            "id": 41019003,
            "Biskvit_id": "1436",
            "shortName": "ОО «Кандалакша» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Кандалакша, ул. Первомайская, д. 83а",
            "city": "Кандалакша",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.156524,
                "longitude": 32.412383
            }
        },
        {
            "id": 23006001,
            "Biskvit_id": "1905",
            "shortName": "ОО «Петровский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Азов, ул. Зои Космодемьянской, д. 88/12",
            "city": "Азов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.100432,
                "longitude": 39.419674
            }
        },
        {
            "id": 29000087,
            "Biskvit_id": "5110",
            "shortName": "ДО «Бульвар Рокоссовского» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Ивантеевская, д. 23",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.815701,
                "longitude": 37.731847
            }
        },
        {
            "id": 29000027,
            "Biskvit_id": "4129",
            "shortName": "ДО «Егорьевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Егорьевск, ул. К. Маркса, д. 90а",
            "city": "Егорьевск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.378718,
                "longitude": 39.045561
            }
        },
        {
            "id": 26000006,
            "Biskvit_id": "2406",
            "shortName": "ОО «Выборг» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Выборг, пр. Ленина, д. 10",
            "city": "Выборг",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.71186,
                "longitude": 28.743619
            }
        },
        {
            "id": 21013000,
            "Biskvit_id": "1751",
            "shortName": "РОО «Курский»",
            "address": "Курская область, г. Курск, ул. Радищева, д. 24",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.732855,
                "longitude": 36.18988
            }
        },
        {
            "id": 25015023,
            "Biskvit_id": "2318",
            "shortName": "ДО «Проспект Металлургов» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, пр-т Металлургов, д. 56",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.231818,
                "longitude": 50.272436
            }
        },
        {
            "id": 27004004,
            "Biskvit_id": "1223",
            "shortName": "ОО «Центральный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Мирный, ул. Тихонова, д. 3",
            "city": "Мирный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.546996,
                "longitude": 113.981073
            }
        },
        {
            "id": 29000083,
            "Biskvit_id": "4310",
            "shortName": "ДО «Алтуфьево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Алтуфьевское шоссе, д. 90",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.900168,
                "longitude": 37.588305
            }
        },
        {
            "id": 29000022,
            "Biskvit_id": "0927",
            "shortName": "ДО «Гагаринский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинский пр-т, д. 64",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.692475,
                "longitude": 37.551726
            }
        },
        {
            "id": 24006033,
            "Biskvit_id": "3124",
            "shortName": "ОО «Новоильинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, пр-т Авиаторов, д. 72",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.897647,
                "longitude": 87.118661
            }
        },
        {
            "id": 21013012,
            "Biskvit_id": "2151",
            "shortName": "ОО «Сеймский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курск, ул. Харьковская, д. 3",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.674114,
                "longitude": 36.145359
            }
        },
        {
            "id": 23008055,
            "Biskvit_id": "4555",
            "shortName": "ДО «На Российской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. им. 40-летия Победы, д. 144/4",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.055206,
                "longitude": 39.019681
            }
        },
        {
            "id": 29000103,
            "Biskvit_id": "1130",
            "shortName": "ДО «Кузнецкий мост» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Рождественка, д. 8/15, стр. 3",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.762399,
                "longitude": 37.62395
            }
        },
        {
            "id": 29000292,
            "Biskvit_id": "4127",
            "shortName": "ДО «Полянка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Полянка, д. 30",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.734202,
                "longitude": 37.618866
            }
        },
        {
            "id": 28000001,
            "Biskvit_id": "5572",
            "shortName": "ДО «Бродников» Филиала № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, Бродников пер., д. 4",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб: 09:30-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.737446,
                "longitude": 37.617959
            }
        },
        {
            "id": 21005000,
            "Biskvit_id": "1044",
            "shortName": "РОО «Смоленский»",
            "address": "Смоленская область, г. Смоленск, ул. Октябрьской революции, д. 9",
            "city": "Смоленск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.77494,
                "longitude": 32.044568
            }
        },
        {
            "id": 25011009,
            "Biskvit_id": "1762",
            "shortName": "ОО «Зеленая Роща» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Менделеева, д. 137",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.713481,
                "longitude": 55.993591
            }
        },
        {
            "id": 29000138,
            "Biskvit_id": "2429",
            "shortName": "ДО «Центральный» в г. Москве Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Кузнецкий Мост, д. 17, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.762272,
                "longitude": 37.624822
            }
        },
        {
            "id": 22006017,
            "Biskvit_id": "1012",
            "shortName": "ДО «Чкаловский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Циолковского, д. 57",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.805619,
                "longitude": 60.612863
            }
        },
        {
            "id": 29000179,
            "Biskvit_id": "3700",
            "shortName": "ДО Кредитный центр «Марксистский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Марксистская, д.5, стр.1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.737182,
                "longitude": 37.663952
            }
        },
        {
            "id": 29000180,
            "Biskvit_id": "2900",
            "shortName": "ДО «Ломоносовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинский пр-т, д. 69",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.690374,
                "longitude": 37.550657
            }
        },
        {
            "id": 22006016,
            "Biskvit_id": "0912",
            "shortName": "ДО «Уралмаш» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, просп. Космонавтов, д. 23а",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.888702,
                "longitude": 60.61262
            }
        },
        {
            "id": 22006020,
            "Biskvit_id": "0602",
            "shortName": "ДО «ВУЗовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, пр-т Ленина, д. 101/ ул. Гагарина, д. 16",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.843294,
                "longitude": 60.644277
            }
        },
        {
            "id": 41020003,
            "Biskvit_id": "1004",
            "shortName": "ОО «На Коммунистической» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Сыктывкар, ул. Коммунистическая, д. 67",
            "city": "Сыктывкар",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.659428,
                "longitude": 50.79972
            }
        },
        {
            "id": 29000054,
            "Biskvit_id": "1110",
            "shortName": "ДО «Мосфильмовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Мосфильмовская, д. 70",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.71518,
                "longitude": 37.506612
            }
        },
        {
            "id": 29000058,
            "Biskvit_id": "0510",
            "shortName": "ДО «Крылатское» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Осенний бульвар, д. 7, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.757794,
                "longitude": 37.406944
            }
        },
        {
            "id": 29000173,
            "Biskvit_id": "2200",
            "shortName": "ДО «На Рижской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, пр-т Мира, д. 76, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.790712,
                "longitude": 37.635179
            }
        },
        {
            "id": 29000231,
            "Biskvit_id": "4225",
            "shortName": "ДО «Ростелеком» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Гончарная, д. 30, стр.1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.742428,
                "longitude": 37.647468
            }
        },
        {
            "id": 22006034,
            "Biskvit_id": "3902",
            "shortName": "ДО «Асбестский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Асбест, ул. Ленинградская, д. 20",
            "city": "Асбест",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.01192,
                "longitude": 61.462004
            }
        },
        {
            "id": 25007002,
            "Biskvit_id": "3152",
            "shortName": "ОО «Аткарский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Аткарск, ул. Чапаева, д. 100",
            "city": "Аткарск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.876801,
                "longitude": 45.008309
            }
        },
        {
            "id": 29000238,
            "Biskvit_id": "5310",
            "shortName": "ДО «Новомытищинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г.Мытищи, Новомытищинский пр-т, д. 30/1, помещение 1",
            "city": "Мытищи",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.911961,
                "longitude": 37.738522
            }
        },
        {
            "id": 29000037,
            "Biskvit_id": "1403",
            "shortName": "ДО «На Пионерской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Балашиха, ул. Пионерская, д. 13",
            "city": "Балашиха",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.794806,
                "longitude": 37.967933
            }
        },
        {
            "id": 27002002,
            "Biskvit_id": "3156",
            "shortName": "ОО «Белогорский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Белогорск, ул. Победы, 18",
            "city": "Белогорск",
            "scheduleFl": "пн-пт: 09:00-18:00 cб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.920844,
                "longitude": 128.464071
            }
        },
        {
            "id": 29000089,
            "Biskvit_id": "5210",
            "shortName": "ДО «ГУМ» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Красная площадь, д. 3",
            "city": "Москва",
            "scheduleFl": "пн-вс: 10:00-22:00",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.75474,
                "longitude": 37.621408
            }
        },
        {
            "id": 25009001,
            "Biskvit_id": "2257",
            "shortName": "ОО «Локомотивный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Агрыз, ул. Вокзальная, д. 17",
            "city": "Агрыз",
            "scheduleFl": "пн-пт: 08:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.525092,
                "longitude": 53.013502
            }
        },
        {
            "id": 21008001,
            "Biskvit_id": "1816",
            "shortName": "ОО «Алексеевский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Алексеевка, ул. Победы, д. 63",
            "city": "Алексеевка",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.630423,
                "longitude": 38.6846
            }
        },
        {
            "id": 27007001,
            "Biskvit_id": "2923",
            "shortName": "ДО «Болоньский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Амурск, пр-т Комсомольский, д. 15",
            "city": "Амурск",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.226278,
                "longitude": 136.90846
            }
        },
        {
            "id": 29000213,
            "Biskvit_id": "1625",
            "shortName": "ДО «На Мытной» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Мытная, д. 7, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.722142,
                "longitude": 37.618569
            }
        },
        {
            "id": 22006033,
            "Biskvit_id": "0622",
            "shortName": "ДО «Артемовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Артемовский, ул. Садовая, д. 12",
            "city": "Артемовский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.339029,
                "longitude": 61.901334
            }
        },
        {
            "id": 25014047,
            "Biskvit_id": "0728",
            "shortName": "ОО «На Нефтяников» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Елабуга, пр-т Нефтяников, д. 29",
            "city": "Елабуга",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.753326,
                "longitude": 52.020378
            }
        },
        {
            "id": 25007004,
            "Biskvit_id": "2652",
            "shortName": "ОО «Ершовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Ершов, ул. Вокзальная, д. 36",
            "city": "Ершов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.348304,
                "longitude": 48.277233
            }
        },
        {
            "id": 27002001,
            "Biskvit_id": "3856",
            "shortName": "ОО «Завитинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Завитинск, ул. Кирова, 16А",
            "city": "Завитинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.118545,
                "longitude": 129.446415
            }
        },
        {
            "id": 41019004,
            "Biskvit_id": "4036",
            "shortName": "ОО «Заозёрский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Заозерск, ул. Колышкина, д. 2",
            "city": "Заозерск",
            "scheduleFl": "пн: выходной вт-пт: 11:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.397783,
                "longitude": 32.44651
            }
        },
        {
            "id": 22002019,
            "Biskvit_id": "2649",
            "shortName": "ОО «Златоустовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Златоуст, ул. Таганайская, д. 204, пом. нежилое №2, IV секция",
            "city": "Златоуст",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.173113,
                "longitude": 59.672425
            }
        },
        {
            "id": 29000299,
            "Biskvit_id": "2325",
            "shortName": "ДО «Новоясеневский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Новоясеневский пр-т, д. 9",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.608816,
                "longitude": 37.535412
            }
        },
        {
            "id": 22006035,
            "Biskvit_id": "1122",
            "shortName": "ДО «Богдановичский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Богданович, ул. Первомайская, д. 28",
            "city": "Богданович",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.776927,
                "longitude": 62.047948
            }
        },
        {
            "id": 41021001,
            "Biskvit_id": "0926",
            "shortName": "ОО «На Предтеченской» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Новгородская область, г. Великий Новгород, ул. Большая Санкт-Петербургская, д. 5/1",
            "city": "Великий Новгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.526959,
                "longitude": 31.272718
            }
        },
        {
            "id": 25013017,
            "Biskvit_id": "3942",
            "shortName": "ОО «Верещагинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Верещагино, ул. К. Маркса, д. 17",
            "city": "Верещагино",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.076649,
                "longitude": 54.655451
            }
        },
        {
            "id": 27003005,
            "Biskvit_id": "2554",
            "shortName": "ОО «Приморский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, пр-т Острякова, д. 8",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.130447,
                "longitude": 131.901376
            }
        },
        {
            "id": 27003006,
            "Biskvit_id": "2654",
            "shortName": "ОО «Тихоокеанский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, пр-т Океанский, д. 98а",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.13292,
                "longitude": 131.904098
            }
        },
        {
            "id": 27003007,
            "Biskvit_id": "2754",
            "shortName": "ОО «Дальневосточный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, ул. Мордовцева, д. 8а",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 43.119333,
                "longitude": 131.884604
            }
        },
        {
            "id": 29000229,
            "Biskvit_id": "4803",
            "shortName": "ДО «Георгиевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Георгиевский пер., д. 2",
            "city": "Москва",
            "scheduleFl": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.758478,
                "longitude": 37.614734
            }
        },
        {
            "id": 18001001,
            "Biskvit_id": "1655",
            "shortName": "ОО «На Коцоева» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Северная Осетия - Алания, г. Владикавказ, ул. Коцоева, д. 13",
            "city": "Владикавказ",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.01848,
                "longitude": 44.679229
            }
        },
        {
            "id": 25006034,
            "Biskvit_id": "2250",
            "shortName": "ОО «Строгановский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Рождественская, д. 36",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 56.327086,
                "longitude": 43.983852
            }
        },
        {
            "id": 21016005,
            "Biskvit_id": "1521",
            "shortName": "ДО «Никитинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, ул. Средне-Московская, д. 1д",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 51.664507,
                "longitude": 39.20017
            }
        },
        {
            "id": 25006038,
            "Biskvit_id": "2950",
            "shortName": "ОО «Центральный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Минина, д. 19/6",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.326393,
                "longitude": 44.022479
            }
        },
        {
            "id": 21016007,
            "Biskvit_id": "2421",
            "shortName": "ДО «Солнечный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, ул. 20-летия Октября, д. 90а",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.654757,
                "longitude": 39.189444
            }
        },
        {
            "id": 25006040,
            "Biskvit_id": "3750",
            "shortName": "ОО «Персональный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Максима Горького, д. 152",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.316224,
                "longitude": 44.004396
            }
        },
        {
            "id": 25009031,
            "Biskvit_id": "1157",
            "shortName": "ОО «Северная столица» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Глазов, ул. Парковая, д. 45а",
            "city": "Глазов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.141656,
                "longitude": 52.653223
            }
        },
        {
            "id": 21007005,
            "Biskvit_id": "3541",
            "shortName": "ОО «Грязинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Грязи, ул. Правды, д. 17",
            "city": "Грязи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.490061,
                "longitude": 39.955986
            }
        },
        {
            "id": 25013018,
            "Biskvit_id": "3842",
            "shortName": "ОО «Губахинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Губаха, пр-т Ленина, д. 27",
            "city": "Губаха",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.840152,
                "longitude": 57.551889
            }
        },
        {
            "id": 27004009,
            "Biskvit_id": "4056",
            "shortName": "ОО «Нерюнгри» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Нерюнгри, пр-т Ленина, д. 6",
            "city": "Нерюнгри",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.660196,
                "longitude": 124.71038
            }
        },
        {
            "id": 29000040,
            "Biskvit_id": "3425",
            "shortName": "ДО «На Каширском» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Домодедово, микрорайон Центральный, Каширское шоссе, д. 29",
            "city": "Домодедово",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.438741,
                "longitude": 37.767537
            }
        },
        {
            "id": 29000285,
            "Biskvit_id": "3927",
            "shortName": "ДО «Подольский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Подольск, Революционный пр-т, д. 54",
            "city": "Подольск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.432919,
                "longitude": 37.550837
            }
        },
        {
            "id": 29000281,
            "Biskvit_id": "5229",
            "shortName": "ДО «Пушкинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Пушкино, ул. Тургенева, д. 24, пом. 018",
            "city": "Пушкино",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.01085,
                "longitude": 37.854359
            }
        },
        {
            "id": 25014042,
            "Biskvit_id": "3464",
            "shortName": "ОО «Казанский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Петербургская, д. 80",
            "city": "Казань",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.777667,
                "longitude": 49.140298
            }
        },
        {
            "id": 25007010,
            "Biskvit_id": "2952",
            "shortName": "ОО «Вольский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, р.пос. Сенной, ул. Привокзальная, д 36Б",
            "city": "р.п. Сенной",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.159935,
                "longitude": 46.965235
            }
        },
        {
            "id": 29000246,
            "Biskvit_id": "1129",
            "shortName": "ДО «Раменский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Раменское, ул. Карла Маркса, д. 4, помещение № 1",
            "city": "Раменское",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.596488,
                "longitude": 38.273405
            }
        },
        {
            "id": 25003000,
            "Biskvit_id": "1018",
            "shortName": "РОО «Кировский»",
            "address": "Кировская область, г. Киров, ул. Воровского, д. 92, корп. 2",
            "city": "Киров",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.596384,
                "longitude": 49.614851
            }
        },
        {
            "id": 25003002,
            "Biskvit_id": "3218",
            "shortName": "ОО «Октябрьский проспект» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Кировская область, г. Киров, пр-т Октябрьский, д. 50",
            "city": "Киров",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.61081,
                "longitude": 49.657593
            }
        },
        {
            "id": 25003004,
            "Biskvit_id": "0148",
            "shortName": "ОО «Северный» в г. Кирове Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Кировская область, г. Киров, пр-т Октябрьский, д. 11",
            "city": "Киров",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.637195,
                "longitude": 49.620223
            }
        },
        {
            "id": 29000006,
            "Biskvit_id": "0800",
            "shortName": "ДО «Проспект Космонавтов» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Королев, пр-т Космонавтов, д. 29/12, корп. 1, пом. I",
            "city": "Королев",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.912254,
                "longitude": 37.86831
            }
        },
        {
            "id": 41018004,
            "Biskvit_id": "1038",
            "shortName": "ОО «На Ленинском проспекте» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Калининград, Ленинский пр-т, д. 28",
            "city": "Калининград",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.712035,
                "longitude": 20.507514
            }
        },
        {
            "id": 25010013,
            "Biskvit_id": "2661",
            "shortName": "ОО «Орский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Орск, ул. Советская, д. 62а",
            "city": "Орск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.205915,
                "longitude": 58.557023
            }
        },
        {
            "id": 25010015,
            "Biskvit_id": "2961",
            "shortName": "ОО «Новоорский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, пос. Новоорск, ул. Рабочая, д. 6",
            "city": "п. Новоорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.38404,
                "longitude": 58.985376
            }
        },
        {
            "id": 22006030,
            "Biskvit_id": "0902",
            "shortName": "ДО «Каменск-Уральский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Каменск-Уральский, ул. Ленина, д. 36А",
            "city": "Каменск-Уральский",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.415903,
                "longitude": 61.912303
            }
        },
        {
            "id": 25002004,
            "Biskvit_id": "1409",
            "shortName": "ОО «На Палантая» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Марий Эл, г. Йошкар-Ола, ул. Палантая, д. 112",
            "city": "Йошкар-Ола",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.632664,
                "longitude": 47.88767
            }
        },
        {
            "id": 22005003,
            "Biskvit_id": "5015",
            "shortName": "ОО «Премиальный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Нижневартовск, ул. Ленина, д. 38а",
            "city": "Нижневартовск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.935407,
                "longitude": 76.584998
            }
        },
        {
            "id": 21016001,
            "Biskvit_id": "2341",
            "shortName": "ДО «Нововоронежский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Нововоронеж, ул. Курчатова, д. 14",
            "city": "Нововоронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.311578,
                "longitude": 39.212127
            }
        },
        {
            "id": 21014000,
            "Biskvit_id": "2551",
            "shortName": "РОО «Костромской»",
            "address": "Костромская область, г. Кострома, пл. Мира д. 2",
            "city": "Кострома",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.771835,
                "longitude": 40.940665
            }
        },
        {
            "id": 41017002,
            "Biskvit_id": "1439",
            "shortName": "ОО «Котласский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Котлас, пр-т Мира, д. 33",
            "city": "Котлас",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.243579,
                "longitude": 46.642802
            }
        },
        {
            "id": 29000010,
            "Biskvit_id": "3525",
            "shortName": "ДО «Дом правительства Московской области» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Красногорск, бульвар Строителей, д. 1",
            "city": "Красногорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.816085,
                "longitude": 37.380812
            }
        },
        {
            "id": 22006012,
            "Biskvit_id": "1422",
            "shortName": "ДО «Красноуфимский» в г. Красноуфимске Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Красноуфимск, ул. Сухобского, д. 20",
            "city": "Красноуфимск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.598899,
                "longitude": 57.767961
            }
        },
        {
            "id": 25013021,
            "Biskvit_id": "1842",
            "shortName": "ОО «Сибирский тракт» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Революции, д. 26",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.004323,
                "longitude": 56.25439
            }
        },
        {
            "id": 25013004,
            "Biskvit_id": "1742",
            "shortName": "ОО «Кунгурский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Кунгур, ул. Ленина, д. 42",
            "city": "Кунгур",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.43335,
                "longitude": 56.938502
            }
        },
        {
            "id": 22006004,
            "Biskvit_id": "1722",
            "shortName": "ДО «Кушвинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Кушва, ул. Станционная, д. 90",
            "city": "Кушва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.267105,
                "longitude": 59.712598
            }
        },
        {
            "id": 29000001,
            "Biskvit_id": "1125",
            "shortName": "ДО «Лобня» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Лобня, ул. Ленина, д. 9",
            "city": "Лобня",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.012385,
                "longitude": 37.482061
            }
        },
        {
            "id": 25006288,
            "Biskvit_id": "2868",
            "shortName": "ОО «Балахнинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, р-н Балахнинский, г.Балахна, пл.Советская, дом 16, пом. П4",
            "city": "Балахна",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.493506,
                "longitude": 43.611312
            }
        },
        {
            "id": 29000002,
            "Biskvit_id": "4403",
            "shortName": "ДО «На Октябрьском» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Люберцы, Октябрьский пр-т, д. 380д",
            "city": "Люберцы",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.660673,
                "longitude": 37.913379
            }
        },
        {
            "id": 22004061,
            "Biskvit_id": "3163",
            "shortName": "ОО «В поселке Харп» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО, Приуральский район, п.Харп, ул. Дзержинского, 12",
            "city": "п. Харп",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.815974,
                "longitude": 65.800579
            }
        },
        {
            "id": 27005000,
            "Biskvit_id": "1956",
            "shortName": "РОО «Магаданский»",
            "address": "Магаданская область, г. Магадан, пр-т Карла Маркса, д. 33/15",
            "city": "Магадан",
            "scheduleFl": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.564577,
                "longitude": 150.804921
            }
        },
        {
            "id": 23001163,
            "Biskvit_id": "3758",
            "shortName": "ОО «На Невской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Невская, д. 11",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.7169,
                "longitude": 44.508935
            }
        },
        {
            "id": 27005001,
            "Biskvit_id": "2023",
            "shortName": "ОО «Колымский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Магаданская область, г. Магадан, пр-т Ленина, д. 30Б",
            "city": "Магадан",
            "scheduleFl": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.56196,
                "longitude": 150.797734
            }
        },
        {
            "id": 22004063,
            "Biskvit_id": "3763",
            "shortName": "ОО «Красноселькупский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО, c.Красноселькуп, ул. 40 лет Победы, 24",
            "city": "с. Красноселькуп",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 65.701937,
                "longitude": 82.45883
            }
        },
        {
            "id": 41019001,
            "Biskvit_id": "0826",
            "shortName": "ОО «Мончегорский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Мончегорск, пр-т Металлургов, д. 35",
            "city": "Мончегорск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.93859,
                "longitude": 32.927926
            }
        },
        {
            "id": 41021000,
            "Biskvit_id": "0193",
            "shortName": "РОО «Новгородский»",
            "address": "Новгородская область, г. Великий Новгород, пр-т Мира, д. 24",
            "city": "Великий Новгород",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.536637,
                "longitude": 31.232293
            }
        },
        {
            "id": 41000002,
            "Biskvit_id": "1890",
            "shortName": "Операционный офис в г. Выборге Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Ленинградская область, г. Выборг, ул. Крепостная, д. 16",
            "city": "Выборг",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.712829,
                "longitude": 28.733872
            }
        },
        {
            "id": 23006043,
            "Biskvit_id": "3605",
            "shortName": "ОО «Александровский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т 40 летия Победы, д. 85",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.239107,
                "longitude": 39.827293
            }
        },
        {
            "id": 23006044,
            "Biskvit_id": "3705",
            "shortName": "ОО «Скобелевский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пер. Университетский, д. 129",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 47.23253,
                "longitude": 39.724292
            }
        },
        {
            "id": 25015030,
            "Biskvit_id": "3518",
            "shortName": "ДО «Губернский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Сызрань, ул. Октябрьская, д. 22",
            "city": "Сызрань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.165933,
                "longitude": 48.480046
            }
        },
        {
            "id": 21003001,
            "Biskvit_id": "1151",
            "shortName": "ОО «На Советской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Муром, ул. Советская, д. 75",
            "city": "Муром",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.574294,
                "longitude": 42.036619
            }
        },
        {
            "id": 18002002,
            "Biskvit_id": "1755",
            "shortName": "ОО «Нальчикский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Кабардино-Балкарская Республика, г. Нальчик, ул. Кешокова, д. 57",
            "city": "Нальчик",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.48049,
                "longitude": 43.603406
            }
        },
        {
            "id": 23006022,
            "Biskvit_id": "1605",
            "shortName": "ОО «Заводской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Новочеркасск, ул. Машиностроителей, д. 7а",
            "city": "Новочеркасск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.472551,
                "longitude": 40.065401
            }
        },
        {
            "id": 29000004,
            "Biskvit_id": "4203",
            "shortName": "ДО «Одинцово» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Одинцово, ул. Можайское ш., д. 153а",
            "city": "Одинцово",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.686107,
                "longitude": 37.303126
            }
        },
        {
            "id": 25010002,
            "Biskvit_id": "2361",
            "shortName": "ОО «Уральский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, ул. Чкалова, д. 26/1",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.769481,
                "longitude": 55.129995
            }
        },
        {
            "id": 41000024,
            "Biskvit_id": "1490",
            "shortName": "Операционный офис в г. Гатчине Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Ленинградская область, г. Гатчина, пр-т 25 Октября, д. 38",
            "city": "Гатчина",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.573227,
                "longitude": 30.125443
            }
        },
        {
            "id": 25007011,
            "Biskvit_id": "2252",
            "shortName": "ОО «Ртищевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Ртищево, ул. Красная, д. 5",
            "city": "Ртищево",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.257202,
                "longitude": 43.786797
            }
        },
        {
            "id": 29000005,
            "Biskvit_id": "4103",
            "shortName": "ДО «Центральный бульвар» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Орехово-Зуево, Центральный бульвар, д. 7",
            "city": "Орехово-Зуево",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.80271,
                "longitude": 38.977029
            }
        },
        {
            "id": 21004000,
            "Biskvit_id": "0951",
            "shortName": "РОО «Тамбовский»",
            "address": "Тамбовская область, г. Тамбов, ул. Интернациональная, д. 16а",
            "city": "Тамбов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-14:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.720957,
                "longitude": 41.454457
            }
        },
        {
            "id": 25012006,
            "Biskvit_id": "2818",
            "shortName": "ОО «Терновский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Пенза, ул. Терновского, д. 255",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.132773,
                "longitude": 45.021119
            }
        },
        {
            "id": 25013005,
            "Biskvit_id": "3542",
            "shortName": "ОО «Полет» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, пр-т Комсомольский, д. 98",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.983348,
                "longitude": 56.254893
            }
        },
        {
            "id": 25013006,
            "Biskvit_id": "4442",
            "shortName": "ОО «Камский мост» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Ленина, д. 66",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.008943,
                "longitude": 56.229129
            }
        },
        {
            "id": 25013007,
            "Biskvit_id": "4342",
            "shortName": "ОО «Камский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Краснова, д. 14/Сибирская, д. 37",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 58.007551,
                "longitude": 56.25156
            }
        },
        {
            "id": 25015022,
            "Biskvit_id": "2118",
            "shortName": "ДО «Георгиевский» Филиала № 6318 Банка ВТБ ПАО)",
            "address": "Самарская область, г. Самара, ул. Ульяновская, д. 53",
            "city": "Самара",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 53.197745,
                "longitude": 50.113084
            }
        },
        {
            "id": 25011015,
            "Biskvit_id": "2762",
            "shortName": "ОО «Туймазинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Туймазы, ул. Гагарина, д. 29",
            "city": "Туймазы",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.603863,
                "longitude": 53.697191
            }
        },
        {
            "id": 21006034,
            "Biskvit_id": "2645",
            "shortName": "ОО «Баташёвский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Тургеневская, д. 59",
            "city": "Тула",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 54.185051,
                "longitude": 37.612614
            }
        },
        {
            "id": 25013008,
            "Biskvit_id": "1942",
            "shortName": "ОО «Театральный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Ленина, д. 59",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.149474,
                "longitude": 56.474153
            }
        },
        {
            "id": 29000025,
            "Biskvit_id": "4110",
            "shortName": "ДО «ЗИО Подольск» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Подольск, ул. Железнодорожная, д. 2",
            "city": "Подольск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.419248,
                "longitude": 37.570042
            }
        },
        {
            "id": 41000026,
            "Biskvit_id": "0790",
            "shortName": "Дополнительный офис «Удельный» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "г. Санкт-Петербург, Светлановский пр., д. 11, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.006678,
                "longitude": 30.337625
            }
        },
        {
            "id": 18002015,
            "Biskvit_id": "5586",
            "shortName": "ОО в г. Нальчике Филиала в г. Ставрополе",
            "address": "Кабардино-Балкарская Республика, г. Нальчик, пр-т Ленина, д. 17",
            "city": "Нальчик",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.475224,
                "longitude": 43.591531
            }
        },
        {
            "id": 18002017,
            "Biskvit_id": "5589",
            "shortName": "ДО в г. Пятигорске Филиала в г. Ставрополе",
            "address": "Ставропольский край, г. Пятигорск, ул. Малыгина, д. 24а",
            "city": "Пятигорск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.038577,
                "longitude": 43.061336
            }
        },
        {
            "id": 25015029,
            "Biskvit_id": "0928",
            "shortName": "ДО «Проспект Кирова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, пр-т Кирова, д. 391А",
            "city": "Самара",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.250313,
                "longitude": 50.224808
            }
        },
        {
            "id": 22005012,
            "Biskvit_id": "5115",
            "shortName": "ОО «Александровский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, ул. Университетская, д. 9",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.246816,
                "longitude": 73.416362
            }
        },
        {
            "id": 23006034,
            "Biskvit_id": "2305",
            "shortName": "ОО «Троицкий» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Таганрог, ул. Ленина, д. 159",
            "city": "Таганрог",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.228393,
                "longitude": 38.908442
            }
        },
        {
            "id": 25007001,
            "Biskvit_id": "2552",
            "shortName": "ОО «Пугачевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Пугачев, ул. Бубенца, д. 21/1",
            "city": "Пугачев",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.009893,
                "longitude": 48.813662
            }
        },
        {
            "id": 26000002,
            "Biskvit_id": "2706",
            "shortName": "ДО № 27 «Магазейная, 66» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, г. Пушкин, ул. Магазейная, д. 66, Лит. А, пом. 1-Н",
            "city": "Пушкин",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.720454,
                "longitude": 30.416417
            }
        },
        {
            "id": 18002006,
            "Biskvit_id": "1559",
            "shortName": "ОО «Пять вершин» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Пятигорск, пр-т Кирова, д. 86",
            "city": "Пятигорск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.03592,
                "longitude": 43.058452
            }
        },
        {
            "id": 23008048,
            "Biskvit_id": "5558",
            "shortName": "ОО в ст. Павловская Филиала в г. Ростове-на-Дону",
            "address": "Краснодарский край, ст. Павловская, ул. Ленина, д. 18/1",
            "city": "ст. Павловская",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.13324,
                "longitude": 39.782386
            }
        },
        {
            "id": 26000037,
            "Biskvit_id": "0406",
            "shortName": "ДО «На Невском, № 4» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Невский пр., д. 153, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.925173,
                "longitude": 30.380205
            }
        },
        {
            "id": 26000041,
            "Biskvit_id": "1406",
            "shortName": "ДО № 14 «Глинки, 2» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Глинки, д. 2, литера А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.927477,
                "longitude": 30.296159
            }
        },
        {
            "id": 27003014,
            "Biskvit_id": "2154",
            "shortName": "ОО «Никольский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Уссурийск, ул. Вокзальная площадь, д. 3",
            "city": "Уссурийск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.797247,
                "longitude": 131.952122
            }
        },
        {
            "id": 25011000,
            "Biskvit_id": "1062",
            "shortName": "РОО «Уфимский»",
            "address": "Республика Башкортостан, г. Уфа, пл. Верхнеторговая, д. 3",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.725753,
                "longitude": 55.945297
            }
        },
        {
            "id": 21010005,
            "Biskvit_id": "1268",
            "shortName": "ОО «Рыбинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Рыбинск, ул. Крестовая, д. 79",
            "city": "Рыбинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.050621,
                "longitude": 38.842829
            }
        },
        {
            "id": 23006033,
            "Biskvit_id": "1505",
            "shortName": "ОО «Сальский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Сальск, ул. Пушкина, д. 33",
            "city": "Сальск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.47419,
                "longitude": 41.540192
            }
        },
        {
            "id": 29000198,
            "Biskvit_id": "1525",
            "shortName": "ДО «Троицк» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, г. Троицк, Октябрьский пр-т, д. 17 Б",
            "city": "Троицк",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.478327,
                "longitude": 37.298706
            }
        },
        {
            "id": 23006049,
            "Biskvit_id": "5548",
            "shortName": "ДО в г. Таганроге Филиала в г. Ростове-на-Дону",
            "address": "Ростовская область, г. Таганрог, пл. Октябрьская, д. 4",
            "city": "Таганрог",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.209763,
                "longitude": 38.936407
            }
        },
        {
            "id": 26000045,
            "Biskvit_id": "1806",
            "shortName": "ДО № 18 «Светлановский, 11» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Светлановский пр., д. 11, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.006678,
                "longitude": 30.337625
            }
        },
        {
            "id": 26000046,
            "Biskvit_id": "0326",
            "shortName": "ДО № 33 «Каменноостровский, 44» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Каменноостровский пр-т, д. 44/16, лит. Б, пом.7Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.969209,
                "longitude": 30.307972
            }
        },
        {
            "id": 27007038,
            "Biskvit_id": "1623",
            "shortName": "ДО «Амурский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Комсомольская, д. 80",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 48.472871,
                "longitude": 135.060302
            }
        },
        {
            "id": 21006026,
            "Biskvit_id": "2345",
            "shortName": "ОО «Центральный» в г. Туле Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, пр-т Ленина, д. 2",
            "city": "Тула",
            "scheduleFl": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.19348,
                "longitude": 37.616503
            }
        },
        {
            "id": 21006028,
            "Biskvit_id": "2745",
            "shortName": "ОО «Пассаж» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Советская, д. 64",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.191479,
                "longitude": 37.617294
            }
        },
        {
            "id": 22001005,
            "Biskvit_id": "4715",
            "shortName": "ОО «Знаменский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Челюскинцев д. 1, стр. 2",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 57.160483,
                "longitude": 65.540877
            }
        },
        {
            "id": 22001006,
            "Biskvit_id": "5615",
            "shortName": "ОО «Троицкий» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Володарского, д.3/5",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.16058,
                "longitude": 65.530214
            }
        },
        {
            "id": 22001007,
            "Biskvit_id": "5215",
            "shortName": "ОО «Георгиевский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул.Республики, д.171/3",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.132093,
                "longitude": 65.581606
            }
        },
        {
            "id": 24007062,
            "Biskvit_id": "5824",
            "shortName": "ОО «Байкальский Прайм» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Российская, д. 10",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 52.28496,
                "longitude": 104.275522
            }
        },
        {
            "id": 26000014,
            "Biskvit_id": "4706",
            "shortName": "ДО «Василеостровский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Большой пр-т В.О., д.10, лит. А, часть нежил. пом. 1-Н: комн. №№ 15-38 на -м этаже, комн. №№57-68 на 2-м этаже, комн. №№ 87-104 на 3-м этаже, комн. №№ 105-109 на 4 этаже",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 09:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 59.939879,
                "longitude": 30.287167
            }
        },
        {
            "id": 26000017,
            "Biskvit_id": "1826",
            "shortName": "ДО № 6 «Маршала Жукова, 36» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Маршала Жукова, д. 36, корп. 1, литер А, пом. 23Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.853211,
                "longitude": 30.224815
            }
        },
        {
            "id": 29000262,
            "Biskvit_id": "5010",
            "shortName": "ДО «ЦИК «Химки-Правобережный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Химки, ул. Пролетарская, д. 8, стр. 1",
            "city": "Химки",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.892334,
                "longitude": 37.44055
            }
        },
        {
            "id": 27007027,
            "Biskvit_id": "1456",
            "shortName": "ДО «Большая» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Карла Маркса, д. 91",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.497445,
                "longitude": 135.097914
            }
        },
        {
            "id": 26000022,
            "Biskvit_id": "2626",
            "shortName": "ДО № 39 «Московский, 6» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Московский пр-т, д. 6, лит А, пом. 3-Н, комн. 1-22",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00 пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.924754,
                "longitude": 30.318042
            }
        },
        {
            "id": 22002035,
            "Biskvit_id": "1349",
            "shortName": "ОО «Университетский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Лесопарковая, д. 7",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.155618,
                "longitude": 61.365426
            }
        },
        {
            "id": 22006042,
            "Biskvit_id": "0212",
            "shortName": "ДО «Верхнесалдинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Верхняя Салда, ул. Энгельса, д. 67",
            "city": "Верхняя Салда",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.051264,
                "longitude": 60.560257
            }
        },
        {
            "id": 41025008,
            "Biskvit_id": "2560",
            "shortName": "ОО № 7 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Сталеваров, д. 45",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.125143,
                "longitude": 37.904467
            }
        },
        {
            "id": 26000026,
            "Biskvit_id": "3126",
            "shortName": "ДО № 42 «Савушкина, 131» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Савушкина, д. 131, литера «А», пом.26-Н, комн. №№ 1-3, 23-39 и часть комн. №9",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.987942,
                "longitude": 30.214206
            }
        },
        {
            "id": 26000032,
            "Biskvit_id": "3726",
            "shortName": "ДО № 46 «Большая Морская, 11» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Большая Морская, д. 11, лит. А, на 1 этаже пом.2-Н и подвале 2-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.935782,
                "longitude": 30.316713
            }
        },
        {
            "id": 41018008,
            "Biskvit_id": "2138",
            "shortName": "ОО «Черняховский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Черняховск, ул. Ленина, д.16А, помещение № 1-4 в цокольном этаже №1, литер III",
            "city": "Черняховск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.630706,
                "longitude": 21.819503
            }
        },
        {
            "id": 25013019,
            "Biskvit_id": "4142",
            "shortName": "ОО «Чусовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Чусовой, ул. Электродеповская, д. 13",
            "city": "Чусовой",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.292733,
                "longitude": 57.838847
            }
        },
        {
            "id": 23001025,
            "Biskvit_id": "2458",
            "shortName": "ОО «Кировский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. 64-й Армии, д. 44",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.620903,
                "longitude": 44.426137
            }
        },
        {
            "id": 26000057,
            "Biskvit_id": "1936",
            "shortName": "ДО № 50 «Кронштадтский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Кронштадтский район, г. Кронштадт, пр. Ленина, д. 57, пом. 12-Н, комн. №№1,2,3,4 лит.А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.99179,
                "longitude": 29.775846
            }
        },
        {
            "id": 26000060,
            "Biskvit_id": "0436",
            "shortName": "ДО № 55 «Балтийский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, наб. Обводного канала, д. 120, литер 1",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.906932,
                "longitude": 30.298692
            }
        },
        {
            "id": 26000061,
            "Biskvit_id": "2936",
            "shortName": "ДО № 57 «Площадь Островского» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пл. Островского., д. 2, литер A",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:30-17:30 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.931733,
                "longitude": 30.338065
            }
        },
        {
            "id": 27002004,
            "Biskvit_id": "3756",
            "shortName": "ОО «Шимановский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Шимановск, ул. Вокзальная, 5",
            "city": "Шимановск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.003973,
                "longitude": 127.683319
            }
        },
        {
            "id": 21010001,
            "Biskvit_id": "1168",
            "shortName": "ОО «Московский проспект» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, пр-т Московский, д. 147",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.588955,
                "longitude": 39.859615
            }
        },
        {
            "id": 21016000,
            "Biskvit_id": "4041",
            "shortName": "РОО «Воронежский»",
            "address": "Воронежская область, г. Воронеж, пр-т Революции, д. 58",
            "city": "Воронеж",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.66401,
                "longitude": 39.203871
            }
        },
        {
            "id": 21010003,
            "Biskvit_id": "1468",
            "shortName": "ОО «Победа» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, ул. Труфанова, д. 19",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.685753,
                "longitude": 39.765166
            }
        },
        {
            "id": 21010004,
            "Biskvit_id": "2068",
            "shortName": "ОО «Сретенский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, ул. Свободы, д. 26/63",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.625764,
                "longitude": 39.877626
            }
        },
        {
            "id": 25010006,
            "Biskvit_id": "2261",
            "shortName": "ОО «Ясный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Ясный, ул. Ленина, д. 9",
            "city": "Ясный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.036011,
                "longitude": 59.872786
            }
        },
        {
            "id": 41019005,
            "Biskvit_id": "3936",
            "shortName": "ОО «Алакуртти» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, c. Алакуртти, ул. Содружества, д. 16",
            "city": "с. Алакуртти",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.968769,
                "longitude": 30.334086
            }
        },
        {
            "id": 26000067,
            "Biskvit_id": "2736",
            "shortName": "ДО № 2 «Луначарского, 11» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр. Луначарского, д. 11, к. 1, лит. А, часть пом. 20-Н (на 1 эт. часть комн. №47, комн. №№ 54,55,56,57,62,63,64, в подв. комн. №№3, 26)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.042878,
                "longitude": 30.329244
            }
        },
        {
            "id": 27001000,
            "Biskvit_id": "0856",
            "shortName": "РОО «Сахалинский»",
            "address": "Сахалинская область, г. Южно-Сахалинск, yл. Ленина, д. 234",
            "city": "Южно-Сахалинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.95571,
                "longitude": 142.729776
            }
        },
        {
            "id": 21010009,
            "Biskvit_id": "1868",
            "shortName": "ОО «Железнодорожный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, ул. Угличская, д. 21",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.629262,
                "longitude": 39.846544
            }
        },
        {
            "id": 27004008,
            "Biskvit_id": "2823",
            "shortName": "ОО «Алдан» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Алдан, ул. Ленина, д. 20",
            "city": "Алдан",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.608902,
                "longitude": 125.388096
            }
        },
        {
            "id": 23002000,
            "Biskvit_id": "1020",
            "shortName": "РОО «Астраханский»",
            "address": "Астраханская область, г. Астрахань, ул. Савушкина, д. 12Б",
            "city": "Астрахань",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.370956,
                "longitude": 48.048729
            }
        },
        {
            "id": 27002007,
            "Biskvit_id": "1256",
            "shortName": "ОО «На Шевченко» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Благовещенск, ул. Шевченко, д. 36 ЛА1",
            "city": "Благовещенск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.263492,
                "longitude": 127.528287
            }
        },
        {
            "id": 23001007,
            "Biskvit_id": "1808",
            "shortName": "ОО «Дзержинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. 8-ой Воздушной армии, д. 58",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.758772,
                "longitude": 44.501614
            }
        },
        {
            "id": 26000078,
            "Biskvit_id": "4436",
            "shortName": "ДО «На Шпалерной» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Шпалерная, д. 40а",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 09:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 59.949249,
                "longitude": 30.36303
            }
        },
        {
            "id": 23001009,
            "Biskvit_id": "2208",
            "shortName": "ОО «На Коммунистической» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Коммунистическая, д. 19Д",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.715878,
                "longitude": 44.522805
            }
        },
        {
            "id": 23001010,
            "Biskvit_id": "2608",
            "shortName": "ОО «На Комсомольской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Комсомольская, д. 8",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.709208,
                "longitude": 44.521287
            }
        },
        {
            "id": 23001012,
            "Biskvit_id": "2808",
            "shortName": "ОО ЦИК «Панорама» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. 13-й Гвардейской, 7А",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.715152,
                "longitude": 44.530288
            }
        },
        {
            "id": 21016015,
            "Biskvit_id": "1841",
            "shortName": "ДО «Площадь Ленина» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, пл. Ленина, д. 3",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.659551,
                "longitude": 39.199883
            }
        },
        {
            "id": 27001001,
            "Biskvit_id": "3123",
            "shortName": "ОО «Корсаковский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Сахалинская область, г. Корсаков, ул. Советская, д. 36",
            "city": "Корсаков",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.633556,
                "longitude": 142.781348
            }
        },
        {
            "id": 21014002,
            "Biskvit_id": "1941",
            "shortName": "ОО «Заволжский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Костромская область, г. Кострома, мкр. Паново, д. 11",
            "city": "Кострома",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.736832,
                "longitude": 40.910087
            }
        },
        {
            "id": 21005007,
            "Biskvit_id": "5494",
            "shortName": "ОО в г. Смоленске Филиала в г. Воронеже",
            "address": "Смоленская область, г. Смоленск, пр-т Гагарина, д. 5а",
            "city": "Смоленск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.776233,
                "longitude": 32.049922
            }
        },
        {
            "id": 21012008,
            "Biskvit_id": "5495",
            "shortName": "ОО в г. Твери Филиала в г. Воронеже",
            "address": "Тверская область, г. Тверь, пер. Свободный, д. 9",
            "city": "Тверь",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.857721,
                "longitude": 35.903991
            }
        },
        {
            "id": 17000003,
            "Biskvit_id": "5328",
            "shortName": "ДО «Кутузовский» Филиала в г. Москве",
            "address": "г. Москва, пл. Победы, д. 2, корп. 2",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.737507,
                "longitude": 37.51838
            }
        },
        {
            "id": 17000004,
            "Biskvit_id": "5325",
            "shortName": "ДО «Бродников переулок» Филиала в г. Москве",
            "address": "г. Москва, Бродников пер., д. 4",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.737446,
                "longitude": 37.617959
            }
        },
        {
            "id": 17000006,
            "Biskvit_id": "5425",
            "shortName": "ДО «Лубянский» Филиала в г. Москве",
            "address": "г. Москва, ул. Большая Лубянка, д. 16, стр. 1",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.762936,
                "longitude": 37.628846
            }
        },
        {
            "id": 23008026,
            "Biskvit_id": "1855",
            "shortName": "ДО «Екатерининский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. Ленина, д.82/ ул. Суворова, д. 105",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 45.021679,
                "longitude": 38.981368
            }
        },
        {
            "id": 21002002,
            "Biskvit_id": "2141",
            "shortName": "ОО «На Лежневской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ивановская область, г. Иваново, ул. Лежневская, д. 119",
            "city": "Иваново",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.974092,
                "longitude": 40.975511
            }
        },
        {
            "id": 21002003,
            "Biskvit_id": "4541",
            "shortName": "ОО «На Ленина» в г. Иваново Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ивановская область, г. Иваново, пр-т Ленина, д. 36",
            "city": "Иваново",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.998568,
                "longitude": 40.974613
            }
        },
        {
            "id": 25009021,
            "Biskvit_id": "1257",
            "shortName": "ОО «Родниковый край» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Молодежная, д. 35",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.852844,
                "longitude": 53.290317
            }
        },
        {
            "id": 29000250,
            "Biskvit_id": "4927",
            "shortName": "ДО «Сергиево-Посадский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Сергиев Посад, проспект Красной Армии, д. 203в   ",
            "city": "Сергиев Посад",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.322984,
                "longitude": 38.143752
            }
        },
        {
            "id": 29000251,
            "Biskvit_id": "1003",
            "shortName": "ДО «Сергиев Посад» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Сергиев Посад, ул. К.Маркса, д. 4",
            "city": "Сергиев Посад",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.311501,
                "longitude": 38.135712
            }
        },
        {
            "id": 21002004,
            "Biskvit_id": "3721",
            "shortName": "ОО «Красные ряды» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ивановская область, г. Кинешма, ул. Рылеевская, д. 1",
            "city": "Кинешма",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.443726,
                "longitude": 42.169354
            }
        },
        {
            "id": 28000006,
            "Biskvit_id": "5872",
            "shortName": "ДО «Лермонтовский» Филиала № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, Красноворотский пр-д, д. 3",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб: 09:30-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.770882,
                "longitude": 37.649552
            }
        },
        {
            "id": 41018002,
            "Biskvit_id": "2038",
            "shortName": "ОО «Южный» в г. Калининграде Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Калининград, ул. Киевская, д. 1",
            "city": "Калининград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.692396,
                "longitude": 20.504702
            }
        },
        {
            "id": 25006044,
            "Biskvit_id": "5520",
            "shortName": "ДО в г. Дзержинске Филиала в г. Нижнем Новгороде",
            "address": "Нижегородская область, г. Дзержинск, пр-т Ленина, д. 59",
            "city": "Дзержинск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.238387,
                "longitude": 43.457116
            }
        },
        {
            "id": 29000253,
            "Biskvit_id": "0903",
            "shortName": "ДО «На Крупской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Серпухов, ул. Крупской, д. 10а",
            "city": "Серпухов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.922938,
                "longitude": 37.429411
            }
        },
        {
            "id": 21005005,
            "Biskvit_id": "1144",
            "shortName": "ОО «Октябрьский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Смоленск, ул. Исаковского, д. 5",
            "city": "Смоленск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.778466,
                "longitude": 32.056947
            }
        },
        {
            "id": 21005006,
            "Biskvit_id": "1644",
            "shortName": "ОО «Киселевский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Смоленск, ул. Рыленкова, д. 35-б",
            "city": "Смоленск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.761451,
                "longitude": 32.101243
            }
        },
        {
            "id": 25013031,
            "Biskvit_id": "1642",
            "shortName": "ОО «Соликамский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Соликамск, ул. Коммунистическая, д. 21",
            "city": "Соликамск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.696711,
                "longitude": 56.68179
            }
        },
        {
            "id": 22002017,
            "Biskvit_id": "1849",
            "shortName": "ОО «Карталинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Карталы, ул. Орджоникидзе, д. 1",
            "city": "Карталы",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-16:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.050601,
                "longitude": 60.636174
            }
        },
        {
            "id": 26000003,
            "Biskvit_id": "3706",
            "shortName": "ОО «Кингисеппский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Кингисепп, пр-т К.Маркса, д. 25/2",
            "city": "Кингисепп",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.37075,
                "longitude": 28.608018
            }
        },
        {
            "id": 22002015,
            "Biskvit_id": "2222",
            "shortName": "ОО «На Кирова» в г. Кургане Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Курганская область, г. Курган, ул. Кирова, д. 111/II",
            "city": "Курган",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.439936,
                "longitude": 65.328757
            }
        },
        {
            "id": 25013033,
            "Biskvit_id": "5478",
            "shortName": "ОО в г. Перми Филиала в г. Нижнем Новгороде",
            "address": "Пермский край, г. Пермь, ул. Луначарского, д. 54",
            "city": "Пермь",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.009311,
                "longitude": 56.244526
            }
        },
        {
            "id": 25015035,
            "Biskvit_id": "5479",
            "shortName": "ОО в г. Самаре Филиала в г. Нижнем Новгороде",
            "address": "Самарская область, г. Самара, ул. Ново-Садовая, д. 160Д, стр.2",
            "city": "Самара",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.230374,
                "longitude": 50.177718
            }
        },
        {
            "id": 22006049,
            "Biskvit_id": "5565",
            "shortName": "ДО в г. Нижнем Тагиле Филиала в г. Екатеринбурге",
            "address": "Свердловская область, г. Нижний Тагил, ул. Горошникова, д.66",
            "city": "Нижний Тагил",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.90652,
                "longitude": 59.973397
            }
        },
        {
            "id": 22006048,
            "Biskvit_id": "1922",
            "shortName": "ДО «Талицкий» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, Талицкий р-н, ст. Талица, 2028 км.",
            "city": "ст. Талица",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.062237,
                "longitude": 63.744983
            }
        },
        {
            "id": 18002012,
            "Biskvit_id": "1059",
            "shortName": "ОО «На Ленина» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Ставрополь, ул. Ленина, д. 359",
            "city": "Ставрополь",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.037477,
                "longitude": 41.942907
            }
        },
        {
            "id": 27004002,
            "Biskvit_id": "1323",
            "shortName": "ОО «Ленский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Ленск, ул. Победы, д. 6",
            "city": "Ленск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.715694,
                "longitude": 114.917585
            }
        },
        {
            "id": 21007000,
            "Biskvit_id": "1051",
            "shortName": "РОО «Липецкий»",
            "address": "Липецкая область, г. Липецк, ул. Гагарина, д. 33",
            "city": "Липецк",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.616787,
                "longitude": 39.598429
            }
        },
        {
            "id": 29000202,
            "Biskvit_id": "0103",
            "shortName": "ДО «Дмитров» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Дмитров, ул. Профессиональная, д. 1а",
            "city": "Дмитров",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.348397,
                "longitude": 37.517994
            }
        },
        {
            "id": 29000203,
            "Biskvit_id": "1227",
            "shortName": "ДО «Долгопрудный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Долгопрудный, ул. Первомайская, д. 33, пом. 5",
            "city": "Долгопрудный",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.939661,
                "longitude": 37.516072
            }
        },
        {
            "id": 25013014,
            "Biskvit_id": "5242",
            "shortName": "ОО «Лысьвенский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Лысьва, ул. Федосеева, д. 33",
            "city": "Лысьва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00 пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.101882,
                "longitude": 57.807927
            }
        },
        {
            "id": 21007002,
            "Biskvit_id": "1341",
            "shortName": "ОО «На Космонавтов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Липецк, ул. Космонавтов, д. 102",
            "city": "Липецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.607437,
                "longitude": 39.543488
            }
        },
        {
            "id": 29000289,
            "Biskvit_id": "2427",
            "shortName": "ДО «Ленинградский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградский пр-т, д. 65, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.802912,
                "longitude": 37.518892
            }
        },
        {
            "id": 29000300,
            "Biskvit_id": "2000",
            "shortName": "ДО Кредитный центр «Зубовский бульвар» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Зубовский бульвар, д. 27/26, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.7366,
                "longitude": 37.588099
            }
        },
        {
            "id": 41019008,
            "Biskvit_id": "4506",
            "shortName": "ОО «Первомайский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Мурманск, пр-т Кольский, д. 22",
            "city": "Мурманск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00 пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 68.945796,
                "longitude": 33.09981
            }
        },
        {
            "id": 26000051,
            "Biskvit_id": "3206",
            "shortName": "ДО № 20 «Большой проспект Петроградской стороны, 32» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Ропшинская, д. 1/32, лит. А, пом 2Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.957665,
                "longitude": 30.298055
            }
        },
        {
            "id": 29000293,
            "Biskvit_id": "4327",
            "shortName": "ДО ЦИК «Пушечный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Кузнецкий мост, д. 16/5, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.761598,
                "longitude": 37.622082
            }
        },
        {
            "id": 29000119,
            "Biskvit_id": "4827",
            "shortName": "ДО «Северо-Западный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Свободы, д. 13/2, стр. 1А",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.829264,
                "longitude": 37.451312
            }
        },
        {
            "id": 25006001,
            "Biskvit_id": "1750",
            "shortName": "ОО «Арзамасский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Арзамас, Комсомольский бульвар, д. 17/4",
            "city": "Арзамас",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-14:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.407699,
                "longitude": 43.836052
            }
        },
        {
            "id": 25006042,
            "Biskvit_id": "4350",
            "shortName": "ОО «Сормовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, шоссе Сормовское, д. 14",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.321251,
                "longitude": 43.926189
            }
        },
        {
            "id": 41019012,
            "Biskvit_id": "3436",
            "shortName": "ОО «Александровский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Полярный, ул. Советская, д. 14",
            "city": "Полярный",
            "scheduleFl": "вт-пт: 11:00-19:00 сб: 10:00-17:00 вс, пн: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.19609,
                "longitude": 33.460538
            }
        },
        {
            "id": 18002007,
            "Biskvit_id": "3059",
            "shortName": "ДО «Ессентукский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Ессентуки, ул. Вокзальная, д. 2",
            "city": "Ессентуки",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.047824,
                "longitude": 42.855541
            }
        },
        {
            "id": 18002008,
            "Biskvit_id": "1459",
            "shortName": "ОО «Кисловодский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Кисловодск, пр-т Первомайский, д. 31",
            "city": "Кисловодск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.906187,
                "longitude": 42.715368
            }
        },
        {
            "id": 29000184,
            "Biskvit_id": "2400",
            "shortName": "ДО «Земляной вал» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Земляной Вал, д. 52/16, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.748949,
                "longitude": 37.655131
            }
        },
        {
            "id": 29000185,
            "Biskvit_id": "0700",
            "shortName": "ДО «Новый Арбат» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Б. Молчановка, д. 17",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.753002,
                "longitude": 37.59259
            }
        },
        {
            "id": 29000303,
            "Biskvit_id": "2703",
            "shortName": "ДО «Вернадский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, пр-т Вернадского, 29",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.681712,
                "longitude": 37.516449
            }
        },
        {
            "id": 17000005,
            "Biskvit_id": "5228",
            "shortName": "ДО «Крестовский» Филиала в г. Москве",
            "address": "г. Москва, пр-т Мира, д. 81",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.801318,
                "longitude": 37.634335
            }
        },
        {
            "id": 29000189,
            "Biskvit_id": "2803",
            "shortName": "ДО «Бибирево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Пришвина, д. 23",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.885499,
                "longitude": 37.604682
            }
        },
        {
            "id": 26000005,
            "Biskvit_id": "0836",
            "shortName": "ОО «Волховский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Волхов, пл. Привокзальная, д. 1",
            "city": "Волхов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.921425,
                "longitude": 32.300166
            }
        },
        {
            "id": 22006031,
            "Biskvit_id": "1222",
            "shortName": "ДО «Камышловский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Камышлов, ул. Карла Маркса, д. 52",
            "city": "Камышлов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.842571,
                "longitude": 62.707554
            }
        },
        {
            "id": 29000282,
            "Biskvit_id": "1727",
            "shortName": "ДО «Зеленоградский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, г. Зеленоград, корп. 401",
            "city": "Зеленоград",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.000401,
                "longitude": 37.208776
            }
        },
        {
            "id": 21016002,
            "Biskvit_id": "0821",
            "shortName": "ДО «Лискинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Лиски, ул. Коммунистическая, д. 17",
            "city": "Лиски",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.981276,
                "longitude": 39.504133
            }
        },
        {
            "id": 29000098,
            "Biskvit_id": "0525",
            "shortName": "ДО «Обручевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинский пр-т, д. 111, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.661333,
                "longitude": 37.509352
            }
        },
        {
            "id": 29000048,
            "Biskvit_id": "5403",
            "shortName": "ДО «Люблино центр» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Совхозная, д. 41",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.674575,
                "longitude": 37.760234
            }
        },
        {
            "id": 29000056,
            "Biskvit_id": "0810",
            "shortName": "ДО «Митино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Митинская, д. 36, корп. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.847078,
                "longitude": 37.362154
            }
        },
        {
            "id": 29000060,
            "Biskvit_id": "2110",
            "shortName": "ДО «Кантемировский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Кантемировская, д. 47",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.637799,
                "longitude": 37.656182
            }
        },
        {
            "id": 26000073,
            "Biskvit_id": "3636",
            "shortName": "ДО № 28 «Славы, 40» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр. Славы, д. 40, корп. 1, лит. А, нежил. пом. 61-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.861381,
                "longitude": 30.398845
            }
        },
        {
            "id": 26000101,
            "Biskvit_id": "2390",
            "shortName": "ДО № 64 «Ушаковская,3» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Ушаковская наб., д. 3, корп. 1А, лит. А, пом. 21-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.981798,
                "longitude": 30.314646
            }
        },
        {
            "id": 29000342,
            "Biskvit_id": "3001",
            "shortName": "ДО «Щука» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Щукинская, д. 42",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-21:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.809474,
                "longitude": 37.464571
            }
        },
        {
            "id": 29000255,
            "Biskvit_id": "0829",
            "shortName": "ДО «Щелковский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Щелково, Пролетарский просп., д. 7",
            "city": "Щелково",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.917067,
                "longitude": 37.995395
            }
        },
        {
            "id": 29000061,
            "Biskvit_id": "1610",
            "shortName": "ДО «Белорусский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, 4-й Лесной пер., д. 4",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.779069,
                "longitude": 37.586931
            }
        },
        {
            "id": 27007035,
            "Biskvit_id": "0356",
            "shortName": "ДО «Ленина» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Ленина, 48",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.478109,
                "longitude": 135.085436
            }
        },
        {
            "id": 29000062,
            "Biskvit_id": "1910",
            "shortName": "ДО «Черемушки» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Профсоюзная, д. 56",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.670021,
                "longitude": 37.55248
            }
        },
        {
            "id": 27007037,
            "Biskvit_id": "0623",
            "shortName": "ДО «Клубная» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Клубная, д. 23",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.435733,
                "longitude": 135.130253
            }
        },
        {
            "id": 29000068,
            "Biskvit_id": "2710",
            "shortName": "ДО «Медведково» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Широкая, д.13а",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.888109,
                "longitude": 37.662461
            }
        },
        {
            "id": 29000463,
            "Biskvit_id": "2504",
            "shortName": "ДО «Куровской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Орехово-Зуевский район,  г. Куровское, ул.40 лет Октября, 52а",
            "city": "Куровское",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.586568,
                "longitude": 38.913132
            }
        },
        {
            "id": 29000304,
            "Biskvit_id": "3103",
            "shortName": "ДО ЦИК «Площадь Победы» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, площадь Победы, д.1, корп.Б",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.735596,
                "longitude": 37.519539
            }
        },
        {
            "id": 41019000,
            "Biskvit_id": "0795",
            "shortName": "РОО «Мурманский»",
            "address": "Мурманская область, г. Мурманск, пр-т Ленина, д. 82",
            "city": "Мурманск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 68.971253,
                "longitude": 33.076795
            }
        },
        {
            "id": 29000193,
            "Biskvit_id": "3603",
            "shortName": "ДО «Покровка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Покровка, д. 28, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.760428,
                "longitude": 37.650028
            }
        },
        {
            "id": 29000194,
            "Biskvit_id": "3803",
            "shortName": "ДО «Большая Ордынка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Ордынка, д. 24",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.739868,
                "longitude": 37.623115
            }
        },
        {
            "id": 29000195,
            "Biskvit_id": "4003",
            "shortName": "ДО «Б. Черкасский, 10/11» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Б. Черкасский пер., д. 10/11, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.756057,
                "longitude": 37.626663
            }
        },
        {
            "id": 29000172,
            "Biskvit_id": "1900",
            "shortName": "ДО «Марьино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Люблинская, д. 165",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.650505,
                "longitude": 37.745924
            }
        },
        {
            "id": 28000004,
            "Biskvit_id": "4772",
            "shortName": "ДО «Гоголевский» Филиала № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, Гоголевский б-р, д. 5, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб: 09:30-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.745149,
                "longitude": 37.599741
            }
        },
        {
            "id": 29000055,
            "Biskvit_id": "0410",
            "shortName": "ДО «Беляево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Профсоюзная, д. 104",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-21:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.64192,
                "longitude": 37.523465
            }
        },
        {
            "id": 28000005,
            "Biskvit_id": "5472",
            "shortName": "ДО «Садовое кольцо» Филиала 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, р-н Хамовники, б-р Зубовский, д. 27, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб: 09:30-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.736858,
                "longitude": 37.588889
            }
        },
        {
            "id": 21016012,
            "Biskvit_id": "0551",
            "shortName": "ДО «Юго-Западный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, пр-т Патриотов, д. 3а",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.644062,
                "longitude": 39.142975
            }
        },
        {
            "id": 23006041,
            "Biskvit_id": "2705",
            "shortName": "ОО «Универсальный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Красноармейская, д. 120",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.22597,
                "longitude": 39.704341
            }
        },
        {
            "id": 23006046,
            "Biskvit_id": "4005",
            "shortName": "ОО «Театральная площадь» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пл. Театральная, д. 4",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.227029,
                "longitude": 39.74684
            }
        },
        {
            "id": 29000233,
            "Biskvit_id": "4525",
            "shortName": "ДО «Южный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, район Чертаново Северное, ул. Кировоградская, д. 14",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.622609,
                "longitude": 37.605939
            }
        },
        {
            "id": 29000237,
            "Biskvit_id": "3500",
            "shortName": "ДО «ЦИК «Мытищи» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Мытищи, ул. Сукромка, стр. 7",
            "city": "Мытищи",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.903539,
                "longitude": 37.713441
            }
        },
        {
            "id": 27002010,
            "Biskvit_id": "3556",
            "shortName": "ОО «Магдагачинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, п. Магдагачи, ул. Горького, 16",
            "city": "п. Магдагачи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.449741,
                "longitude": 125.802606
            }
        },
        {
            "id": 21009000,
            "Biskvit_id": "1066",
            "shortName": "РОО «Брянский»",
            "address": "Брянская область, г. Брянск, пр-т Ленина, д. 99",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.251951,
                "longitude": 34.373711
            }
        },
        {
            "id": 21010002,
            "Biskvit_id": "1368",
            "shortName": "ОО «Гостиный Двор» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, ул. Комсомольская, д. 6",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.624626,
                "longitude": 39.884148
            }
        },
        {
            "id": 25006000,
            "Biskvit_id": "1050",
            "shortName": "РОО «Нижегородский»",
            "address": "г Нижний Новгород, ул. Ковалихинская, д. 14/43",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.322814,
                "longitude": 44.013155
            }
        },
        {
            "id": 26000070,
            "Biskvit_id": "3136",
            "shortName": "ДО № 61 «Савушкина, 7» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Савушкина, д. 7, лит. А, часть пом.1-Н (часть комн. №3, комн. №№4-10)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.986452,
                "longitude": 30.297614
            }
        },
        {
            "id": 23008053,
            "Biskvit_id": "4155",
            "shortName": "ДО «Краснодарский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. Октябрьская, д. 28",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.018054,
                "longitude": 38.96412
            }
        },
        {
            "id": 25006284,
            "Biskvit_id": "2468",
            "shortName": "ОО «Выксунский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Выкса, ул. Красные Зори, д. 7б",
            "city": "Выкса",
            "scheduleFl": "пн-пт: 09:00-18:00 cб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.320442,
                "longitude": 42.167171
            }
        },
        {
            "id": 29000077,
            "Biskvit_id": "3610",
            "shortName": "ДО «Лубянский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Лубянка, д. 16, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.762936,
                "longitude": 37.628846
            }
        },
        {
            "id": 29000093,
            "Biskvit_id": "0501",
            "shortName": "ДО «Каланчевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Каланчевская, д. 35",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.776806,
                "longitude": 37.647926
            }
        },
        {
            "id": 29000210,
            "Biskvit_id": "1225",
            "shortName": "ДО «Сокол» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградский пр-т, д. 77, кор. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.805214,
                "longitude": 37.508185
            }
        },
        {
            "id": 29000212,
            "Biskvit_id": "1325",
            "shortName": "ДО «Остоженка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Остоженка, д. 11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.741744,
                "longitude": 37.59975
            }
        },
        {
            "id": 18002014,
            "Biskvit_id": "2259",
            "shortName": "ДО «Суворовский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Ставрополь, ул. Мира, д. 284/1",
            "city": "Ставрополь",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.03677,
                "longitude": 41.96682
            }
        },
        {
            "id": 26000004,
            "Biskvit_id": "3806",
            "shortName": "ОО «Киришский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Кириши, ул. Советская, д. 18",
            "city": "Кириши",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.448711,
                "longitude": 32.014106
            }
        },
        {
            "id": 29000214,
            "Biskvit_id": "1725",
            "shortName": "ДО «Воздвиженка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Воздвиженка, д. 9",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.752592,
                "longitude": 37.604753
            }
        },
        {
            "id": 29000216,
            "Biskvit_id": "1925",
            "shortName": "ДО «Олимпийский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Мичуринский пр-т, Олимпийская деревня, д.1к.1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.679438,
                "longitude": 37.469638
            }
        },
        {
            "id": 29000217,
            "Biskvit_id": "2225",
            "shortName": "ДО «Южнонагатинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Варшавское шоссе, д. 26",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.684503,
                "longitude": 37.621947
            }
        },
        {
            "id": 29000218,
            "Biskvit_id": "2125",
            "shortName": "ДО «Хамовники» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Комсомольский пр-т, д. 48",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.71983,
                "longitude": 37.571174
            }
        },
        {
            "id": 29000219,
            "Biskvit_id": "2025",
            "shortName": "ДО «Римский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, бульвар Энтузиастов, д. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.746481,
                "longitude": 37.682619
            }
        },
        {
            "id": 29000220,
            "Biskvit_id": "2425",
            "shortName": "ДО «Маяковский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. 1-я Тверская - Ямская, д. 7",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.771525,
                "longitude": 37.592815
            }
        },
        {
            "id": 29000223,
            "Biskvit_id": "2625",
            "shortName": "ДО «Ходынский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Авиаконструктора Микояна, д. 12",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.792361,
                "longitude": 37.527615
            }
        },
        {
            "id": 29000226,
            "Biskvit_id": "3125",
            "shortName": "ДО «На набережной» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Фрунзенская наб., д. 22/2, стр. 11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.727932,
                "longitude": 37.589716
            }
        },
        {
            "id": 27002012,
            "Biskvit_id": "5537",
            "shortName": "ОО в г. Благовещенске Филиала в г. Хабаровске",
            "address": "Амурская область, г. Благовещенск, пер. Советский, д. 65/1",
            "city": "Благовещенск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.267614,
                "longitude": 127.554249
            }
        },
        {
            "id": 25009032,
            "Biskvit_id": "2757",
            "shortName": "ОО «Сарапульский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Сарапул, ул. Гоголя, д. 40у",
            "city": "Сарапул",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.474763,
                "longitude": 53.798099
            }
        },
        {
            "id": 29000286,
            "Biskvit_id": "0603",
            "shortName": "ДО «На Соборной» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Ногинск, ул. Соборная, д. 12",
            "city": "Ногинск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.853218,
                "longitude": 38.442028
            }
        },
        {
            "id": 29000245,
            "Biskvit_id": "0303",
            "shortName": "ДО ЦИК «Пушкино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Пушкино, ул. Чехова, д. 14а",
            "city": "Пушкино",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.008334,
                "longitude": 37.851467
            }
        },
        {
            "id": 26000007,
            "Biskvit_id": "1063",
            "shortName": "ОО «Гатчинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Гатчина, пр-т 25 Октября, д. 38",
            "city": "Гатчина",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.573227,
                "longitude": 30.125443
            }
        },
        {
            "id": 25006023,
            "Biskvit_id": "1350",
            "shortName": "ОО «Дзержинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Дзержинск, пр-т Чкалова, д.2",
            "city": "Дзержинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.240043,
                "longitude": 43.462182
            }
        },
        {
            "id": 29000029,
            "Biskvit_id": "0503",
            "shortName": "ДО «Центр Железнодорожный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Железнодорожный, ш. Саввинское, д. 4, кор. 1",
            "city": "Железнодорожный",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.743634,
                "longitude": 38.012463
            }
        },
        {
            "id": 25014031,
            "Biskvit_id": "1528",
            "shortName": "ОО ЦИК «На Пушкина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Пушкина, д. 20",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.790322,
                "longitude": 49.125027
            }
        },
        {
            "id": 29000162,
            "Biskvit_id": "0630",
            "shortName": "ДО «Текстильщики» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Люблинская, д. 4, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.707841,
                "longitude": 37.729925
            }
        },
        {
            "id": 22001157,
            "Biskvit_id": "5363",
            "shortName": "ОО «Ялуторовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г.Ялуторовск, ул. Ленина, 50/2",
            "city": "Ялуторовск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.655159,
                "longitude": 66.310939
            }
        },
        {
            "id": 21010010,
            "Biskvit_id": "1968",
            "shortName": "ОО «Локомотивный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, пр-т Московский, д. 115",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.597652,
                "longitude": 39.872757
            }
        },
        {
            "id": 25010011,
            "Biskvit_id": "1861",
            "shortName": "ОО «Олимпийский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, ул. Новая, д. 4",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.81129,
                "longitude": 55.091305
            }
        },
        {
            "id": 25010012,
            "Biskvit_id": "1961",
            "shortName": "ОО «Промышленный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, пр-т Братьев Коростелевых, д. 14",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.78817,
                "longitude": 55.077507
            }
        },
        {
            "id": 29000243,
            "Biskvit_id": "3327",
            "shortName": "ДО «Орехово - Зуевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Орехово-Зуево, проезд Юбилейный, д. 8",
            "city": "Орехово-Зуево",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.807886,
                "longitude": 38.968144
            }
        },
        {
            "id": 27007034,
            "Biskvit_id": "0723",
            "shortName": "ДО «Ургальский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, пос. Новый Ургал, ул. Киевская, д. 2",
            "city": "п. Новый Ургал",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.073446,
                "longitude": 132.604433
            }
        },
        {
            "id": 22006043,
            "Biskvit_id": "3802",
            "shortName": "ДО «Свободный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, пос. Свободный, ул. Карбышева, д. 17",
            "city": "п. Свободный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.034701,
                "longitude": 60.388814
            }
        },
        {
            "id": 27003012,
            "Biskvit_id": "1954",
            "shortName": "ОО «Партизанский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Партизанск, ул. Ленинская, д. 31",
            "city": "Партизанск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.120373,
                "longitude": 133.122213
            }
        },
        {
            "id": 25012009,
            "Biskvit_id": "2018",
            "shortName": "ОО «Аврора» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Пенза, ул. Собинова/пр-т Строителей, д. 7Е/35Б",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.22088,
                "longitude": 44.938186
            }
        },
        {
            "id": 25013027,
            "Biskvit_id": "2642",
            "shortName": "ОО «Гагаринский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, бульвар Гагарина, д. 26",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.012262,
                "longitude": 56.278761
            }
        },
        {
            "id": 27007081,
            "Biskvit_id": "4823",
            "shortName": "ОО «Анадырский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Чукотский автономный округ, г. Анадырь, ул. Ленина, д. 20",
            "city": "Анадырь",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.734889,
                "longitude": 177.518967
            }
        },
        {
            "id": 29000175,
            "Biskvit_id": "2600",
            "shortName": "ДО «На Автозаводской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Автозаводская, д. 6",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.709449,
                "longitude": 37.661042
            }
        },
        {
            "id": 25014028,
            "Biskvit_id": "1964",
            "shortName": "ОО «Зеленодольский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Зеленодольск, ул. Маркса, д. 47",
            "city": "Зеленодольск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.850666,
                "longitude": 48.500249
            }
        },
        {
            "id": 25009029,
            "Biskvit_id": "2557",
            "shortName": "ОО «Дерябинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. 10 Октября, д. 8а",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 56.871301,
                "longitude": 53.21264
            }
        },
        {
            "id": 27006006,
            "Biskvit_id": "4223",
            "shortName": "ОО «Авачинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Камчатский край, г. Вилючинск, ул. Победы, д. 2, пом. 92",
            "city": "Вилючинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.930346,
                "longitude": 158.40518
            }
        },
        {
            "id": 27006003,
            "Biskvit_id": "2123",
            "shortName": "ОО «Вилючинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Камчатский край, г. Вилючинск, ул. Вилкова, д. 37",
            "city": "Вилючинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.916458,
                "longitude": 158.521764
            }
        },
        {
            "id": 27006000,
            "Biskvit_id": "1156",
            "shortName": "РОО «Камчатский»",
            "address": "Камчатский край, г. Петропавловск-Камчатский, пр-т Рыбаков, д. 2/1",
            "city": "Петропавловск-Камчатский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.05485,
                "longitude": 158.638985
            }
        },
        {
            "id": 25001002,
            "Biskvit_id": "4218",
            "shortName": "ОО «Рузаевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Мордовия, г. Рузаевка, ул. Привокзальная пл., д. 2",
            "city": "Рузаевка",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.058274,
                "longitude": 44.94911
            }
        },
        {
            "id": 21012006,
            "Biskvit_id": "0321",
            "shortName": "ОО «Петербургский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Тверь, Петербургское шоссе, д. 43в",
            "city": "Тверь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.871217,
                "longitude": 35.852158
            }
        },
        {
            "id": 18002016,
            "Biskvit_id": "5587",
            "shortName": "ДО в г. Невинномысске Филиала в г. Ставрополе",
            "address": "Ставропольский край, г. Невинномысск, ул. Менделеева, д. 21",
            "city": "Невинномысск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.643789,
                "longitude": 41.932881
            }
        },
        {
            "id": 25008008,
            "Biskvit_id": "2253",
            "shortName": "ОО «Северо-Западный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Чебоксары, пр-т М.Горького, д. 40/1",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.149351,
                "longitude": 47.170428
            }
        },
        {
            "id": 21013005,
            "Biskvit_id": "2521",
            "shortName": "ОО «Курский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курск, ул. Ленина, д. 72",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.743323,
                "longitude": 36.193752
            }
        },
        {
            "id": 41019011,
            "Biskvit_id": "4136",
            "shortName": "ОО «Кольский, 158» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Мурманск, пр-т Кольский, д. 158",
            "city": "Мурманск",
            "scheduleFl": "вт-сб: 10:00-19:00 вс, пн: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 68.913702,
                "longitude": 33.095705
            }
        },
        {
            "id": 22002029,
            "Biskvit_id": "2749",
            "shortName": "ОО «На Гагарина» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Гагарина, д. 8",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.142807,
                "longitude": 61.442448
            }
        },
        {
            "id": 22005082,
            "Biskvit_id": "3663",
            "shortName": "ОО «Излучинск» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО - Югра, Нижневартовский район, п.Излучинск, ул. Энергетиков 1, вход № 2",
            "city": "п. Излучинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.954659,
                "longitude": 76.885467
            }
        },
        {
            "id": 25006036,
            "Biskvit_id": "3050",
            "shortName": "ОО «Канавинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Октябрьской революции, д. 51",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.302612,
                "longitude": 43.938092
            }
        },
        {
            "id": 25001000,
            "Biskvit_id": "0818",
            "shortName": "РОО «Саранский»",
            "address": "Республика Мордовия, г. Саранск, пр-т Ленина, д. 19",
            "city": "Саранск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.18817,
                "longitude": 45.188654
            }
        },
        {
            "id": 22001011,
            "Biskvit_id": "2602",
            "shortName": "ОО «Пермякова» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Пермякова, д. 78а/2",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.109753,
                "longitude": 65.566514
            }
        },
        {
            "id": 29000261,
            "Biskvit_id": "1510",
            "shortName": "ДО «Химки» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Химки, Химки-центр, Ленинградское ш., вл. 5",
            "city": "Химки",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.888765,
                "longitude": 37.433526
            }
        },
        {
            "id": 23008322,
            "Biskvit_id": "4758",
            "shortName": "ДО «Славянск-на-Кубани» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Славянск-на-Кубани, ул. Ленина, д. 22",
            "city": "Славянск-на-Кубани",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.258625,
                "longitude": 38.129064
            }
        },
        {
            "id": 29000007,
            "Biskvit_id": "0625",
            "shortName": "ДО «Проспект Королева» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Королев, пр-т Королева д. 5Д, кор. 1, помещение 01",
            "city": "Королев",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.921768,
                "longitude": 37.844118
            }
        },
        {
            "id": 21012002,
            "Biskvit_id": "4241",
            "shortName": "ОО «Удомельский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Удомля, ул. Попова, д. 25",
            "city": "Удомля",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.871514,
                "longitude": 35.007948
            }
        },
        {
            "id": 26000013,
            "Biskvit_id": "0226",
            "shortName": "ДО № 32 «Малый пр. В.О., 22» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Василеостровский р-н, Малый пр., В.О. д. 22, Лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.94577,
                "longitude": 30.27097
            }
        },
        {
            "id": 25013026,
            "Biskvit_id": "2442",
            "shortName": "ОО «Мирный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Мира, д. 26",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.98165,
                "longitude": 56.196493
            }
        },
        {
            "id": 26000016,
            "Biskvit_id": "3006",
            "shortName": "ДО № 30 «Стачек, 47» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Стачек, д. 47, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.878432,
                "longitude": 30.25834
            }
        },
        {
            "id": 22002000,
            "Biskvit_id": "2049",
            "shortName": "РОО «Челябинский»",
            "address": "Челябинская область, г. Челябинск, пр-т Ленина, д. 83",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.158637,
                "longitude": 61.371382
            }
        },
        {
            "id": 22002030,
            "Biskvit_id": "2449",
            "shortName": "ОО «Курчатовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, пр-т Комсомольский, д. 41",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.194044,
                "longitude": 61.338944
            }
        },
        {
            "id": 21014004,
            "Biskvit_id": "3241",
            "shortName": "ОО «Шарьинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Костромская область, г. Шарья, ул. Чапаева, д. 7",
            "city": "Шарья",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.370647,
                "longitude": 45.514509
            }
        },
        {
            "id": 29000257,
            "Biskvit_id": "0929",
            "shortName": "ДО «Электростальский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Электросталь, ул. Победы, д.16",
            "city": "Электросталь",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.770051,
                "longitude": 38.443519
            }
        },
        {
            "id": 24003181,
            "Biskvit_id": "5043",
            "shortName": "ДО «Заозерный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Заозерная, стр. 15, к. 1.",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.043644,
                "longitude": 73.316047
            }
        },
        {
            "id": 25001121,
            "Biskvit_id": "4568",
            "shortName": "ОО «Дальний» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Мордовия, р.п. Зубова Поляна, ул. Советская, д. 28",
            "city": "Зубова Поляна",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.076455,
                "longitude": 42.835266
            }
        },
        {
            "id": 21013020,
            "Biskvit_id": "5493",
            "shortName": "ОО «На Радищева» Филиала №3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курск, ул. Радищева, д. 28 пом. 1",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.734506,
                "longitude": 36.189026
            }
        },
        {
            "id": 25015000,
            "Biskvit_id": "1262",
            "shortName": "РОО «Самарский»",
            "address": "Самарская область, г. Самара, ул. Молодогвардейская, д. 204",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.202076,
                "longitude": 50.10888
            }
        },
        {
            "id": 26000064,
            "Biskvit_id": "2036",
            "shortName": "ДО «На Мойке» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Аптекарский пер, д. 5, лит. А, пом. №№ 2Н, 9Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 09:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 59.942872,
                "longitude": 30.327169
            }
        },
        {
            "id": 21009061,
            "Biskvit_id": "3416",
            "shortName": "ОО «Красноармейский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Брянск, ул. Красноармейская, д. 65",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.238911,
                "longitude": 34.34677
            }
        },
        {
            "id": 26000071,
            "Biskvit_id": "3336",
            "shortName": "ДО № 36 «Парадная, 9» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Парадная, д. 9, лит. А, часть нежил. пом. 1-Н (комн. №№ 12-21)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.940781,
                "longitude": 30.370378
            }
        },
        {
            "id": 26000072,
            "Biskvit_id": "3536",
            "shortName": "ДО «Московский, 73» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр. Московский , д. 73, корп. 3, лит.А, пом. 9-Н (комн. №№1,2), пом. 10-Н (комн. №№1-5), пом. 11-Н (комн. №№1-2)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.904085,
                "longitude": 30.317889
            }
        },
        {
            "id": 26000074,
            "Biskvit_id": "3736",
            "shortName": "ДО № 34 «Большая Конюшенная, 5» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Большая Конюшенная, д. 5, лит. А, пом. 5-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.940389,
                "longitude": 30.323818
            }
        },
        {
            "id": 26000076,
            "Biskvit_id": "4236",
            "shortName": "ДО № 56 «Невская Ратуша» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Дегтярный переулок, д. 11, лит.А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.939465,
                "longitude": 30.384751
            }
        },
        {
            "id": 24010010,
            "Biskvit_id": "1724",
            "shortName": "ДО «Центральный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Бердск, ул. Первомайская, д. 26а",
            "city": "Бердск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.762038,
                "longitude": 83.0942
            }
        },
        {
            "id": 24007004,
            "Biskvit_id": "2811",
            "shortName": "ОО «Европейский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Ангарск, 22 мкр., д. 13, помещение 106",
            "city": "Ангарск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.507238,
                "longitude": 103.858219
            }
        },
        {
            "id": 22006005,
            "Biskvit_id": "2002",
            "shortName": "ДО «Центральный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Нижний Тагил, пр-т Ленина, д. 71",
            "city": "Нижний Тагил",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.910235,
                "longitude": 59.984114
            }
        },
        {
            "id": 24006028,
            "Biskvit_id": "2307",
            "shortName": "ОО ЦИК «На Кирова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, Центральный район, ул. Кирова, д. 58а",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.757207,
                "longitude": 87.145691
            }
        },
        {
            "id": 24007031,
            "Biskvit_id": "1611",
            "shortName": "ОО «Ново-Ленинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Академика Образцова, д. 35",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.340073,
                "longitude": 104.204708
            }
        },
        {
            "id": 24006046,
            "Biskvit_id": "2124",
            "shortName": "ОО «Кемеровский-Прайм» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, ул. Черняховского, д. 2",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.348155,
                "longitude": 86.072878
            }
        },
        {
            "id": 24009054,
            "Biskvit_id": "3846",
            "shortName": "ОО «Иланский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Иланский, ул. Садовая, д. 8, пом. 4",
            "city": "Иланский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.243109,
                "longitude": 96.076356
            }
        },
        {
            "id": 24001001,
            "Biskvit_id": "1224",
            "shortName": "ОО «Петровский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Петровск-Забайкальский, мкр. 1, д. 9",
            "city": "Петровск-Забайкальский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.255778,
                "longitude": 108.8162
            }
        },
        {
            "id": 41022001,
            "Biskvit_id": "1065",
            "shortName": "ОО «На ул. Андропова» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Петрозаводск, ул. Андропова, д. 15",
            "city": "Петрозаводск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-16:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.790984,
                "longitude": 34.362096
            }
        },
        {
            "id": 24009034,
            "Biskvit_id": "3146",
            "shortName": "ОО «На Матросова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Александра Матросова, д. 7",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.987921,
                "longitude": 92.888208
            }
        },
        {
            "id": 24006052,
            "Biskvit_id": "3607",
            "shortName": "ОО «Тайгинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Тайга, пр-т Кирова, 5а",
            "city": "Тайга",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.064716,
                "longitude": 85.621996
            }
        },
        {
            "id": 24010007,
            "Biskvit_id": "4224",
            "shortName": "ДО «Искитимский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Искитим, ул. Советская, д. 201",
            "city": "Искитим",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.643488,
                "longitude": 83.30843
            }
        },
        {
            "id": 22006028,
            "Biskvit_id": "2422",
            "shortName": "ДО «Юбилейный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Луначарского, д. 128",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.842413,
                "longitude": 60.618684
            }
        },
        {
            "id": 24001002,
            "Biskvit_id": "0824",
            "shortName": "ОО «Могочинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Могочинский район, г. Могоча, ул. Клубная, д. 2",
            "city": "Могоча",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.737042,
                "longitude": 119.761651
            }
        },
        {
            "id": 21006025,
            "Biskvit_id": "1945",
            "shortName": "ОО «На Пузакова» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Пузакова, д. 1",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.218584,
                "longitude": 37.622648
            }
        },
        {
            "id": 23006000,
            "Biskvit_id": "2005",
            "shortName": "РОО «Ростовский»",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Большая Садовая, д. 121",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.226447,
                "longitude": 39.735458
            }
        },
        {
            "id": 24010017,
            "Biskvit_id": "0640",
            "shortName": "ДО «На Станционной» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Станционная, д. 30а",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.998003,
                "longitude": 82.853065
            }
        },
        {
            "id": 29000222,
            "Biskvit_id": "2825",
            "shortName": "ДО «Краснопресненский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Красная Пресня, д.11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.761188,
                "longitude": 37.572324
            }
        },
        {
            "id": 25013016,
            "Biskvit_id": "4542",
            "shortName": "ОО «Торговая площадь» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Березники, ул. Мира, д. 62",
            "city": "Березники",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.408256,
                "longitude": 56.850494
            }
        },
        {
            "id": 25011004,
            "Biskvit_id": "3162",
            "shortName": "ОО «Салаватский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Салават, ул. Ленина, д. 42",
            "city": "Салават",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.350354,
                "longitude": 55.926145
            }
        },
        {
            "id": 22002028,
            "Biskvit_id": "2149",
            "shortName": "ОО «Тракторозаводский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Салютная, д. 2",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.171694,
                "longitude": 61.457234
            }
        },
        {
            "id": 27004000,
            "Biskvit_id": "1056",
            "shortName": "РОО «Якутский»",
            "address": "Республика Саха (Якутия), г. Якутск, ул. Октябрьская, д. 3",
            "city": "Якутск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.025052,
                "longitude": 129.724273
            }
        },
        {
            "id": 25010003,
            "Biskvit_id": "1261",
            "shortName": "ОО «Октябрьский» в г. Орске Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Орск, пр-т Ленина, д. 90",
            "city": "Орск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.247993,
                "longitude": 58.459843
            }
        },
        {
            "id": 24010034,
            "Biskvit_id": "1924",
            "shortName": "ДО «Кольцовский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, р.пос. Кольцово, пр-т Никольский, д. 2, помещения 4,18",
            "city": "р.п. Кольцово",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.582396,
                "longitude": 79.26487
            }
        },
        {
            "id": 24003004,
            "Biskvit_id": "1743",
            "shortName": "ОО «На Кузнечной» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Богдана Хмельницкого, д. 162",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.971833,
                "longitude": 73.411655
            }
        },
        {
            "id": 24004005,
            "Biskvit_id": "1471",
            "shortName": "ОО «Таксимовский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, пос. Таксимо, ул. 70 лет Октября, д. 51",
            "city": "п. Таксимо",
            "scheduleFl": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.359175,
                "longitude": 114.838183
            }
        },
        {
            "id": 24001010,
            "Biskvit_id": "4340",
            "shortName": "ОО «Каларский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Каларский район, пгт. Новая Чара, ул. Молдаванова, д. 4",
            "city": "пгт. Новая Чара",
            "scheduleFl": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.799769,
                "longitude": 118.275361
            }
        },
        {
            "id": 24001011,
            "Biskvit_id": "1024",
            "shortName": "ОО «Чернышевский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Чернышевский район, пгт. Чернышевск, ул. Первомайская, д. 37",
            "city": "пгт. Чернышевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.514489,
                "longitude": 117.012618
            }
        },
        {
            "id": 24010062,
            "Biskvit_id": "5124",
            "shortName": "ДО «Юго-Западный» Филиала №5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Троллейная, д. 130в",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.964463,
                "longitude": 82.852301
            }
        },
        {
            "id": 24010037,
            "Biskvit_id": "0313",
            "shortName": "ДО «Татарский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Татарск, ул. Ленина, д. 55",
            "city": "Татарск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.221373,
                "longitude": 75.982283
            }
        },
        {
            "id": 28000002,
            "Biskvit_id": "5772",
            "shortName": "ДО «Деловая столица» Филиала № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, Пресненская наб., д. 10 стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.748914,
                "longitude": 37.535475
            }
        },
        {
            "id": 24001000,
            "Biskvit_id": "0540",
            "shortName": "РОО «Читинский»",
            "address": "Забайкальский край, г. Чита, ул. Чкалова, д. 136",
            "city": "Чита",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.037093,
                "longitude": 113.503295
            }
        },
        {
            "id": 24001013,
            "Biskvit_id": "0724",
            "shortName": "ОО «Железнодорожный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Чита, ул. Горбунова, д. 13, стр. 2, пом. 2",
            "city": "Чита",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.034394,
                "longitude": 113.452495
            }
        },
        {
            "id": 26000042,
            "Biskvit_id": "1506",
            "shortName": "ДО № 15 «Бутлерова, 40» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Бутлерова, д. 40, лит А, пом 43Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб,вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.010115,
                "longitude": 30.404325
            }
        },
        {
            "id": 29000424,
            "Biskvit_id": "2109",
            "shortName": "ДО «Талдомский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская обл., г. Талдом, пл. К. Маркса,  д. 17",
            "city": "Талдом",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.731501,
                "longitude": 37.527741
            }
        },
        {
            "id": 29000057,
            "Biskvit_id": "0710",
            "shortName": "ДО «Преображенский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Черкизовская, д. 12, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.797078,
                "longitude": 37.725388
            }
        },
        {
            "id": 22002032,
            "Biskvit_id": "3349",
            "shortName": "ОО «Синегорье» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Свободы, д. 110б",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.143368,
                "longitude": 61.41451
            }
        },
        {
            "id": 26000050,
            "Biskvit_id": "3306",
            "shortName": "ДО № 21 ЦИК «Чайковского, 32» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Чайковского, д. 32, лит. А, пом. 2Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб,вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.946757,
                "longitude": 30.356319
            }
        },
        {
            "id": 25005004,
            "Biskvit_id": "1331",
            "shortName": "ОО «Черемшан» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Ульяновская область, г. Димитровград, ул. Куйбышева, д. 205",
            "city": "Димитровград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.216315,
                "longitude": 49.622074
            }
        },
        {
            "id": 22001003,
            "Biskvit_id": "1615",
            "shortName": "ОО «Тобольский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тобольск, 8 мкр., д. 7",
            "city": "Тобольск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.223179,
                "longitude": 68.280334
            }
        },
        {
            "id": 41020000,
            "Biskvit_id": "0591",
            "shortName": "РОО «Сыктывкарский»",
            "address": "Республика Коми, г. Сыктывкар, ул. Коммунистическая, д. 67",
            "city": "Сыктывкар",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.659428,
                "longitude": 50.79972
            }
        },
        {
            "id": 24001008,
            "Biskvit_id": "1424",
            "shortName": "ОО «Даурский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, пгт. Забайкальск, ул. Советская, д. 6 а, пом. 1",
            "city": "пгт. Забайкальск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 49.641969,
                "longitude": 117.335966
            }
        },
        {
            "id": 24010022,
            "Biskvit_id": "2240",
            "shortName": "ДО «На Никитина» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Никитина, д. 20",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.01054,
                "longitude": 82.958078
            }
        },
        {
            "id": 22004004,
            "Biskvit_id": "3322",
            "shortName": "ОО «Заполярный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Новый Уренгой, пр-т Губкина, д. 26",
            "city": "Новый Уренгой",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.098324,
                "longitude": 76.676878
            }
        },
        {
            "id": 21009002,
            "Biskvit_id": "1166",
            "shortName": "ОО «Бежицкий» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Брянск, ул. Куйбышева, д. 12",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.307751,
                "longitude": 34.307604
            }
        },
        {
            "id": 24007039,
            "Biskvit_id": "2213",
            "shortName": "ОО «Тайшетский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Тайшет, ул. Транспортная, д. 14",
            "city": "Тайшет",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.939711,
                "longitude": 98.004275
            }
        },
        {
            "id": 24009055,
            "Biskvit_id": "4146",
            "shortName": "ОО «Ачинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Ачинск, ул. Кирова, 27, пом. 61",
            "city": "Ачинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.302023,
                "longitude": 90.515667
            }
        },
        {
            "id": 24004002,
            "Biskvit_id": "1171",
            "shortName": "ОО «Бурятия» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Коммунистическая, д. 47А",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: с 9:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.83206,
                "longitude": 107.585625
            }
        },
        {
            "id": 25006035,
            "Biskvit_id": "2650",
            "shortName": "ОО «Заводской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, Автозаводский район, пр-т Ленина, д. 111, помещение П6",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.248166,
                "longitude": 43.875686
            }
        },
        {
            "id": 24003011,
            "Biskvit_id": "2943",
            "shortName": "ОО «Центральный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Тарская, д. 14",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.991594,
                "longitude": 73.368859
            }
        },
        {
            "id": 24010000,
            "Biskvit_id": "2424",
            "shortName": "РОО «Новосибирский»",
            "address": "Новосибирская область, г. Новосибирск, ул. Фрунзе, д. 232, 234, 234/1",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.030204,
                "longitude": 82.92043
            }
        },
        {
            "id": 29000454,
            "Biskvit_id": "5801",
            "shortName": "ДО «Истринский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Истра, ул. Ленина, д. 75",
            "city": "Истра",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.913061,
                "longitude": 36.858146
            }
        },
        {
            "id": 25012000,
            "Biskvit_id": "1218",
            "shortName": "РОО «Пензенский»",
            "address": "Пензенская область, г. Пенза, ул. Московская, д. 40",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.190747,
                "longitude": 45.015091
            }
        },
        {
            "id": 25006043,
            "Biskvit_id": "4250",
            "shortName": "ОО ЦИК «На Белинского» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Белинского, д. 36",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.310103,
                "longitude": 43.99641
            }
        },
        {
            "id": 24002005,
            "Biskvit_id": "1114",
            "shortName": "ОО «Московский проспект» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, пр-т Ленина, д. 45",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.342925,
                "longitude": 83.781878
            }
        },
        {
            "id": 21011004,
            "Biskvit_id": "2321",
            "shortName": "ОО «На Ленина» в г. Рязани Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, ул. Ленина, д. 45",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.627788,
                "longitude": 39.745861
            }
        },
        {
            "id": 25007008,
            "Biskvit_id": "3352",
            "shortName": "ОО «На Лермонтова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. им. М.Ю. Лермонтова д. 28а",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.526962,
                "longitude": 46.05322
            }
        },
        {
            "id": 41025002,
            "Biskvit_id": "5260",
            "shortName": "ОО «На Батюшкова» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Вологда, ул. Батюшкова, д. 11",
            "city": "Вологда",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.219727,
                "longitude": 39.883752
            }
        },
        {
            "id": 26000001,
            "Biskvit_id": "1326",
            "shortName": "ДО № 37 «Труда, 7» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Санкт-Петербург, г. Колпино, ул. Труда, д. 7/5",
            "city": "Колпино",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.748917,
                "longitude": 30.606752
            }
        },
        {
            "id": 25014001,
            "Biskvit_id": "2564",
            "shortName": "ДО «Альметьевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Альметьевск, пр-т Строителей, д. 10А",
            "city": "Альметьевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.904059,
                "longitude": 52.270532
            }
        },
        {
            "id": 22006006,
            "Biskvit_id": "2202",
            "shortName": "ДО «На Фрунзе» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Нижний Тагил, ул. Фрунзе, д. 50",
            "city": "Нижний Тагил",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.921321,
                "longitude": 59.941686
            }
        },
        {
            "id": 24007021,
            "Biskvit_id": "2313",
            "shortName": "ОО «Нижнеудинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Нижнеудинск, ул. Аллейная, д. 7",
            "city": "Нижнеудинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.892442,
                "longitude": 99.030681
            }
        },
        {
            "id": 41025006,
            "Biskvit_id": "3060",
            "shortName": "ОО «На Ленина» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Ленина, д. 56",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.125018,
                "longitude": 37.926611
            }
        },
        {
            "id": 41019007,
            "Biskvit_id": "3426",
            "shortName": "ОО «Североморский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Североморск, ул. Сафонова, д. 10",
            "city": "Североморск",
            "scheduleFl": "вт-пт: 10:00-18:00 сб: 10:00-17:00 вс, пн: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.075026,
                "longitude": 33.420419
            }
        },
        {
            "id": 25011008,
            "Biskvit_id": "1562",
            "shortName": "ДО «Бульвар Славы» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, пр-т Октября, д. 107А, пом. 3",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.782563,
                "longitude": 56.031293
            }
        },
        {
            "id": 29000066,
            "Biskvit_id": "2510",
            "shortName": "ДО «Москва-Сити» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Пресненская наб., д. 10, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.748914,
                "longitude": 37.535475
            }
        },
        {
            "id": 27003010,
            "Biskvit_id": "1754",
            "shortName": "ОО «Алеутский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, ул. Верхнепортовая, д. 1",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.110336,
                "longitude": 131.880751
            }
        },
        {
            "id": 24007025,
            "Biskvit_id": "1711",
            "shortName": "ОО «Зиминский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Зима, ул. Вокзальная, д. 18",
            "city": "Зима",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-16:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.92642,
                "longitude": 102.051662
            }
        },
        {
            "id": 18001003,
            "Biskvit_id": "3955",
            "shortName": "ОО «Владикавказский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Северная Осетия - Алания, г. Владикавказ, пр-т Мира, д. 1",
            "city": "Владикавказ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.024386,
                "longitude": 44.680864
            }
        },
        {
            "id": 22006026,
            "Biskvit_id": "0122",
            "shortName": "ДО «Европейский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Стрелочников, д. 41",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.856427,
                "longitude": 60.596495
            }
        },
        {
            "id": 25013022,
            "Biskvit_id": "5042",
            "shortName": "ОО «Пермский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. 1-я Красноармейская, д. 40",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.000789,
                "longitude": 56.261118
            }
        },
        {
            "id": 22004062,
            "Biskvit_id": "3463",
            "shortName": "ОО «Губкинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО, г.Губкинский, мкр. 12, дом 40",
            "city": "Губкинский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.434193,
                "longitude": 76.506387
            }
        },
        {
            "id": 25006287,
            "Biskvit_id": "2768",
            "shortName": "ОО «На ул. Силкина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Саров, ул. Силкина, д. 13",
            "city": "Саров",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.91958,
                "longitude": 43.350549
            }
        },
        {
            "id": 22002009,
            "Biskvit_id": "2549",
            "shortName": "ОО «Магнитогорский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Магнитогорск, пр-т Ленина, д. 89",
            "city": "Магнитогорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.395561,
                "longitude": 58.986373
            }
        },
        {
            "id": 24009049,
            "Biskvit_id": "3313",
            "shortName": "ОО «Арбатский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Весны, д. 26",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.039062,
                "longitude": 92.916738
            }
        },
        {
            "id": 25015027,
            "Biskvit_id": "2918",
            "shortName": "ДО «Энергия» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Стара-Загора, д. 139",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.23509,
                "longitude": 50.221969
            }
        },
        {
            "id": 22002026,
            "Biskvit_id": "2249",
            "shortName": "ОО «Детский Мир» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, пр-т Ленина, д. 45",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.160267,
                "longitude": 61.410198
            }
        },
        {
            "id": 22005007,
            "Biskvit_id": "4122",
            "shortName": "ОО «Радужный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Радужный, мкр. 7, стр. 1 «А»",
            "city": "Радужный",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.126052,
                "longitude": 77.453921
            }
        },
        {
            "id": 29000109,
            "Biskvit_id": "3227",
            "shortName": "ДО «Новоарбатский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Новый Арбат, д. 36",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.753666,
                "longitude": 37.57713
            }
        },
        {
            "id": 24010015,
            "Biskvit_id": "0240",
            "shortName": "ДО ЦИК «На Крылова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Крылова, д. 36",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.040776,
                "longitude": 82.930329
            }
        },
        {
            "id": 28000003,
            "Biskvit_id": "6972",
            "shortName": "ДО «Охотный ряд-Прайм» Филиала № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, Охотный ряд, д. 1",
            "city": "Москва",
            "scheduleFl": "пн-чт: 09:00-18:00 пт: 09:00-16:45 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.757997,
                "longitude": 37.615901
            }
        },
        {
            "id": 22002036,
            "Biskvit_id": "1249",
            "shortName": "ОО «Меридиан» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, пр-т Ленина, д. 28",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.161563,
                "longitude": 61.424859
            }
        },
        {
            "id": 29000230,
            "Biskvit_id": "3925",
            "shortName": "ДО «На Янгеля» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Академика Янгеля, д. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.596457,
                "longitude": 37.599822
            }
        },
        {
            "id": 21008021,
            "Biskvit_id": "1516",
            "shortName": "ДО «Солнечный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Старый Оскол, мкр. Жукова, д. 25",
            "city": "Старый Оскол",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.310142,
                "longitude": 37.894442
            }
        },
        {
            "id": 25009024,
            "Biskvit_id": "1357",
            "shortName": "ОО «Пушкинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Пушкинская, д. 116",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.83456,
                "longitude": 53.21838
            }
        },
        {
            "id": 25014024,
            "Biskvit_id": "0248",
            "shortName": "ОО «Яр Чаллы» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Набережные Челны, пр-т Московский, д. 131",
            "city": "Набережные Челны",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.737882,
                "longitude": 52.419311
            }
        },
        {
            "id": 22005010,
            "Biskvit_id": "3015",
            "shortName": "ОО «Олимпийский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, ул. Привокзальная, д. 16/2",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.288683,
                "longitude": 73.331525
            }
        },
        {
            "id": 25007007,
            "Biskvit_id": "1752",
            "shortName": "ОО «Юбилейный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. Усть-Курдюмская, д. 5",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.570983,
                "longitude": 46.06771
            }
        },
        {
            "id": 24007040,
            "Biskvit_id": "2613",
            "shortName": "ОО «Тулунский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Тулун, ул. Ленина, д. 90, пом. 57",
            "city": "Тулун",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.562095,
                "longitude": 100.580347
            }
        },
        {
            "id": 21003006,
            "Biskvit_id": "1551",
            "shortName": "ОО «На Суздальском» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Владимир, пр-т Суздальский, д. 11а",
            "city": "Владимир",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.165885,
                "longitude": 40.46525
            }
        },
        {
            "id": 29000283,
            "Biskvit_id": "2027",
            "shortName": "ДО «Коломенский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Коломна, ул. Октябрьской революции, д. 350",
            "city": "Коломна",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.085172,
                "longitude": 38.797662
            }
        },
        {
            "id": 25013025,
            "Biskvit_id": "2242",
            "shortName": "ОО «Индустриальный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, шоссе Космонавтов, д.115",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.989699,
                "longitude": 56.197724
            }
        },
        {
            "id": 25013029,
            "Biskvit_id": "4042",
            "shortName": "ОО «Магистраль» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Генкеля, д.17",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.006512,
                "longitude": 56.181114
            }
        },
        {
            "id": 21011001,
            "Biskvit_id": "2951",
            "shortName": "ОО «Мещерский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, ул. Дзержинского, д. 60/2",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.620376,
                "longitude": 39.723538
            }
        },
        {
            "id": 24009035,
            "Biskvit_id": "3446",
            "shortName": "ОО «На Металлургов» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, пр-т Металлургов, д. 34",
            "city": "Красноярск",
            "scheduleFl": "пн-пт:10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.046846,
                "longitude": 92.946805
            }
        },
        {
            "id": 26000075,
            "Biskvit_id": "4336",
            "shortName": "ДО № 11 «Ленинский, 120» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Ленинский пр-т, д. 120, лит. А, пом.7-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.852339,
                "longitude": 30.258978
            }
        },
        {
            "id": 24009036,
            "Biskvit_id": "1846",
            "shortName": "ОО «Енисейский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Красной Армии, д. 12",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 56.013855,
                "longitude": 92.853353
            }
        },
        {
            "id": 24010003,
            "Biskvit_id": "2740",
            "shortName": "ДО «Гвардеец» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Амосова, д. 64",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.159774,
                "longitude": 82.961635
            }
        },
        {
            "id": 24005006,
            "Biskvit_id": "2624",
            "shortName": "ОО «Проспект Ленина» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, пр-т Ленина, д. 80а",
            "city": "Томск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.484004,
                "longitude": 84.948466
            }
        },
        {
            "id": 25008000,
            "Biskvit_id": "1053",
            "shortName": "РОО «Чебоксарский»",
            "address": "Чувашская Республика, г. Чебоксары, бул. Президентский, д. 27А",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.133738,
                "longitude": 47.243191
            }
        },
        {
            "id": 24004003,
            "Biskvit_id": "1271",
            "shortName": "ОО «Железнодорожный» в г. Улан-Удэ Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Революции 1905 года, д. 68",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.843757,
                "longitude": 107.581349
            }
        },
        {
            "id": 24004004,
            "Biskvit_id": "1571",
            "shortName": "ОО «На Бабушкина» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Бабушкина, д. 14А",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.813851,
                "longitude": 107.59397
            }
        },
        {
            "id": 22001000,
            "Biskvit_id": "1015",
            "shortName": "РОО «Тюменский»",
            "address": "г. Тюмень, ул. Советская, д. 54",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.156236,
                "longitude": 65.542386
            }
        },
        {
            "id": 24007042,
            "Biskvit_id": "2413",
            "shortName": "ОО «Усть-Кутский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Усть-Кут, ул. Калинина , д. 8",
            "city": "Усть-Кут",
            "scheduleFl": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.779249,
                "longitude": 105.746881
            }
        },
        {
            "id": 24001007,
            "Biskvit_id": "0624",
            "shortName": "ОО «Борзинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Борзинский район, г. Борзя, ул. Ленина, д. 31",
            "city": "Борзя",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.390058,
                "longitude": 116.527222
            }
        },
        {
            "id": 24007044,
            "Biskvit_id": "2513",
            "shortName": "ОО «Вихоревский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, Братский район, г. Вихоревка, ул. Дзержинского, д. 72",
            "city": "Вихоревка",
            "scheduleFl": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.121757,
                "longitude": 101.172579
            }
        },
        {
            "id": 29000254,
            "Biskvit_id": "5327",
            "shortName": "ДО «Ступинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Ступино, ул. Андропова, д. 56/30а",
            "city": "Ступино",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.887797,
                "longitude": 38.069703
            }
        },
        {
            "id": 22006013,
            "Biskvit_id": "2702",
            "shortName": "ДО «Лесной» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Лесной, пр-т Коммунистический, д. 23",
            "city": "Лесной",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.633897,
                "longitude": 59.790051
            }
        },
        {
            "id": 24009000,
            "Biskvit_id": "2046",
            "shortName": "РОО «Красноярский»",
            "address": "Красноярский край, г. Красноярск, ул. Ленина, д. 46",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.014323,
                "longitude": 92.879144
            }
        },
        {
            "id": 21006024,
            "Biskvit_id": "1745",
            "shortName": "ДО «На Ложевой» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Ложевая, д. 125А",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.203045,
                "longitude": 37.643686
            }
        },
        {
            "id": 29000208,
            "Biskvit_id": "1629",
            "shortName": "ДО «Воскресенский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Воскресенск, ул. Советская, д. 18-а",
            "city": "Воскресенск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.325032,
                "longitude": 38.682983
            }
        },
        {
            "id": 22002007,
            "Biskvit_id": "2302",
            "shortName": "ОО «Курганский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Курганская область, г. Курган, ул. Гоголя, д. 44",
            "city": "Курган",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.438624,
                "longitude": 65.339878
            }
        },
        {
            "id": 24009039,
            "Biskvit_id": "2246",
            "shortName": "ОО «Южный Берег» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, пр-т имени газеты Красноярский рабочий, д. 160И",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.997784,
                "longitude": 92.909354
            }
        },
        {
            "id": 29000182,
            "Biskvit_id": "3600",
            "shortName": "ДО ЦИК «Новослободский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Новослободская, д. 41",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.783392,
                "longitude": 37.596866
            }
        },
        {
            "id": 29000166,
            "Biskvit_id": "0100",
            "shortName": "ДО ЦИК «На Мясницкой» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Мясницкая, д. 35",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.766045,
                "longitude": 37.638081
            }
        },
        {
            "id": 29000167,
            "Biskvit_id": "0400",
            "shortName": "ДО «Тверской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Тверская, д. 6/1, стр. 7",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.760256,
                "longitude": 37.611446
            }
        },
        {
            "id": 29000130,
            "Biskvit_id": "0629",
            "shortName": "ДО «Черкизовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Б. Черкизовская, д. 5А",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.797306,
                "longitude": 37.718723
            }
        },
        {
            "id": 24009057,
            "Biskvit_id": "4246",
            "shortName": "ОО «Саянский» в пос. Саянском Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, пос. Саянский, ул. Комсомольская, д. 1Б",
            "city": "пос. Саянский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.549195,
                "longitude": 94.698035
            }
        },
        {
            "id": 25011005,
            "Biskvit_id": "1462",
            "shortName": "ОО «Стерлитамакский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Стерлитамак, ул. Коммунистическая, д.71",
            "city": "Стерлитамак",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.621997,
                "longitude": 55.908565
            }
        },
        {
            "id": 0,
            "Biskvit_id": "0086",
            "shortName": "ДОПЗП в г. Санкт-Петербурге",
            "address": "г. Санкт-Петербург, Дегтярный переулок, д. 11, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.939465,
                "longitude": 30.384751
            }
        },
        {
            "id": 21003003,
            "Biskvit_id": "2251",
            "shortName": "ОО «Ковровский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Ковров, пр-т Ленина, д. 42",
            "city": "Ковров",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.358592,
                "longitude": 41.312235
            }
        },
        {
            "id": 27007022,
            "Biskvit_id": "2556",
            "shortName": "ДО «Первостроителей» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Комсомольск-на-Амуре, пр-т Первостроителей, д. 18",
            "city": "Комсомольск-на-Амуре",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.538372,
                "longitude": 137.010993
            }
        },
        {
            "id": 27003003,
            "Biskvit_id": "1354",
            "shortName": "ОО «Вторая речка» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, ул. Русская, д. 39б",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.169305,
                "longitude": 131.921687
            }
        },
        {
            "id": 24010026,
            "Biskvit_id": "3040",
            "shortName": "ДО «На Маркса» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Ватутина, д. 21/1",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.984879,
                "longitude": 82.894064
            }
        },
        {
            "id": 29000165,
            "Biskvit_id": "1030",
            "shortName": "ДО «Щелковское шоссе, 69» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Щелковское шоссе, д. 69",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.810638,
                "longitude": 37.794864
            }
        },
        {
            "id": 24010027,
            "Biskvit_id": "4440",
            "shortName": "ДО «Николаевский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, Красный пр-т, д. 16",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.020559,
                "longitude": 82.924562
            }
        },
        {
            "id": 29000181,
            "Biskvit_id": "3400",
            "shortName": "ДО «Русаковский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Сокольническая пл., д.4, корп.1-2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.789922,
                "longitude": 37.677894
            }
        },
        {
            "id": 24005007,
            "Biskvit_id": "3140",
            "shortName": "ОО «На Кирова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, пр-т Комсомольский д. 70",
            "city": "Томск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.466365,
                "longitude": 84.982557
            }
        },
        {
            "id": 26000063,
            "Biskvit_id": "2236",
            "shortName": "ДО № 51 «Каменноостровский, 24» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Каменноостровский пр-т, д. 24, лит. А, пом. 1-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.961688,
                "longitude": 30.314979
            }
        },
        {
            "id": 25014021,
            "Biskvit_id": "2264",
            "shortName": "ОО «Центральный» в г. Набережные Челны Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Набережные Челны, ул. Хасана Туфана, д. 29А",
            "city": "Набережные Челны",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.742164,
                "longitude": 52.393404
            }
        },
        {
            "id": 24005000,
            "Biskvit_id": "1440",
            "shortName": "РОО «Томский»",
            "address": "Томская область, г. Томск, пр-т Ленина, д. 26",
            "city": "Томск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.461889,
                "longitude": 84.950416
            }
        },
        {
            "id": 25011018,
            "Biskvit_id": "3562",
            "shortName": "ОО «На Бессонова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Бессонова, д. 2",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.740272,
                "longitude": 55.991722
            }
        },
        {
            "id": 24006032,
            "Biskvit_id": "2524",
            "shortName": "ОО «Купеческий» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, Центральный район, г. Новокузнецк, ул. Кирова, д. 97",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.75783,
                "longitude": 87.159786
            }
        },
        {
            "id": 24007048,
            "Biskvit_id": "4524",
            "shortName": "ОО «Саянский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Саянск, мкр. Олимпийский, д. 28",
            "city": "Саянск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.112436,
                "longitude": 102.182079
            }
        },
        {
            "id": 24001015,
            "Biskvit_id": "0924",
            "shortName": "ОО «Хилокский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, Хилокский район, г. Хилок, ул. Дзержинского, 11, помещение 2",
            "city": "Хилок",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.362147,
                "longitude": 110.459048
            }
        },
        {
            "id": 21011000,
            "Biskvit_id": "1251",
            "shortName": "РОО «Рязанский»",
            "address": "Рязанская область, г. Рязань, ул. Почтовая, д. 60а",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.629497,
                "longitude": 39.739124
            }
        },
        {
            "id": 21016010,
            "Biskvit_id": "0151",
            "shortName": "ДО «Северный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, ул. Владимира Невского, д. № 13",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.707055,
                "longitude": 39.146882
            }
        },
        {
            "id": 24009040,
            "Biskvit_id": "2446",
            "shortName": "ОО «Октябрьский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Высотная, д. 2",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.024788,
                "longitude": 92.784515
            }
        },
        {
            "id": 24002006,
            "Biskvit_id": "1214",
            "shortName": "ОО «Северо-Западный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, пр-т Ленина, д. 151",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.371091,
                "longitude": 83.750976
            }
        },
        {
            "id": 24002013,
            "Biskvit_id": "1714",
            "shortName": "ОО «Васильевский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Бийск, ул. Васильева, д. 57а",
            "city": "Бийск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.509529,
                "longitude": 85.147245
            }
        },
        {
            "id": 25010008,
            "Biskvit_id": "2561",
            "shortName": "ОО «Проспект Победы» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, пр-т Победы, д. 14",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.775455,
                "longitude": 55.108355
            }
        },
        {
            "id": 24002000,
            "Biskvit_id": "1014",
            "shortName": "РОО «Барнаульский»",
            "address": "Алтайский край, г. Барнаул, ул. Малахова, д. 88в",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.354966,
                "longitude": 83.697221
            }
        },
        {
            "id": 22001155,
            "Biskvit_id": "3363",
            "shortName": "ОО «Голышмановский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "п.г.т. Голышманово, ул.Садовая, 79",
            "city": "п. Голышманово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.394735,
                "longitude": 68.377136
            }
        },
        {
            "id": 21001000,
            "Biskvit_id": "0651",
            "shortName": "РОО «Калужский»",
            "address": "Калужская область, г Калуга, ул. Герцена, д. 37",
            "city": "Калуга",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.515413,
                "longitude": 36.254091
            }
        },
        {
            "id": 21016011,
            "Biskvit_id": "0351",
            "shortName": "ДО «Левобережный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, ул. Остужева, д. 6",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.68559,
                "longitude": 39.260528
            }
        },
        {
            "id": 29000930,
            "Biskvit_id": "2097",
            "shortName": "ДО «РЭУ им. Г. В. Плеханова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Стремянный пер., д. 36",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.727334,
                "longitude": 37.627813
            }
        },
        {
            "id": 21016019,
            "Biskvit_id": "5489",
            "shortName": "ДО «На Кольцовской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, ул. Кольцовская, д. 31",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.668467,
                "longitude": 39.193083
            }
        },
        {
            "id": 29000263,
            "Biskvit_id": "0729",
            "shortName": "ДО «Чеховский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Чехов, ул. Советская площадь, д. 5",
            "city": "Чехов",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.14235,
                "longitude": 37.454357
            }
        },
        {
            "id": 27002011,
            "Biskvit_id": "3456",
            "shortName": "ОО «Тындинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Тында, ул. Привокзальная, д. 1",
            "city": "Тында",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 09:00-14:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.139967,
                "longitude": 124.740105
            }
        },
        {
            "id": 21006030,
            "Biskvit_id": "1345",
            "shortName": "ОО «Суворов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Суворов, ул. Тульская, д. 17",
            "city": "Суворов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.116447,
                "longitude": 36.508045
            }
        },
        {
            "id": 22006038,
            "Biskvit_id": "3102",
            "shortName": "ДО «Пионерский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Сулимова, д. 23, помещения № № 10-18, 20, 42, 84",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.838011,
                "longitude": 60.597474
            }
        },
        {
            "id": 25014037,
            "Biskvit_id": "2364",
            "shortName": "ОО «Савиново» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, пр-т Ямашева, д. 76",
            "city": "Казань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.827606,
                "longitude": 49.137397
            }
        },
        {
            "id": 22006032,
            "Biskvit_id": "2922",
            "shortName": "ДО «Качканарский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Качканар, ул. Свердлова, д. 4",
            "city": "Качканар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.705311,
                "longitude": 59.487687
            }
        },
        {
            "id": 25015002,
            "Biskvit_id": "3618",
            "shortName": "ДО «Кинельский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Кинель, ул. Маяковского, д.84-а",
            "city": "Кинель",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.218249,
                "longitude": 50.64707
            }
        },
        {
            "id": 21006102,
            "Biskvit_id": "3145",
            "shortName": "ОО «Новомосковский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Новомосковск, ул. Комсомольская/ Октябрьская, д. 34/25",
            "city": "Новомосковск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.010665,
                "longitude": 38.289907
            }
        },
        {
            "id": 41022004,
            "Biskvit_id": "1526",
            "shortName": "ОО «Кондопожский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Кондопога, пр-т Калинина, д. 4",
            "city": "Кондопога",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.204091,
                "longitude": 34.259311
            }
        },
        {
            "id": 23006023,
            "Biskvit_id": "4205",
            "shortName": "ОО «Каменск-Шахтинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Каменск-Шахтинский, пер. Строителей, д. 22",
            "city": "Каменск-Шахтинский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.146326,
                "longitude": 40.181715
            }
        },
        {
            "id": 23001001,
            "Biskvit_id": "1408",
            "shortName": "ОО «Камышинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Камышин, ул. Пролетарская, д. 18а",
            "city": "Камышин",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.082692,
                "longitude": 45.405822
            }
        },
        {
            "id": 24003009,
            "Biskvit_id": "2043",
            "shortName": "ОО «Входной» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, мкр. Входной, д. 3",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.950257,
                "longitude": 73.169972
            }
        },
        {
            "id": 21007001,
            "Biskvit_id": "2851",
            "shortName": "ОО «На Неделина» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Липецк, ул. Неделина, д. 61",
            "city": "Липецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.601202,
                "longitude": 39.575154
            }
        },
        {
            "id": 24007035,
            "Biskvit_id": "1411",
            "shortName": "ОО «Черемховский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Черемхово, ул. Некрасова, д. 2",
            "city": "Черемхово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.14126,
                "longitude": 103.084491
            }
        },
        {
            "id": 24003000,
            "Biskvit_id": "1043",
            "shortName": "РОО «Омский»",
            "address": "Омская область, г. Омск, ул. Маяковского угол Маршала Жукова, д. 37/101, кор. 1",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.97145,
                "longitude": 73.391541
            }
        },
        {
            "id": 41018000,
            "Biskvit_id": "0594",
            "shortName": "РОО «Калининградский»",
            "address": "Калининградская область, г. Калининград, ул. Больничная, д. 5",
            "city": "Калининград",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.713912,
                "longitude": 20.503849
            }
        },
        {
            "id": 25014025,
            "Biskvit_id": "0348",
            "shortName": "ОО «На Бумажников» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Набережные Челны, пр-т Набержночелнинский, д. 7",
            "city": "Набережные Челны",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.703429,
                "longitude": 52.333675
            }
        },
        {
            "id": 27003009,
            "Biskvit_id": "1454",
            "shortName": "ОО «Уссурийский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Уссурийск, ул. Некрасова, д. 22",
            "city": "Уссурийск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.789054,
                "longitude": 131.953954
            }
        },
        {
            "id": 27003011,
            "Biskvit_id": "1254",
            "shortName": "ОО «Портовый» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Находка, ул. Гагарина, д. 12",
            "city": "Находка",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 42.791925,
                "longitude": 132.864612
            }
        },
        {
            "id": 29000129,
            "Biskvit_id": "0429",
            "shortName": "ДО «Хамовнический» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. 3-Я Фрунзенская, д. 9",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.72124,
                "longitude": 37.576825
            }
        },
        {
            "id": 28000000,
            "Biskvit_id": "0072",
            "shortName": "Филиал № 7777 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Полянка, д. 10, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:30-20:00 сб: 09:30-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 1
            },
            "coordinates": {
                "latitude": 55.740325,
                "longitude": 37.615955
            }
        },
        {
            "id": 29000003,
            "Biskvit_id": "3203",
            "shortName": "ДО «Наро-Фоминск» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Наро-Фоминск, ул. Площадь Свободы, д. 2, корп. 1, пом. 4",
            "city": "Наро-Фоминск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.388087,
                "longitude": 36.735112
            }
        },
        {
            "id": 29000049,
            "Biskvit_id": "0310",
            "shortName": "ДО «ЦМТ» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Краснопресненская набережная, д. 12",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.754203,
                "longitude": 37.556388
            }
        },
        {
            "id": 29000132,
            "Biskvit_id": "1529",
            "shortName": "ДО «Аэропорт Внуково» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Рейсовая 2-я, д. 2, корп. 5",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.605226,
                "longitude": 37.286346
            }
        },
        {
            "id": 29000290,
            "Biskvit_id": "3027",
            "shortName": "ДО «Никитский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Большая Никитская, д. 33, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.75709,
                "longitude": 37.595618
            }
        },
        {
            "id": 25003006,
            "Biskvit_id": "1718",
            "shortName": "ДО «Кирово-Чепецкий» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Кировская область, г. Кирово-Чепецк, пр-т Россия, д. 32",
            "city": "Кирово-Чепецк",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.544983,
                "longitude": 50.043815
            }
        },
        {
            "id": 24010031,
            "Biskvit_id": "3340",
            "shortName": "ДО «Площадь Гарина-Михайловского» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Ленина, д. 86",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.036623,
                "longitude": 82.898816
            }
        },
        {
            "id": 41023003,
            "Biskvit_id": "2006",
            "shortName": "ОО «На Советской» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Псковская область, г. Псков, ул. Советская, д. 40",
            "city": "Псков",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.814322,
                "longitude": 28.335927
            }
        },
        {
            "id": 23008021,
            "Biskvit_id": "0855",
            "shortName": "ДО «Южный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Новороссийск, пр-кт Дзержинского, д. 205-б",
            "city": "Новороссийск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.686511,
                "longitude": 37.77935
            }
        },
        {
            "id": 21013016,
            "Biskvit_id": "2351",
            "shortName": "ДО «Железногорский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Железногорск, ул. Ленина, д. 64",
            "city": "Железногорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.350339,
                "longitude": 35.346919
            }
        },
        {
            "id": 41018005,
            "Biskvit_id": "1438",
            "shortName": "ОО «Европа» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Калининград, ул. Театральная, д. 30",
            "city": "Калининград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.718057,
                "longitude": 20.500103
            }
        },
        {
            "id": 29000116,
            "Biskvit_id": "4227",
            "shortName": "ДО «Проспект Мира» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, пр-т Мира, д.41, стр.2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.781615,
                "longitude": 37.632637
            }
        },
        {
            "id": 25013024,
            "Biskvit_id": "2142",
            "shortName": "ОО «Первый» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, Комсомольский пр-т, д. 70",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.996349,
                "longitude": 56.25368
            }
        },
        {
            "id": 23006039,
            "Biskvit_id": "2105",
            "shortName": "ОО «Северный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т Космонавтов, д. 23Б",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.291561,
                "longitude": 39.713423
            }
        },
        {
            "id": 29000168,
            "Biskvit_id": "0500",
            "shortName": "ДО «Неглинный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Неглинная ул., д. 14, стр. 1А",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.764273,
                "longitude": 37.620393
            }
        },
        {
            "id": 24007028,
            "Biskvit_id": "2711",
            "shortName": "ОО «Спутник» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Розы Люксембург, д. 243",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.352555,
                "longitude": 104.167356
            }
        },
        {
            "id": 29000014,
            "Biskvit_id": "0127",
            "shortName": "ДО «Академический» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Дмитрия Ульянова, д. 24",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.686005,
                "longitude": 37.575828
            }
        },
        {
            "id": 29000038,
            "Biskvit_id": "2210",
            "shortName": "ДО «Видновский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Видное, просп. Ленинского Комсомола, д.17 корп.2",
            "city": "Видное",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.545263,
                "longitude": 37.708141
            }
        },
        {
            "id": 29000032,
            "Biskvit_id": "5629",
            "shortName": "ДО «Ивантеевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Ивантеевка, ул. Дзержинского, д. 11а",
            "city": "Ивантеевка",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.973254,
                "longitude": 37.909462
            }
        },
        {
            "id": 25014035,
            "Biskvit_id": "1464",
            "shortName": "ОО «Идель» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Чистопольская, д. 5",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.819464,
                "longitude": 49.101689
            }
        },
        {
            "id": 24007033,
            "Biskvit_id": "2724",
            "shortName": "ОО «Авиационный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Новаторов, д. 3А",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.351846,
                "longitude": 104.20849
            }
        },
        {
            "id": 25005002,
            "Biskvit_id": "1831",
            "shortName": "ОО «На Тюленева» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Ульяновская область, г. Ульяновск, пр-т Генерала Тюленева, д. 2А",
            "city": "Ульяновск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.374197,
                "longitude": 48.597914
            }
        },
        {
            "id": 25014040,
            "Biskvit_id": "2864",
            "shortName": "ОО «На Декабристов» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Декабристов, д. 185/47",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.832257,
                "longitude": 49.079698
            }
        },
        {
            "id": 25005000,
            "Biskvit_id": "1031",
            "shortName": "РОО «Ульяновский»",
            "address": "Ульяновская область, г. Ульяновск, ул. Гончарова, д. 33/2",
            "city": "Ульяновск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.32167,
                "longitude": 48.401048
            }
        },
        {
            "id": 24006047,
            "Biskvit_id": "4007",
            "shortName": "ОО «Белово» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Белово, ул. Юбилейная, д. 5",
            "city": "Белово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.411138,
                "longitude": 86.310941
            }
        },
        {
            "id": 23001000,
            "Biskvit_id": "1008",
            "shortName": "РОО «Волгоградский»",
            "address": "Волгоградская область, г. Волгоград, ул. Краснознаменская, д. 5А",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.702792,
                "longitude": 44.511558
            }
        },
        {
            "id": 23008024,
            "Biskvit_id": "0755",
            "shortName": "ДО «Черемушки» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. Северная, д. 324",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.040534,
                "longitude": 38.970103
            }
        },
        {
            "id": 41017005,
            "Biskvit_id": "1639",
            "shortName": "ОО «На Воскресенской» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Архангельск, ул. Воскресенская, д. 118",
            "city": "Архангельск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.549413,
                "longitude": 40.569904
            }
        },
        {
            "id": 41018007,
            "Biskvit_id": "1738",
            "shortName": "ОО «Балтийский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Балтийск, пр-т Ленина, д. 61",
            "city": "Балтийск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.653683,
                "longitude": 19.909937
            }
        },
        {
            "id": 23006024,
            "Biskvit_id": "4105",
            "shortName": "ОО «Батайский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Батайск, ул. Кирова, д. 30/11",
            "city": "Батайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.138064,
                "longitude": 39.748286
            }
        },
        {
            "id": 24009241,
            "Biskvit_id": "3743",
            "shortName": "ДО «Черногорский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Хакасия, г. Черногорск, ул. Юбилейная, д. 16",
            "city": "Черногорск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.826673,
                "longitude": 91.329855
            }
        },
        {
            "id": 41017004,
            "Biskvit_id": "1139",
            "shortName": "ОО «На Троицком» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Архангельск, пр-т Троицкий, д. 81",
            "city": "Архангельск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.548242,
                "longitude": 40.518053
            }
        },
        {
            "id": 25014039,
            "Biskvit_id": "2664",
            "shortName": "ОО «Караваево» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Максимова, д. 3",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.860125,
                "longitude": 49.095877
            }
        },
        {
            "id": 41022007,
            "Biskvit_id": "1565",
            "shortName": "ОО «Кемский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Кемь, пр-т Пролетарский, д. 59",
            "city": "Кемь",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.954329,
                "longitude": 34.584177
            }
        },
        {
            "id": 25009026,
            "Biskvit_id": "1757",
            "shortName": "ОО «Строительный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Клубная, д. 76/8",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.829034,
                "longitude": 53.130588
            }
        },
        {
            "id": 25009028,
            "Biskvit_id": "2457",
            "shortName": "ОО «На Гагарина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Гагарина, д. 25",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.803564,
                "longitude": 53.186957
            }
        },
        {
            "id": 25002002,
            "Biskvit_id": "1109",
            "shortName": "ОО «Пролетарский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Марий Эл, г. Йошкар-Ола, ул. Комсомольская, д. 88",
            "city": "Йошкар-Ола",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.644891,
                "longitude": 47.898548
            }
        },
        {
            "id": 25002003,
            "Biskvit_id": "1309",
            "shortName": "ОО «Машиностроитель» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Марий Эл, г. Йошкар-Ола, ул. Суворова, д. 15",
            "city": "Йошкар-Ола",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.633897,
                "longitude": 47.866829
            }
        },
        {
            "id": 25009025,
            "Biskvit_id": "1457",
            "shortName": "ОО «Ворошиловский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Ворошилова, д. 29",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.877223,
                "longitude": 53.266782
            }
        },
        {
            "id": 27002000,
            "Biskvit_id": "0956",
            "shortName": "РОО «Благовещенский»",
            "address": "Амурская область, г. Благовещенск, ул. Красноармейская, 123",
            "city": "Благовещенск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.268749,
                "longitude": 127.539202
            }
        },
        {
            "id": 21014003,
            "Biskvit_id": "3141",
            "shortName": "ОО «Буйский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Костромская область, г. Буй, ул. 10 Годовщины Октября, д. 52",
            "city": "Буй",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.46201,
                "longitude": 41.557439
            }
        },
        {
            "id": 23001002,
            "Biskvit_id": "3008",
            "shortName": "ОО «Волго-Донской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, пр-т им. Героев Сталинграда, 32",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.515716,
                "longitude": 44.55854
            }
        },
        {
            "id": 25002005,
            "Biskvit_id": "1418",
            "shortName": "ОО «Волжский» в г. Волжске Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Марий Эл, г. Волжск, ул. Ленина, д. 52б",
            "city": "Волжск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.864439,
                "longitude": 48.364136
            }
        },
        {
            "id": 41020001,
            "Biskvit_id": "1404",
            "shortName": "ОО «Воркутинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Воркута, ул. Ленина, д. 38",
            "city": "Воркута",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.496078,
                "longitude": 64.058243
            }
        },
        {
            "id": 25009030,
            "Biskvit_id": "2057",
            "shortName": "ОО «Воткинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Воткинск, ул. Мира, д. 5",
            "city": "Воткинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.0549,
                "longitude": 53.987617
            }
        },
        {
            "id": 29000302,
            "Biskvit_id": "5610",
            "shortName": "ДО «Проспект Пацаева» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Долгопрудный, пр-т Пацаева, д. 9",
            "city": "Долгопрудный",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.947812,
                "longitude": 37.499381
            }
        },
        {
            "id": 21006021,
            "Biskvit_id": "2045",
            "shortName": "ОО «Донской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Донской, мкр. Центральный, ул. Октябрьская, д. 44",
            "city": "Донской",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.968108,
                "longitude": 38.320235
            }
        },
        {
            "id": 41017001,
            "Biskvit_id": "2139",
            "shortName": "ОО «Ненецкий» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ненецкий автономный округ, г. Нарьян-Мар, ул. Ленина, д. 21А",
            "city": "Нарьян-Мар",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.63714,
                "longitude": 53.000745
            }
        },
        {
            "id": 22002014,
            "Biskvit_id": "3022",
            "shortName": "ОО «Озерский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Озерск, ул. Карла Маркса, д. 4б",
            "city": "Озерск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.753022,
                "longitude": 60.685222
            }
        },
        {
            "id": 25013011,
            "Biskvit_id": "3242",
            "shortName": "ОО «Прикамский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Вильямса, д. 39б",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.106295,
                "longitude": 56.304004
            }
        },
        {
            "id": 41019002,
            "Biskvit_id": "3836",
            "shortName": "ОО «Оленегорский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Оленегорск, ул. Мурманская, д. 1",
            "city": "Оленегорск",
            "scheduleFl": "пн: выходной вт-пт: 10:00-18:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 68.138515,
                "longitude": 33.272412
            }
        },
        {
            "id": 21015001,
            "Biskvit_id": "1541",
            "shortName": "ОО «Северный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Орловская область, г. Орел, Московское шоссе, д. 126",
            "city": "Орел",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.001152,
                "longitude": 36.140643
            }
        },
        {
            "id": 21015041,
            "Biskvit_id": "3516",
            "shortName": "ОО «Ливенский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Орловская область г. Ливны ул. Ленина, д. 20 б",
            "city": "Ливны",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.423732,
                "longitude": 37.608311
            }
        },
        {
            "id": 25006021,
            "Biskvit_id": "2350",
            "shortName": "ОО «Мещерский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, Канавинский район, бульвар Мещерский, д. 7, корп. 3, пом. П. 18",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.338364,
                "longitude": 43.934103
            }
        },
        {
            "id": 22006007,
            "Biskvit_id": "1522",
            "shortName": "ДО «На Вагонке» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Нижний Тагил, ул. Ильича, д. 1",
            "city": "Нижний Тагил",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.92602,
                "longitude": 60.100661
            }
        },
        {
            "id": 22006008,
            "Biskvit_id": "1022",
            "shortName": "ДО «Демидовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Нижний Тагил, пр-т Строителей д. 29",
            "city": "Нижний Тагил",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.908882,
                "longitude": 59.989162
            }
        },
        {
            "id": 24002001,
            "Biskvit_id": "1614",
            "shortName": "ОО «Новоалтайский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Новоалтайск, ул. Октябрьская, д. 14",
            "city": "Новоалтайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.390186,
                "longitude": 83.935077
            }
        },
        {
            "id": 24006029,
            "Biskvit_id": "2207",
            "shortName": "ОО «Проспект Металлургов» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, Центральный район, пр-т Металлургов, д. 25",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.754918,
                "longitude": 87.117044
            }
        },
        {
            "id": 41022005,
            "Biskvit_id": "1265",
            "shortName": "ОО «Костомукшский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Костомукша, ул. Героев, д. 2",
            "city": "Костомукша",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.588582,
                "longitude": 30.591974
            }
        },
        {
            "id": 25013013,
            "Biskvit_id": "2342",
            "shortName": "ОО «Краснокамский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Краснокамск, пр-т Комсомольский, д. 12",
            "city": "Краснокамск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.081945,
                "longitude": 55.752204
            }
        },
        {
            "id": 25012004,
            "Biskvit_id": "1118",
            "shortName": "ОО «Центральный» в г. Кузнецке Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Кузнецк, ул. Кирова, д. 95",
            "city": "Кузнецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.121799,
                "longitude": 46.591814
            }
        },
        {
            "id": 21013004,
            "Biskvit_id": "1041",
            "shortName": "ОО «На Гайдара» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курчатов, ул. Гайдара, д. 6",
            "city": "Курчатов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.660898,
                "longitude": 35.658904
            }
        },
        {
            "id": 23002001,
            "Biskvit_id": "1120",
            "shortName": "ОО «Жилгородок» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Астраханская область, г. Астрахань, ул. Б.Хмельницкого, д. 22",
            "city": "Астрахань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.335121,
                "longitude": 48.01744
            }
        },
        {
            "id": 23002004,
            "Biskvit_id": "1720",
            "shortName": "ОО «Аркадия» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Астраханская область, г. Астрахань, пл. Вокзальная , д. 6",
            "city": "Астрахань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.35812,
                "longitude": 48.0526
            }
        },
        {
            "id": 21008027,
            "Biskvit_id": "2016",
            "shortName": "ОО «Локомотивный» в г. Белгороде Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, ул. Белгородского полка, д. 23",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.59204,
                "longitude": 36.599853
            }
        },
        {
            "id": 21005002,
            "Biskvit_id": "1544",
            "shortName": "ОО «Рославльский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Рославль, ул. Ленина, д. 5",
            "city": "Рославль",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.947129,
                "longitude": 32.859789
            }
        },
        {
            "id": 23006031,
            "Biskvit_id": "3305",
            "shortName": "ОО «Сельмаш» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Селиванова, д. 64/112",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.250314,
                "longitude": 39.767906
            }
        },
        {
            "id": 41022008,
            "Biskvit_id": "1765",
            "shortName": "ОО «Сегежский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Сегежа, ул. Мира, д. 14",
            "city": "Сегежа",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.743565,
                "longitude": 34.314233
            }
        },
        {
            "id": 23008034,
            "Biskvit_id": "3255",
            "shortName": "ДО «Курортный проспект» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Сочи, Хостинский р-н, ул. Курортный пр-т, д. 73",
            "city": "Сочи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.572248,
                "longitude": 39.734551
            }
        },
        {
            "id": 22002023,
            "Biskvit_id": "3122",
            "shortName": "ОО «Трехгорный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Трехгорный, ул. Мира д. 12",
            "city": "Трехгорный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.814989,
                "longitude": 58.447402
            }
        },
        {
            "id": 22002061,
            "Biskvit_id": "5022",
            "shortName": "ОО «Троицкий» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Троицк, ул. Гагарина, д. 82",
            "city": "Троицк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.085023,
                "longitude": 61.547883
            }
        },
        {
            "id": 41020002,
            "Biskvit_id": "1304",
            "shortName": "ОО «Ухтинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Ухта, пр-т Ленина, д. 37/1",
            "city": "Ухта",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.566138,
                "longitude": 53.66681
            }
        },
        {
            "id": 27007030,
            "Biskvit_id": "2223",
            "shortName": "ДО «Индустриальный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Морозова Павла Леонтьевича, д. 91",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.435733,
                "longitude": 135.104948
            }
        },
        {
            "id": 27007031,
            "Biskvit_id": "2623",
            "shortName": "ДО «Южный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Суворова, д. 42",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.391982,
                "longitude": 135.109853
            }
        },
        {
            "id": 22002020,
            "Biskvit_id": "3722",
            "shortName": "ОО «Чебаркульский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Чебаркульский, ул. Октябрьская, д. 9/2",
            "city": "Чебаркуль",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.446204,
                "longitude": 60.39565
            }
        },
        {
            "id": 25008006,
            "Biskvit_id": "1653",
            "shortName": "ОО «Элара» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Чебоксары, пр-т Московский, д. 40",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.143559,
                "longitude": 47.204447
            }
        },
        {
            "id": 21012003,
            "Biskvit_id": "0621",
            "shortName": "ОО «Бологовский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Бологое, ул. Кирова, д. 5",
            "city": "Бологое",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.885402,
                "longitude": 34.05171
            }
        },
        {
            "id": 21009005,
            "Biskvit_id": "1366",
            "shortName": "ОО «На Крахмалева» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Брянск, ул. Крахмалева, д. 47",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.262385,
                "longitude": 34.343662
            }
        },
        {
            "id": 41021003,
            "Biskvit_id": "2836",
            "shortName": "ОО «Большая Санкт-Петербургская, 4» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Новгородская область, г. Великий Новгород, ул. Большая Санкт-Петербургская, д. 4",
            "city": "Великий Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.526339,
                "longitude": 31.273957
            }
        },
        {
            "id": 23001005,
            "Biskvit_id": "1508",
            "shortName": "ОО «Советский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Туркменская, д. 12",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.678604,
                "longitude": 44.473892
            }
        },
        {
            "id": 22002018,
            "Biskvit_id": "2949",
            "shortName": "ОО «Копейский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Копейск, пр-т Победы, д. 27А",
            "city": "Копейск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.116892,
                "longitude": 61.60242
            }
        },
        {
            "id": 29000028,
            "Biskvit_id": "4529",
            "shortName": "ДО «Железнодорожный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Железнодорожный, ул. Пролетарская, д. 2, пом. 1 (№1-13)",
            "city": "Железнодорожный",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.749993,
                "longitude": 38.007585
            }
        },
        {
            "id": 22002016,
            "Biskvit_id": "1649",
            "shortName": "ОО «Аносовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Златоуст, ул. Аносова, д. 186",
            "city": "Златоуст",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.200241,
                "longitude": 59.720306
            }
        },
        {
            "id": 21002001,
            "Biskvit_id": "1641",
            "shortName": "ОО «На Энгельса» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ивановская область, г. Иваново, пр-т Шереметевский, д. 151",
            "city": "Иваново",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.01417,
                "longitude": 40.984979
            }
        },
        {
            "id": 25009022,
            "Biskvit_id": "2357",
            "shortName": "ОО «Удмуртия» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Пушкинская, д. 367",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.872752,
                "longitude": 53.207349
            }
        },
        {
            "id": 25002001,
            "Biskvit_id": "1209",
            "shortName": "ОО «Царевококшайский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Марий Эл, г. Йошкар-Ола, ул. Советская, д. 141",
            "city": "Йошкар-Ола",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.633748,
                "longitude": 47.896922
            }
        },
        {
            "id": 25014036,
            "Biskvit_id": "1128",
            "shortName": "ОО «Юдинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Лейтенанта Красикова, д. 6",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.819853,
                "longitude": 48.897116
            }
        },
        {
            "id": 21001002,
            "Biskvit_id": "1741",
            "shortName": "ОО «На Ленина, 64» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Калужская область, г. Калуга, ул. Ленина, 64",
            "city": "Калуга",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.518774,
                "longitude": 36.266964
            }
        },
        {
            "id": 23001008,
            "Biskvit_id": "2008",
            "shortName": "ОО «Краснооктябрьский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. им. Генерала Штеменко, д. 33",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.774776,
                "longitude": 44.556555
            }
        },
        {
            "id": 23001014,
            "Biskvit_id": "1908",
            "shortName": "ОО «Спутник» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волжский, пр-т Ленина, д. 75",
            "city": "Волжский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.790537,
                "longitude": 44.750375
            }
        },
        {
            "id": 29000205,
            "Biskvit_id": "1210",
            "shortName": "ДО «Дубна» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Дубна, пр-т Боголюбова, д. 25, пом.1",
            "city": "Дубна",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.733812,
                "longitude": 37.155524
            }
        },
        {
            "id": 23008023,
            "Biskvit_id": "3455",
            "shortName": "ДО «Ейский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Ейск, ул. Карла Либкнехта, д. 58",
            "city": "Ейск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.707971,
                "longitude": 38.276558
            }
        },
        {
            "id": 21005004,
            "Biskvit_id": "1344",
            "shortName": "ОО «Вяземский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Вязьма, пл. Советская, д. 2",
            "city": "Вязьма",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.211178,
                "longitude": 34.28423
            }
        },
        {
            "id": 41018009,
            "Biskvit_id": "1838",
            "shortName": "ОО «Гусевский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Гусев, ул. Зои Космодемьянской, д. 2",
            "city": "Гусев",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.590411,
                "longitude": 22.199006
            }
        },
        {
            "id": 25005005,
            "Biskvit_id": "2031",
            "shortName": "ОО «Соцгород» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Ульяновская область, г. Димитровград, пр-т Ленина, д. 20",
            "city": "Димитровград",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.230785,
                "longitude": 49.554826
            }
        },
        {
            "id": 21003007,
            "Biskvit_id": "2441",
            "shortName": "ОО «Октябрьский проспект» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Владимир, пр-т Октябрьский, д. 47",
            "city": "Владимир",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.142295,
                "longitude": 40.388534
            }
        },
        {
            "id": 23001004,
            "Biskvit_id": "1308",
            "shortName": "ОО «Красноармейский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, бульвар имени Энгельса, д. 25",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.514648,
                "longitude": 44.543952
            }
        },
        {
            "id": 29000144,
            "Biskvit_id": "3229",
            "shortName": "ДО «Войковский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградское шоссе, д. 16А, стр. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.821578,
                "longitude": 37.498725
            }
        },
        {
            "id": 29000147,
            "Biskvit_id": "3529",
            "shortName": "ДО «Юго-Западный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, просп. Вернадского, д. 105, корп. 3",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.663811,
                "longitude": 37.484864
            }
        },
        {
            "id": 21013011,
            "Biskvit_id": "1651",
            "shortName": "ОО «Дзержинского, 67» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курск, ул. Дзержинского, д. 67",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.723087,
                "longitude": 36.173405
            }
        },
        {
            "id": 21007003,
            "Biskvit_id": "4441",
            "shortName": "ОО «На Катукова» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Липецк, ул. Катукова, д. 23а",
            "city": "Липецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.58415,
                "longitude": 39.522459
            }
        },
        {
            "id": 22005006,
            "Biskvit_id": "3522",
            "shortName": "ОО «Мегионский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Мегион, ул. Нефтянников, д. 4",
            "city": "Мегион",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.036367,
                "longitude": 76.109205
            }
        },
        {
            "id": 21013013,
            "Biskvit_id": "4641",
            "shortName": "ОО «Энтузиастов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Курск, пр-т Энтузиастов, д. 1а",
            "city": "Курск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.738309,
                "longitude": 36.136996
            }
        },
        {
            "id": 29000149,
            "Biskvit_id": "3929",
            "shortName": "ДО «Каширский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Каширское шоссе, д. 26, корп. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.653517,
                "longitude": 37.648178
            }
        },
        {
            "id": 29000150,
            "Biskvit_id": "4029",
            "shortName": "ДО «Молодежный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ярцевская, д. 32",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.741287,
                "longitude": 37.417688
            }
        },
        {
            "id": 29000154,
            "Biskvit_id": "4829",
            "shortName": "ДО «На Андропова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, просп. Андропова, д. 30",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.679138,
                "longitude": 37.662434
            }
        },
        {
            "id": 29000157,
            "Biskvit_id": "5129",
            "shortName": "ДО «Мичуринский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Мичуринский пр-т, д. 34",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.69834,
                "longitude": 37.498025
            }
        },
        {
            "id": 29000117,
            "Biskvit_id": "4627",
            "shortName": "ДО «Рязанский проспект» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Академика Скрябина, д. 1/58, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.715728,
                "longitude": 37.797685
            }
        },
        {
            "id": 29000122,
            "Biskvit_id": "5227",
            "shortName": "ДО «Солнцево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Богданова, д. 50",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.650632,
                "longitude": 37.394449
            }
        },
        {
            "id": 29000196,
            "Biskvit_id": "4303",
            "shortName": "ДО «Шуваловский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Мичуринский пр-т, д. 7",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.702729,
                "longitude": 37.509703
            }
        },
        {
            "id": 29000041,
            "Biskvit_id": "4703",
            "shortName": "ДО «Кедровый» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Профсоюзная, д. 12",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.685437,
                "longitude": 37.570123
            }
        },
        {
            "id": 29000042,
            "Biskvit_id": "4503",
            "shortName": "ДО «Ленинградское шоссе» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградское шоссе, д. 13, к.1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.818685,
                "longitude": 37.497198
            }
        },
        {
            "id": 29000235,
            "Biskvit_id": "3029",
            "shortName": "ДО «Мытищинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Мытищи, ул. Воровского, д. 1, пом. V",
            "city": "Мытищи",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.918736,
                "longitude": 37.761626
            }
        },
        {
            "id": 29000071,
            "Biskvit_id": "3010",
            "shortName": "ДО «Нагорно-Южный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Варшавское шоссе, д. 87",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.652938,
                "longitude": 37.620698
            }
        },
        {
            "id": 29000072,
            "Biskvit_id": "3403",
            "shortName": "ДО «На Венёвской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Веневская, д.6",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.54785,
                "longitude": 37.543255
            }
        },
        {
            "id": 29000073,
            "Biskvit_id": "3310",
            "shortName": "ДО «Твин Плаза» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Новоясеневский пр-т вл. 2а, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: 10:00-17:00",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.617774,
                "longitude": 37.505768
            }
        },
        {
            "id": 29000076,
            "Biskvit_id": "3410",
            "shortName": "ДО «Лермонтовский проспект» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Лермонтовский пр-т, д. 10, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.700562,
                "longitude": 37.851808
            }
        },
        {
            "id": 29000081,
            "Biskvit_id": "4010",
            "shortName": "ДО «Строгинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Маршала Катукова ул., д. 16",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.807395,
                "longitude": 37.40628
            }
        },
        {
            "id": 29000084,
            "Biskvit_id": "4910",
            "shortName": "ДО «Нахимовский проспект» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Нахимовский пр-т, д. 11, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.663512,
                "longitude": 37.6054
            }
        },
        {
            "id": 29000095,
            "Biskvit_id": "4410",
            "shortName": "ДО «Тимирязевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Дмитровское ш., д. 13а",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.818715,
                "longitude": 37.573501
            }
        },
        {
            "id": 29000188,
            "Biskvit_id": "2603",
            "shortName": "ДО «Химкинский бульвар» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Химкинский бульвар, д. 16, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.851985,
                "longitude": 37.443012
            }
        },
        {
            "id": 29000044,
            "Biskvit_id": "5103",
            "shortName": "ДО «Жулебино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Привольная, 65/32",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.681534,
                "longitude": 37.849886
            }
        },
        {
            "id": 29000045,
            "Biskvit_id": "4903",
            "shortName": "ДО «Площадь Гагарина» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинский пр-т, д. 34/1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.707365,
                "longitude": 37.57775
            }
        },
        {
            "id": 29000063,
            "Biskvit_id": "2310",
            "shortName": "ДО «На Красносельской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Нижняя Красносельская, д.45/17",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.773034,
                "longitude": 37.675765
            }
        },
        {
            "id": 29000067,
            "Biskvit_id": "2610",
            "shortName": "ДО «Бутовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, бульвар Дмитрия Донского, д.11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-21:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.566807,
                "longitude": 37.576394
            }
        },
        {
            "id": 29000069,
            "Biskvit_id": "2810",
            "shortName": "ДО «Шоссе Энтузиастов» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, шоссе Энтузиастов, д.31, стр. 39",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.758863,
                "longitude": 37.75205
            }
        },
        {
            "id": 29000192,
            "Biskvit_id": "3703",
            "shortName": "ДО «Багратионовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Барклая, д.7, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.740588,
                "longitude": 37.501285
            }
        },
        {
            "id": 25007009,
            "Biskvit_id": "3052",
            "shortName": "ОО «Татищевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, пос. Светлый, ул. Кузнецова, д. 1",
            "city": "п. Светлый",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.673439,
                "longitude": 45.621166
            }
        },
        {
            "id": 25006032,
            "Biskvit_id": "2050",
            "shortName": "ОО «Приокский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, Приокский район, пр-т Гагарина, д. 162 А",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.256858,
                "longitude": 43.972219
            }
        },
        {
            "id": 41017009,
            "Biskvit_id": "1539",
            "shortName": "ОО «Новодвинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Новодвинск, пл. Ленина, д. 1",
            "city": "Новодвинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.41378,
                "longitude": 40.819806
            }
        },
        {
            "id": 23006038,
            "Biskvit_id": "1305",
            "shortName": "ОО «Платовский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Новочеркасск, ул. Московская, д. 19",
            "city": "Новочеркасск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.41404,
                "longitude": 40.097524
            }
        },
        {
            "id": 21006029,
            "Biskvit_id": "1245",
            "shortName": "ОО «На Орджоникидзе» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Новомосковск, ул. Орджоникидзе, д. 2",
            "city": "Новомосковск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.032221,
                "longitude": 38.261718
            }
        },
        {
            "id": 29000239,
            "Biskvit_id": "1103",
            "shortName": "ДО «Протвинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Протвино, ул. Ленина, д. 24Б",
            "city": "Протвино",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.875869,
                "longitude": 37.223967
            }
        },
        {
            "id": 21012004,
            "Biskvit_id": "0421",
            "shortName": "ОО «Ржевский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Ржев, ул. Б. Спасская, д. 44",
            "city": "Ржев",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.251747,
                "longitude": 34.327232
            }
        },
        {
            "id": 25010010,
            "Biskvit_id": "1761",
            "shortName": "ОО «Молодежный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, пр-т Дзержинского, д. 18",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.832416,
                "longitude": 55.124587
            }
        },
        {
            "id": 27004010,
            "Biskvit_id": "1523",
            "shortName": "ОО «Айхальский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), п. Айхал, ул. Промышленная, д. 24",
            "city": "п. Айхал",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 65.950491,
                "longitude": 111.496755
            }
        },
        {
            "id": 21004022,
            "Biskvit_id": "2916",
            "shortName": "ОО «На Мичуринской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тамбовская область, г. Тамбов, ул. Мичуринская, д. 213б",
            "city": "Тамбов",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.769612,
                "longitude": 41.392949
            }
        },
        {
            "id": 25006290,
            "Biskvit_id": "3068",
            "shortName": "ОО «Городецкий» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, р-н Городецкий. г. Городец, ул. Як. Петрова, д.1 пом.П5",
            "city": "Городец",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.644822,
                "longitude": 43.47236
            }
        },
        {
            "id": 25006291,
            "Biskvit_id": "3168",
            "shortName": "ОО «Заволжский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, Городецкий район, г.Заволжье, ул.Пономарева, д.6А, П1",
            "city": "Заволжье",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.629486,
                "longitude": 43.41238
            }
        },
        {
            "id": 22001156,
            "Biskvit_id": "3563",
            "shortName": "ОО «На Республики» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Заводоуковск, ул. Республики, 3",
            "city": "Заводоуковск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.496751,
                "longitude": 66.558344
            }
        },
        {
            "id": 25011242,
            "Biskvit_id": "5362",
            "shortName": "ОО «На Комсомольской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Кумертау, ул. Комсомольская, д. 12",
            "city": "Кумертау",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.754702,
                "longitude": 55.793832
            }
        },
        {
            "id": 26000461,
            "Biskvit_id": "2490",
            "shortName": "ДО №66 «Парнас» Филиала № 7806 Банка ВТБ",
            "address": "г. Санкт-Петербург, ул. Федора Абрамова, д. 4",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.070307,
                "longitude": 30.334948
            }
        },
        {
            "id": 21016081,
            "Biskvit_id": "3016",
            "shortName": "ДО «Александровский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Александров, ул. Ленина, д. 13, корп. 7, нежилое помещение М II. комн. 3 и 4",
            "city": "Александров",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.397923,
                "longitude": 38.720856
            }
        },
        {
            "id": 21005041,
            "Biskvit_id": "3716",
            "shortName": "ОО «Заднепровский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Смоленск, ул. Ново-Московская, д. 2/8",
            "city": "Смоленск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.794585,
                "longitude": 32.056947
            }
        },
        {
            "id": 29000370,
            "Biskvit_id": "3301",
            "shortName": "ДО «Фрязино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Фрязино, пр-т Мира, д. 17, пом. 13",
            "city": "Фрязино",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.956617,
                "longitude": 38.058322
            }
        },
        {
            "id": 22001146,
            "Biskvit_id": "2263",
            "shortName": "ОО «На Широтной» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Тюмень, ул. Широтная, д. 193/4",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.096402,
                "longitude": 65.621887
            }
        },
        {
            "id": 25015036,
            "Biskvit_id": "5532",
            "shortName": "ОО в г. Тольятти Филиала в г. Нижнем Новгороде",
            "address": "Самарская область, г. Тольятти, Новый проезд, д. 8",
            "city": "Тольятти",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.515809,
                "longitude": 49.283732
            }
        },
        {
            "id": 25005007,
            "Biskvit_id": "5481",
            "shortName": "ОО в г. Ульяновске Филиала в г. Нижнем Новгороде",
            "address": "Ульяновская область, г. Ульяновск, ул. Кузнецова, д. 5а",
            "city": "Ульяновск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.311256,
                "longitude": 48.39926
            }
        },
        {
            "id": 25011021,
            "Biskvit_id": "5482",
            "shortName": "ОО в г. Уфе Филиала в г. Нижнем Новгороде",
            "address": "Республика Башкортостан, г. Уфа, ул. Карла Маркса, д. 23",
            "city": "Уфа",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.725727,
                "longitude": 55.940419
            }
        },
        {
            "id": 41025017,
            "Biskvit_id": "1990",
            "shortName": "Операционный офис в г. Вологде Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Вологодская область, г. Вологда, пр-т Победы, д. 39",
            "city": "Вологда",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.22302,
                "longitude": 39.877707
            }
        },
        {
            "id": 23006040,
            "Biskvit_id": "2205",
            "shortName": "ОО «Западный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т Коммунистический, д. 27",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.207455,
                "longitude": 39.631541
            }
        },
        {
            "id": 22005015,
            "Biskvit_id": "2215",
            "shortName": "ОО «Югорский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, пр-т Комсомольский, д. 25",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.239012,
                "longitude": 73.454612
            }
        },
        {
            "id": 41023000,
            "Biskvit_id": "0297",
            "shortName": "РОО «Псковский»",
            "address": "Псковская область, г. Псков, Интернациональный пер., д. 1-а",
            "city": "Псков",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.822188,
                "longitude": 28.321366
            }
        },
        {
            "id": 21011002,
            "Biskvit_id": "2541",
            "shortName": "ОО «Площадь Новаторов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, пл. Новаторов, д. 2",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.639753,
                "longitude": 39.654448
            }
        },
        {
            "id": 21004003,
            "Biskvit_id": "1141",
            "shortName": "ОО «На Советской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тамбовская область, г. Тамбов, ул. Чичканова/Советская, д. 89/164",
            "city": "Тамбов",
            "scheduleFl": "пн-пт: 09:00-18:00 cб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.737945,
                "longitude": 41.450738
            }
        },
        {
            "id": 23008044,
            "Biskvit_id": "3855",
            "shortName": "ДО «Тихорецкий» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Тихорецк, ул. Ленинградская, д. 230",
            "city": "Тихорецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.860009,
                "longitude": 40.130187
            }
        },
        {
            "id": 41000005,
            "Biskvit_id": "0490",
            "shortName": "Дополнительный офис «Кировский» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Российская Федерация, г. Санкт-Петербург, пр. Стачек, д. 47, лит. А, пом.3Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.878432,
                "longitude": 30.25834
            }
        },
        {
            "id": 41000023,
            "Biskvit_id": "0590",
            "shortName": "Дополнительный офис «Смольнинский» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "г. Санкт-Петербург, Дегтярный переулок, д. 11, лит.А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.939465,
                "longitude": 30.384751
            }
        },
        {
            "id": 18002000,
            "Biskvit_id": "5545",
            "shortName": "РОО «Ставропольский»",
            "address": "Ставропольский край, г. Ставрополь, ул. Маршала Жукова, д. 7",
            "city": "Ставрополь",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.041859,
                "longitude": 41.969137
            }
        },
        {
            "id": 25006045,
            "Biskvit_id": "5473",
            "shortName": "ОО «На Решетниковской» Филиала Банка ВТБ (ПАО) в г. Нижнем Новгороде",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Решетниковская, д. 4",
            "city": "Нижний Новгород",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.314727,
                "longitude": 44.001827
            }
        },
        {
            "id": 25003009,
            "Biskvit_id": "3361",
            "shortName": "ОО «На Мопра» Филиала Банка ВТБ (ПАО) в г. Кирове",
            "address": "Кировская область, г. Киров, ул. Мопра, д. 113а",
            "city": "Киров",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.609835,
                "longitude": 49.653362
            }
        },
        {
            "id": 26000048,
            "Biskvit_id": "3606",
            "shortName": "ДО № 24 «Бабушкина, 36» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Бабушкина, д. 36, лит. А, пом.1-Н, 2-Н, 3-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.880902,
                "longitude": 30.437868
            }
        },
        {
            "id": 21011081,
            "Biskvit_id": "3316",
            "shortName": "ОО «Есенинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, Солотчинское шоссе, д. 2",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.63154,
                "longitude": 39.774418
            }
        },
        {
            "id": 21003010,
            "Biskvit_id": "2616",
            "shortName": "ОО «Гусь-Хрустальный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Владимирская область, г. Гусь-Хрустальный, ул. Калинина, д. 32/14",
            "city": "Гусь-Хрустальный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.614409,
                "longitude": 40.671566
            }
        },
        {
            "id": 26000018,
            "Biskvit_id": "1726",
            "shortName": "ДО № 5 «Большевиков, 21» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Большевиков, д. 21, лит. Р, пом. 25Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.905154,
                "longitude": 30.483009
            }
        },
        {
            "id": 26000036,
            "Biskvit_id": "5036",
            "shortName": "ДО «Проспект Просвещения» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Просвещения, д. 34, лит. А, пом. 17Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.053732,
                "longitude": 30.334248
            }
        },
        {
            "id": 22001013,
            "Biskvit_id": "4022",
            "shortName": "ОО «Звездный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Тимофея Чаркова, д. 81, помещение 1",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.179134,
                "longitude": 65.65684
            }
        },
        {
            "id": 27004011,
            "Biskvit_id": "1423",
            "shortName": "ОО «Удачный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Республика Саха (Якутия), г. Удачный, Новый г., нежилые помещения 18, 19, 20, 21, 22, часть помещения 1",
            "city": "Удачный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.410133,
                "longitude": 112.244791
            }
        },
        {
            "id": 22002041,
            "Biskvit_id": "5563",
            "shortName": "ОО в г. Челябинске Филиала в г. Екатеринбурге",
            "address": "Челябинская область, г. Челябинск, пр-т Ленина, д. 26а",
            "city": "Челябинск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.161913,
                "longitude": 61.431345
            }
        },
        {
            "id": 26000058,
            "Biskvit_id": "4226",
            "shortName": "ДО № 49 «Тореза, 9» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Тореза, д. 9, лит. А, пом. 59Н, 60Н, 61Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.000263,
                "longitude": 30.364081
            }
        },
        {
            "id": 21008032,
            "Biskvit_id": "2316",
            "shortName": "ОО «Ватутинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Валуйки, ул. 1 Мая, д. 41",
            "city": "Валуйки",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.212745,
                "longitude": 38.099429
            }
        },
        {
            "id": 29000265,
            "Biskvit_id": "1401",
            "shortName": "ДО «Арена Плаза» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградский проспект, д. 36",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.791248,
                "longitude": 37.559388
            }
        },
        {
            "id": 41019013,
            "Biskvit_id": "2190",
            "shortName": "ОО «Полярные Зори» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Полярные Зори, ул. Сивко, д. 1",
            "city": "Полярные зори",
            "scheduleFl": "пн-пт: 11:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.365726,
                "longitude": 32.502574
            }
        },
        {
            "id": 22002034,
            "Biskvit_id": "3649",
            "shortName": "ОО «На Кирова» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Кирова, д. 1",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.182937,
                "longitude": 61.399715
            }
        },
        {
            "id": 41021004,
            "Biskvit_id": "2090",
            "shortName": "ОО «Боровичи» Филиала 7806 Банка ВТБ (ПАО)",
            "address": "Новгородская область, г. Боровичи, ул. Подбельского, д. 36",
            "city": "Боровичи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.393341,
                "longitude": 33.917789
            }
        },
        {
            "id": 25008010,
            "Biskvit_id": "4428",
            "shortName": "ОО «Шумерлинский» в г. Шумерля Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Шумерля, ул. Октябрьская, д. 11",
            "city": "Шумерля",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.494655,
                "longitude": 46.413597
            }
        },
        {
            "id": 26000081,
            "Biskvit_id": "2290",
            "shortName": "ДО № 63 «Прибрежная, 18» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Прибрежная ул., д. 18, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.832521,
                "longitude": 30.505062
            }
        },
        {
            "id": 26000027,
            "Biskvit_id": "3026",
            "shortName": "ДО № 38 «Дачный, 17» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Дачный пр-т, д. 17, корп. 3, лит. А, пом. 14-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.843909,
                "longitude": 30.249492
            }
        },
        {
            "id": 26000030,
            "Biskvit_id": "3526",
            "shortName": "ДО № 44 «Долгоозерная, 14» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Долгоозерная, д. 14, лит. А, пом. 5-Н, комн. №№ 1-10, пом. 9-Н, комн. №№ 1-9",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.017423,
                "longitude": 30.246374
            }
        },
        {
            "id": 26000031,
            "Biskvit_id": "3626",
            "shortName": "ДО № 45 «Индустриальный, 26» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр. Индустриальный, д. 26/24, лит. А, пом. 4, комн. №№ 7,8,9,11,12, часть комн. №3",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.947653,
                "longitude": 30.473469
            }
        },
        {
            "id": 18002063,
            "Biskvit_id": "2358",
            "shortName": "ОО «Михайловский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Михайловск, ул. Ленина, д. 175",
            "city": "Михайловск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.135638,
                "longitude": 42.019892
            }
        },
        {
            "id": 18002022,
            "Biskvit_id": "2258",
            "shortName": "РОО «Банк ВТБ в Чеченской Республике»",
            "address": "Чеченская Республика, г. Грозный, ул. Мира, д. 68",
            "city": "Грозный",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.3216,
                "longitude": 45.689798
            }
        },
        {
            "id": 25003001,
            "Biskvit_id": "3818",
            "shortName": "ОО «Вятский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Кировская область, г. Киров, пр-т Октябрьский, д. 153",
            "city": "Киров",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.583218,
                "longitude": 49.65771
            }
        },
        {
            "id": 17000001,
            "Biskvit_id": "5025",
            "shortName": "ДО «Земляной вал» Филиала в г. Москве",
            "address": "г. Москва, ул. Земляной вал, д. 14-16, стр. 1",
            "city": "Москва",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.761305,
                "longitude": 37.65629
            }
        },
        {
            "id": 24003001,
            "Biskvit_id": "2743",
            "shortName": "ОО «Красный путь» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Красный Путь, д. 80, кор. 2",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.007034,
                "longitude": 73.34535
            }
        },
        {
            "id": 21008000,
            "Biskvit_id": "1016",
            "shortName": "РОО «Белгородский»",
            "address": "Белгородская область, г. Белгород, пр-т Ватутина, д. 8",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.574448,
                "longitude": 36.582003
            }
        },
        {
            "id": 24003005,
            "Biskvit_id": "2443",
            "shortName": "ОО «На Дианова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Дианова, д. 5, кор. 1",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.993319,
                "longitude": 73.264025
            }
        },
        {
            "id": 24007030,
            "Biskvit_id": "3111",
            "shortName": "ОО «На Свердлова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Свердлова, д. 36",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.28636,
                "longitude": 104.288269
            }
        },
        {
            "id": 21010007,
            "Biskvit_id": "1668",
            "shortName": "ОО «Заволжский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, пр-т Авиаторов, д. 90",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.655203,
                "longitude": 39.944505
            }
        },
        {
            "id": 24007024,
            "Biskvit_id": "4111",
            "shortName": "ОО «На Декабрьских Событий» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Декабрьских событий, д. 85",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:30 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.285853,
                "longitude": 104.305813
            }
        },
        {
            "id": 24002009,
            "Biskvit_id": "2014",
            "shortName": "ОО «Малаховское кольцо» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, ул. Малахова, д.48 / ул. Юрина, д. 227",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.367911,
                "longitude": 83.705018
            }
        },
        {
            "id": 25014038,
            "Biskvit_id": "2464",
            "shortName": "ОО «Горки» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Р.Зорге, д. 57/29",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.751396,
                "longitude": 49.207879
            }
        },
        {
            "id": 27002009,
            "Biskvit_id": "3656",
            "shortName": "ОО «Ерофей Павлович» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, Сковородинский р-н, пос. Ерофей Павлович, ул. Ленина, 22",
            "city": "п. Ерофей Павлович",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.956036,
                "longitude": 121.949651
            }
        },
        {
            "id": 25015031,
            "Biskvit_id": "1819",
            "shortName": "ОО «На Автовазе» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, Южное шоссе, д. 36, стр. 135",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.556898,
                "longitude": 49.26034
            }
        },
        {
            "id": 25006293,
            "Biskvit_id": "3368",
            "shortName": "ОО «Семеновский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Семенов, ул. Луначарского, д.12",
            "city": "Семенов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.791152,
                "longitude": 44.491885
            }
        },
        {
            "id": 21016018,
            "Biskvit_id": "3621",
            "shortName": "ДО «Борисоглебский» Филиала № 3652 Банка ВТБ ПАО)",
            "address": "Воронежская область, г. Борисоглебск, ул. Третьяковская, д. 2а",
            "city": "Борисоглебск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.365881,
                "longitude": 42.076351
            }
        },
        {
            "id": 24010008,
            "Biskvit_id": "4140",
            "shortName": "ДО «Карасук» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Карасук, ул. Ленина, д. 106",
            "city": "Карасук",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.73489,
                "longitude": 78.032166
            }
        },
        {
            "id": 24006040,
            "Biskvit_id": "2913",
            "shortName": "ОО «Радуга» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, пр-т Шахтеров, д. 95",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.404882,
                "longitude": 86.120642
            }
        },
        {
            "id": 24007221,
            "Biskvit_id": "4243",
            "shortName": "ДО «Юбилейный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, микрорайон Юбилейный, д. 19/1.",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.227534,
                "longitude": 104.304025
            }
        },
        {
            "id": 26000622,
            "Biskvit_id": "3990",
            "shortName": "ДО № 9 «Балтийская Жемчужина» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Адмирала Трибуца, д. 7, лит. А, пом. 23-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.851815,
                "longitude": 30.146212
            }
        },
        {
            "id": 21012007,
            "Biskvit_id": "0121",
            "shortName": "ДО «Чайковский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Тверь, пр-кт. Чайковского, д. 37",
            "city": "Тверь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.838179,
                "longitude": 35.89393
            }
        },
        {
            "id": 23001013,
            "Biskvit_id": "1208",
            "shortName": "ДО «Волжский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волжский, ул. Мира, д. 30",
            "city": "Волжский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.776557,
                "longitude": 44.795713
            }
        },
        {
            "id": 29000097,
            "Biskvit_id": "0825",
            "shortName": "ДО «Университет» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ломоносовский пр-т, д. 25, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.693597,
                "longitude": 37.532448
            }
        },
        {
            "id": 25014401,
            "Biskvit_id": "4268",
            "shortName": "ОО «На Фучика» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Юлиуса Фучика, д. 72",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.755849,
                "longitude": 49.232358
            }
        },
        {
            "id": 25008101,
            "Biskvit_id": "4468",
            "shortName": "ОО «Канашский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Чувашия, г. Канаш, ул. Железнодорожная, д. 89",
            "city": "Канаш",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.512898,
                "longitude": 47.480939
            }
        },
        {
            "id": 22004006,
            "Biskvit_id": "1515",
            "shortName": "ОО «Ноябрьский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Ноябрьск, ул. Изыскателей, д. 33",
            "city": "Ноябрьск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.206513,
                "longitude": 75.437122
            }
        },
        {
            "id": 24003002,
            "Biskvit_id": "2243",
            "shortName": "ОО «Железнодорожный» в г. Омске Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, пр-т Карла Маркса, д.72",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.943364,
                "longitude": 73.383636
            }
        },
        {
            "id": 24003003,
            "Biskvit_id": "1543",
            "shortName": "ОО «На Декабристов» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. 10 лет Октября, д. 43",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.985163,
                "longitude": 73.393122
            }
        },
        {
            "id": 25015034,
            "Biskvit_id": "4328",
            "shortName": "ОО «Лесная слобода» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. 40 лет Победы, д. 28",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.53859,
                "longitude": 49.356532
            }
        },
        {
            "id": 41025000,
            "Biskvit_id": "1589",
            "shortName": "РОО «Череповецкий»",
            "address": "Вологодская область, г. Череповец, ул. Сталеваров, д. 30",
            "city": "Череповец",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.121569,
                "longitude": 37.90727
            }
        },
        {
            "id": 21008030,
            "Biskvit_id": "5490",
            "shortName": "ОО в г. Белгороде Филиала в г. Воронеже",
            "address": "Белгородская область, г. Белгород, ул. Победы, д. 73а",
            "city": "Белгород",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.592298,
                "longitude": 36.590951
            }
        },
        {
            "id": 25007121,
            "Biskvit_id": "5062",
            "shortName": "ОО «На Революционной» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Вольск, ул. Революционная, д. 14",
            "city": "Вольск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.041436,
                "longitude": 47.394674
            }
        },
        {
            "id": 25007023,
            "Biskvit_id": "4628",
            "shortName": "ОО «Балашовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Балашов, ул. 30 лет Победы, д. 170",
            "city": "Балашов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.547835,
                "longitude": 43.14973
            }
        },
        {
            "id": 23002005,
            "Biskvit_id": "1958",
            "shortName": "ОО «Ахтубинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Астраханская область, г. Ахтубинск, ул. Жуковского, д. 24",
            "city": "Ахтубинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.278648,
                "longitude": 46.17434
            }
        },
        {
            "id": 21009006,
            "Biskvit_id": "5512",
            "shortName": "ОО в г. Брянске Филиала в г. Воронеже",
            "address": "Брянская область, г. Брянск, ул. Арсенальская, д. 16",
            "city": "Брянск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.249198,
                "longitude": 34.374996
            }
        },
        {
            "id": 25007012,
            "Biskvit_id": "1252",
            "shortName": "ОО «Кировский» в г. Саратове Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. Танкистов, д. 15",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.548838,
                "longitude": 46.016695
            }
        },
        {
            "id": 23006055,
            "Biskvit_id": "5255",
            "shortName": "ОО «Площадь Космонавтов» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Волкова, д. 11",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.283731,
                "longitude": 39.714707
            }
        },
        {
            "id": 26000079,
            "Biskvit_id": "5536",
            "shortName": "ОО «Мурино» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, пос. Мурино, пр-т Авиаторов Балтики, д. 7",
            "city": "п. Мурино",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.052326,
                "longitude": 30.438587
            }
        },
        {
            "id": 21010011,
            "Biskvit_id": "5497",
            "shortName": "ОО в г. Ярославле Филиала в г. Воронеже",
            "address": "Ярославская область, г. Ярославль, пер. Первомайский, д. 4",
            "city": "Ярославль",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.629128,
                "longitude": 39.887543
            }
        },
        {
            "id": 41017010,
            "Biskvit_id": "1939",
            "shortName": "ОО «Ягринский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Северодвинск, ул. Адмирала Нахимова, д. 5",
            "city": "Северодвинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.593236,
                "longitude": 39.809659
            }
        },
        {
            "id": 41017011,
            "Biskvit_id": "2039",
            "shortName": "ОО «Площадь Егорова» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Архангельская область, г. Северодвинск, пр-т Ленина, д. 2/33",
            "city": "Северодвинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.567388,
                "longitude": 39.82105
            }
        },
        {
            "id": 22006046,
            "Biskvit_id": "4222",
            "shortName": "ДО «Североуральский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Североуральск, ул. Ленина, д. 17а",
            "city": "Североуральск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.154463,
                "longitude": 59.965995
            }
        },
        {
            "id": 26000080,
            "Biskvit_id": "5636",
            "shortName": "ОО «Кудрово» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, д. Кудрово, Европейский пр-т, д. 16",
            "city": "д. Кудрово",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.908683,
                "longitude": 30.514935
            }
        },
        {
            "id": 23008050,
            "Biskvit_id": "3259",
            "shortName": "ДО «На Стасова» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, Карасунский внутриг.ской округ, ул. им. Стасова, д. 186",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.031349,
                "longitude": 39.044079
            }
        },
        {
            "id": 21001006,
            "Biskvit_id": "2516",
            "shortName": "ОО «Людиново» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Калужская область, г. Людиново, ул. Маяковского, д. 6",
            "city": "Людиново",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.860189,
                "longitude": 34.44236
            }
        },
        {
            "id": 27007041,
            "Biskvit_id": "4723",
            "shortName": "ДО «На Серышева» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Хабаровск, ул. Серышева, д. 74",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.493235,
                "longitude": 135.064614
            }
        },
        {
            "id": 22002025,
            "Biskvit_id": "3622",
            "shortName": "ОО «На Мира» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Снежинск, пр-т Мира, д. 21",
            "city": "Снежинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.07475,
                "longitude": 60.754653
            }
        },
        {
            "id": 41018010,
            "Biskvit_id": "1238",
            "shortName": "ОО «Советск» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Калининградская область, г. Советск, ул. Первомайская, д. 11",
            "city": "Советск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.081545,
                "longitude": 21.880256
            }
        },
        {
            "id": 24003014,
            "Biskvit_id": "5578",
            "shortName": "ОО в г. Омске Филиала в г. Красноярске",
            "address": "Омская область, г. Омск, ул. Тарская, д. 6",
            "city": "Омск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.990339,
                "longitude": 73.368841
            }
        },
        {
            "id": 41020006,
            "Biskvit_id": "1504",
            "shortName": "ОО «Сосногорский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Сосногорск, ул. Зои Космодемьянской, д. 18",
            "city": "Сосногорск",
            "scheduleFl": "пн: выходной вт-пт: 10:00-18:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.599446,
                "longitude": 53.874267
            }
        },
        {
            "id": 41000010,
            "Biskvit_id": "1390",
            "shortName": "Дополнительный офис «Московская застава» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Российская Федерация, г. Санкт-Петербург, Лиговский пр. д. 281, лит А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.899365,
                "longitude": 30.337257
            }
        },
        {
            "id": 26000024,
            "Biskvit_id": "2926",
            "shortName": "ДО № 41 «Ленсовета, 88» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Ленсовета, д. 88, литера «А», пом. 46-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.832842,
                "longitude": 30.350274
            }
        },
        {
            "id": 25013023,
            "Biskvit_id": "5342",
            "shortName": "ОО «Комсомольский проспект» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, Комсомольский пр-т, д. 33",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00 пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.006726,
                "longitude": 56.242622
            }
        },
        {
            "id": 25009042,
            "Biskvit_id": "4828",
            "shortName": "ОО «Петровский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. им. Петрова, д. 51А",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.870204,
                "longitude": 53.294171
            }
        },
        {
            "id": 27001004,
            "Biskvit_id": "4623",
            "shortName": "ОО «Холмский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Сахалинская область, г. Холмск, ул. Победы, д. 2",
            "city": "Холмск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.042053,
                "longitude": 142.043562
            }
        },
        {
            "id": 21009004,
            "Biskvit_id": "1466",
            "shortName": "ОО «2-я Аллея» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Брянск, ул. 2-я Аллея, д. 15",
            "city": "Брянск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.209195,
                "longitude": 34.411575
            }
        },
        {
            "id": 25007005,
            "Biskvit_id": "1518",
            "shortName": "ОО «Энгельсский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Энгельс, ул. Волоха, д. 1А",
            "city": "Энгельс",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.49357,
                "longitude": 46.121923
            }
        },
        {
            "id": 25013020,
            "Biskvit_id": "2842",
            "shortName": "ОО «Победа» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Соликамск, ул. 20 лет Победы, д. 173/В",
            "city": "Соликамск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.642199,
                "longitude": 56.758794
            }
        },
        {
            "id": 41017000,
            "Biskvit_id": "0192",
            "shortName": "РОО «Архангельский»",
            "address": "Архангельская область, г. Архангельск, наб. Северной Двины, д. 55, помещение 4-Н",
            "city": "Архангельск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.530993,
                "longitude": 40.527018
            }
        },
        {
            "id": 24010018,
            "Biskvit_id": "0940",
            "shortName": "ДО «На Станиславского» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Станиславского, д. 11",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.98478,
                "longitude": 82.871885
            }
        },
        {
            "id": 24010020,
            "Biskvit_id": "1840",
            "shortName": "ДО «На Горького» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Максима Горького, д. 78",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.027,
                "longitude": 82.923205
            }
        },
        {
            "id": 24010021,
            "Biskvit_id": "2140",
            "shortName": "ДО «На Хмельницкого» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Богдана Хмельницкого, д. 17",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.069669,
                "longitude": 82.940965
            }
        },
        {
            "id": 21010141,
            "Biskvit_id": "4116",
            "shortName": "ДО «Сокол» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ярославская область, г. Ярославль, пр-т Фрунзе, д. 52б",
            "city": "Ярославль",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.583237,
                "longitude": 39.907755
            }
        },
        {
            "id": 21016013,
            "Biskvit_id": "2051",
            "shortName": "ДО «Московский проспект» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, Московский пр-т, д. 126",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.718908,
                "longitude": 39.181548
            }
        },
        {
            "id": 24010029,
            "Biskvit_id": "4040",
            "shortName": "ДО «Инской-Первомайский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Героев Революции, д. 37",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.975796,
                "longitude": 83.081318
            }
        },
        {
            "id": 22004000,
            "Biskvit_id": "1815",
            "shortName": "РОО «Ямальский»",
            "address": "Ямало-Ненецкий Автономный округ, г. Новый Уренгой, ул. 26 съезда КПСС, д. 7А",
            "city": "Новый Уренгой",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.087777,
                "longitude": 76.68207
            }
        },
        {
            "id": 24010033,
            "Biskvit_id": "2940",
            "shortName": "ДО «Краснообский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, р. пос. Краснообск, БГ-1-6",
            "city": "р.п. Краснообск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.918747,
                "longitude": 82.983635
            }
        },
        {
            "id": 22005000,
            "Biskvit_id": "4215",
            "shortName": "РОО «Ханты-Мансийский»",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, пр-т Мира, д. 1",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.262497,
                "longitude": 73.378668
            }
        },
        {
            "id": 41025004,
            "Biskvit_id": "1836",
            "shortName": "ОО «На Преминина» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Вологда, ул. Сергея Преминина, д. 1, нежилые помещения №№ 35-37, 48-54",
            "city": "Вологда",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.220501,
                "longitude": 39.891523
            }
        },
        {
            "id": 24007003,
            "Biskvit_id": "2411",
            "shortName": "ОО «206 квартал» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Ангарск, 206 квартал, д. 3, помещение 200",
            "city": "Ангарск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.502019,
                "longitude": 103.83232
            }
        },
        {
            "id": 24003006,
            "Biskvit_id": "2543",
            "shortName": "ОО «21-я Амурская» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. 21-я Амурская, д. 7",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.026035,
                "longitude": 73.410487
            }
        },
        {
            "id": 24003008,
            "Biskvit_id": "1943",
            "shortName": "ОО «Московка» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Новокирпичная, д. 5",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.923419,
                "longitude": 73.449617
            }
        },
        {
            "id": 24003010,
            "Biskvit_id": "1343",
            "shortName": "ОО «Привокзальный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. Леконта, д. 2",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.937407,
                "longitude": 73.384364
            }
        },
        {
            "id": 18002010,
            "Biskvit_id": "2159",
            "shortName": "ДО «Георгиевский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Георгиевск, ул. Калинина, д. 107",
            "city": "Георгиевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.134186,
                "longitude": 43.454529
            }
        },
        {
            "id": 23008321,
            "Biskvit_id": "4958",
            "shortName": "ДО «На Мачуги» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. В. Н. Мачуги, д. 49/1",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.012791,
                "longitude": 39.074271
            }
        },
        {
            "id": 24007034,
            "Biskvit_id": "1740",
            "shortName": "ОО «Энергетик» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Братск, Энергетик ж.р., ул. Холоднова, № 11",
            "city": "Братск",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.303222,
                "longitude": 101.754607
            }
        },
        {
            "id": 24010009,
            "Biskvit_id": "3940",
            "shortName": "ДО «Барабинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Барабинск, ул. Калинина, д. 1",
            "city": "Барабинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.351063,
                "longitude": 78.342956
            }
        },
        {
            "id": 22005001,
            "Biskvit_id": "2315",
            "shortName": "ОО «Нижневартовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Нижневартовск, ул. Ленина, д. 46",
            "city": "Нижневартовск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.933344,
                "longitude": 76.593451
            }
        },
        {
            "id": 23006035,
            "Biskvit_id": "2805",
            "shortName": "ОО «Центральный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Таганрог, ул. Греческая, д. 17/ 1-й Крепостной пер. 24",
            "city": "Таганрог",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.206396,
                "longitude": 38.944177
            }
        },
        {
            "id": 25015010,
            "Biskvit_id": "1119",
            "shortName": "ОО «Автозаводский» в г. Тольятти Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. Маршала Жукова, д. 2",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.516462,
                "longitude": 49.307951
            }
        },
        {
            "id": 23001015,
            "Biskvit_id": "2908",
            "shortName": "ОО «Новый город» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волжский, ул. Мира, д. 74А",
            "city": "Волжский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.767472,
                "longitude": 44.807823
            }
        },
        {
            "id": 25015032,
            "Biskvit_id": "1019",
            "shortName": "ОО «На Жилина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. Жилина, д. 9",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.510433,
                "longitude": 49.410646
            }
        },
        {
            "id": 24001021,
            "Biskvit_id": "2324",
            "shortName": "ОО «Краснокаменский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Забайкальский край, г. Краснокаменск, пр-т Строителей, д. 21",
            "city": "Краснокаменск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.101463,
                "longitude": 118.045986
            }
        },
        {
            "id": 24006056,
            "Biskvit_id": "4624",
            "shortName": "ОО «Таштагольский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Таштагол, ул. Ленина, д. 62",
            "city": "Таштагол",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.770271,
                "longitude": 87.890467
            }
        },
        {
            "id": 24007045,
            "Biskvit_id": "4424",
            "shortName": "ОО «На Волжской» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Байкальская, д. 126/2",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.263326,
                "longitude": 104.311257
            }
        },
        {
            "id": 24002021,
            "Biskvit_id": "2224",
            "shortName": "ОО «Камень-на-Оби» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Камень-на-Оби, ул. Пушкина, д. 25",
            "city": "Камень-на-Оби",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.791098,
                "longitude": 81.347632
            }
        },
        {
            "id": 24002011,
            "Biskvit_id": "2514",
            "shortName": "ОО «Магистральный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, пр-т Ленина, д. 68",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.350676,
                "longitude": 83.775015
            }
        },
        {
            "id": 24009056,
            "Biskvit_id": "3946",
            "shortName": "ОО «Боготольский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Боготол, ул. 40 лет Октября, д. 12",
            "city": "Боготол",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.210222,
                "longitude": 89.533818
            }
        },
        {
            "id": 24002002,
            "Biskvit_id": "2714",
            "shortName": "ОО «Красногвардейский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Новоалтайск, ул. Красногвардейская, д. 5",
            "city": "Новоалтайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.413921,
                "longitude": 83.928878
            }
        },
        {
            "id": 23008161,
            "Biskvit_id": "2758",
            "shortName": "ДО «На Энгельса» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Новороссийск, ул. Энгельса, д. 32",
            "city": "Новороссийск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.717648,
                "longitude": 37.772307
            }
        },
        {
            "id": 22001002,
            "Biskvit_id": "3115",
            "shortName": "ОО «Ишимский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Ишим, ул. Карла Маркса, д. 9/1",
            "city": "Ишим",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.110209,
                "longitude": 69.474294
            }
        },
        {
            "id": 24006042,
            "Biskvit_id": "2407",
            "shortName": "ОО «Площадь Советов» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, пр-т Советский, д. 56",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.3555,
                "longitude": 86.088249
            }
        },
        {
            "id": 22002010,
            "Biskvit_id": "2849",
            "shortName": "ОО «Южный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Магнитогорск, ул. Труда, д.39, кор. А",
            "city": "Магнитогорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.364128,
                "longitude": 58.964715
            }
        },
        {
            "id": 21006035,
            "Biskvit_id": "1145",
            "shortName": "ОО «Узловая» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Узловая, ул. Беклемищева, д. 85",
            "city": "Узловая",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.977657,
                "longitude": 38.157352
            }
        },
        {
            "id": 24002020,
            "Biskvit_id": "5724",
            "shortName": "ОО «Алейский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Алейск, ул. Комсомольская, д. 118",
            "city": "Алейск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.496416,
                "longitude": 82.774265
            }
        },
        {
            "id": 21001001,
            "Biskvit_id": "2451",
            "shortName": "ДО «Обнинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Калужская область, г. Обнинск, просп. Маркса, д. 8",
            "city": "Обнинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.112767,
                "longitude": 36.589711
            }
        },
        {
            "id": 24007032,
            "Biskvit_id": "3911",
            "shortName": "ОО «На 2-ой Железнодорожной» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Маяковского, д. 25",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.286211,
                "longitude": 104.24789
            }
        },
        {
            "id": 24006049,
            "Biskvit_id": "1307",
            "shortName": "ОО «Киселевский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Киселевск, ул. Советская, д. 14, помещение 6а",
            "city": "Киселевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.002633,
                "longitude": 86.641844
            }
        },
        {
            "id": 41022002,
            "Biskvit_id": "1965",
            "shortName": "ОО «Антикайнена, 1 а» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Петрозаводск, ул. Антикайнена, д. 1А",
            "city": "Петрозаводск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.780763,
                "longitude": 34.362455
            }
        },
        {
            "id": 22001004,
            "Biskvit_id": "2415",
            "shortName": "ОО «На Ямской» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Ямская, д.77/1 лит. А",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.159668,
                "longitude": 65.491577
            }
        },
        {
            "id": 29000345,
            "Biskvit_id": "1901",
            "shortName": "ДО «Бульвар Ушакова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, бульвар Адмирала Ушакова, д. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.548574,
                "longitude": 37.553244
            }
        },
        {
            "id": 25015026,
            "Biskvit_id": "2518",
            "shortName": "ДО «Созвездие» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Гагарина, д. 51",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.200016,
                "longitude": 50.179505
            }
        },
        {
            "id": 22004002,
            "Biskvit_id": "2515",
            "shortName": "ОО «Надымский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Надым, ул. Пионерская, д. 13",
            "city": "Надым",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 65.528843,
                "longitude": 72.507797
            }
        },
        {
            "id": 24009052,
            "Biskvit_id": "3613",
            "shortName": "ОО «Взлетный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Молокова, д. 60, пом. 109",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.03963,
                "longitude": 92.899823
            }
        },
        {
            "id": 24006036,
            "Biskvit_id": "2607",
            "shortName": "ОО «Прокопьевский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Прокопьевск, Центральный район, пр-т Шахтеров, д. 43",
            "city": "Прокопьевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.887242,
                "longitude": 86.748465
            }
        },
        {
            "id": 24010001,
            "Biskvit_id": "1240",
            "shortName": "ДО «Березовая роща» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Кошурникова, д. 8",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.042968,
                "longitude": 82.951152
            }
        },
        {
            "id": 24010002,
            "Biskvit_id": "1340",
            "shortName": "ДО «Затулинка» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Зорге, д. 179",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.934691,
                "longitude": 82.9214
            }
        },
        {
            "id": 29000017,
            "Biskvit_id": "0427",
            "shortName": "ДО «Арбат, 51» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Арбат, д. 51, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.747784,
                "longitude": 37.586688
            }
        },
        {
            "id": 29000259,
            "Biskvit_id": "4629",
            "shortName": "ДО «Новокуркино» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Химки, пр-т Мельникова, д. 2-Б, пом. III",
            "city": "Химки",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.901183,
                "longitude": 37.407537
            }
        },
        {
            "id": 41000025,
            "Biskvit_id": "1190",
            "shortName": "Дополнительный офис «Меридиан» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Санкт-Петербург, муниципальный округ Гагаринское, ул. Типанова, дом 25, корпус 1, строение 1",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.853885,
                "longitude": 30.347462
            }
        },
        {
            "id": 22002027,
            "Biskvit_id": "2349",
            "shortName": "ОО «Северо-Западный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. 40 лет Победы, д. 29",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.184546,
                "longitude": 61.301817
            }
        },
        {
            "id": 24010005,
            "Biskvit_id": "2924",
            "shortName": "ДО «Родники» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, ул. Гребенщикова, д. 8",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.110239,
                "longitude": 82.941037
            }
        },
        {
            "id": 24002012,
            "Biskvit_id": "4214",
            "shortName": "ДО «Идеал» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, ул. Пролетарская, д. 127а, пом. 1",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.334833,
                "longitude": 83.776794
            }
        },
        {
            "id": 24006037,
            "Biskvit_id": "1407",
            "shortName": "ОО «Гагаринский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Прокопьевск, Рудничный район, пр-к Гагарина, д. 16",
            "city": "Прокопьевск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.882863,
                "longitude": 86.675684
            }
        },
        {
            "id": 25011001,
            "Biskvit_id": "1362",
            "shortName": "ОО «Нефтекамский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Нефтекамск, ул. Ленина, д. 15",
            "city": "Нефтекамск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.087595,
                "longitude": 54.248829
            }
        },
        {
            "id": 22006010,
            "Biskvit_id": "1402",
            "shortName": "ДО «Новоуральский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Новоуральск, ул. Фрунзе, д. 9",
            "city": "Новоуральск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.246047,
                "longitude": 60.08636
            }
        },
        {
            "id": 24009037,
            "Biskvit_id": "3246",
            "shortName": "ОО «Норильский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Норильск, Ленинский пр-т, д. 48",
            "city": "Норильск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.357849,
                "longitude": 88.185851
            }
        },
        {
            "id": 25011011,
            "Biskvit_id": "2062",
            "shortName": "ОО «Звездный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Юрия Гагарина, д. 45а",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.771866,
                "longitude": 56.077071
            }
        },
        {
            "id": 22005016,
            "Biskvit_id": "3515",
            "shortName": "ДО «Комсомольский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Югорск, ул. Ленина, д. 29",
            "city": "Югорск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.314929,
                "longitude": 63.328847
            }
        },
        {
            "id": 24007041,
            "Biskvit_id": "3611",
            "shortName": "ОО «Усольский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Усолье-Сибирское, пр-т Красных партизан, д. 24",
            "city": "Усолье-Сибирское",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.732421,
                "longitude": 103.656457
            }
        },
        {
            "id": 24007026,
            "Biskvit_id": "2311",
            "shortName": "ОО «На Байкальской» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Байкальская, д. 241",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.254572,
                "longitude": 104.339356
            }
        },
        {
            "id": 25006028,
            "Biskvit_id": "1450",
            "shortName": "ОО «На ул. Коминтерна, д. 127» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Коминтерна, д. 127",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.352028,
                "longitude": 43.868032
            }
        },
        {
            "id": 25011013,
            "Biskvit_id": "2362",
            "shortName": "ОО «Библиотечный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, пр-т Октября, д. 72, кв-л П",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.761363,
                "longitude": 56.013354
            }
        },
        {
            "id": 24005001,
            "Biskvit_id": "1540",
            "shortName": "ОО «Северский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Северск, пр-т Коммунистический, д. 42",
            "city": "Северск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.601585,
                "longitude": 84.882395
            }
        },
        {
            "id": 24007038,
            "Biskvit_id": "1811",
            "shortName": "ОО «Слюдянка» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Слюдянка, ул. Парижской Коммуны, д. 1 А",
            "city": "Слюдянка",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-16:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.656356,
                "longitude": 103.719941
            }
        },
        {
            "id": 24007046,
            "Biskvit_id": "2113",
            "shortName": "ОО «Усть-Илимский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Усть-Илимск, пр-т Мира, д. 45",
            "city": "Усть-Илимск",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00 пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.940221,
                "longitude": 102.733366
            }
        },
        {
            "id": 41022003,
            "Biskvit_id": "1865",
            "shortName": "ОО «Державинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Карелия, г. Петрозаводск, ул. Кирова, д. 19",
            "city": "Петрозаводск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.792536,
                "longitude": 34.368384
            }
        },
        {
            "id": 41018042,
            "Biskvit_id": "2690",
            "shortName": "ОО «На Сельме» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Калининград, ул. Генерала Челнокова, д. 25",
            "city": "Калининград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.739534,
                "longitude": 20.485352
            }
        },
        {
            "id": 24005002,
            "Biskvit_id": "1640",
            "shortName": "ОО «На Льва Толстого» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, ул. Льва Толстого, д. 83",
            "city": "Томск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.476722,
                "longitude": 84.999068
            }
        },
        {
            "id": 24005004,
            "Biskvit_id": "1358",
            "shortName": "ОО «На Нахимова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, ул. Нахимова, д. 8",
            "city": "Томск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.455617,
                "longitude": 84.959956
            }
        },
        {
            "id": 26000010,
            "Biskvit_id": "4006",
            "shortName": "ДО «Тихвинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, Тихвинский муниципальный район, Тихвинское городское поселение, г. Тихвин, мкр-н 1-й, д. 27А, пом. 1",
            "city": "Тихвин",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.645419,
                "longitude": 33.544341
            }
        },
        {
            "id": 23008033,
            "Biskvit_id": "1555",
            "shortName": "ДО «Лазаревский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Сочи, Лазаревский район, ул. Победы, д. 70",
            "city": "Сочи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.912428,
                "longitude": 39.3288
            }
        },
        {
            "id": 21006022,
            "Biskvit_id": "2145",
            "shortName": "ОО «Ефремов» в г. Ефремове Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Ефремов, ул. Ленина. д. 26",
            "city": "Ефремов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.14611,
                "longitude": 38.115338
            }
        },
        {
            "id": 25007003,
            "Biskvit_id": "1352",
            "shortName": "ОО «Балаковский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Балаково, ул. Ленина, д. 56",
            "city": "Балаково",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.035126,
                "longitude": 47.781767
            }
        },
        {
            "id": 24007049,
            "Biskvit_id": "5411",
            "shortName": "ОО «Лермонтовский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Лермонтова, д.281/1",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.246898,
                "longitude": 104.270348
            }
        },
        {
            "id": 24009061,
            "Biskvit_id": "5413",
            "shortName": "ОО «На Кравченко» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Ачинск, 4 мкр., д. 1",
            "city": "Ачинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.257433,
                "longitude": 90.487146
            }
        },
        {
            "id": 25006025,
            "Biskvit_id": "3350",
            "shortName": "ОО «Саровский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Саров, ул. Московская, д. 11",
            "city": "Саров",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.945505,
                "longitude": 43.327687
            }
        },
        {
            "id": 25011003,
            "Biskvit_id": "3062",
            "shortName": "ОО «Экватор» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Ленина, д. 65/4",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.738359,
                "longitude": 55.952843
            }
        },
        {
            "id": 25006022,
            "Biskvit_id": "2550",
            "shortName": "ОО «Кстовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Кстово, пр-т Победы, д. 3 «Г»",
            "city": "Кстово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.153989,
                "longitude": 44.210066
            }
        },
        {
            "id": 24007043,
            "Biskvit_id": "2013",
            "shortName": "ОО «Братский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Братск, ж.р. Центральный, ул. Мира, д. 27",
            "city": "Братск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.153427,
                "longitude": 101.619743
            }
        },
        {
            "id": 24007036,
            "Biskvit_id": "2511",
            "shortName": "ОО «Шелеховский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Шелехов, 7 квартал, д. 1",
            "city": "Шелехов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.211556,
                "longitude": 104.092014
            }
        },
        {
            "id": 24009047,
            "Biskvit_id": "2846",
            "shortName": "ОО «Железногорский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, ЗАТО Железногорск, г. Железногорск, ул. Ленина, д.21, пом. 37",
            "city": "Железногорск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.250412,
                "longitude": 93.531447
            }
        },
        {
            "id": 24002003,
            "Biskvit_id": "2414",
            "shortName": "ОО «Заринский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Заринск, ул. Металлургов, д. 8, кв. 74 (магазин)",
            "city": "Заринск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.703128,
                "longitude": 84.927787
            }
        },
        {
            "id": 23008001,
            "Biskvit_id": "1255",
            "shortName": "ДО «Армавирский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Армавир, ул. Ленина, д. 76",
            "city": "Армавир",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.999299,
                "longitude": 41.127057
            }
        },
        {
            "id": 22004003,
            "Biskvit_id": "3615",
            "shortName": "ОО «Уренгойский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Новый Уренгой, мкр. Мирный, д. 1/1Б",
            "city": "Новый Уренгой",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.118567,
                "longitude": 76.670994
            }
        },
        {
            "id": 21015002,
            "Biskvit_id": "2041",
            "shortName": "ОО «На Комсомольской» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Орловская область, г. Орел, ул. Комсомольская, д. 229а",
            "city": "Орел",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.941027,
                "longitude": 36.050389
            }
        },
        {
            "id": 24002008,
            "Biskvit_id": "1414",
            "shortName": "ОО ЦИК «На Павловском тракте» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Барнаул, ул. Павловский тракт, д. 251д",
            "city": "Барнаул",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.342511,
                "longitude": 83.684914
            }
        },
        {
            "id": 21006039,
            "Biskvit_id": "2716",
            "shortName": "ОО «На Металлургов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Металлургов, д. 86-б",
            "city": "Тула",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.19653,
                "longitude": 37.67873
            }
        },
        {
            "id": 25014053,
            "Biskvit_id": "4528",
            "shortName": "ОО «Лениногорский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Лениногорск, пр-т Шашина, д. 37",
            "city": "Лениногорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.596639,
                "longitude": 52.439173
            }
        },
        {
            "id": 22002321,
            "Biskvit_id": "1032",
            "shortName": "ОО «Академический» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, Советский район, ул. Блюхера, д. 55.",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.131614,
                "longitude": 61.369783
            }
        },
        {
            "id": 41020021,
            "Biskvit_id": "0691",
            "shortName": "ОО «Усинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Усинск, ул. Нефтяников, д. 36",
            "city": "Усинск",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 65.992852,
                "longitude": 57.542205
            }
        },
        {
            "id": 26000481,
            "Biskvit_id": "2790",
            "shortName": "ОО «Тосненский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Тосно, пр-т Ленина, д. 29",
            "city": "Тосно",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.543943,
                "longitude": 30.870371
            }
        },
        {
            "id": 41000014,
            "Biskvit_id": "2538",
            "shortName": "ОО «Всеволожский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Всеволожск, Всеволожский пр-т, д. 68",
            "city": "Всеволожск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.016132,
                "longitude": 30.647086
            }
        },
        {
            "id": 24007001,
            "Biskvit_id": "2111",
            "shortName": "ОО «Ангарский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Ангарск, 89 квартал, д. 4, помещение 1",
            "city": "Ангарск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.536361,
                "longitude": 103.894564
            }
        },
        {
            "id": 25014043,
            "Biskvit_id": "3564",
            "shortName": "ОО «На Губкина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Академика Губкина, д. 2",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.802761,
                "longitude": 49.187146
            }
        },
        {
            "id": 27002005,
            "Biskvit_id": "3256",
            "shortName": "ОО «Свободненский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Свободный, ул. Некрасова, 92",
            "city": "Свободный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.348844,
                "longitude": 128.147074
            }
        },
        {
            "id": 29000341,
            "Biskvit_id": "2401",
            "shortName": "ДО «Черноголовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Черноголовка, пр-д Строителей, д. 1б",
            "city": "Черноголовка",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.01151,
                "longitude": 38.377727
            }
        },
        {
            "id": 24005121,
            "Biskvit_id": "4143",
            "shortName": "ОО «На Суворова» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, ул. Суворова, д. 17а",
            "city": "Томск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.513134,
                "longitude": 85.023988
            }
        },
        {
            "id": 27003013,
            "Biskvit_id": "2254",
            "shortName": "ОО «Спасский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Спасск-Дальний, ул. Советская, д. 79а",
            "city": "Спасск-Дальний",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.593738,
                "longitude": 132.814864
            }
        },
        {
            "id": 41023002,
            "Biskvit_id": "1236",
            "shortName": "ОО «На Ленина» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Псковская область, г. Великие Луки, пр-т Ленина, д. 26/12",
            "city": "Великие Луки",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.344127,
                "longitude": 30.518654
            }
        },
        {
            "id": 27002008,
            "Biskvit_id": "1656",
            "shortName": "ОО «Солнечный» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Благовещенск, ул. Игнатьевское шоссе, д. 15",
            "city": "Благовещенск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.295871,
                "longitude": 127.514238
            }
        },
        {
            "id": 29000295,
            "Biskvit_id": "0529",
            "shortName": "ДО «Хорошевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Генерала Глаголева, д. 30, корп. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.788631,
                "longitude": 37.46679
            }
        },
        {
            "id": 41023004,
            "Biskvit_id": "1126",
            "shortName": "ОО «ТК ИМПЕРИАЛ» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Псковская область, г. Псков, ул. Коммунальная, д. 41",
            "city": "Псков",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.820448,
                "longitude": 28.290239
            }
        },
        {
            "id": 25010014,
            "Biskvit_id": "2761",
            "shortName": "ОО «Новый город» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Орск, пр-т Ленина/ ул. Московская, д. 38/16",
            "city": "Орск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.232086,
                "longitude": 58.466177
            }
        },
        {
            "id": 21011022,
            "Biskvit_id": "2816",
            "shortName": "ОО «Вокзальный» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, ул. Вокзальная, д. 6",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.63019,
                "longitude": 39.721562
            }
        },
        {
            "id": 29000464,
            "Biskvit_id": "2604",
            "shortName": "ДО «Луховицкий» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Луховицы, ул.  Жуковского, д.30а /1",
            "city": "Луховицы",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.94414,
                "longitude": 39.03365
            }
        },
        {
            "id": 26000482,
            "Biskvit_id": "2890",
            "shortName": "ДО №65 «Московский,180» Филиала № 7806 Банка ВТБ",
            "address": "г. Санкт-Петербург, Московский пр-т, д. 180, литера А, пом. 1-Н.",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.876174,
                "longitude": 30.32098
            }
        },
        {
            "id": 22004041,
            "Biskvit_id": "1263",
            "shortName": "ОО «Тарко-Салинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО, г. Тарко-Сале, мкр.Советский, 1а",
            "city": "Тарко-Сале",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 64.915548,
                "longitude": 77.761872
            }
        },
        {
            "id": 25006241,
            "Biskvit_id": "3762",
            "shortName": "ОО «Борский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Бор, ул. Мичурина, д. 14",
            "city": "Бор",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.362601,
                "longitude": 44.060119
            }
        },
        {
            "id": 41020061,
            "Biskvit_id": "3790",
            "shortName": "ОО «Эжвинский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Сыктывкар, пр-т Бумажников, д. 44.",
            "city": "Сыктывкар",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.779185,
                "longitude": 50.747834
            }
        },
        {
            "id": 21006033,
            "Biskvit_id": "2445",
            "shortName": "ОО «На Демонстрации» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, ул. Демонстрации, д. 2Г",
            "city": "Тула",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.193175,
                "longitude": 37.611634
            }
        },
        {
            "id": 29000326,
            "Biskvit_id": "2201",
            "shortName": "ДО «Марьинский парк» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Братиславская, д. 14",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.659124,
                "longitude": 37.755015
            }
        },
        {
            "id": 29000474,
            "Biskvit_id": "3604",
            "shortName": "ДО «На Рогожской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Ногинск, ул. Рогожская, д.81",
            "city": "Ногинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.856321,
                "longitude": 38.440483
            }
        },
        {
            "id": 22005085,
            "Biskvit_id": "4663",
            "shortName": "ОО «Пыть-Яхский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО – Югра, г.Пыть-Ях, 2 мкр., д.7",
            "city": "Пыть-Ях",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.753679,
                "longitude": 72.838826
            }
        },
        {
            "id": 22005088,
            "Biskvit_id": "5163",
            "shortName": "ОО «На Свердлова» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО – Югра, г.Ханты-Мансийск, ул. Свердлова, 11",
            "city": "Ханты-Мансийск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.007332,
                "longitude": 69.027723
            }
        },
        {
            "id": 29000436,
            "Biskvit_id": "3901",
            "shortName": "ДО «Бронницкий» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская обл.,г. Бронницы, ул. Ново-Бронницкая, д. 52",
            "city": "Бронницы",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.421103,
                "longitude": 38.260524
            }
        },
        {
            "id": 22004064,
            "Biskvit_id": "3863",
            "shortName": "ОО «Лабытнангский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО,г.Лабытнанги, ул. Школьная, 34",
            "city": "Лабытнанги",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 66.660915,
                "longitude": 66.381448
            }
        },
        {
            "id": 22001151,
            "Biskvit_id": "2763",
            "shortName": "ОО «На Московском тракте» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Тюмень, ул. Московский тракт, д. 137/4",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.095067,
                "longitude": 65.478489
            }
        },
        {
            "id": 26000012,
            "Biskvit_id": "1426",
            "shortName": "ДО № 13 «Петергоф» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Санкт-Петербург, г. Петергоф, Санкт-Петербургский п-т, д. 25, Лит. А., пом. 1-Н",
            "city": "Петергоф",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.878802,
                "longitude": 29.918983
            }
        },
        {
            "id": 29000430,
            "Biskvit_id": "2709",
            "shortName": "ДО «Шатурский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, р-н Шатурский, г. Шатура, пр-т Маршала Борзова, д. 16",
            "city": "Шатура",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.581027,
                "longitude": 39.521839
            }
        },
        {
            "id": 22001150,
            "Biskvit_id": "2663",
            "shortName": "ОО «На Муравленко» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Тюмень, ул. Газовиков, 41/4",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.173391,
                "longitude": 65.559544
            }
        },
        {
            "id": 22005081,
            "Biskvit_id": "3263",
            "shortName": "ОО «Белоярский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО- Югра, г.Белоярский, ул. Набережная, д.14",
            "city": "Белоярский",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10.00-17.00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.716139,
                "longitude": 66.659989
            }
        },
        {
            "id": 26000009,
            "Biskvit_id": "2306",
            "shortName": "ОО «Сосновоборский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская область, г. Сосновый Бор, ул. Ленинградская, д. 34а",
            "city": "Сосновый Бор",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.896066,
                "longitude": 29.078079
            }
        },
        {
            "id": 22001124,
            "Biskvit_id": "1663",
            "shortName": "ОО «На Пермякова, 23» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Тюмень, ул. Пермякова, д. 23, к. 1/1",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.11746,
                "longitude": 65.578812
            }
        },
        {
            "id": 25011261,
            "Biskvit_id": "4168",
            "shortName": "ОО «Сибайский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Сибай, ул. Заки Валиди, д. 31",
            "city": "Сибай",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.716097,
                "longitude": 58.672529
            }
        },
        {
            "id": 26000504,
            "Biskvit_id": "3490",
            "shortName": "ДО №67 «Новгородский,10» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пос. Шушары, Новгородский пр., д. 10",
            "city": "Шушары",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.806821,
                "longitude": 30.369282
            }
        },
        {
            "id": 25006286,
            "Biskvit_id": "2668",
            "shortName": "ОО «Павловский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Павлово, ул. Шмидта, д. 25",
            "city": "Павлово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.963969,
                "longitude": 43.066277
            }
        },
        {
            "id": 29000455,
            "Biskvit_id": "1704",
            "shortName": "ДО «Каширский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Кашира, ул. Советская, д.12",
            "city": "Кашира",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.834512,
                "longitude": 38.15039
            }
        },
        {
            "id": 23006341,
            "Biskvit_id": "4558",
            "shortName": "ОО «Звезда» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, пос. Персиановский, ул. Школьная, д. 39, пом. 1",
            "city": "пос. Персиановский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.521772,
                "longitude": 40.114952
            }
        },
        {
            "id": 25011241,
            "Biskvit_id": "5262",
            "shortName": "ОО «Затон» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Ахметова, д. 299",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.789758,
                "longitude": 55.879621
            }
        },
        {
            "id": 22005083,
            "Biskvit_id": "3963",
            "shortName": "ОО «Междуреченский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО – Югра, п.г.т.Междуреченский, ул. Ленина, д.14",
            "city": "п. Междуреченский",
            "scheduleFl": "пн-пт: 10.00-19.00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10.00-17.00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.597841,
                "longitude": 65.900778
            }
        },
        {
            "id": 41000006,
            "Biskvit_id": "1090",
            "shortName": "Дополнительный офис «Василеостровский» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Российская Федерация, г. Санкт-Петербург, Большой пр. В.О., д.78 лит.В, пом.1Н, 24Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.930678,
                "longitude": 30.25498
            }
        },
        {
            "id": 22002011,
            "Biskvit_id": "3849",
            "shortName": "ДО «Уральский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Магнитогорск, пр-т К. Маркса, д. 112, пом. 1",
            "city": "Магнитогорск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.403115,
                "longitude": 58.977507
            }
        },
        {
            "id": 23008042,
            "Biskvit_id": "0255",
            "shortName": "ДО «Темрюк» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Темрюк, ул.Таманская, д. 58",
            "city": "Темрюк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.275644,
                "longitude": 37.376393
            }
        },
        {
            "id": 23008022,
            "Biskvit_id": "2955",
            "shortName": "ДО «Кропоткинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Кропоткин, ул. Красная, д. 83",
            "city": "Кропоткин",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.433485,
                "longitude": 40.566768
            }
        },
        {
            "id": 25010241,
            "Biskvit_id": "4368",
            "shortName": "ОО «На Салмышской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Оренбург, ул. Салмышская, д. 43/5",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.821656,
                "longitude": 55.168883
            }
        },
        {
            "id": 22002261,
            "Biskvit_id": "5422",
            "shortName": "ОО «Энергия» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Богдана Хмельницкого, д. 21",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.258207,
                "longitude": 61.388854
            }
        },
        {
            "id": 23008301,
            "Biskvit_id": "4658",
            "shortName": "ДО «Кореновский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Кореновск, ул. Мира, д. 112",
            "city": "Кореновск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.466591,
                "longitude": 39.446578
            }
        },
        {
            "id": 25006296,
            "Biskvit_id": "3668",
            "shortName": "ДО «Первомайский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Первомайск, ул. Октябрьская, д. 9",
            "city": "Первомайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.866772,
                "longitude": 43.802859
            }
        },
        {
            "id": 18002241,
            "Biskvit_id": "4858",
            "shortName": "ДО «Моздокский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Северная Осетия-Алания, р-н Моздокский, г. Моздок, ул. Соколовского, д. 28",
            "city": "Моздок",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.732398,
                "longitude": 44.664461
            }
        },
        {
            "id": 24009321,
            "Biskvit_id": "4443",
            "shortName": "ОО «Канский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Канск, ул. Парижской Коммуны, д.64",
            "city": "Канск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.203067,
                "longitude": 95.704094
            }
        },
        {
            "id": 24004006,
            "Biskvit_id": "5580",
            "shortName": "ОО в г. Улан-Удэ Филиала в г. Красноярске",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Ботаническая, д. 3а",
            "city": "Улан-Удэ",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.842255,
                "longitude": 107.629283
            }
        },
        {
            "id": 26000028,
            "Biskvit_id": "3226",
            "shortName": "ДО № 31 «Просвещения, 87» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Просвещения, д. 87 к. 1, лит. А, часть пом. 10-Н, 77-Н (пом. №№1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26, 27,28,29,30,31,32)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.036097,
                "longitude": 30.414521
            }
        },
        {
            "id": 25008004,
            "Biskvit_id": "1353",
            "shortName": "ДО «Калининский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Чебоксары, ул. Калинина, д. 105А",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.137656,
                "longitude": 47.277821
            }
        },
        {
            "id": 22004001,
            "Biskvit_id": "4115",
            "shortName": "ОО «Северный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ямало-Ненецкий Автономный округ, г. Муравленко, ул. Дружбы народов, д. 3",
            "city": "Муравленко",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 63.787808,
                "longitude": 74.508515
            }
        },
        {
            "id": 29000910,
            "Biskvit_id": "3309",
            "shortName": "ДО «На Астахова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Коломна, ул. Астахова, д.4 к.2",
            "city": "Коломна",
            "scheduleFl": "пн: выходной вс-сб: 10:00-19:00 вс: 10:00-15:00",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.065473,
                "longitude": 38.746476
            }
        },
        {
            "id": 18002041,
            "Biskvit_id": "2158",
            "shortName": "ОО «Каспийский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Дагестан, г. Каспийск, мкр. 8, д. 1",
            "city": "Каспийск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 42.890853,
                "longitude": 47.635665
            }
        },
        {
            "id": 24009341,
            "Biskvit_id": "4543",
            "shortName": "ДО «Крыловский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Хакасия, г. Абакан, ул. Крылова, д. 78, с. 1",
            "city": "Абакан",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.736051,
                "longitude": 91.441498
            }
        },
        {
            "id": 26000025,
            "Biskvit_id": "2826",
            "shortName": "ДО № 40 «Большевиков, 2» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, пр-т Большевиков, д. 2, литера «А», пом. 21-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.91789,
                "longitude": 30.47337
            }
        },
        {
            "id": 26000521,
            "Biskvit_id": "3690",
            "shortName": "ДО № 68 «Металлистов, 116» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, п-т Металлистов, д. 116, к. 1",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-18:00, пт: 10.00-17.00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.97206,
                "longitude": 30.394794
            }
        },
        {
            "id": 27007024,
            "Biskvit_id": "0456",
            "shortName": "ДО «Дземги» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Комсомольск-на-Амуре, пр-т Победы, д. 22",
            "city": "Комсомольск-на-Амуре",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.58909,
                "longitude": 137.059871
            }
        },
        {
            "id": 25012008,
            "Biskvit_id": "5018",
            "shortName": "ОО «Орбита» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Заречный, пр-т Мира, д. 5",
            "city": "Заречный",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.197583,
                "longitude": 45.181773
            }
        },
        {
            "id": 21005001,
            "Biskvit_id": "1244",
            "shortName": "ОО «Ярцевский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Ярцево, пр-т Металлургов, д. 58",
            "city": "Ярцево",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.046295,
                "longitude": 32.720874
            }
        },
        {
            "id": 25013012,
            "Biskvit_id": "3442",
            "shortName": "ОО «Чкаловский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Куйбышева, д. 103",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.98749,
                "longitude": 56.248317
            }
        },
        {
            "id": 23006030,
            "Biskvit_id": "3205",
            "shortName": "ОО «Проспект Стачки» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т Стачки, д. 23/48",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.210749,
                "longitude": 39.674526
            }
        },
        {
            "id": 24004041,
            "Biskvit_id": "3543",
            "shortName": "ОО «Проспект Строителей» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Улан-Удэ, пр-т Строителей, д. 64",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.812832,
                "longitude": 107.65334
            }
        },
        {
            "id": 25014046,
            "Biskvit_id": "0328",
            "shortName": "ОО «На Бутлерова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Курашова, д. 20",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.789932,
                "longitude": 49.142176
            }
        },
        {
            "id": 25012013,
            "Biskvit_id": "5477",
            "shortName": "ОО в г. Пензе Филиала в г. Нижнем Новгороде",
            "address": "Пензенская область, г. Пенза, ул. Московская, д. 9",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.186453,
                "longitude": 45.01466
            }
        },
        {
            "id": 27006002,
            "Biskvit_id": "2456",
            "shortName": "ОО «Елизовский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Камчатский край, г. Елизово, ул. Ленина, д. 21А",
            "city": "Елизово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.187704,
                "longitude": 158.384043
            }
        },
        {
            "id": 27006001,
            "Biskvit_id": "4156",
            "shortName": "ОО «На Лукашевского» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Камчатский край, г. Петропавловск-Камчатский, ул. Лукашевского, д. 11",
            "city": "Петропавловск-Камчатский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.060457,
                "longitude": 158.636353
            }
        },
        {
            "id": 24000220,
            "Biskvit_id": "4043",
            "shortName": "ОО «Лесосибирский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Лесосибирск, 5-й мкр., д. 26, пом. 44",
            "city": "Лесосибирск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.220842,
                "longitude": 92.503962
            }
        },
        {
            "id": 23001006,
            "Biskvit_id": "1608",
            "shortName": "ОО «Спартановский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Николая Отрады, д. 6",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.81476,
                "longitude": 44.624063
            }
        },
        {
            "id": 29000036,
            "Biskvit_id": "2729",
            "shortName": "ДО «Красногорский» Филиала № 7701 Банка ВТБ ПАО)",
            "address": "Московская область, г. Красногорск, ул. Ленина, д. 38б",
            "city": "Красногорск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.833855,
                "longitude": 37.29894
            }
        },
        {
            "id": 23008054,
            "Biskvit_id": "4255",
            "shortName": "ДО «Прикубанский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. им. Тургенева / Монтажников, д. 138/3/2",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.058243,
                "longitude": 38.962216
            }
        },
        {
            "id": 21004001,
            "Biskvit_id": "1451",
            "shortName": "ОО «Мичуринский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тамбовская область, г. Мичуринск, Советская, д. 327А",
            "city": "Мичуринск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.891251,
                "longitude": 40.511297
            }
        },
        {
            "id": 23006045,
            "Biskvit_id": "3805",
            "shortName": "ОО «Военвед» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Таганрогская, д. 104",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.262625,
                "longitude": 39.664285
            }
        },
        {
            "id": 29000190,
            "Biskvit_id": "3303",
            "shortName": "ДО «Рублевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Рублевское шоссе, д.28, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.746796,
                "longitude": 37.421308
            }
        },
        {
            "id": 25006030,
            "Biskvit_id": "1550",
            "shortName": "ОО «Автозаводский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Веденяпина, д. 13",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.234075,
                "longitude": 43.873323
            }
        },
        {
            "id": 25015006,
            "Biskvit_id": "0528",
            "shortName": "ДО «Москва» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, Московское шоссе, д. 45",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.222827,
                "longitude": 50.19166
            }
        },
        {
            "id": 25001001,
            "Biskvit_id": "4418",
            "shortName": "ОО «Химмаш» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Мордовия, г. Саранск, пр-т 70 лет Октября, д. 77а",
            "city": "Саранск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.191889,
                "longitude": 45.224515
            }
        },
        {
            "id": 25008005,
            "Biskvit_id": "1553",
            "shortName": "ОО «Новоюжный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Чебоксары, пр-т И. Яковлева, д. 4б",
            "city": "Чебоксары",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.101976,
                "longitude": 47.265883
            }
        },
        {
            "id": 25012012,
            "Biskvit_id": "3918",
            "shortName": "ОО «Карпинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Пенза, ул. Карпинского, д. 37А",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.209907,
                "longitude": 44.978422
            }
        },
        {
            "id": 21005003,
            "Biskvit_id": "1744",
            "shortName": "ОО «Сафоновский» Фоново Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Смоленская область, г. Сафоново, ул. Советская, д. 6",
            "city": "Сафоново",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.109595,
                "longitude": 33.246622
            }
        },
        {
            "id": 29000269,
            "Biskvit_id": "1501",
            "shortName": "ДО «Можайский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Можайский городской округ, г. Можайск, ул. Московская, д. 36",
            "city": "Можайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.506041,
                "longitude": 36.020404
            }
        },
        {
            "id": 29000053,
            "Biskvit_id": "5803",
            "shortName": "ДО «Волгоградский проспект» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Волгоградский пр-т, д. 94, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 cб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.704073,
                "longitude": 37.771328
            }
        },
        {
            "id": 18002009,
            "Biskvit_id": "1359",
            "shortName": "ОО «Буденновский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Буденновск, мкр. 6, д. 12а",
            "city": "Буденновск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.797495,
                "longitude": 44.157927
            }
        },
        {
            "id": 18002011,
            "Biskvit_id": "5305",
            "shortName": "ДО «45-ая параллель» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Ставрополь, ул. 50 лет ВЛКСМ, д. 109",
            "city": "Ставрополь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.999421,
                "longitude": 41.919182
            }
        },
        {
            "id": 25014048,
            "Biskvit_id": "1564",
            "shortName": "ОО «Бугульминский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Бугульма, ул. Мусы Джалиля, д. 46",
            "city": "Бугульма",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.532255,
                "longitude": 52.791187
            }
        },
        {
            "id": 21008023,
            "Biskvit_id": "1416",
            "shortName": "ОО «Губкинский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Губкин, ул. Королева, д. 2",
            "city": "Губкин",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.278061,
                "longitude": 37.50981
            }
        },
        {
            "id": 21008025,
            "Biskvit_id": "1616",
            "shortName": "ОО «Проспект Славы» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, пр-т Славы, д. 35а",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.596718,
                "longitude": 36.592181
            }
        },
        {
            "id": 21008026,
            "Biskvit_id": "1916",
            "shortName": "ОО «На Щорса» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Белгород, ул. Щорса, д. 45а",
            "city": "Белгород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 50.563669,
                "longitude": 36.57232
            }
        },
        {
            "id": 18002004,
            "Biskvit_id": "1659",
            "shortName": "ОО «Невинномысский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Невинномысск, ул. Гагарина, д. 21В",
            "city": "Невинномысск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.636292,
                "longitude": 41.94341
            }
        },
        {
            "id": 18002001,
            "Biskvit_id": "1259",
            "shortName": "ОО «Минеральные воды» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ставропольский край, г. Минеральные воды, пр-т 22 Партсъезда, д. 83/ул. Тбилисская д. 33",
            "city": "Минеральные воды",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.201691,
                "longitude": 43.135636
            }
        },
        {
            "id": 41025010,
            "Biskvit_id": "4860",
            "shortName": "ОО № 18 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Металлургов, д. 12",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.13043,
                "longitude": 37.904647
            }
        },
        {
            "id": 41025016,
            "Biskvit_id": "3860",
            "shortName": "ОО № 8 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Наседкина, д. 21",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.092053,
                "longitude": 37.903946
            }
        },
        {
            "id": 25013032,
            "Biskvit_id": "5142",
            "shortName": "ОО «Чайковский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Чайковский, ул. Ленина, д. 39б",
            "city": "Чайковский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.778012,
                "longitude": 54.151568
            }
        },
        {
            "id": 22002033,
            "Biskvit_id": "3549",
            "shortName": "ОО «Металлургический» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Челябинская область, г. Челябинск, ул. Сталеваров, д. 11",
            "city": "Челябинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.259869,
                "longitude": 61.403263
            }
        },
        {
            "id": 25015003,
            "Biskvit_id": "4318",
            "shortName": "ДО «На Ленинградской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Ленинградская, д. 48-50",
            "city": "Самара",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.187408,
                "longitude": 50.092315
            }
        },
        {
            "id": 29000074,
            "Biskvit_id": "3210",
            "shortName": "ДО «Чертаново» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Чертановская, д. 1в, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.639461,
                "longitude": 37.607143
            }
        },
        {
            "id": 29000443,
            "Biskvit_id": "4601",
            "shortName": "ДО «Площадь Дмитрия Донского» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская обл., г. Дзержинский, пл. Дмитрия Донского, д. 6",
            "city": "Дзержинский",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.629958,
                "longitude": 37.850281
            }
        },
        {
            "id": 21012009,
            "Biskvit_id": "3821",
            "shortName": "ОО «Конаковский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тверская область, г. Конаково, пр-т Ленина, д. 11а",
            "city": "Конаково",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.716275,
                "longitude": 36.773201
            }
        },
        {
            "id": 23008043,
            "Biskvit_id": "3355",
            "shortName": "ДО «Тимашевский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Тимашевск, ул. Пионерская, д. 191",
            "city": "Тимашевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.612246,
                "longitude": 38.937602
            }
        },
        {
            "id": 23002101,
            "Biskvit_id": "4458",
            "shortName": "ОО «Бабаевский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Астраханская область, г. Астрахань, ул. Бабаевского, д. 62",
            "city": "Астрахань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.399353,
                "longitude": 48.095495
            }
        },
        {
            "id": 29000452,
            "Biskvit_id": "5601",
            "shortName": "ДО «Звенигородский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Звенигород, ул. Пролетарская, д.23 корп.2, офис 3                             ",
            "city": "Звенигород",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.733503,
                "longitude": 36.853474
            }
        },
        {
            "id": 27007025,
            "Biskvit_id": "2756",
            "shortName": "ДО «Биробиджанский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Еврейская Автономная область, г. Биробиджан, ул. Комсомольская, д. 16",
            "city": "Биробиджан",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.784809,
                "longitude": 132.938364
            }
        },
        {
            "id": 23008037,
            "Biskvit_id": "3155",
            "shortName": "ДО «Белореченский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Белореченск, ул. Чапаева, д. 68Б",
            "city": "Белореченск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.760315,
                "longitude": 39.869882
            }
        },
        {
            "id": 23006047,
            "Biskvit_id": "3659",
            "shortName": "ОО «Миллерово» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Миллерово, ул. Ленина, д. 12",
            "city": "Миллерово",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.919604,
                "longitude": 40.391094
            }
        },
        {
            "id": 25014061,
            "Biskvit_id": "4728",
            "shortName": "ОО «Чистопольский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Чистополь, ул. Бебеля, д. 118",
            "city": "Чистополь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.370498,
                "longitude": 50.643809
            }
        },
        {
            "id": 25005006,
            "Biskvit_id": "1531",
            "shortName": "ОО «Засвияжский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Ульяновская область, г. Ульяновск, ул. Рябикова, д. 60а",
            "city": "Ульяновск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.277525,
                "longitude": 48.291714
            }
        },
        {
            "id": 23008051,
            "Biskvit_id": "2058",
            "shortName": "ДО «Геленджик» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Геленджик, ул. Горького/Октябрьская, д. 23/11",
            "city": "Геленджик",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.564056,
                "longitude": 38.081992
            }
        },
        {
            "id": 23002024,
            "Biskvit_id": "2558",
            "shortName": "ОО «На Воробьёва» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Астраханская область, г. Астрахань, проезд Воробьева, д.3",
            "city": "Астрахань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 46.332414,
                "longitude": 48.049555
            }
        },
        {
            "id": 25015039,
            "Biskvit_id": "4228",
            "shortName": "ДО «Отрадный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Отрадный, ул. Гайдара, д. 56",
            "city": "Отрадный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.379971,
                "longitude": 51.340506
            }
        },
        {
            "id": 25006027,
            "Biskvit_id": "1250",
            "shortName": "ОО «Заречный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, пр. Ленина, д. 42",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.282605,
                "longitude": 43.926692
            }
        },
        {
            "id": 23006025,
            "Biskvit_id": "3005",
            "shortName": "ОО «Волгодонский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Волгодонск, ул. 30 лет Победы, д. 4",
            "city": "Волгодонск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.506807,
                "longitude": 42.162527
            }
        },
        {
            "id": 24002014,
            "Biskvit_id": "2114",
            "shortName": "ОО «Чуйский тракт» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Алтайский край, г. Бийск, пер. Коммунарский, д. 23",
            "city": "Бийск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.540557,
                "longitude": 85.219919
            }
        },
        {
            "id": 41022000,
            "Biskvit_id": "0196",
            "shortName": "РОО «Петрозаводский»",
            "address": "Республика Карелия, г. Петрозаводск, ул. Куйбышева, д. 4",
            "city": "Петрозаводск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.78833,
                "longitude": 34.380188
            }
        },
        {
            "id": 25015009,
            "Biskvit_id": "0318",
            "shortName": "ДО «Сызранский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Сызрань, ул. Советская, д. 80",
            "city": "Сызрань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.153563,
                "longitude": 48.470443
            }
        },
        {
            "id": 41025005,
            "Biskvit_id": "5560",
            "shortName": "ОО № 5 в г. Вологде Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Вологда, ул. Ленинградская, д. 128",
            "city": "Вологда",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.209742,
                "longitude": 39.845394
            }
        },
        {
            "id": 24007141,
            "Biskvit_id": "3443",
            "shortName": "ОО «На Советской» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Иркутская область, г. Иркутск, ул. Ядринцева, д. 1/6",
            "city": "Иркутск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.279511,
                "longitude": 104.336544
            }
        },
        {
            "id": 25007014,
            "Biskvit_id": "1552",
            "shortName": "ОО «Заводской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. им. Орджоникидзе Г.К., д. 16",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.503057,
                "longitude": 45.959813
            }
        },
        {
            "id": 24003007,
            "Biskvit_id": "2643",
            "shortName": "ОО «На Мира» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, пр-т Мира, д. 20, кор. 1",
            "city": "Омск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.02508,
                "longitude": 73.297245
            }
        },
        {
            "id": 25007017,
            "Biskvit_id": "1952",
            "shortName": "ОО «Приоритет» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. Московская, д. 101",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.535736,
                "longitude": 46.025246
            }
        },
        {
            "id": 21002081,
            "Biskvit_id": "3916",
            "shortName": "ОО «Тейковский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Россия, Ивановская область, г. Тейково, ул.Октябрьская д.1",
            "city": "Тейково",
            "scheduleFl": "пн-пт: 09:00-18:00 сб,вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.854675,
                "longitude": 40.535768
            }
        },
        {
            "id": 26000522,
            "Biskvit_id": "3590",
            "shortName": "ДО №70 «Площадь Восстания» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Восстания, д. 1",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.932004,
                "longitude": 30.360901
            }
        },
        {
            "id": 25014044,
            "Biskvit_id": "3664",
            "shortName": "ОО «Азино» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, пр-т Победы, д. 100",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.768891,
                "longitude": 49.220832
            }
        },
        {
            "id": 41020005,
            "Biskvit_id": "1204",
            "shortName": "ОО «Октябрьский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Республика Коми, г. Сыктывкар, ул. Ленина, д. 47а",
            "city": "Сыктывкар",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.670321,
                "longitude": 50.836731
            }
        },
        {
            "id": 21002000,
            "Biskvit_id": "0751",
            "shortName": "РОО «Ивановский»",
            "address": "Ивановская область, г. Иваново, пр-т Шереметевский, д. 49",
            "city": "Иваново",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.00349,
                "longitude": 40.989596
            }
        },
        {
            "id": 23001221,
            "Biskvit_id": "4258",
            "shortName": "ОО «На Рокоссовского» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Волгоградская область, г. Волгоград, ул. Рокоссовского, д. 56",
            "city": "Волгоград",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.727504,
                "longitude": 44.520416
            }
        },
        {
            "id": 25009034,
            "Biskvit_id": "5474",
            "shortName": "ОО в г. Ижевске Филиала в г. Нижнем Новгороде",
            "address": "Удмуртская республика, г. Ижевск, ул. Красногеройская, д. 63",
            "city": "Ижевск",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.849753,
                "longitude": 53.220411
            }
        },
        {
            "id": 23008341,
            "Biskvit_id": "5058",
            "shortName": "ДО «Таманский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, ст. Тамань, ул. Карла Маркса, д. 105",
            "city": "Тамань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.216343,
                "longitude": 36.720928
            }
        },
        {
            "id": 21006001,
            "Biskvit_id": "1545",
            "shortName": "ОО «Алексин» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Алексин, ул. Ленина, д. 14",
            "city": "Алексин",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.500505,
                "longitude": 37.06713
            }
        },
        {
            "id": 25015024,
            "Biskvit_id": "2418",
            "shortName": "ДО «Красноглинский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул.Сергея Лазо, д. 44",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.346946,
                "longitude": 50.226299
            }
        },
        {
            "id": 24003013,
            "Biskvit_id": "3243",
            "shortName": "ОО «Левобережный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Омская область, г. Омск, ул. 70 лет Октября, д. 15",
            "city": "Омск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.982084,
                "longitude": 73.319047
            }
        },
        {
            "id": 24010016,
            "Biskvit_id": "0340",
            "shortName": "ДО «Академический» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Новосибирская область, г. Новосибирск, пр-т Строителей, д. 17",
            "city": "Новосибирск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.86015,
                "longitude": 83.084669
            }
        },
        {
            "id": 25015012,
            "Biskvit_id": "1419",
            "shortName": "ОО «Ладья» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. Автостроителей, д. 68А",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.533003,
                "longitude": 49.32687
            }
        },
        {
            "id": 25012005,
            "Biskvit_id": "1818",
            "shortName": "ОО «Суворовский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пензенская область, г. Пенза, ул.Суворова, д. 146А",
            "city": "Пенза",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.202529,
                "longitude": 44.996226
            }
        },
        {
            "id": 22005087,
            "Biskvit_id": "4766",
            "shortName": "ОО «Советский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО – Югра, г.Советский, ул. Садовая, д.2",
            "city": "Советский",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.371723,
                "longitude": 63.566604
            }
        },
        {
            "id": 26000621,
            "Biskvit_id": "3890",
            "shortName": "ОО «Аэродром» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Ленинградская обл., г. Гатчина, ул. Авиатриссы Зверевой дом 14.",
            "city": "Гатчина",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.554396,
                "longitude": 30.08943
            }
        },
        {
            "id": 22001009,
            "Biskvit_id": "1115",
            "shortName": "ОО «Юбилейный» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Республики, д. 94/1",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.141832,
                "longitude": 65.561385
            }
        },
        {
            "id": 21009001,
            "Biskvit_id": "1666",
            "shortName": "ОО «Клинцовский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Брянская область, г. Клинцы, ул. Октябрьская, д. 2",
            "city": "Клинцы",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.745092,
                "longitude": 32.240266
            }
        },
        {
            "id": 29000414,
            "Biskvit_id": "5104",
            "shortName": "ДО «Пущинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Пущино, просп. Науки, д. 1 д",
            "city": "Пущино",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.831857,
                "longitude": 37.623555
            }
        },
        {
            "id": 21006027,
            "Biskvit_id": "2245",
            "shortName": "ДО «Зеленстрой» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Тула, пр-кт Ленина, д. 119",
            "city": "Тула",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.160143,
                "longitude": 37.586706
            }
        },
        {
            "id": 24004061,
            "Biskvit_id": "3943",
            "shortName": "ОО «Восточный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Туполева, д. 20-20А",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.863094,
                "longitude": 107.737494
            }
        },
        {
            "id": 23006027,
            "Biskvit_id": "2405",
            "shortName": "ОО «Проспект Ленина» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т Ленина, д. 56",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.249623,
                "longitude": 39.718777
            }
        },
        {
            "id": 23006241,
            "Biskvit_id": "2658",
            "shortName": "ОО «Победа» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Еременко, д. 64",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.231661,
                "longitude": 39.617662
            }
        },
        {
            "id": 29000124,
            "Biskvit_id": "5527",
            "shortName": "ДО «Тверская, 8» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Тверская, д. 8, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.76212,
                "longitude": 37.60964
            }
        },
        {
            "id": 41019141,
            "Biskvit_id": "4190",
            "shortName": "ОО «Заполярный» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Заполярный, ул. Мира, д. 8",
            "city": "Заполярный",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 69.426909,
                "longitude": 30.816607
            }
        },
        {
            "id": 25015038,
            "Biskvit_id": "4128",
            "shortName": "ДО «Крутые ключи» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, бульвар Ивана Финютина, д. 20, н. 1",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.321093,
                "longitude": 50.310022
            }
        },
        {
            "id": 21016014,
            "Biskvit_id": "1441",
            "shortName": "ДО «Ленинский проспект» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Воронежская область, г. Воронеж, Ленинский пр-т, д. 81",
            "city": "Воронеж",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.654785,
                "longitude": 39.242921
            }
        },
        {
            "id": 21006023,
            "Biskvit_id": "1845",
            "shortName": "ОО «На Лукашина» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Тульская область, г. Щекино, ул. Лукашина, д. 10",
            "city": "Щекино",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.0205,
                "longitude": 37.505058
            }
        },
        {
            "id": 25008001,
            "Biskvit_id": "1453",
            "shortName": "ОО «Новочебоксарский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Чувашская Республика, г. Новочебоксарск, ул. Винокурова, д. 28",
            "city": "Новочебоксарск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.115238,
                "longitude": 47.488342
            }
        },
        {
            "id": 22002008,
            "Biskvit_id": "3602",
            "shortName": "ОО «На Куйбышева» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Курганская область, г. Курган, ул. Куйбышева, д. 28",
            "city": "Курган",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.431667,
                "longitude": 65.343445
            }
        },
        {
            "id": 18002005,
            "Biskvit_id": "2455",
            "shortName": "ОО «Махачкалинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Дагестан, г. Махачкала, ул. Танкаева, д. 54",
            "city": "Махачкала",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 42.980969,
                "longitude": 47.486222
            }
        },
        {
            "id": 29000161,
            "Biskvit_id": "5929",
            "shortName": "ДО «Профсоюзный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Профсоюзная, д. 15",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.679514,
                "longitude": 37.565335
            }
        },
        {
            "id": 29000328,
            "Biskvit_id": "2601",
            "shortName": "ДО «На Можайском шоссе» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Можайское ш., д. 45Б",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.716448,
                "longitude": 37.40698
            }
        },
        {
            "id": 41000022,
            "Biskvit_id": "0190",
            "shortName": "Дополнительный офис «На Думской» Ф. ОПЕРУ Банка ВТБ (ПАО) в Санкт-Петербурге",
            "address": "Российская Федерация, г. Санкт-Петербург, ул. Думская, д. 7, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.933176,
                "longitude": 30.327762
            }
        },
        {
            "id": 24002015,
            "Biskvit_id": "4414",
            "shortName": "ОО «Горно-Алтайский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Алтай, г. Горно-Алтайск, пр-т Коммунистический, д. 2",
            "city": "Горно-Алтайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.958881,
                "longitude": 85.967749
            }
        },
        {
            "id": 25014041,
            "Biskvit_id": "3364",
            "shortName": "ОО «Дербышки» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Мира, д. 33",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.863666,
                "longitude": 49.222512
            }
        },
        {
            "id": 27003002,
            "Biskvit_id": "1654",
            "shortName": "ОО «Артем» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Артем, пл. Ленина, д. 3",
            "city": "Артем",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.354902,
                "longitude": 132.180887
            }
        },
        {
            "id": 27003004,
            "Biskvit_id": "1554",
            "shortName": "ОО «Первомайский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, ул. Калинина, д. 277",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.093913,
                "longitude": 131.904466
            }
        },
        {
            "id": 24005003,
            "Biskvit_id": "1940",
            "shortName": "ОО «Иркутский тракт» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, Иркутский тракт, д. 26",
            "city": "Томск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.502877,
                "longitude": 85.006399
            }
        },
        {
            "id": 23006026,
            "Biskvit_id": "3905",
            "shortName": "ОО «Шахтинский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Шахты, ул. Советская, д. 147",
            "city": "Шахты",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.707703,
                "longitude": 40.217387
            }
        },
        {
            "id": 27003008,
            "Biskvit_id": "2454",
            "shortName": "ОО «Арсеньевский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Арсеньев, ул. Калининская, д. 2",
            "city": "Арсеньев",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.158326,
                "longitude": 133.265297
            }
        },
        {
            "id": 27003001,
            "Biskvit_id": "1854",
            "shortName": "ОО «Лесозаводский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Лесозаводск, ул. Пушкинская, д. 14",
            "city": "Лесозаводск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.464379,
                "longitude": 133.38992
            }
        },
        {
            "id": 29000112,
            "Biskvit_id": "3627",
            "shortName": "ДО «Перовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Владимирская 2-я, д. 45",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.749359,
                "longitude": 37.786267
            }
        },
        {
            "id": 29000080,
            "Biskvit_id": "3710",
            "shortName": "ДО «Новогиреево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Свободный пр-т, д. 20",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.750859,
                "longitude": 37.815983
            }
        },
        {
            "id": 29000085,
            "Biskvit_id": "4710",
            "shortName": "ДО «ВДНХ» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, пр-т Мира, д. 180",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.824253,
                "longitude": 37.645896
            }
        },
        {
            "id": 25011017,
            "Biskvit_id": "3462",
            "shortName": "ОО «На Первомайской» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Первомайская, д. 52",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.812317,
                "longitude": 56.091633
            }
        },
        {
            "id": 27003015,
            "Biskvit_id": "5485",
            "shortName": "ОО в г. Владивостоке Филиала в г. Хабаровске",
            "address": "Приморский край, г. Владивосток, ул. Светланская, д. 78",
            "city": "Владивосток",
            "scheduleFl": "Не обслуживает ФЛ",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 0,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.114601,
                "longitude": 131.909074
            }
        },
        {
            "id": 24005005,
            "Biskvit_id": "2440",
            "shortName": "ОО «Каштак» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Томская область, г. Томск, ул. Говорова, д. 46",
            "city": "Томск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.510293,
                "longitude": 84.984498
            }
        },
        {
            "id": 25013010,
            "Biskvit_id": "3142",
            "shortName": "ОО «Лидер» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Пермь, ул. Маршала Рыбалко, д. 28",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.003178,
                "longitude": 55.948765
            }
        },
        {
            "id": 29000064,
            "Biskvit_id": "1810",
            "shortName": "ДО «На Енисейской» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Енисейская, д.11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.865288,
                "longitude": 37.661437
            }
        },
        {
            "id": 26000040,
            "Biskvit_id": "1206",
            "shortName": "ДО № 12 «Наличная, 51» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Наличная, д. 51, лит. А",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.951101,
                "longitude": 30.234454
            }
        },
        {
            "id": 25013015,
            "Biskvit_id": "3342",
            "shortName": "ОО «Северный» в г. Березники Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Пермский край, г. Березники, ул. Пятилетки, д. 43",
            "city": "Березники",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.40592,
                "longitude": 56.806943
            }
        },
        {
            "id": 26000021,
            "Biskvit_id": "3406",
            "shortName": "ДО № 22 «Сестрорецкий» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Курортный район, г. Сестрорецк, ул. Володарского, д. 5, пом. 6-Н, лит.А",
            "city": "Сестрорецк",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.093474,
                "longitude": 29.972038
            }
        },
        {
            "id": 29000248,
            "Biskvit_id": "1100",
            "shortName": "ДО «Реутовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Реутов, ул. Ленина, д. 4",
            "city": "Реутов",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.754193,
                "longitude": 37.859183
            }
        },
        {
            "id": 25006024,
            "Biskvit_id": "2850",
            "shortName": "ОО «Проспект Циолковского» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Дзержинск, просп. Циолковского, д. 79, пом. п7",
            "city": "Дзержинск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.225938,
                "longitude": 43.396848
            }
        },
        {
            "id": 29000092,
            "Biskvit_id": "0401",
            "shortName": "ДО «Краснопрудный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Краснопрудная, д. 18, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.777287,
                "longitude": 37.662883
            }
        },
        {
            "id": 29000186,
            "Biskvit_id": "1703",
            "shortName": "ДО «Сухаревский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Б. Сухаревская пл., д. 14/7",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.771808,
                "longitude": 37.636671
            }
        },
        {
            "id": 29000427,
            "Biskvit_id": "2409",
            "shortName": "ДО «На Машинцева» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Химки, ул. Машинцева, строен. 5Б",
            "city": "Химки",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.890956,
                "longitude": 37.407825
            }
        },
        {
            "id": 29000200,
            "Biskvit_id": "3800",
            "shortName": "ДО «Жуковка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Одинцовский район, дер. Жуковка, д. 123-Б",
            "city": "д. Жуковка",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.737983,
                "longitude": 37.244134
            }
        },
        {
            "id": 29000650,
            "Biskvit_id": "3209",
            "shortName": "ДО «Некрасовка» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Рождественская, д. 29",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.707491,
                "longitude": 37.928632
            }
        },
        {
            "id": 26000069,
            "Biskvit_id": "3036",
            "shortName": "ДО № 60 «Наличная, 28» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Наличная, д. 28/16, лит. Б, пом. 13-Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.941249,
                "longitude": 30.231148
            }
        },
        {
            "id": 25014022,
            "Biskvit_id": "3264",
            "shortName": "ОО «На Мира» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Набережные Челны, пр-т Мира, д. 24 К (7/20)",
            "city": "Набережные Челны",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.730248,
                "longitude": 52.395586
            }
        },
        {
            "id": 25014026,
            "Biskvit_id": "2764",
            "shortName": "ОО «Нижнекамский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Нижнекамск, пр-т Мира, д. 61В",
            "city": "Нижнекамск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.645329,
                "longitude": 51.806211
            }
        },
        {
            "id": 21013014,
            "Biskvit_id": "2921",
            "shortName": "ОО «Льговский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Курская область, г. Льгов, ул. К. Маркса, д. 1/6",
            "city": "Льгов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.686238,
                "longitude": 35.277488
            }
        },
        {
            "id": 25015015,
            "Biskvit_id": "0918",
            "shortName": "ДО «Новокуйбышевский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Новокуйбышевск, ул. Коммунистическая, д. 39",
            "city": "Новокуйбышевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.09861,
                "longitude": 49.947336
            }
        },
        {
            "id": 25015017,
            "Biskvit_id": "0618",
            "shortName": "ДО «Солнечный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Ново-Садовая, д. 182",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.237995,
                "longitude": 50.192306
            }
        },
        {
            "id": 25015037,
            "Biskvit_id": "1928",
            "shortName": "ДО «Южный город» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, пос. Придорожный, пр-т Николаевский, д. 35",
            "city": "п. Придорожный",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.111184,
                "longitude": 50.142441
            }
        },
        {
            "id": 24004001,
            "Biskvit_id": "1371",
            "shortName": "ДО «Северобайкальский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Бурятия, г. Северобайкальск, Ленинградский пр-т, д. 5/1А",
            "city": "Северобайкальск",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.634923,
                "longitude": 109.336729
            }
        },
        {
            "id": 25011010,
            "Biskvit_id": "1962",
            "shortName": "ОО «Черниковский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Первомайская, д. 44",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.813921,
                "longitude": 56.086656
            }
        },
        {
            "id": 27007000,
            "Biskvit_id": "2954",
            "shortName": "РОО «Хабаровский»",
            "address": "Хабаровский край, г. Хабаровск, ул. Муравьева-Амурского, д. 18",
            "city": "Хабаровск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.473749,
                "longitude": 135.060311
            }
        },
        {
            "id": 23006261,
            "Biskvit_id": "4158",
            "shortName": "ОО «Парк Гагарина» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Каменск-Шахтинский, пр-т Карла Маркса, д. 71",
            "city": "Каменск-Шахтинский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.320706,
                "longitude": 40.269444
            }
        },
        {
            "id": 22006047,
            "Biskvit_id": "1602",
            "shortName": "ДО «Серовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Серов, ул. Льва Толстого, д. 32",
            "city": "Серов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.603961,
                "longitude": 60.581296
            }
        },
        {
            "id": 24006050,
            "Biskvit_id": "3307",
            "shortName": "ОО «Юргинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Юрга, ул. Московская, д. 11",
            "city": "Юрга",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.721219,
                "longitude": 84.932135
            }
        },
        {
            "id": 23008035,
            "Biskvit_id": "2755",
            "shortName": "ДО «Морской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Сочи, Адлеровский район, ул. Ульянова, д. 80Б",
            "city": "Сочи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.431266,
                "longitude": 39.925147
            }
        },
        {
            "id": 29000451,
            "Biskvit_id": "5401",
            "shortName": "ДО «Зарайский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Зарайск, пл. Бахрушиных, д. 1",
            "city": "Зарайск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.76582,
                "longitude": 38.878331
            }
        },
        {
            "id": 25007021,
            "Biskvit_id": "2352",
            "shortName": "ОО «На Тихой» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Энгельс, ул. Тихая, д. 55",
            "city": "Энгельс",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.496469,
                "longitude": 46.112967
            }
        },
        {
            "id": 29000013,
            "Biskvit_id": "4000",
            "shortName": "ДО «Люберецкий» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Люберцы, ул. Смирновская, д.2",
            "city": "Люберцы",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.67655,
                "longitude": 37.891172
            }
        },
        {
            "id": 29000344,
            "Biskvit_id": "3201",
            "shortName": "ДО «Киевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Киевская, д. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 cб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.74332,
                "longitude": 37.562694
            }
        },
        {
            "id": 21007004,
            "Biskvit_id": "1421",
            "shortName": "ДО «Площадь Петра Великого» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Липецкая область, г. Липецк, ул. Первомайская, д. 1",
            "city": "Липецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.614382,
                "longitude": 39.57148
            }
        },
        {
            "id": 23008028,
            "Biskvit_id": "2055",
            "shortName": "ДО «Красная площадь» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Краснодар, ул. им. Александра Покрышкина, д. 30",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.101834,
                "longitude": 38.980838
            }
        },
        {
            "id": 25009023,
            "Biskvit_id": "2657",
            "shortName": "ОО «На Кирова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Удмуртская Республика, г. Ижевск, ул. Кирова, д. 11",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.860713,
                "longitude": 53.18684
            }
        },
        {
            "id": 23008000,
            "Biskvit_id": "3459",
            "shortName": "РОО «Краснодарский»",
            "address": "Краснодарский край, г. Краснодар, ул. Красноармейская / ул. им. Гоголя, д. № 43/68",
            "city": "Краснодар",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 45.027674,
                "longitude": 38.967165
            }
        },
        {
            "id": 25009000,
            "Biskvit_id": "1057",
            "shortName": "РОО «Ижевский»",
            "address": "Удмуртская Республика, г. Ижевск, ул. Советская, д. 8а",
            "city": "Ижевск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.845106,
                "longitude": 53.209514
            }
        },
        {
            "id": 29000174,
            "Biskvit_id": "2300",
            "shortName": "ДО «Ленинградский проспект» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ленинградский пр-т, д. 60, корп. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.79934,
                "longitude": 37.536185
            }
        },
        {
            "id": 29000439,
            "Biskvit_id": "4201",
            "shortName": "ДО «Волоколамский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Волоколамск, ул. Ново-Солдатская, д. 5/1",
            "city": "Волоколамск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.030905,
                "longitude": 35.953946
            }
        },
        {
            "id": 21008029,
            "Biskvit_id": "1316",
            "shortName": "ОО «На Ленина» в г. Старом Осколе Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Белгородская область, г. Старый Оскол, ул. Ленина, д. 21/1",
            "city": "Старый Оскол",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.295552,
                "longitude": 37.836689
            }
        },
        {
            "id": 24006034,
            "Biskvit_id": "3207",
            "shortName": "ОО «Осинники» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Осинники, ул. Победы, д. 24/1",
            "city": "Осинники",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.597242,
                "longitude": 87.336548
            }
        },
        {
            "id": 21011003,
            "Biskvit_id": "4341",
            "shortName": "ОО «На Новоселов» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Рязанская область, г. Рязань, ул. Новоселов, д. 21в",
            "city": "Рязань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.61096,
                "longitude": 39.80506
            }
        },
        {
            "id": 24006048,
            "Biskvit_id": "2907",
            "shortName": "ОО «Березовский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Березовский, пр-т Ленина, д. 14",
            "city": "Березовский",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.668787,
                "longitude": 86.276032
            }
        },
        {
            "id": 24006031,
            "Biskvit_id": "1207",
            "shortName": "ОО «Проспект Шахтеров» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, пр-т Шахтеров, д. 26, пом. 284",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.779942,
                "longitude": 87.291183
            }
        },
        {
            "id": 29000343,
            "Biskvit_id": "3101",
            "shortName": "ДО «Московский» в г. Московском Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Moскoвский, мкр. 3-й, строен. 9а",
            "city": "Московский",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.427709,
                "longitude": 37.104724
            }
        },
        {
            "id": 23008181,
            "Biskvit_id": "2858",
            "shortName": "ДО «Анапский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, Анапский район, г. Анапа, ул. Ленина, д. 144б, пом.2",
            "city": "Анапа",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.877492,
                "longitude": 37.324228
            }
        },
        {
            "id": 22006039,
            "Biskvit_id": "3302",
            "shortName": "ДО «На Белинского» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Белинского, д. 222",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.79999,
                "longitude": 60.629401
            }
        },
        {
            "id": 29000301,
            "Biskvit_id": "2500",
            "shortName": "ДО «Семеновский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Семеновская пл., д. 7, корп. 17",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.78361,
                "longitude": 37.721301
            }
        },
        {
            "id": 29000091,
            "Biskvit_id": "0601",
            "shortName": "ДО «Измайловский бульвар» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Измайловский б-р, д. 46",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: 10:00-17:00",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.796344,
                "longitude": 37.805841
            }
        },
        {
            "id": 29000118,
            "Biskvit_id": "4727",
            "shortName": "ДО «Садовый-Триумфальный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Садовая-Триумфальная, д. 4/10, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.770431,
                "longitude": 37.599193
            }
        },
        {
            "id": 23008038,
            "Biskvit_id": "0455",
            "shortName": "ДО «Серебряковский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Новороссийск, Анапское шоссе, д. 18а",
            "city": "Новороссийск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.728177,
                "longitude": 37.757871
            }
        },
        {
            "id": 24006001,
            "Biskvit_id": "2807",
            "shortName": "ОО «Анжерский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Анжеро-Судженск, ул. Ленина, д. 12",
            "city": "Анжеро-Судженск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.081733,
                "longitude": 86.018342
            }
        },
        {
            "id": 24006000,
            "Biskvit_id": "2007",
            "shortName": "РОО «Кузбасский»",
            "address": "Кемеровская область, г. Кемерово, пр-т Ленина, д. 76",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 09:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.345155,
                "longitude": 86.117624
            }
        },
        {
            "id": 24006025,
            "Biskvit_id": "1807",
            "shortName": "ОО «Мариинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Мариинск, ул. Ленина, д. 105",
            "city": "Мариинск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.211859,
                "longitude": 87.739595
            }
        },
        {
            "id": 22006044,
            "Biskvit_id": "0612",
            "shortName": "ДО «Первоуральский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Первоуральск, ул. Ленина, д. 7",
            "city": "Первоуральск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.907205,
                "longitude": 59.950939
            }
        },
        {
            "id": 24006053,
            "Biskvit_id": "3113",
            "shortName": "ОО «Новокузнецкий» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, ул. Орджоникидзе, д. 29",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.76377,
                "longitude": 87.122937
            }
        },
        {
            "id": 24006055,
            "Biskvit_id": "3707",
            "shortName": "ОО «На Павловского» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Новокузнецк, ул. Павловского , д. 27",
            "city": "Новокузнецк",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.771737,
                "longitude": 87.134436
            }
        },
        {
            "id": 25007018,
            "Biskvit_id": "2152",
            "shortName": "ОО «На Тархова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Саратовская область, г. Саратов, ул. им. Тархова С.Ф., д.41/1",
            "city": "Саратов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.609788,
                "longitude": 46.015329
            }
        },
        {
            "id": 22006222,
            "Biskvit_id": "5122",
            "shortName": "ДО «Академический» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Академика Сахарова, д. 70",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.786587,
                "longitude": 60.515027
            }
        },
        {
            "id": 24006043,
            "Biskvit_id": "2507",
            "shortName": "ОО «Бульвар Строителей» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Кемерово, Ленинский район, бульвар Строителей, д. 16",
            "city": "Кемерово",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.350607,
                "longitude": 86.162198
            }
        },
        {
            "id": 29000284,
            "Biskvit_id": "1027",
            "shortName": "ДО «Даниловский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Люсиновская, д. 72, помещ. 7/1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.713699,
                "longitude": 37.621839
            }
        },
        {
            "id": 29000104,
            "Biskvit_id": "2327",
            "shortName": "ДО «Курский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Земляной вал, д. 27, стр. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.759035,
                "longitude": 37.658293
            }
        },
        {
            "id": 29000078,
            "Biskvit_id": "3910",
            "shortName": "ДО «На Каменке» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Зеленоград, ул. Каменка, кор. 1805",
            "city": "Зеленоград",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.979717,
                "longitude": 37.162692
            }
        },
        {
            "id": 25014045,
            "Biskvit_id": "1664",
            "shortName": "ОО «На Мавлютова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Татарстан, г. Казань, ул. Хусаина Мавлютова, д. 17",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.753651,
                "longitude": 49.189616
            }
        },
        {
            "id": 24009001,
            "Biskvit_id": "3240",
            "shortName": "ОО «Абаканский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Республика Хакасия, г. Абакан, ул. Вяткина, д. 21",
            "city": "Абакан",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.72137,
                "longitude": 91.4474
            }
        },
        {
            "id": 24009048,
            "Biskvit_id": "2646",
            "shortName": "ОО «Зеленогорский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Зеленогорск, ул. Ленина, д. 20",
            "city": "Зеленогорск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.10916,
                "longitude": 94.585341
            }
        },
        {
            "id": 25010000,
            "Biskvit_id": "1061",
            "shortName": "РОО «Оренбургский»",
            "address": "Оренбургская область, г. Оренбург, ул. Постникова, д. 9б",
            "city": "Оренбург",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.767753,
                "longitude": 55.092518
            }
        },
        {
            "id": 25013000,
            "Biskvit_id": "2042",
            "shortName": "РОО «Пермский»",
            "address": "Пермский край, г. Пермь, ул. Ленина, д. 22а/24",
            "city": "Пермь",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.014536,
                "longitude": 56.251111
            }
        },
        {
            "id": 24004000,
            "Biskvit_id": "1071",
            "shortName": "РОО «Улан-Удэнский»",
            "address": "Республика Бурятия, г. Улан-Удэ, ул. Хоца Намсараева, д. 2А",
            "city": "Улан-Удэ",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.841042,
                "longitude": 107.592668
            }
        },
        {
            "id": 41025001,
            "Biskvit_id": "3160",
            "shortName": "ОО «Вологодский» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Вологда, ул. Челюскинцев, д. 9",
            "city": "Вологда",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.217217,
                "longitude": 39.880231
            }
        },
        {
            "id": 24006024,
            "Biskvit_id": "2707",
            "shortName": "ОО «Кольчугинский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Ленинск-Кузнецкий, пр-т Кирова, д. 67",
            "city": "Ленинск-Кузнецкий",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.671883,
                "longitude": 86.174244
            }
        },
        {
            "id": 22006036,
            "Biskvit_id": "3822",
            "shortName": "ДО «Верхняя Пышма» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Верхняя Пышма, ул. Успенский пр-т, д. 42",
            "city": "Верхняя Пышма",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.976589,
                "longitude": 60.563024
            }
        },
        {
            "id": 27002006,
            "Biskvit_id": "3356",
            "shortName": "ДО «Сковородинский» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Амурская область, г. Сковородино, ул. Победы, д. 40А",
            "city": "Сковородино",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.978255,
                "longitude": 123.938889
            }
        },
        {
            "id": 23006028,
            "Biskvit_id": "2505",
            "shortName": "ОО «Южный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, ул. Большая Садовая/пр-т Соколова, 77/24",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.221044,
                "longitude": 39.718894
            }
        },
        {
            "id": 21002121,
            "Biskvit_id": "1017",
            "shortName": "ДО «Фурмановский» Филиала № 3652 Банка ВТБ (ПАО)",
            "address": "Ивановская область, г. Фурманов, ул. Социалистическая, д. 10",
            "city": "Фурманов",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.249085,
                "longitude": 41.108075
            }
        },
        {
            "id": 23006032,
            "Biskvit_id": "1705",
            "shortName": "ОО «Купеческий» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Ростовская область, г. Ростов-на-Дону, пр-т. Буденновский, 91/258",
            "city": "Ростов-на-Дону",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 1,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 47.22332,
                "longitude": 39.721813
            }
        },
        {
            "id": 27007032,
            "Biskvit_id": "1356",
            "shortName": "ДО «Советская Гавань» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, г. Советская Гавань, ул. Пионерская, д. 12",
            "city": "Советская Гавань",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 48.968457,
                "longitude": 140.283843
            }
        },
        {
            "id": 27007033,
            "Biskvit_id": "2256",
            "shortName": "ДО «Ванино» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Хабаровский край, пос. Ванино, пер. Торговый, д. 10",
            "city": "п. Ванино",
            "scheduleFl": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 49.09042,
                "longitude": 140.263802
            }
        },
        {
            "id": 29000298,
            "Biskvit_id": "3629",
            "shortName": "ДО «Домодедовский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Генерала Белова, д. 33А",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.612273,
                "longitude": 37.722127
            }
        },
        {
            "id": 29000197,
            "Biskvit_id": "0203",
            "shortName": "ДО «Солнечногорский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Солнечногорск, ул. Красная, д. 60",
            "city": "Солнечногорск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.18448,
                "longitude": 36.984314
            }
        },
        {
            "id": 29000288,
            "Biskvit_id": "0101",
            "shortName": "ДО «Басманный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Новая Басманная, 37 А",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.76997,
                "longitude": 37.669082
            }
        },
        {
            "id": 29000244,
            "Biskvit_id": "0803",
            "shortName": "ДО «Павлово-Посадский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Павловский Посад, ул. Кирова, д. 4",
            "city": "Павловский Посад",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.779575,
                "longitude": 38.653581
            }
        },
        {
            "id": 29000242,
            "Biskvit_id": "1425",
            "shortName": "ДО «Можайское шоссе» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Одинцовский район, г-кое поселение Одинцово, г. Одинцово, Можайское шоссе., д. 81",
            "city": "Одинцово",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.679032,
                "longitude": 37.283516
            }
        },
        {
            "id": 29000291,
            "Biskvit_id": "2725",
            "shortName": "ДО «На Советской» в г. Балашихе Флиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Балашиха, ул. Советская, д. 19а",
            "city": "Балашиха",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.803135,
                "longitude": 37.934633
            }
        },
        {
            "id": 29000023,
            "Biskvit_id": "1327",
            "shortName": "ДО «Долгоруковский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Долгоруковская, д. 40",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.778735,
                "longitude": 37.602023
            }
        },
        {
            "id": 29000146,
            "Biskvit_id": "3429",
            "shortName": "ДО «Бабушкинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Менжинского, д. 21",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.868854,
                "longitude": 37.667447
            }
        },
        {
            "id": 24009041,
            "Biskvit_id": "2746",
            "shortName": "ОО «Копыловский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Ладо Кецховели, д. 26/1",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.014011,
                "longitude": 92.813971
            }
        },
        {
            "id": 24009042,
            "Biskvit_id": "2946",
            "shortName": "ОО «Правобережный» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, пр-т имени газеты Красноярский рабочий, д. 62",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.012385,
                "longitude": 92.970646
            }
        },
        {
            "id": 22001149,
            "Biskvit_id": "2563",
            "shortName": "ОО «Ленинский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "г. Тюмень, ул. 50 лет Октября, д.39/3",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.147633,
                "longitude": 65.57857
            }
        },
        {
            "id": 29000258,
            "Biskvit_id": "1710",
            "shortName": "ДО «Центральный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Электросталь, пр-т Ленина, д. 30/13",
            "city": "Электросталь",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.791607,
                "longitude": 38.441094
            }
        },
        {
            "id": 24009038,
            "Biskvit_id": "2346",
            "shortName": "ОО «Красная Площадь» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Красноярский край, г. Красноярск, ул. Карла Маркса, д. 148А",
            "city": "Красноярск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.009346,
                "longitude": 92.839268
            }
        },
        {
            "id": 41019009,
            "Biskvit_id": "2026",
            "shortName": "ОО «Ленина, 78» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Мурманск, пр-т Ленина, д. 78",
            "city": "Мурманск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 68.967491,
                "longitude": 33.073283
            }
        },
        {
            "id": 29000141,
            "Biskvit_id": "2929",
            "shortName": "ДО «Савеловский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Бутырская, д. 11",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.79601,
                "longitude": 37.583391
            }
        },
        {
            "id": 22006361,
            "Biskvit_id": "1035",
            "shortName": "ДО «Березовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Березовский, ул. Театральная, д. 1",
            "city": "Березовский",
            "scheduleFl": "вт-сб: 10:00-19:00 вс, пн: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.906664,
                "longitude": 60.804042
            }
        },
        {
            "id": 22004071,
            "Biskvit_id": "5063",
            "shortName": "ОО «Тазовский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ЯНАО, Тазовский район, п.Тазовский, ул. Геофизиков, д. 27, пом.1",
            "city": "п. Тазовский",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.468081,
                "longitude": 78.7054
            }
        },
        {
            "id": 24006026,
            "Biskvit_id": "3007",
            "shortName": "ОО «Междуреченский» Филиала № 5440 Банка ВТБ (ПАО)",
            "address": "Кемеровская область, г. Междуреченск, ул. Чехова, д. 3",
            "city": "Междуреченск",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.689134,
                "longitude": 88.073912
            }
        },
        {
            "id": 29000024,
            "Biskvit_id": "3003",
            "shortName": "ДО «Центральный» в г. Подольске Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Подольск, ул. Комсомольская, д. 1, стр.1а, помещение I",
            "city": "Подольск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.427882,
                "longitude": 37.550109
            }
        },
        {
            "id": 22006051,
            "Biskvit_id": "0112",
            "shortName": "ДО «На ул. Маршала Жукова, д. 10» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Маршала Жукова, д. 5",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.838199,
                "longitude": 60.589821
            }
        },
        {
            "id": 41019006,
            "Biskvit_id": "1536",
            "shortName": "ДО «Апатиты» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Мурманская область, г. Апатиты, ул. Ферсмана, д. 23",
            "city": "Апатиты",
            "scheduleFl": "вт-пт: 10:00-18:00 сб: 10:00-17:00 вс, пн: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 67.566956,
                "longitude": 33.398284
            }
        },
        {
            "id": 41025012,
            "Biskvit_id": "4760",
            "shortName": "ОО № 17 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, пр-т Победы, д. 159",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.122377,
                "longitude": 37.992781
            }
        },
        {
            "id": 41025013,
            "Biskvit_id": "4160",
            "shortName": "ОО № 11 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Верещагина, д. 55",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.130952,
                "longitude": 37.91672
            }
        },
        {
            "id": 27003105,
            "Biskvit_id": "0654",
            "shortName": "ДО «Миллениум» Филиала № 2754 Банка ВТБ (ПАО)",
            "address": "Приморский край, г. Владивосток, п. Аякс, д. 10, лит. П",
            "city": "Владивосток",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.115542,
                "longitude": 131.885494
            }
        },
        {
            "id": 23007000,
            "Biskvit_id": "4655",
            "shortName": "ОО «Майкопский» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Республика Адыгея, г. Майкоп, ул. Пролетарская, д. 240А",
            "city": "Майкоп",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.673994,
                "longitude": 39.936645
            }
        },
        {
            "id": 23008036,
            "Biskvit_id": "0955",
            "shortName": "ДО «Туапсе» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Туапсе, ул. Октябрьской Революции, д. 5",
            "city": "Туапсе",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 44.096527,
                "longitude": 39.072538
            }
        },
        {
            "id": 22006018,
            "Biskvit_id": "0502",
            "shortName": "ДО «Предпринимательский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Крауля, д. 44",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.830477,
                "longitude": 60.56023
            }
        },
        {
            "id": 29000329,
            "Biskvit_id": "2801",
            "shortName": "ДО «Ходынский бульвар» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Ходынский бульвар, д. 2",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.789396,
                "longitude": 37.536832
            }
        },
        {
            "id": 26000065,
            "Biskvit_id": "2536",
            "shortName": "ДО № 54 «Ленинский, 151» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Ленинский пр-т, д. 151, лит. А, комн. №№ 117-140, 142, 153-173",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.851422,
                "longitude": 30.300983
            }
        },
        {
            "id": 29000249,
            "Biskvit_id": "4210",
            "shortName": "ДО «На Носовихинском» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Реутов, Носовихинское ш., вл. 17В",
            "city": "Реутов",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.747409,
                "longitude": 37.871993
            }
        },
        {
            "id": 29000009,
            "Biskvit_id": "2410",
            "shortName": "ДО «Подмосковный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Красногорск, ул. Ленина, д. 25а",
            "city": "Красногорск",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.827135,
                "longitude": 37.312019
            }
        },
        {
            "id": 29000034,
            "Biskvit_id": "0703",
            "shortName": "ДО «Клинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, Клинский р-н, г. Клин, ул. Гагарина, д. 26",
            "city": "Клин",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.327685,
                "longitude": 36.71552
            }
        },
        {
            "id": 29000043,
            "Biskvit_id": "5003",
            "shortName": "ДО «На Лавочкина» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Лавочкина, д. 34",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: 10:00-17:00",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.856341,
                "longitude": 37.493847
            }
        },
        {
            "id": 29000209,
            "Biskvit_id": "5510",
            "shortName": "ДО «Невский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Адмирала Макарова, д. 6, стр. 13",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.83566,
                "longitude": 37.490497
            }
        },
        {
            "id": 29000096,
            "Biskvit_id": "0325",
            "shortName": "ДО «Верхние Лихоборы» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Дмитровское ш., д. 64, кор. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 09:00-21:00 сб: 10:00-19:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.855361,
                "longitude": 37.562982
            }
        },
        {
            "id": 26000068,
            "Biskvit_id": "3236",
            "shortName": "ДО № 59 «Ленинский, 84» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, Ленинский пр-т, д. 84 к 1, лит. А, пом. 20Н (№1-17)",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.857653,
                "longitude": 30.199213
            }
        },
        {
            "id": 26000047,
            "Biskvit_id": "1906",
            "shortName": "ДО № 19 «М. Балканская, 26» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, ул. Малая Балканская, д. 26, лит. А, пом. 16Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.82978,
                "longitude": 30.385604
            }
        },
        {
            "id": 29000297,
            "Biskvit_id": "1025",
            "shortName": "ДО «Алексеевский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, пр-т Мира, д. 97",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.809105,
                "longitude": 37.636338
            }
        },
        {
            "id": 260023,
            "Biskvit_id": "4290",
            "shortName": "ДО № 29 «Пл. Карла Фаберже, 8» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "г. Санкт-Петербург, площадь Карла Фаберже, д. 8, лит. Б, пом. 10Н",
            "city": "Санкт-Петербург",
            "scheduleFl": "пн-пт: 10:00-20:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.935638,
                "longitude": 30.436054
            }
        },
        {
            "id": 29000252,
            "Biskvit_id": "5027",
            "shortName": "ДО «Серпуховский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "Московская область, г. Серпухов, ул. Чехова, д. 26",
            "city": "Серпухов",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.915875,
                "longitude": 37.416781
            }
        },
        {
            "id": 29000171,
            "Biskvit_id": "1800",
            "shortName": "ДО «Вешняки» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Вешняковская, д. 20Б",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: 10:00-15:00",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.721204,
                "longitude": 37.823062
            }
        },
        {
            "id": 29000107,
            "Biskvit_id": "2827",
            "shortName": "ДО «Митинский» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Митинская, д. 35",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.848013,
                "longitude": 37.355201
            }
        },
        {
            "id": 29000187,
            "Biskvit_id": "2303",
            "shortName": "ДО «На Маршала Бирюзова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Маршала Бирюзова, д. 8, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.792189,
                "longitude": 37.496794
            }
        },
        {
            "id": 29000082,
            "Biskvit_id": "4510",
            "shortName": "ДО «Проспект Маршала Жукова» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, просп. Маршала Жукова, д. 48, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.777793,
                "longitude": 37.465748
            }
        },
        {
            "id": 29000133,
            "Biskvit_id": "1829",
            "shortName": "ДО «Планерный» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, ул. Планерная, д. 7, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.863358,
                "longitude": 37.433508
            }
        },
        {
            "id": 41021002,
            "Biskvit_id": "2126",
            "shortName": "ОО «Ломоносова, 15» Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Новгородская область, г. Великий Новгород, ул. Ломоносова, д. 15",
            "city": "Великий Новгород",
            "scheduleFl": "пн-пт: 09:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 58.538633,
                "longitude": 31.24496
            }
        },
        {
            "id": 25010001,
            "Biskvit_id": "2461",
            "shortName": "ОО «Металлург» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская область, г. Новотроицк, ул. Советская, д. 85",
            "city": "Новотроицк",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-14:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 51.191388,
                "longitude": 58.28858
            }
        },
        {
            "id": 25015013,
            "Biskvit_id": "1519",
            "shortName": "ОО «Революционный» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Тольятти, ул. Революционная, д. 11-б",
            "city": "Тольятти",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.527196,
                "longitude": 49.276726
            }
        },
        {
            "id": 25015021,
            "Biskvit_id": "2218",
            "shortName": "ДО «Сквер Калинина» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, ул. Победы/ул. Воронежская д. 100/д. 5",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.229371,
                "longitude": 50.238803
            }
        },
        {
            "id": 25011002,
            "Biskvit_id": "1862",
            "shortName": "ОО «Октябрьский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Октябрьский, пр-т Ленина, д. 7",
            "city": "Октябрьский",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.482662,
                "longitude": 53.470394
            }
        },
        {
            "id": 25011019,
            "Biskvit_id": "2262",
            "shortName": "ОО «Демский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Уфа, ул. Правды, д. 21",
            "city": "Уфа",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 54.701943,
                "longitude": 55.828732
            }
        },
        {
            "id": 22005084,
            "Biskvit_id": "4263",
            "shortName": "ОО «Нефтеюганский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "ХМАО – Югра, г.Нефтеюганск, 16 мкр., здание 41",
            "city": "Нефтеюганск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.083701,
                "longitude": 72.613672
            }
        },
        {
            "id": 22005002,
            "Biskvit_id": "2715",
            "shortName": "ОО «Самотлорский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Нижневартовск, ул. Интернациональная д. 18а",
            "city": "Нижневартовск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10.00-17.00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.943169,
                "longitude": 76.605965
            }
        },
        {
            "id": 41025009,
            "Biskvit_id": "3460",
            "shortName": "ОО № 4 в г. Череповце Филиала № 7806 Банка ВТБ (ПАО)",
            "address": "Вологодская область, г. Череповец, ул. Ленина, д. 151",
            "city": "Череповец",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 59.129114,
                "longitude": 37.887795
            }
        },
        {
            "id": 25014000,
            "Biskvit_id": "2064",
            "shortName": "РОО «Банк ВТБ в Татарстане»",
            "address": "Республика Татарстан, г. Казань, ул. Островского, д. 84",
            "city": "Казань",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.781408,
                "longitude": 49.129007
            }
        },
        {
            "id": 25010004,
            "Biskvit_id": "1561",
            "shortName": "ДО «Бузулук» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Оренбургская обл., г. Бузулук, ул. Комсомольская, зд. №81, часть помещения №1",
            "city": "Бузулук",
            "scheduleFl": "пн-пт: 09:00-18:00 cб: 10:00-15:00 вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.786095,
                "longitude": 52.279057
            }
        },
        {
            "id": 21015000,
            "Biskvit_id": "2751",
            "shortName": "РОО «Орловский»",
            "address": "Орловская область, г. Орел, пер. Воскресенский, д. 18",
            "city": "Орел",
            "scheduleFl": "пн-пт: 09:00-19:00 cб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 52.962138,
                "longitude": 36.069398
            }
        },
        {
            "id": 25011006,
            "Biskvit_id": "2462",
            "shortName": "ОО «Ашкадарский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Республика Башкортостан, г. Стерлитамак, пр-т Ленина, д. 53",
            "city": "Стерлитамак",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.63572,
                "longitude": 55.936575
            }
        },
        {
            "id": 22005061,
            "Biskvit_id": "1163",
            "shortName": "ОО «На Мира» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Нижневартовск, ул. Мира, д. 20",
            "city": "Нижневартовск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 60.944685,
                "longitude": 76.563232
            }
        },
        {
            "id": 22005009,
            "Biskvit_id": "2015",
            "shortName": "ОО «На Мира» в г. Ханты-Мансийске Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Ханты-Мансийск, ул. Мира, д. 52",
            "city": "Ханты-Мансийск",
            "scheduleFl": "пн-пт: 10.00-19.00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 0,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.006717,
                "longitude": 69.036967
            }
        },
        {
            "id": 22005004,
            "Biskvit_id": "2615",
            "shortName": "ОО «Няганьский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Нягань, мкр. 2, д. 16",
            "city": "Нягань",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 10:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 62.143935,
                "longitude": 65.440095
            }
        },
        {
            "id": 22005014,
            "Biskvit_id": "1415",
            "shortName": "ОО «Сургутский» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Ханты-Мансийский автономный округ-Югра, г. Сургут, бульвар Свободы, д. 2, блок 2",
            "city": "Сургут",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 61.249149,
                "longitude": 73.401477
            }
        },
        {
            "id": 29000099,
            "Biskvit_id": "0725",
            "shortName": "ДО «Румянцево» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, п. Московский, Киевское шоссе, 22-й км, домовл. 4, стр.1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.640472,
                "longitude": 37.429798
            }
        },
        {
            "id": 22001015,
            "Biskvit_id": "4922",
            "shortName": "ОО «Корона» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Тюменская область, г. Тюмень, ул. Ленина, д. 38, корп. 1",
            "city": "Тюмень",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 57.154679,
                "longitude": 65.532558
            }
        },
        {
            "id": 23008032,
            "Biskvit_id": "1055",
            "shortName": "ДО «На Московской» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Сочи, ул. Московская, д. 5",
            "city": "Сочи",
            "scheduleFl": "пн-пт: 09:00-18:00 сб: 09:00-16:00 вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.592655,
                "longitude": 39.725334
            }
        },
        {
            "id": 25006033,
            "Biskvit_id": "2450",
            "shortName": "ОО «На Бекетова» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Нижегородская область, г. Нижний Новгород, ул. Бекетова, д. 13",
            "city": "Нижний Новгород",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.290609,
                "longitude": 43.998126
            }
        },
        {
            "id": 23008031,
            "Biskvit_id": "0555",
            "shortName": "ДО «Центральный» Филиала № 2351 Банка ВТБ (ПАО)",
            "address": "Краснодарский край, г. Сочи, ул. К. Либкнехта, д. 10",
            "city": "Сочи",
            "scheduleFl": "пн-пт: 09:00-19:00 сб, вс: выходной",
            "scheduleJurL": "пн-чт: 09:00-18:00 пт: 09:00-17:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 43.590611,
                "longitude": 39.724427
            }
        },
        {
            "id": 22006000,
            "Biskvit_id": "4323",
            "shortName": "РОО «Екатеринбургский»",
            "address": "Свердловская область, г. Екатеринбург, пр-т Ленина, д. 27",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 09:00-20:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.838435,
                "longitude": 60.596235
            }
        },
        {
            "id": 29000070,
            "Biskvit_id": "2910",
            "shortName": "ДО «Улица 1905 года» Филиала № 7701 Банка ВТБ (ПАО)",
            "address": "г. Москва, Звенигородское шоссе, д. 18/20, корп. 1",
            "city": "Москва",
            "scheduleFl": "пн-пт: 10:00-19:00 сб: 10:00-17:00 вс: выходной",
            "scheduleJurL": "пн-чт: 10:00-19:00 пт: 10:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 55.764323,
                "longitude": 37.556119
            }
        },
        {
            "id": 22006045,
            "Biskvit_id": "0522",
            "shortName": "ДО «На Герцена» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Первоуральск, ул. Герцена, д. 21",
            "city": "Первоуральск",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.901543,
                "longitude": 59.944561
            }
        },
        {
            "id": 25015019,
            "Biskvit_id": "1318",
            "shortName": "ДО ЦИК «Октябрьский» Филиала № 6318 Банка ВТБ (ПАО)",
            "address": "Самарская область, г. Самара, Октябрьский район, Московское шоссе д. 4, корп. 4",
            "city": "Самара",
            "scheduleFl": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "scheduleJurL": "пн-пт: 09:00-18:00 сб, вс: выходной",
            "special": {
                "vipZone": 1,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 1,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 53.204277,
                "longitude": 50.148388
            }
        },
        {
            "id": 22006037,
            "Biskvit_id": "2902",
            "shortName": "ДО «На Амундсена» Филиала № 6602 Банка ВТБ (ПАО)",
            "address": "Свердловская область, г. Екатеринбург, ул. Амундсена, д. 62, помещения № 51, 52, 50, 46",
            "city": "Екатеринбург",
            "scheduleFl": "пн-пт: 10:00-19:00 сб, вс: выходной",
            "scheduleJurL": "Не обслуживает ЮЛ",
            "special": {
                "vipZone": 0,
                "vipOffice": 0,
                "ramp": 1,
                "person": 1,
                "juridical": 0,
                "Prime": 0
            },
            "coordinates": {
                "latitude": 56.838011,
                "longitude": 60.597474
            }
        }
    ]
class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in data:
            Department.objects.filter(
                short_name=item.get('shortName'),
                address=item.get('address')
            ).update(biskvit_id=item.get('Biskvit_id'))

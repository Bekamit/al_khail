from django.test import TestCase

estate = [
    {
        "name": "Apartment",
        "name_ar": "شقة",
        "name_tr": "Daire",
        "name_ru": "Квартира",
        "developer": "Developer 1",
        "developer_ar": "مطور 1",
        "developer_tr": "Geliştirici 1",
        "developer_ru": "Застройщик 1",
        "area": 122.36,
        "district": "District 1",
        "district_ar": "المنطقة 1",
        "district_tr": "Bölge 1",
        "district_ru": "Район 1",
        "description": "Комфортная квартира с видом на город",
        "description_ar": "شقة مريحة تطل على المدينة",
        "description_tr": "Şehir manzaralı konforlu daire",
        "description_ru": "Comfortable apartment with city view",
        "type_id": 1,
        "city_id": 1,
        "is_secondary": true
    },
    {
        "name": "Land Plot",
        "name_ar": "قطعة أرض",
        "name_tr": "Arazi",
        "name_ru": "Участок",
        "developer": "Developer 2",
        "developer_ar": "مطور 2",
        "developer_tr": "Geliştirici 2",
        "developer_ru": "Застройщик 2",
        "area": 250.0,
        "district": "District 2",
        "district_ar": "المنطقة 2",
        "district_tr": "Bölge 2",
        "district_ru": "Район 2",
        "description": "Просторный участок с потрясающим видом",
        "description_ar": "قطعة أرض واسعة مع إطلالة رائعة",
        "description_tr": "Muhteşem manzaralı geniş arazi",
        "description_ru": "Spacious land plot with stunning view",
        "type_id": 5,
        "city_id": 2,
        "is_secondary": false
    },
    {
        "name": "Villa",
        "name_ar": "فيلا",
        "name_tr": "Villa",
        "name_ru": "Вилла",
        "developer": "Developer 3",
        "developer_ar": "مطور 3",
        "developer_tr": "Geliştirici 3",
        "developer_ru": "Застройщик 3",
        "area": 350.0,
        "district": "District 3",
        "district_ar": "المنطقة 3",
        "district_tr": "Bölge 3",
        "district_ru": "Район 3",
        "description": "Изысканная вилла с садом и бассейном",
        "description_ar": "فيلا فاخرة مع حديقة ومسبح",
        "description_tr": "Bahçe ve havuzlu şık villa",
        "description_ru": "Elegant villa with garden and pool",
        "type_id": 2,
        "city_id": 3,
        "is_secondary": true
    },
    {
        "name": "Shop",
        "name_ar": "متجر",
        "name_tr": "Mağaza",
        "name_ru": "Магазин",
        "developer": "Developer 4",
        "developer_ar": "مطور 4",
        "developer_tr": "Geliştirici 4",
        "developer_ru": "Застройщик 4",
        "area": 150.0,
        "district": "District 4",
        "district_ar": "المنطقة 4",
        "district_tr": "Bölge 4",
        "district_ru": "Район 4",
        "description": "Просторный магазин в центре города",
        "description_ar": "متجر واسع في وسط المدينة",
        "description_tr": "Şehir merkezinde geniş mağaza",
        "description_ru": "Spacious shop in the city center",
        "type_id": 4,
        "city_id": 4,
        "is_secondary": false
    },
    {
        "name": "Duplex",
        "name_ar": "دوبلكس",
        "name_tr": "Dubleks",
        "name_ru": "Дуплекс",
        "developer": "Developer 5",
        "developer_ar": "مطور 5",
        "developer_tr": "Geliştirici 5",
        "developer_ru": "Застройщик 5",
        "area": 200.0,
        "district": "District 5",
        "district_ar": "المنطقة 5",
        "district_tr": "Bölge 5",
        "district_ru": "Район 5",
        "description": "Просторный дуплекс с современным дизайном",
        "description_ar": "دوبلكس واسع بتصميم عصري",
        "description_tr": "Modern tasarımlı geniş dubleks",
        "description_ru": "Spacious duplex with modern design",
        "type_id": 3,
        "city_id": 5,
        "is_secondary": true
    }
]

estate_types = {
    {
        "type": "apartments",
        "type_ar": "شقق",
        "type_tr": "apartmanlar",
        "type_ru": "квартира"
    },
    {
        "type": "villa",
        "type_ar": "فيللا",
        "type_tr": "villa",
        "type_ru": "вилла"
    },
    {
        "type": "duplex",
        "type_ar": "دوبلكس",
        "type_tr": "duplex",
        "type_ru": "дуплекс"
    },
    {
        "type": "shop",
        "type_ar": "متجر",
        "type_tr": "mağaza",
        "type_ru": "магазин"
    },
    {
        "type": "land",
        "type_ar": "أرض",
        "type_tr": "arazi",
        "type_ru": "участок"
    }
}

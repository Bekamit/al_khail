from django.test import TestCase

# Test data

cities = [
    {
        "city_name": "Istanbul",
        "city_name_ar": "استانبول",
        "city_name_tr": "İstanbul",
        "city_name_ru": "Стамбул",
        "description": "Vibrant city straddling Europe and Asia, rich in history and culture.",
        "description_ar": "مدينة نابضة تقع بين أوروبا وآسيا، غنية بالتاريخ والثقافة.",
        "description_tr": "Avrupa ve Asya'nın kucaklaştığı dinamik şehir, zengin tarih ve kültüre sahip.",
        "description_ru": "Живописный город на стыке Европы и Азии, богат историей и культурой."
    },
    {
        "city_name": "Ankara",
        "city_name_ar": "أنقرة",
        "city_name_tr": "Ankara",
        "city_name_ru": "Анкара",
        "description": "Capital city of Turkey, known for its modern architecture and historic sites.",
        "description_ar": "عاصمة تركيا، مشهورة بعمارتها الحديثة والمواقع التاريخية.",
        "description_tr": "Türkiye'nin başkenti, modern mimarisi ve tarihi siteleri ile ünlü.",
        "description_ru": "Столица Турции, известная своей современной архитектурой и историческими памятниками."
    },
    {
        "city_name": "Izmir",
        "city_name_ar": "إزمير",
        "city_name_tr": "İzmir",
        "city_name_ru": "Измир",
        "description": "Coastal city with a Mediterranean atmosphere, home to ancient ruins.",
        "description_ar": "مدينة ساحلية ذات جو متوسطي، موطن للآثار القديمة.",
        "description_tr": "Akdeniz atmosferine sahip sahil şehri, antik kalıntılara ev sahipliği yapıyor.",
        "description_ru": "Прибрежный город с средиземноморской атмосферой, дом для древних развалин."
    },
    {
        "city_name": "Antalya",
        "city_name_ar": "أنطاليا",
        "city_name_tr": "Antalya",
        "city_name_ru": "Анталья",
        "description": "Turquoise coast city known for its stunning beaches and historical sites.",
        "description_ar": "مدينة على الساحل الأخضر مشهورة بشواطئها الرائعة والمواقع التاريخية.",
        "description_tr": "Berrak turkuaz kıyısıyla ünlü şehir, etkileyici plajları ve tarihi siteleri ile.",
        "description_ru": "Город на берегу бирюзового побережья, известный своими потрясающими пляжами и историческими местами."
    },
    {
        "city_name": "Bursa",
        "city_name_ar": "برسا",
        "city_name_tr": "Bursa",
        "city_name_ru": "Бурса",
        "description": "Historic city known for its Ottoman architecture and silk production.",
        "description_ar": "مدينة تاريخية مشهورة بعمارتها العثمانية وإنتاجها للحرير.",
        "description_tr": "Osmanlı mimarisi ve ipek üretimi ile ünlü tarihi şehir.",
        "description_ru": "Исторический город, известный своей османской архитектурой и производством шелка."
    }
]



from django.test import TestCase

# Test data

CITIES = [
    {
        "city_name_en": "Istanbul",
        "city_name_ar": "استانبول",
        "city_name_tr": "İstanbul",
        "city_name_ru": "Стамбул",
        "city_description_en": "The benefits of buying property in Istanbul include a strategic location between Europe and"
                       " Asia, a diverse cultural heritage, economic activity, attractive views and investment "
                       "opportunities in a booming real estate market.",
        "city_description_ar": "تشمل فوائد شراء العقارات في إسطنبول الموقع الاستراتيجي بين أوروبا وآسيا، والتراث الثقافي"
                          " المتنوع، والنشاط الاقتصادي، والمناظر الجذابة، وفرص الاستثمار في سوق العقارات المزدهر.",
        "city_description_tr": "İstanbul'da mülk satın almanın faydaları arasında Avrupa ile Asya arasında stratejik "
                          "bir konum, çeşitli kültürel miras, ekonomik faaliyet, cazip manzaralar ve gelişen emlak "
                          "piyasasında yatırım fırsatları yer alıyor.",
        "city_description_ru": "Преимущества покупки недвижимости в Стамбуле включают стратегическое расположение между "
                          "Европой и Азией, разнообразие культурного наследия, экономическую активность, привлекательные "
                          "виды и инвестиционные возможности в быстроразвивающемся рынке недвижимости.",
    },
    {
        "city_name_en": "Antalya",
        "city_name_ar": "أنطاليا",
        "city_name_tr": "Antalya",
        "city_name_ru": "Анталья",
        "city_description_en": "Antalya is a city on the Mediterranean coast. Throughout its history, Antalya has been home to "
                       "many cultures and civilizations, combining natural attractions, traditional architecture and art."
                       "\n\nThis city offers you a unique life by the sea, filled with pleasant events. Currently, the "
                       "city has turned into a financial metropolis, where business is actively developing, and one of "
                       "the largest transport hubs in Turkey.",
        "city_description_ar": "أنطاليا هي مدينة على ساحل البحر الأبيض المتوسط. طوال تاريخها، كانت أنطاليا موطنًا للعديد "
                          " من الثقافات والحضارات، حيث جمعت بين المعالم الطبيعية والهندسة المعمارية والفنون التقليدية."
                          "توفر لك هذه المدينة حياة فريدة بجانب البحر، مليئة بالأحداث الممتعة. حاليا، تحولت "
                          "المدينة إلى مدينة مالية، حيث تتطور الأعمال التجارية بنشاط، وواحدة من أكبر مراكز النقل في تركيا",
        "city_description_tr": "Antalya Akdeniz kıyısında bir şehirdir. Antalya, tarihi boyunca birçok kültür ve medeniyete "
                          "ev sahipliği yapmış, doğal güzellikleri, geleneksel mimari ve sanatı bir araya getirmiştir. "
                          "\n\nBu şehir size deniz kenarında, keyifli etkinliklerle dolu eşsiz bir yaşam sunuyor. Şu "
                          "anda şehir, iş dünyasının aktif olarak geliştiği bir finans metropolüne ve Türkiye'nin en "
                          "büyük ulaşım merkezlerinden birine dönüştü.",
        "city_description_ru": "Анталья – город на средиземноморском побережье. На протяжении всей своей истории Анталья "
                          "является домом для множества культур и цивилизаций, соединяя природные достопримечательности,"
                          " традиционную архитектуру и искусство.\n\n Этот город предлагает вам уникальную жизнь у моря, "
                          "наполненную приятными событиями. На текущий момент город превратился в финансовый мегаполис, "
                          "где активно развивается бизнес, один из крупнейших транспортных хабов Турции.",
    },
    {
        "city_name_en": "Dubai",
        "city_name_ar": "المزايا",
        "city_name_tr": "Dubai",
        "city_name_ru": "Дубай",
        "city_description_en": "Historic city known for its Ottoman architecture and silk production.",
        "city_description_ar": "مدينة تاريخية مشهورة بعمارتها العثمانية وإنتاجها للحرير.",
        "city_description_tr": "Osmanlı mimarisi ve ipek üretimi ile ünlü tarihi şehir.",
        "city_description_ru": "Люксовый образ жизни: Дубай предлагает роскошные возможности для отдыха, шопинга и "
                          "развлечений, с множеством ресторанов, культурных событий и развлекательных комплексов. "
                          "Климатические условия: Теплый климат Дубая солнечен в течение большей части года, что "
                          "способствует активному образу жизни и отдыху на свежем воздухе.",
    }
]



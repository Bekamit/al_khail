from django.test import TestCase

translations = {
    'buy': {
        'en': 'buy',
        'ar': 'شراء',
        'tr': 'satın al',
        'ru': 'купить',
    },
    'commercial': {
        'en': 'commercial',
        'ar': 'تجاري',
        'tr': 'ticari',
        'ru': 'коммерческая',
    },
    'place_ad': {
        'en': 'place an ad',
        'ar': 'وضع إعلان',
        'tr': 'ilan vermek',
        'ru': 'разместить объявление',
    },
    'contact_us': {
        'en': 'contact us',
        'ar': 'اتصل بنا',
        'tr': 'bizimle iletişime geçin',
        'ru': 'связаться с нами',
    },
    'find_your_dream_home': {
        'en': 'find your dream home with us!',
        'ar': 'العثور على منزل أحلامك معنا!',
        'tr': 'bizimle hayalinizdeki evinizi bulun!',
        'ru': 'найдите свой дом мечты вместе с нами!',
    },
    'search': {
        'en': 'search',
        'ar': 'بحث',
        'tr': 'arama',
        'ru': 'поиск',
    },
    'city': {
        'en': 'city',
        'ar': 'مدينة',
        'tr': 'şehir',
        'ru': 'город',
    },
    'property_type': {
        'en': 'property type',
        'ar': 'نوع الملكية',
        'tr': 'mülk türü',
        'ru': 'тип недвижимости',
    },
    'popular_new_all': {
        'en': ['popular', 'new', 'all'],
        'ar': ['شائع', 'جديد', 'الكل'],
        'tr': ['popüler', 'yeni', 'hepsi'],
        'ru': ['популярное', 'новые', 'все'],
    },
    'our_properties': {
        'en': 'our properties',
        'ar': 'ممتلكاتنا',
        'tr': 'bizim mülklerimiz',
        'ru': 'наши объекты',
    },
    'why_our_company': {
        'en': 'why our company',
        'ar': 'لماذا شركتنا',
        'tr': 'neden şirketimiz',
        'ru': 'почему наша компания',
    },
    'similar_properties': {
        'en': 'similar properties',
        'ar': 'خصائص مماثلة',
        'tr': 'benzer özellikler',
        'ru': 'похожие объекты',
    },
    'download_catalog': {
        'en': 'download catalog',
        'ar': 'تحميل الكتالوج',
        'tr': 'katalog indir',
        'ru': 'скачать каталог',
    },
    'contact_us_section': {
        'en': 'contact us',
        'ar': 'اتصل بنا',
        'tr': 'bizimle iletişime geçin',
        'ru': 'связаться с нами',
    },
    'request_callback': {
        'en': 'request a callback',
        'ar': 'طلب مكالمة',
        'tr': 'geri arama isteği',
        'ru': 'заказать обратный звонок',
    },
    'sell_through_us': {
        'en': 'sell your apartment through our company!',
        'ar': 'بيع شقتك من خلال شركتنا!',
        'tr': 'dairenizi şirketimiz aracılığıyla satın!',
        'ru': 'продайте квартиру через нашу компанию!',
    },
    'fill_out_form': {
        'en': 'fill out the form below and our agent will contact you soon',
        'ar': 'املأ النموذج أدناه وسيتصل بك وكيلنا قريبًا',
        'tr': 'aşağıdaki formu doldurun ve acentemiz size yakında ulaşacaktır',
        'ru': 'заполните форму ниже, и наш агент свяжется с вами в ближайшее время',
    },
    'your_name': {
        'en': 'your name',
        'ar': 'اسمك',
        'tr': 'adınız',
        'ru': 'ваше имя',
    },
    'your_phone_number': {
        'en': 'your phone number',
        'ar': 'رقم هاتفك',
        'tr': 'telefon numaranız',
        'ru': 'ваш номер телефона',
    },
    'your_city': {
        'en': 'your city',
        'ar': 'مدينتك',
        'tr': 'şehriniz',
        'ru': 'ваш город',
    },
    'best_time_to_call': {
        'en': 'best time to call you',
        'ar': 'أفضل وقت للاتصال بك',
        'tr': 'sizi aramak için en iyi zaman',
        'ru': 'в какое время вам позвонить?',
    },
    'send': {
        'en': 'send',
        'ar': 'إرسال',
        'tr': 'gönder',
        'ru': 'отправить',
    },
}


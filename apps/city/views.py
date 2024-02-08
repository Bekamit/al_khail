from service.views import CustomListAPIView, CustomRetrieveAPIView

from .serializers import CitySerializer
from .models import City

from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter


@extend_schema(
    summary="Получить список городов/⏩cache_content",
    description="Класс представления CityListAPIView возвращает коллекцию из всех городов модели City"
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке,"
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен"
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["Cities"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
    examples=[
        OpenApiExample(
            "Cities Example",
            description="Вариант представления Городов",
            value=
            {
                "language": "TR",
                "cities": [
                    {
                        "id": 6,
                        "city_name": "Dubai",
                        "city_description": "Dubai'de yaşamanın birçok avantajı vardır:\r\n"
                                            "\r\n1. Ekonomik Büyüme: Şehir, canlı bir ekonomi ve birçok iş fırsatıyla "
                                            "birlikte geniş kariyer fırsatları sunmaktadır."
                                            "\r\n2. Uluslararası karakter: Dubai, Doğu ile Batı arasında benzersiz "
                                            "çeşitlilik ve kültürlerarası deneyimler sağlayan kültürel bir köprüdür."
                                            "\r\n3. Altyapı: Şehir, yüksek binalar, yenilikçi ulaşım sistemleri ve "
                                            "modern eğlence komplekslerini içeren modern altyapısıyla tanınmaktadır."
                                            "\r\n4. Güvenlik: Dubai, yaşamak için en güvenli yerlerden biri olarak "
                                            "kabul edilir; bu, sakinlere ve daimi sakinlere gönül rahatlığı sağlar."
                                            "\r\n5. Vergi avantajları: Gelir vergisinin olmaması ve düşük vergi "
                                            "oranları, girişimciler ve yüksek maaşlı profesyoneller için cazip faktörlerdir."
                                            "\r\n6. Eğitim ve Sağlık Hizmetinin Kalitesi: Şehir, yüksek kalitede eğitim"
                                            " ve sağlık hizmetleri sunarak aileler için cazip hale gelmektedir."
                                            "\r\n7. Lüks yaşam tarzı: Dubai, çeşitli restoranlar, kültürel etkinlikler "
                                            "ve eğlence kompleksleriyle lüks dinlenme, alışveriş ve eğlence fırsatları sunmaktadır."
                                            "\r\n8. İklim: Dubai'nin sıcak iklimi yılın büyük bölümünde güneşli olup, "
                                            "aktif bir yaşam tarzına ve açık havada dinlenmeye olanak sağlar.",
                        "city_img": "http://127.0.0.1:8000/media/cities/Dubai/dubai.jpg"
                    },
                ]
            }
        ),
    ],
)
class CityListAPIView(CustomListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    response_key = 'cities'


@extend_schema(
    summary="Получить город по id",
    description="Класс представления CityRetrieveAPIView возвращает один из всех городов модели City"
                "Мультиязычная модель! **ACCEPT-LANGUAGE** для вывода данных на заявленном языке,"
                "если его нет, отдача будет на языке по умолчанию **EN**. Атрибут может быть определен"
                "браузером или переопределен фронтендом.",
    methods=["GET"],
    tags=["Cities"],
    parameters=[
        OpenApiParameter(
            name='ACCEPT-LANGUAGE',
            type=str,
            location=OpenApiParameter.HEADER,
            description='Язык, на котором должны возвращаться данные (опционально).'
        ),
    ],
    examples=[
        OpenApiExample(
            "City Example",
            description="Вариант представления Города",
            value=
            {
                "language": "AR",
                "city": {
                    "id": 6,
                    "city_name": "المزايا",
                    "city_description": "العيش في دبي له العديد من المزايا:\r\n\r\n1. النمو "
                                        "الاقتصادي: توفر المدينة فرص عمل وافرة مع اقتصاد نابض بالحياة والعديد من الفرص "
                                        "التجارية.\r\n2. الطابع الدولي: تعتبر دبي جسراً ثقافياً بين الشرق والغرب، وتوفر تن"
                                        "وعاً فريداً وتجارب متعددة الثقافات.\r\n3. البنية التحتية: تشتهر المدينة ببنيتها"
                                        " التحتية الحديثة، بما في ذلك المباني الشاهقة وأنظمة النقل المبتكرة والمجمعات ا"
                                        "لترفيهية الحديثة.\r\n4. الأمان: تعتبر دبي من أكثر الأماكن أماناً للعيش، مما يوفر "
                                        "راحة البال للمقيمين والمقيمين الدائمين.\r\n5. المزايا الضريبية: يعد غياب ضريبة"
                                        " الدخل ومعدلات الضرائب المنخفضة من العوامل الجذابة لرواد الأعمال والمهنيين ذوي "
                                        "الأجور المرتفعة.\r\n6. جودة التعليم والرعاية الصحية: توفر المدينة خدمات تعليمية"
                                        " ورعاية صحية عالية الجودة، مما يجعلها جذابة للعائلات.\r\n7. نمط الحياة الفاخر"
                                        ": توفر دبي فرصاً فاخرة للترفيه والتسوق والترفيه، مع مجموعة متنوعة من المطاعم"
                                        " والفعاليات الثقافية والمجمعات الترفيهية.\r\n8. المناخ: مناخ دبي الدافئ "
                                        "مشمس معظم أيام السنة، مما يفضي إلى نمط حياة نشط والاستجمام في الهواء الطلق.",
                    "city_img": "http://127.0.0.1:8000/media/cities/Dubai/dubai.jpg"
                }
            }
        ),
    ],
)
class CityRetrieveAPIView(CustomRetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'id'
    response_key = 'city'

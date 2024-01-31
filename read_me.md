**Обновление от 26.01.2024**

*Добавлено:*
- Текстовый редактор models.TextField для админ панели;
- Предотвращен Супер-пупер epic fail на продакшене;
- Добавлен выбор языка представления для пользователей админ панели;
- Объединено в 1 application Analytics обработка всех форм сайта;
- Добавлен CustomMiddleware для отслеживания обращений к админ панели;
- Мелкие настройки отображения данных в админ панели.


**Обновление от 24.01.2024**

*Добавлено:*
- Добавлен контекстный менеджер:
  - `python manage.py getstartcontent -a/--all` - все данные;
  - `python manage.py getstartcontent -t/--estate_type` - добавить виды недвижимости
  - `python manage.py getstartcontent -ct/--city` - добавить первые 3 города;
  - `python manage.py getstartcontent -c/--company` - добавить блок 'о компании';
  - `python manage.py getstartcontent -f/--facilities` - добавить преимущества;
  - `python manage.py getstartcontent -d/--default_value` - добавить дефолтные значения;
  

- Добавлен API 'пожожие объекты':
  - `api/v1/estate/{id}/similar/`


- Исправлено представление StaticData:
  - теперь staticdata.header, staticdata.body, ...
___

**Обновление от 13.01.2024**

*Добавлено:*
- Решена ошибка  Access-Control-Allow-Origin
- Коррекция CustomPagination

___

**Обновление от 12.01.2024**

*Для успешной работы обновления:*
- Обновить/удалить бд
- Удалить все миграции Estate
- Удалить все миграции Appeal
- Провести миграции после pull main

*Добавлено:*
- Пагинация EstateListView, CustomPagination
- Модель Project, на английском только!
- Добавлен PDF к Project
- Испралено представление Singleton моделей StaticData, Company
- Добавлне Search по description к модели Estate
- Добавлен фильтр по город_id, тип_недвижимости_id, is_secondary, проект_id
- Добавлен сортировка по дате создания карточки обьекта и по кол-ву просмотров обьекта
- Добавлены поля visits, project; заменено поле name -> title в модели Estate
- Исправлено представление EstateRetrieveView
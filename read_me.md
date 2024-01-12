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
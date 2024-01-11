# Используем официальный образ Nginx
FROM nginx:1.21.1

# Удаление стандартной конфигурации Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копирование нашей конфигурации в контейнер
COPY nginx.conf /etc/nginx/conf.d/

# Открываем порты 80 и 443
EXPOSE 80 443

# Копируем статические и медиа файлы
COPY /usr/src/app/back_static /usr/share/nginx/html/back_static
COPY /usr/src/app/back_media /usr/share/nginx/html/back_media

# Команда запуска Nginx в режиме daemon
CMD ["nginx", "-g", "daemon off;"]

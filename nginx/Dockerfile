# Этап настройка и создания Nginx
FROM nginx:latest

# Копируем конфигурацию
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
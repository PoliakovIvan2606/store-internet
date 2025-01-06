FROM nginx:latest

# Копируем конфигурацию Nginx в контейнер
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Указываем рабочую директорию
WORKDIR /app
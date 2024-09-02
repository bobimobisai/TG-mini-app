# TG Mini App

## Описание

Этот проект представляет собой мини-приложение, использующее Telegram Bot API и Flask для предоставления различных услуг. 

## Установка

Следуйте этим шагам, чтобы развернуть проект на вашем локальном компьютере:

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/bobimobisai/TG-mini-app.git

2. **Перейдите в директорию проекта:**

    ```bash
    cd TG-mini-app
    cd app


3. **Скачайте и установите Ngrok:**

    ```bash
    ngrok config add-authtoken 2TiRWPzg9P0JQfnxBYcrZsLJ2Rs_61SGxkBEabwZU3KYo2mNE
    sudo ngrok http 8050

!!! Скопируйте домен bз терминала который https и вставьте в .env HTTPS_URL

4. **Запустите контейнеры с помощью Docker Compose:**

    ```bash
    docker-compose up

Перейдите в бота нажмите кнопку Menu -> Выберите /start -> перейдите в веб приложение 

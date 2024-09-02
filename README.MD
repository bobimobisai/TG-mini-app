# TG Mini App

## Описание

Этот проект представляет собой мини-приложение, использующее Telegram Bot API и FastAPi
для предоставления различных услуг. 

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

!!! Скопируйте домен из терминала который https и вставьте в .env HTTPS_URL
Должен выглядеть так https://a3fc-94-181-225-220.ngrok-free.app


4. **пример**
    ```
    Found a bug? Let us know: https://github.com/ngrok/ngrok

    Session Status                online
    Account                       danilgrachev1992@gmail.com (Plan: Free)
    Version                       3.15.1
    Region                        Europe (eu)
    Latency                       57ms
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    https://a3fc-94-181-225-220.ngrok-free.app -> http://localhost:8050

    Connections                   ttl     opn     rt1     rt5     p50     p90
                                0       0       0.00    0.00    0.00    0.00

5. **Запустите контейнеры с помощью Docker Compose:**

    ```bash
    docker-compose up

Перейдите в бота нажмите кнопку Menu -> Выберите /start -> перейдите в веб приложение 

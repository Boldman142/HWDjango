# Настройки почты

EMAIL_HOST_USER = "vahtang-ashotovich@yandex.ru" #Почта откуда слать
EMAIL_HOST_PASSWORD = "klbvxnrgqitdchlz"  #Пароль для связи с SMTP сервером (типо апикея klbvxnrgqitdchlz  tpizybawjfixgvja )

# gmail_send/settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Всегда такой  (smtp поменять на console будет идти в консоль)
EMAIL_HOST = 'smtp.yandex.ru'  # Протокол связи, (для гугла -- smtp.gmail.com --)

EMAIL_PORT = 465  #
EMAIL_USE_TLS = False  #
EMAIL_USE_SSL = True  #

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER   # Откуда, если не указать в функции
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER


# Пас для базы

PASSWORD_BD = 'JutsU#69'

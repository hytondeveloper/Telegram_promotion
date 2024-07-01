from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Bместо str использовать SecretStr для конфиденциальных данных, например, токена бота (скрыто)
    bot_token: SecretStr

    # В данном случае будет использоваться файла .env, который будет прочитан с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file=['/home/user/PycharmProjects/Shaverma_Project/System_files/Config/.env'],
                                      env_file_encoding='utf-8')


# При импорте файла сразу создастся и провалидируется объект конфига, который можно далее импортировать из разных мест
config = Settings()
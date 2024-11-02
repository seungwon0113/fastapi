from app.configs.base_settings import Settings


def get_settings() -> Settings:
    """
    1. pydantic 은 기본적으로 (default 설정) "환경 변수" 에서 설정값을 읽는다.
    2. env_file 을 전달한다면 .env 를 읽는다.

    env_file 과 환경변수 중에서는 항상 환경변수가 우선한다.
    -> 환경변수에 MY_NAME=철수 라고 되어있고

    """
    return Settings(
        _env_file=".env",
        _env_file_encoding="utf-8",
    )


settings = get_settings()

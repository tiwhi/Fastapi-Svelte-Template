import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

import os
from dotenv import load_dotenv


class Settings(BaseSettings):
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) # PUT YOUR .ENV FILE IN fast-api-svelte-template/backend/app/
    load_dotenv(os.path.join(basedir, '.env')) # fast-api-svelte-template/backend/app/.env
    API_V1_STR: str # /api/v1
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    
    SQLALCHEMY_DATABASE_URI: str  # postgresql://postgres:[YOURDATABASEPASSWORD]@localhost:5432/[DATABASENAME]
    
    EMAIL_TEST_USER: EmailStr  # test@example.com 
    FIRST_SUPERUSER: EmailStr  # admin@example.com
    FIRST_SUPERUSER_PASSWORD: str 
    USERS_OPEN_REGISTRATION: bool # True
    EMAILS_ENABLED: bool = False
    
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:5000", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080", "http://localhost:49763", "http://localhost:8000"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings()

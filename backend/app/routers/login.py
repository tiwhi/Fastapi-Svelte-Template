from typing import Any, List

from datetime import timedelta
from app import crud, schemas, dependencies, models
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core import security
from app.core.security import create_access_token, get_password_hash
from app.core.config import settings


router = APIRouter()


@router.post("/token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(dependencies.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.get("/verify_token", response_model=schemas.TokenConfirm)
def verify_token(
    db: Session = Depends(dependencies.get_db),
    current_user: models.User = Depends(dependencies.get_current_active_user),
) -> Any:
    """
    Check if current token is valid.
    """
    if current_user:
        return {'status': 'valid'}
    else:
        return {'status': 'not valid'}

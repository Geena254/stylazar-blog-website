from datetime import timedelta
from typing import Annotated

from crud.crud_users import authenticate_user
from api.deps import SessionDep
from core.security import create_access_token, create_refresh_token, verify_token
from core.config import settings
from models.util import Token, Message
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordRequestForm
from core.exceptions import invalid_credentials

router = APIRouter(tags=["login"])

JWT_COOKIE = "refresh_token"


@router.post("/login/access_token", response_model=Token)
async def login_access_token(
    response: Response,
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    user = authenticate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise invalid_credentials("Incorrect username or password")

    access_token = await create_access_token(data={"sub": str(user.id)})

    refresh_token = await create_refresh_token(data={"sub": str(user.id)})
    max_age = settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60

    response.set_cookie(
        key=JWT_COOKIE,
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="Lax",
        max_age=max_age,
    )

    return Token(access_token=access_token, token_type="bearer")


@router.post("/refresh-token", response_model=Token)
async def refresh_access_token(request: Request) -> dict[str, str]:
    """Generates a new JWT access token from a refresh token"""
    refresh_token = request.cookies.get(JWT_COOKIE)
    if not refresh_token:
        raise invalid_credentials("Refresh token missing.")

    token_data = await verify_token(refresh_token)
    if not token_data:
        raise invalid_credentials("Invalid refresh token.")

    new_access_token = await create_access_token(data={"sub": str(token_data.user_id)})
    return {"access_token": new_access_token, "token_type": "bearer"}

@router.post("/validate-token")
async def validate_access_token(token:str):
    """"""
    token_data = await verify_token(token)
    if not token_data:
        return False
    return True


@router.delete("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout_user(response: Response):
    """"""
    response.delete_cookie(JWT_COOKIE)
    return Message(message="Logged out")


# TODO: Implement password reset token generation - forgotten
@router.post("/password/reset_token")
def get_reset_token():
    """"""
    raise NotImplementedError


# TODO: Implement password resetting - forgotten
@router.post("/password/reset")
def reset_password():
    """"""
    raise NotImplementedError

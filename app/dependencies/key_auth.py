from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from app.settings import settings

API_KEY_NAME = "X-AUTH-HEADER"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    api_key_header_in: str = Security(api_key_header),
):
    if api_key_header_in == settings.API_KEY.get_secret_value():
        return api_key_header_in
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

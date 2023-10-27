from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from gigachat.exceptions import AuthenticationError, ResponseError
from gigachat.models import Models


def _get_kwargs(
    *,
    access_token: Optional[str] = None,
    client_id: Optional[str] = None,
    session_id: Optional[str] = None,
    request_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}

    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    if client_id:
        headers["X-Client-ID"] = client_id
    if session_id:
        headers["X-Session-ID"] = session_id
    if request_id:
        headers["X-Request-ID"] = request_id

    return {
        "method": "GET",
        "url": "/models",
        "headers": headers,
    }


def _build_response(response: httpx.Response) -> Models:
    if response.status_code == HTTPStatus.OK:
        return Models(**response.json())
    elif response.status_code == HTTPStatus.UNAUTHORIZED:
        raise AuthenticationError(response.url, response.status_code, response.content, response.headers)
    else:
        raise ResponseError(response.url, response.status_code, response.content, response.headers)


def sync(
    client: httpx.Client,
    *,
    access_token: Optional[str] = None,
    client_id: Optional[str] = None,
    session_id: Optional[str] = None,
    request_id: Optional[str] = None,
) -> Models:
    """Возвращает массив объектов с данными доступных моделей"""
    kwargs = _get_kwargs(access_token=access_token, client_id=client_id, session_id=session_id, request_id=request_id)
    response = client.request(**kwargs)
    return _build_response(response)


async def asyncio(
    client: httpx.AsyncClient,
    *,
    access_token: Optional[str] = None,
    client_id: Optional[str] = None,
    session_id: Optional[str] = None,
    request_id: Optional[str] = None,
) -> Models:
    """Возвращает массив объектов с данными доступных моделей"""
    kwargs = _get_kwargs(access_token=access_token, client_id=client_id, session_id=session_id, request_id=request_id)
    response = await client.request(**kwargs)
    return _build_response(response)

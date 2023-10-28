import httpx
from .core import ApiError


def upload_to_presigned_url(*, presigned_url: str, file_path: str) -> None:
    with open(file_path, "rb") as file_to_upload:
        response = httpx.put(presigned_url, files={'file': file_to_upload})
        if response.status_code == 200:
            return
        else:
            raise ApiError(
                status_code=response.status_code, body=response.text)


def download_from_presigned_url(*, presigned_url: str) -> str:
    response = httpx.get(presigned_url)
    if response.status_code == 200:
        return response.text
    else:
        raise ApiError(
            status_code=response.status_code, body=response.text)

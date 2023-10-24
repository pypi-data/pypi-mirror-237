import os
import json
from typing import Iterable, Tuple, Sequence, Optional, Callable, IO
from datetime import date
from datetime import timedelta
from dataclasses import dataclass
import urllib.parse
import urllib.request
import base64

from .multipart import encode as multipart_encode
from . import protocol
from ..utils.progress import (
    progress_iter,
    progress_iter_with_sub_progress,
    ProgressInterface,
)
from ..core.error import UserError
from ..core.request import build_opener
from ..core.secret import Secret


@dataclass
class Protocol(protocol.Protocol):
    host: str
    api_key: Secret[str]
    recipients: Sequence[str] = ()
    subject: str = "BiomedIT file transfer"
    message: str = ""
    expires_at: Optional[date] = None
    send_email: bool = False
    chunk_size: int = 1024

    def upload(
        self,
        files: Sequence[str],
        two_factor_callback: Callable[[], str],
        progress: Optional[ProgressInterface] = None,
    ) -> bytes:
        if self.expires_at is None:
            expires_at = date.today() + timedelta(days=7)

        attachment_ids = [
            upload_attachment(
                self.host,
                self.api_key,
                file_name,
                progress=sub_progress,
                chunk_size=self.chunk_size,
            )
            for file_name, sub_progress in progress_iter_with_sub_progress(
                files, progress
            )
        ]

        msg = {
            "message": {
                "recipients": self.recipients,
                "subject": self.subject,
                "message": self.message,
                "expires_at": expires_at.strftime("%Y-%m-%d"),
                "send_email": self.send_email,
                "authorization": 3,
                "attachments": attachment_ids,
            }
        }
        return post(
            self.host + "message",
            json.dumps(msg).encode(),
            self.api_key,
            "application/json",
        )


def upload_attachment(
    host: str,
    api_key: Secret[str],
    file_path: str,
    chunk_size: int = 1024,
    progress: Optional[ProgressInterface] = None,
) -> str:
    with open(file_path, "rb") as stream:
        file_size = stream.seek(0, 2)
        stream.seek(0)
        n_chunks = 1 + (file_size - 1) // chunk_size
        file_name = os.path.basename(file_path)
        if n_chunks == 1:
            post_data: Iterable[Tuple[str, bytes]] = (
                multipart_encode("Filedata", file_name, stream.read()),
            )
        else:
            post_data = (
                multipart_encode(
                    "Filedata",
                    file_name,
                    chunk,
                    extra_data=(
                        ("name", file_name),
                        ("chunk", chunk_no),
                        ("chunks", n_chunks),
                    ),
                )
                for chunk_no, chunk in enumerate(chunk_iter(stream, chunk_size))
            )
        for content_type, data in progress_iter(
            post_data, progress, iterable_length=n_chunks
        ):
            attachment_id = post(host + "attachments", data, api_key, content_type)
    if not isinstance(attachment_id, bytes) or len(attachment_id) > 100:
        raise UserError(
            "LiquidFiles did not return a valid attachment_id. Something went wrong."
        )
    return attachment_id.decode()


def chunk_iter(stream: IO[bytes], chunk_size: int) -> Iterable[bytes]:
    while True:
        chunk = stream.read(chunk_size)
        if not chunk:
            return
        yield chunk


def post(url: str, data: bytes, api_key: Secret[str], content_type: str) -> bytes:
    auth = (
        "Basic "
        + base64.b64encode((api_key.reveal() + ":x").encode()).rstrip().decode()
    )
    request = urllib.request.Request(
        url,
        data,
        method="POST",
        headers={"Authorization": auth, "Content-Type": content_type},
    )
    with https_open(request) as response:
        response_text = response.read()
        return response_text


https_open = build_opener(
    default_opener=urllib.request.build_opener(
        urllib.request.HTTPSHandler(debuglevel=0)
    ).open
)

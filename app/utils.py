from pathlib import Path

from fastapi import UploadFile
from pydub import AudioSegment

from app.configs.settings import AUDIO_DIR, get_settings

settings = get_settings()


def generate_filename(audio_id: str) -> Path:
    return AUDIO_DIR / (audio_id + ".mp3")


def generate_download_url(user_id: str, audio_id: str) -> str:
    return (
        f"http://{settings.BUCKET_HOST}:{settings.BUCKET_PORT}/record?"
        f"id={audio_id}&user={user_id}"
    )


def convert_to_mp3(file_id: str, afile: UploadFile) -> None:
    AudioSegment.from_wav(afile.file).export(
        generate_filename(file_id), format="mp3"
    )

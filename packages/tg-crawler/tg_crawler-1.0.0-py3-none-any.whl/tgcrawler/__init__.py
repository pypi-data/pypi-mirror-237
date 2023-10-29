from pyrogram import Client as TgClient

from tgcrawler.utils import progress_bar

current_bytes = 0
total_bytes = 0


class Client:
    def __init__(self, api_id, api_hash, session_string):
        self.client = TgClient(":memory:", api_id=api_id, api_hash=api_hash, session_string=session_string)
        self.client.start()

    async def download(self, chat, message_id, show_progress):
        chat_ = await self.client.get_chat(chat)
        message = await self.client.get_messages(chat_.id, int(message_id))
        media = await self.client.download_media(
            message,
            progress=progress,
            progress_args=(show_progress, None),
        )
        self.client.stop()
        return media


async def progress(current, total, show_progress, n):
    """Set progress current and total"""
    global current_bytes
    global total_bytes
    current_bytes = current
    total_bytes = total
    if show_progress:
        progress_bar(
            current=current,
            total=total,
            desc="Downloading",
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            ncols=50,
        )


__version__ = "1.0.0"

import asyncio
import pathlib


class FilesHandler:
    @staticmethod
    async def create_directory(dir_name: str) -> None:
        dir_path: pathlib.Path = pathlib.Path(dir_name)
        if not dir_path.exists():
            await asyncio.get_event_loop().run_in_executor(None, directory_path.mkdir)
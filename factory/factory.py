from typing import Optional

from aiogram.filters.callback_data import CallbackData


class UserCallbackFactory(CallbackData, prefix="user"):
    page: str
    back_page: Optional[str]

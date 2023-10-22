from aiogram.filters.callback_data import CallbackData


class HrCallbackFactory(CallbackData, prefix='house_request'):
    house_request_id: int

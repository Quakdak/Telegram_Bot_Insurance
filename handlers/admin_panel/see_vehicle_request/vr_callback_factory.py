from aiogram.filters.callback_data import CallbackData


class VrCallbackFactory(CallbackData, prefix='vehicle_request'):
    vehicle_request_id: int

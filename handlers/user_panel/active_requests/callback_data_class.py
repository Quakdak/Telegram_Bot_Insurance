from aiogram.filters.callback_data import CallbackData


class HrActiveCallbackFactory(CallbackData, prefix='house_active_request'):
    request_id: int


class VrActiveCallbackFactory(CallbackData, prefix='vehicle_active_request'):
    request_id: int

from aiogram.filters.callback_data import CallbackData


class HrActiveCallbackFactory(CallbackData, prefix='house_active_request'):
    HR_request_id: int


class VrActiveCallbackFactory(CallbackData, prefix='vehicle_active_request'):
    VR_request_id: int

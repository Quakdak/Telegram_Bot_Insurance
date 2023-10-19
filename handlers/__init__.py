__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart

from handlers.start import start
from handlers.user_panel.apply_request import apply_request
from handlers.user_panel.request_for_transport.request_for_transport import request_for_transport
from handlers.user_panel.request_for_transport.start_inspection_transport import start_inspection_transport
from handlers.user_panel.request_for_transport.reference_photo_transport import reference_photo_transport
from handlers.user_panel.request_for_house.request_for_house import request_for_house
from handlers.user_panel.request_for_house.start_inspection_house import start_inspection_house
from handlers.user_panel.request_for_house.reference_photo_house import reference_photo_house


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(apply_request, F.data == 'apply_request')
    router.callback_query.register(request_for_transport, F.data == 'request_for_transport')
    router.callback_query.register(start_inspection_transport, F.data == 'start_inspection_transport')
    router.callback_query.register(reference_photo_transport, F.data == 'reference_photo_transport')
    router.callback_query.register(request_for_house, F.data == 'request_for_house')
    router.callback_query.register(start_inspection_house, F.data == 'start_inspection_house')
    router.callback_query.register(reference_photo_house, F.data == 'reference_photo_house')

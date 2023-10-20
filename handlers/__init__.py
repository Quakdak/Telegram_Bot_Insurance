__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart
from handlers.user_panel.state_request.state_request_transport import request_transport

from handlers.start import start
from handlers.done import done
from handlers.user_panel.apply_request import apply_request
from handlers.user_panel.request_for_transport.request_for_transport import request_for_transport
from handlers.user_panel.request_for_transport.start_inspection_transport import start_inspection_transport
from handlers.user_panel.request_for_transport.reference_photo_transport import reference_photo_transport
from handlers.user_panel.request_for_house.request_for_house import request_for_house
from handlers.user_panel.request_for_house.start_inspection_house import start_inspection_house
from handlers.user_panel.request_for_house.reference_photo_house import reference_photo_house

from handlers.user_panel.request_for_transport.add_photo.vin_number import vin_number, got_vin_number, \
    getting_vin_number
from handlers.user_panel.request_for_transport.add_photo.transport_outside import transport_outside, \
    got_transport_outside, getting_transport_outside
from handlers.user_panel.request_for_transport.add_photo.windshield import windshield, got_windshield, \
    getting_windshield
from handlers.user_panel.request_for_transport.add_photo.mark_windshield import mark_windshield, got_mark_windshield, \
    getting_mark_windshield
from handlers.user_panel.request_for_transport.add_photo.wheel import wheel, got_wheel, getting_wheel
from handlers.user_panel.request_for_transport.add_photo.odometer import odometer, got_odometer, getting_odometer
from handlers.user_panel.request_for_transport.add_photo.transport_inside import transport_inside, got_transport_inside, \
    getting_transport_inside
from handlers.user_panel.request_for_transport.add_photo.damage import damage, got_damage, getting_damage
from handlers.user_panel.request_for_transport.add_photo.key import key, got_key, getting_key

from handlers.user_panel.request_for_transport.end_inspection_transport import end_inspection_transport


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(apply_request, F.data == 'apply_request')

    router.callback_query.register(request_for_transport, F.data == 'request_for_transport')
    router.callback_query.register(start_inspection_transport, F.data == 'start_inspection_transport')
    router.callback_query.register(reference_photo_transport, F.data == 'reference_photo_transport')

    router.callback_query.register(request_for_house, F.data == 'request_for_house')
    router.callback_query.register(start_inspection_house, F.data == 'start_inspection_house')
    router.callback_query.register(reference_photo_house, F.data == 'reference_photo_house')

    router.callback_query.register(vin_number, F.data == 'vin_number')
    router.callback_query.register(vin_number, F.data == 'add_more_vin_number')
    router.message.register(getting_vin_number, F.photo, request_transport.wait_vin_number)
    router.callback_query.register(got_vin_number, F.data == 'end_add_vin_number')

    router.callback_query.register(transport_outside, F.data == 'transport_outside')
    router.callback_query.register(transport_outside, F.data == 'add_more_transport_outside')
    router.message.register(getting_transport_outside, F.photo, request_transport.wait_transport_outside)
    router.callback_query.register(got_transport_outside, F.data == 'end_add_transport_outside')

    router.callback_query.register(windshield, F.data == 'windshield')
    router.callback_query.register(windshield, F.data == 'add_more_windshield')
    router.message.register(getting_windshield, F.photo, request_transport.wait_windshield)
    router.callback_query.register(got_windshield, F.data == 'end_add_windshield')

    router.callback_query.register(mark_windshield, F.data == 'mark_windshield')
    router.callback_query.register(mark_windshield, F.data == 'add_more_mark_windshield')
    router.message.register(getting_mark_windshield, F.photo, request_transport.wait_mark_windshield)
    router.callback_query.register(got_mark_windshield, F.data == 'end_add_mark_windshield')

    router.callback_query.register(wheel, F.data == 'wheel')
    router.callback_query.register(wheel, F.data == 'add_more_wheel')
    router.message.register(getting_wheel, F.photo, request_transport.wait_wheel)
    router.callback_query.register(got_wheel, F.data == 'end_add_wheel')

    router.callback_query.register(odometer, F.data == 'odometer')
    router.callback_query.register(odometer, F.data == 'add_more_odometer')
    router.message.register(getting_odometer, F.photo, request_transport.wait_odometer)
    router.callback_query.register(got_odometer, F.data == 'end_add_odometer')

    router.callback_query.register(transport_inside, F.data == 'transport_inside')
    router.callback_query.register(transport_inside, F.data == 'add_more_transport_inside')
    router.message.register(getting_transport_inside, F.photo, request_transport.wait_transport_inside)
    router.callback_query.register(got_transport_inside, F.data == 'end_add_transport_inside')

    router.callback_query.register(damage, F.data == 'damage')
    router.callback_query.register(damage, F.data == 'add_more_damage')
    router.message.register(getting_damage, F.photo, request_transport.wait_damage)
    router.callback_query.register(got_damage, F.data == 'end_add_damage')

    router.callback_query.register(key, F.data == 'key')
    router.callback_query.register(key, F.data == 'add_more_key')
    router.message.register(getting_key, F.photo, request_transport.wait_key)
    router.callback_query.register(got_key, F.data == 'end_add_key')

    router.callback_query.register(end_inspection_transport, F.data == 'end_inspection_transport')
    router.callback_query.register(done, F.data == 'done')

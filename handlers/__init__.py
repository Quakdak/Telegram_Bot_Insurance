__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart
from handlers.user_panel.state_request.state_request_transport import request_transport

from handlers.start import start
from handlers.done import done
from handlers.user_panel.apply_request import apply_request
from handlers.user_panel.active_requests import active_requests
from handlers.user_panel.to_main import to_main
from handlers.user_panel.request_for_transport.request_for_transport import request_for_transport
from handlers.user_panel.request_for_transport.start_inspection_transport import start_inspection_transport
from handlers.user_panel.request_for_transport.reference_photo_transport import reference_photo_transport
from handlers.user_panel.request_for_house.request_for_house import request_for_house
from handlers.user_panel.request_for_house.start_inspection_house import start_inspection_house
from handlers.user_panel.request_for_house.reference_photo_house import reference_photo_house

from handlers.user_panel.request_for_transport.add_photo.vin_number import *
from handlers.user_panel.request_for_transport.add_photo.transport_outside import *
from handlers.user_panel.request_for_transport.add_photo.windshield import *
from handlers.user_panel.request_for_transport.add_photo.mark_windshield import *
from handlers.user_panel.request_for_transport.add_photo.wheel import *
from handlers.user_panel.request_for_transport.add_photo.odometer import *
from handlers.user_panel.request_for_transport.add_photo.transport_inside import *
from handlers.user_panel.request_for_transport.add_photo.damage import *
from handlers.user_panel.request_for_transport.add_photo.key import *

from handlers.user_panel.request_for_transport.end_inspection_transport import end_inspection_transport

from handlers.user_panel.request_for_house.add_photo.general_view_house import *
from handlers.user_panel.request_for_house.add_photo.outside_engineering import *
from handlers.user_panel.request_for_house.add_photo.facades_buildings import *
from handlers.user_panel.request_for_house.add_photo.mechanical_protection import *
from handlers.user_panel.request_for_house.add_photo.front_door import *
from handlers.user_panel.request_for_house.add_photo.inside_engineering import *
from handlers.user_panel.request_for_house.add_photo.fire_alarm_system import *
from handlers.user_panel.request_for_house.add_photo.security_alarm_system import *
from handlers.user_panel.request_for_house.add_photo.interior import *
from handlers.user_panel.request_for_house.add_photo.window import *
from handlers.user_panel.request_for_house.add_photo.defect import *
from handlers.user_panel.request_for_house.add_photo.household_property import *
from handlers.user_panel.request_for_house.add_photo.fence import *

from handlers.user_panel.request_for_house.end_inspection_house import end_inspection_house


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(apply_request, F.data == 'apply_request')
    router.callback_query.register(active_requests, F.data == 'active_requests')
    router.callback_query.register(to_main, F.data == 'to_main')
    router.callback_query.register(done, F.data == 'done')

    router.callback_query.register(request_for_transport, F.data == 'request_for_transport')
    router.callback_query.register(start_inspection_transport, F.data == 'start_inspection_transport')
    router.callback_query.register(reference_photo_transport, F.data == 'reference_photo_transport')
    router.callback_query.register(end_inspection_transport, F.data == 'end_inspection_transport')

    router.callback_query.register(request_for_house, F.data == 'request_for_house')
    router.callback_query.register(start_inspection_house, F.data == 'start_inspection_house')
    router.callback_query.register(reference_photo_house, F.data == 'reference_photo_house')
    router.callback_query.register(end_inspection_house, F.data == 'end_inspection_house')

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

    router.callback_query.register(general_view_house, F.data == 'general_view_house')
    router.callback_query.register(general_view_house, F.data == 'general_view_house')
    router.message.register(getting_general_view_house, F.photo, request_house.wait_general_view_house)
    router.callback_query.register(got_general_view_house, F.data == 'end_add_general_view_house')

    router.callback_query.register(outside_engineering, F.data == 'outside_engineering')
    router.callback_query.register(outside_engineering, F.data == 'add_more_outside_engineering')
    router.message.register(getting_outside_engineering, F.photo, request_house.wait_outside_engineering)
    router.callback_query.register(got_outside_engineering, F.data == 'end_add_outside_engineering')

    router.callback_query.register(facades_buildings, F.data == 'facades_buildings')
    router.callback_query.register(facades_buildings, F.data == 'add_more_facades_buildings')
    router.message.register(getting_facades_buildings, F.photo, request_house.wait_facades_buildings)
    router.callback_query.register(got_facades_buildings, F.data == 'end_add_facades_buildings')

    router.callback_query.register(mechanical_protection, F.data == 'mechanical_protection')
    router.callback_query.register(mechanical_protection, F.data == 'add_more_mechanical_protection')
    router.message.register(getting_mechanical_protection, F.photo, request_house.wait_mechanical_protection)
    router.callback_query.register(got_mechanical_protection, F.data == 'end_add_mechanical_protection')

    router.callback_query.register(front_door, F.data == 'front_door')
    router.callback_query.register(front_door, F.data == 'add_more_front_door')
    router.message.register(getting_front_door, F.photo, request_house.wait_front_door)
    router.callback_query.register(got_front_door, F.data == 'end_add_front_door')

    router.callback_query.register(inside_engineering, F.data == 'inside_engineering')
    router.callback_query.register(inside_engineering, F.data == 'add_more_inside_engineering')
    router.message.register(getting_inside_engineering, F.photo, request_house.wait_inside_engineering)
    router.callback_query.register(got_inside_engineering, F.data == 'end_add_inside_engineering')

    router.callback_query.register(fire_alarm_system, F.data == 'fire_alarm_system')
    router.callback_query.register(fire_alarm_system, F.data == 'fire_alarm_system')
    router.message.register(getting_fire_alarm_system, F.photo, request_house.wait_fire_alarm_system)
    router.callback_query.register(got_fire_alarm_system, F.data == 'end_add_fire_alarm_system')

    router.callback_query.register(security_alarm_system, F.data == 'security_alarm_system')
    router.callback_query.register(security_alarm_system, F.data == 'add_more_security_alarm_system')
    router.message.register(getting_security_alarm_system, F.photo, request_house.wait_security_alarm_system)
    router.callback_query.register(got_security_alarm_system, F.data == 'end_add_security_alarm_system')

    router.callback_query.register(key, F.data == 'key')
    router.callback_query.register(key, F.data == 'add_more_key')
    router.message.register(getting_key, F.photo, request_transport.wait_key)
    router.callback_query.register(got_key, F.data == 'end_add_key')

    router.callback_query.register(interior, F.data == 'interior')
    router.callback_query.register(interior, F.data == 'add_more_interior')
    router.message.register(getting_interior, F.photo, request_house.wait_interior)
    router.callback_query.register(got_interior, F.data == 'end_add_interior')

    router.callback_query.register(window, F.data == 'window')
    router.callback_query.register(window, F.data == 'add_more_window')
    router.message.register(getting_window, F.photo, request_house.wait_window)
    router.callback_query.register(got_window, F.data == 'end_add_window')

    router.callback_query.register(defect, F.data == 'defect')
    router.callback_query.register(defect, F.data == 'add_more_defect')
    router.message.register(getting_defect, F.photo, request_house.wait_defect)
    router.callback_query.register(got_defect, F.data == 'end_add_defect')

    router.callback_query.register(household_property, F.data == 'household_property')
    router.callback_query.register(household_property, F.data == 'add_more_household_property')
    router.message.register(getting_household_property, F.photo, request_house.wait_household_property)
    router.callback_query.register(got_household_property, F.data == 'end_add_household_property')

    router.callback_query.register(fence, F.data == 'fence')
    router.callback_query.register(fence, F.data == 'add_more_fence')
    router.message.register(getting_fence, F.photo, request_house.wait_fence)
    router.callback_query.register(got_fence, F.data == 'end_add_fence')

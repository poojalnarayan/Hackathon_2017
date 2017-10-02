from dronekit import connect, VehicleMode, LocationGlobalRelative
from time import sleep
import pygame
from pymavlink import mavutil

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for j in joysticks:
	j.init()

vehicle = connect("0.0.0.0:14561", wait_ready=True)

def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
	"""
	Move vehicle in direction based on specified velocity vectors.
	"""
	msg = vehicle.message_factory.set_position_target_local_ned_encode(
	0,       # time_boot_ms (not used)
	0, 0,    # target system, target component
	mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
	0b0000111111000111, # type_mask (only speeds enabled)
	0, 0, 0, # x, y, z positions (not used)
	velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
	0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
	0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
	vehicle.send_mavlink(msg)



while not vehicle.is_armable:
	print(" Waiting for vehicle to initialise...")
	sleep(1)
	print("Arming motors")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(10)
while True:
	if vehicle.location.global_relative_frame.alt > 9:
		break;
while(True):
	pygame.event.get()
	#for p in range(joysticks[0].get_numbuttons()):
	print(0 , " :" ,  joysticks[0].get_button(0))
	x = 0
	y = 0
	if joysticks[0].get_button(0):	# booster straight
		x+=50
	if joysticks[0].get_button(2):	#straight
		x+=10
	if joysticks[0].get_button(3):  #left
		y-=10
	if joysticks[0].get_button(1):  #right
		y+=10

	send_ned_velocity(x,y, 0, 1)	
	#point1 = LocationGlobalRelative(lat, lon, 0)
	#vehicle.simple_goto(point1)
'''
while True:
	while not vehicle.is_armable:
		print " Waiting for vehicle to initialise..."
		sleep(1)
		print "Arming motors"
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True
	vehicle.simple_takeoff(10)
	while True:
		if vehicle.location.global_relative_frame.alt > 9:
			break;
	point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
	vehicle.simple_goto(point1)
'''

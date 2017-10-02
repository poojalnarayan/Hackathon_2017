from dronekit import connect, VehicleMode
from time import sleep

vehicle = connect("0.0.0.0:14551", wait_ready=True)

while True:
	print "Location: %s" % vehicle.location.global_frame
	print " Attitude: %s" % vehicle.attitude
	print " Velocity: %s" % vehicle.velocity
	print " GPS: %s" % vehicle.gps_0
	sleep(1)

import pygame

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print(joystick_count)
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

#print(pygame.joystick.get_count())
for j in joysticks:
	j.init()
	print(j.get_init())

h_axis_pos = joysticks[0].get_axis(0)
v_axis_pos = joysticks[0].get_axis(1)
print (h_axis_pos, v_axis_pos)

while(True):
	pygame.event.get()
	for p in range(joysticks[0].get_numbuttons()):
		print(p , " :" ,  joysticks[0].get_button(p))
	#exit()


for p in range(joysticks[0].get_numhats()):
	print(p , " :" ,  joysticks[0].get_hat(p))

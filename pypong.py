import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800 ,600
speed = [0,0]
movement = 0
cpu_movement = 0
black = 0,0,0
white = 255,255,255
p1Score = 0
cpuScore = 0 

started = False

screen = pygame.display.set_mode(size)

font = pygame.font.SysFont(None, 60)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
paddle_cpu = pygame.image.load("paddle.png")
paddle1 = pygame.image.load("paddle.png")
scoreLabel = font.render("Score: "+str(p1Score),1,white)
clock = pygame.time.Clock()

scoreRect = scoreLabel.get_rect()
cpuRect = paddle_cpu.get_rect()
p1Rect = paddle1.get_rect()


def start():
	global cpuRect, p1Rect, ballrect, scoreRect,height,width
	cpuRect = cpuRect.move(height/2,0)
	p1Rect = p1Rect.move(300,height-25)
	ballrect = ballrect.move(height/2,width/2)
	scoreRect = scoreRect.move(width/2,height/2)
	started = False

def score(player):
	global cpuScore, p1Score,ballrect,cpuRect,speed,started,cpu_movement
	if player == "cpu":
		speed = [0,0]
		cpuScore += 1
		cpuRect.left = width/2
		ballrect.left = width/2
		ballrect.y = height/2
		started = False
		cpu_movement = 1
		print "CPU: " + str(cpuScore)+"; P1: "+ str(p1Score)
	if player == "p1":
		p1Score += 1
		print "CPU: " + str(cpuScore)+"; P1: "+ str(p1Score)

start()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_SPACE and started == False:
				started = True
				p1Score = 0
				speed = [1,1]
				cpu_movement = 1
			if event.key == K_LEFT:
				movement = -5
			elif event.key == K_RIGHT:
				movement = 5
		if event.type == KEYUP:
			if event.key in [K_LEFT, K_RIGHT]:
				movement = 0 
	
	
	if ballrect.left < 0:
		speed[0] = -speed[0]
		#cpu_movement = 1
	if ballrect.right > width:
		speed[0] = -speed[0]
		#cpu_movement = -1
	
	#TODO add in deflection of the paddle
	
	if ballrect.colliderect(cpuRect):
		speed[1] = -speed[1]
		
	if ballrect.colliderect(p1Rect):
		speed[0] = 1
		if speed[1] > 0:
			speed[1] += 1
			if speed[1] >= 8:
				speed[1] = 8
		if ballrect.centerx > (p1Rect.centerx - 5) and ballrect.centerx < (p1Rect.centerx + 5) :
			speed[0] = 0
		if ballrect.left >= p1Rect.centerx/4 and speed[0] > 0:
			
			speed[0] = 2
			#cpu_movement = -cpu_movement
		if ballrect.left <= p1Rect.centerx and speed[0] > 0:
			speed[0] = -speed[0]
			#cpu_movement = -cpu_movement
		if ballrect.right >= (p1Rect.centerx+(p1Rect.centerx/4) ) and speed[0] < 0:
			speed[0] = -2
			#cpu_movement = -cpu_movement
		if ballrect.right >= p1Rect.centerx and speed[0] < 0:
			speed[0] = -speed[0]
			#cpu_movement = -cpu_movement
		speed[1] = -speed[1]
		score("p1")
		
	if ballrect.bottom > height:
		score("cpu")
	if cpuRect.left < 0:
		cpuRect.left = 0
	if  cpuRect.right > width:
		cpuRect.right = width
	if p1Rect.left < 0:
		p1Rect.left = 0
	if p1Rect.right > width:
		p1Rect.right = width
	cpu_movement = speed[0]
	ballrect = ballrect.move(speed)
	cpuRect.left = cpuRect.left + cpu_movement
	p1Rect.left = p1Rect.left + movement
	scoreLabel = font.render("Score: "+str(p1Score),1,white)	
	
	
	screen.fill(black)
	screen.blit(scoreLabel,scoreRect)
	screen.blit(ball, ballrect)
	screen.blit(paddle1,p1Rect)
	screen.blit(paddle_cpu,cpuRect)
	
	
	pygame.display.update()
	
	
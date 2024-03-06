import sys, pygame
pygame.init()

size = width, height = 600, 400
speed = [1, 1]
background = pygame.image.load("bgmayfco.jpg")

screen = pygame.display.set_mode(size)

rock = pygame.image.load("rock115.png")
rockrect = rock.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    rockrect = rockrect.move(speed)
    if rockrect.left < 0 or rockrect.right > width:
        speed[0] = -speed[0]
    if rockrect.top < 0 or rockrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(rock, rockrect)
    pygame.display.flip()
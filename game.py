from utils import *

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
player = Player(0, 0, 80, 80, 1, 500, 500, win, pygame.image.load("temp0.png"))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill([0, 0, 0])
    player.move()
    player.draw()
pygame.quit()
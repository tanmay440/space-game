import pygame
import collision
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
#movement class
class Player:

    def __init__(self, x, y, width, height, vel, sh, sw, win, sprite, PLANETS = []) -> None:
        self.x = x
        self.y = y
        self.win = win
        self.width = width
        self.height = height
        self.vel = vel
        self.sh = sh
        self.sw = sw
        self.sprite = sprite
        self.facing = "idle"
        self.planets = PLANETS

    def has_colided(self):
        self.r = collision.Planet_Collision((((self.width)**2)+((self.height)**2))**0.5, self.x, self.y)
        i = 0
        for x, y, r in self.planets:
            i += 1
            if self.r.has_colided(r, x, y):
                return i
    
    def move(self):
        x = self.has_colided()
        if x != None:
            return
        keys = pygame.key.get_pressed()
        self.facing = "idle"
        if keys[pygame.K_LEFT] and self.x > self.vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            self.x -= self.vel
            self.facing = "left"

        if keys[pygame.K_RIGHT] and self.x < self.sw - self.vel - self.width:  # Making sure the top right corner of our character is less than the screen width - its width
            self.x += self.vel
            self.facing = "right"
        if keys[pygame.K_UP] and self.y > self.vel:  # Same principles apply for the y coordinate
            self.y -= self.vel
            self.facing = "up"
        if keys[pygame.K_DOWN] and self.y < self.sh - self.height - self.vel:
            self.y += self.vel
            self.facing = "down"
        del x
    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y, self.width, self.height))
        pygame.display.update()

#gameloop stuff

clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
test_planets = [(256, 256, 50)]
player = Player(0, 0, 80, 80, 10, 500, 500, win, pygame.image.load("temp0.png"), test_planets)
run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill([0, 0, 0])
    win.blit(pygame.image.load("beachball0.png"), (96, 96, 320, 320))
    player.move()
    player.draw()
'''
    if player.x < player.vel:
        print("left")
    elif player.y < player.vel:
        print("up")
    elif player.x< player.sw-player.vel-player.width:
        print("right")
    elif  player.y < player.sh-player.height-player.vel:
        print("down")
'''
pygame.quit()
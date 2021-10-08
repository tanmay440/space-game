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
#        has_colided(self)
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

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y, self.width, self.height))
        pygame.display.update()

#gameloop stuff

clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
player = Player(0, 0, 80, 80, 10, 500, 500, win, pygame.image.load("temp0.png"))
run = True
test_planets = [(1, 2, 3), (3, 4, 5)]
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill([0, 0, 0])
    player.move()
    player.draw()
pygame.quit()
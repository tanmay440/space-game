import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game")
class Player:
    def __init__(self, x, y, width, height, vel, sh, sw, win, sprite) -> None:
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
    def move(self):

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

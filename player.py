from circleshape import *
from constants import *
from asteroidfield import *
from shots import *


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    #draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255),self.triangle(),width=2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_q]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def move_backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= forward * PLAYER_SPEED * dt
    def shoot(self):
        shot = Shot(self.position.x,self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN







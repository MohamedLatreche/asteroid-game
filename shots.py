from circleshape import *



class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.color = (255, 255, 255)  # Optional

    def update(self, dt):
        # Move shot forward
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

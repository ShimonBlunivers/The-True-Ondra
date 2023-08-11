

import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, world, room, position, size, color = [0, 0, 0], image_path = None, priority = 0):
        self.world = world
        super().__init__(self.world.entity_group)
        self.room = room
        self.position = position
        self.size = size
        self.color = color
        self.render_priority = priority
        self.active = self.room.active

        if image_path != None:
            self.image = pygame.image.load(f"{image_path}.png")
            self.image = pygame.transform.scale(self.image, self.size)
        else:
            self.image = None

        self.room.entities.append(self)

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self):
        self.active = self.room.active
        self.rect.topleft = self.position

    def draw(self, surface):
        
        if self.image == None:
            pygame.draw.rect(surface, self.color, self.rect)
        else:
            surface.blit(self.image, self.rect)
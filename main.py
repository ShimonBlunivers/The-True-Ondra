import pygame
from entity import Entity
from ondra import Ondra
from room import Room

pygame.init()

class World:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    resolution = (1920, 1080)
    running = True

    def __init__(self):
        
        self.world = self
        self.screen = pygame.display.set_mode([self.resolution[0], self.resolution[1]])

        pygame.display.set_caption('TheTrueOndra')
        self.icon = pygame.image.load("files/icon.png")
        pygame.display.set_icon(self.icon)

        self.entity_group = pygame.sprite.Group()
        self.room_group = pygame.sprite.Group()

        self.room_list = [[]]

        self.starting_room = Room(self, [10, 10], self.GREEN, "Spawn")
        self.starting_room.active = True

        self.active_room = [self.starting_room.ID[0], self.starting_room.ID[1]]

        self.room1 = Room(self, [11, 10], self.WHITE)
        self.room2 = Room(self, [9, 10], self.BLUE)
        self.room3 = Room(self, [10, 11], self.RED)
        self.room4 = Room(self, [12, 10], [100, 100, 100])


        self.entity = Entity(self, self.room2, [200, 200], [200, 240], [125, 69, 42], "files/teo/texture")
        
        self.ondra = Ondra(self, [100, 100])

    def update(self):
        self.entity_group.update()
        for room in filter(lambda room: room.active, self.room_group.sprites()):
            room.update()

        self.debug_control()

    def render(self):
        for entity in sorted(self.entity_group.sprites(), key = lambda sprite: sprite.render_priority):
            if entity.active:
                entity.draw(self.screen)
        self.update_screen()

    def update_screen(self):
        pygame.display.flip()
        self.screen.fill(self.room_list[self.active_room[0]][self.active_room[1]].color)


    # TOOLS

    def change_room(self, ID):
        self.room_list[self.active_room[0]][self.active_room[1]].active = False
        self.active_room = ID
        self.room_list[self.active_room[0]][self.active_room[1]].active = True

    def debug_control(self):
        keys = pygame.key.get_pressed()


world = World()

while world.running:
    
    world.render()
    world.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
            pygame.quit()
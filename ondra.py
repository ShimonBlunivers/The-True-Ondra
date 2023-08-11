
import pygame

class Ondra(pygame.sprite.Sprite):

    def __init__(self, world, position):
        self.world = world
        super().__init__(self.world.entity_group)

        self.starting_position = position
        self.position = position

        self.size = [200, 200]

        self.original_image = pygame.image.load("files/ondra/texture.png")
        self.original_image = pygame.transform.scale(self.original_image, self.size)

        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.movement_speed = 1

        self.render_priority = 10
        self.active = True

    def update(self):
        self.rect.topleft = self.position
        self.control()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def control(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            if not self.check_side_collision([-1, 0])[0]: self.position[0] -= self.movement_speed
        if keys[pygame.K_d]:
            if not self.check_side_collision([1, 0])[0]: self.position[0] += self.movement_speed
        if keys[pygame.K_w]:
            if not self.check_side_collision([0, -1])[1]: self.position[1] -= self.movement_speed
        if keys[pygame.K_s]:
            if not self.check_side_collision([0, 1])[1]: self.position[1] += self.movement_speed

    def check_side_collision(self, direction):
        collision = [False, False]

        if direction[0] == -1:
            if self.rect.left < 0:
                try:
                    if self.world.room_list[self.world.active_room[0] + direction[0]][self.world.active_room[1]] == None: collision[0] = True
                    else:
                        if self.rect.right < 0:
                            self.world.change_room(self.world.room_list[self.world.active_room[0] + direction[0]][self.world.active_room[1]].ID)
                            self.position[0] = self.world.resolution[0] - self.size[0] 
                except: collision[0] = True
        elif direction[0] == 1:
            if self.rect.right > self.world.resolution[0]:
                try:
                    if self.world.room_list[self.world.active_room[0] + direction[0]][self.world.active_room[1]] == None: collision[0] = True
                    else:
                        if self.rect.left > self.world.resolution[0]:
                            self.world.change_room(self.world.room_list[self.world.active_room[0] + direction[0]][self.world.active_room[1]].ID)
                            self.position[0] = 0
                except: collision[0] = True
        elif direction[1] == -1:
            if self.rect.top < 0:
                try:
                    if self.world.room_list[self.world.active_room[0]][self.world.active_room[1] + direction[1]] == None: collision[1] = True
                    else:
                        if self.rect.bottom < 0:
                            self.world.change_room(self.world.room_list[self.world.active_room[0]][self.world.active_room[1] + direction[1]].ID)
                            self.position[1] = self.world.resolution[1] - self.size[1] 
                except: collision[1] = True
        elif direction[1] == 1:
            if self.rect.bottom > self.world.resolution[1]:
                try:
                    if self.world.room_list[self.world.active_room[0]][self.world.active_room[1] + direction[1]] == None: collision[1] = True
                    else:
                        if self.rect.top > self.world.resolution[1]:
                            self.world.change_room(self.world.room_list[self.world.active_room[0]][self.world.active_room[1] + direction[1]].ID)
                            self.position[1] = 0
                except: collision[1] = True

        return collision
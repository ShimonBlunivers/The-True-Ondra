import pygame

class Room(pygame.sprite.Sprite):

    def __init__(self, world, ID, color, name = "Undefined"):
        
        self.world = world
        super().__init__(self.world.room_group)
        self.ID = ID # [X, Y]
        self.color = color
        self.active = False

        self.entities = []

        self.name = name

        for y in range(self.ID[0]+1):
            try: self.world.room_list[y]
            except: self.world.room_list.append([])
            for x in range(self.ID[1]+1):
                try: self.world.room_list[y][x]
                except: self.world.room_list[y].append(None)
                
        if self.world.room_list[self.ID[0]][self.ID[1]] != self:
            if self.world.room_list[self.ID[0]][self.ID[1]] == None: self.world.room_list[self.ID[0]][self.ID[1]] = self
            else: print('\033[91m' + "Warning: " + '\033[0m'f"Room with ID {self.ID[0], self.ID[1]} is occupied!")
    
    def update(self):
        ()

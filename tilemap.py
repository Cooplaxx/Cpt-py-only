import pygame as pg
import pytmx
from settings import *


def collide_hit_rect(one, two): #what happens when two rects come into contact
    return one.hit_rect.colliderect(two.rect)

class Map: #class of map
    def __init__(self, filename): #initializes map structure
        self.data = [] #list for data
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap: #class for the tiled created maps
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth #width of map
        self.height = tm.height * tm.tileheight #height of map
        self.tmxdata = tm

    def render(self, surface): #renders in the map image
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self): #makes the map
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera: #camera class that follows the player
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity): #applys the camera to an entity in this case player
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect): #the rect the camera follows
        return rect.move(self.camera.topleft)

    def update(self, target): #updates camera movement
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        #limit scrolling to map size
        x = min(0, x)  #left
        y = min(0, y)  #top
        x = max(-(self.width - WIDTH), x)  #right
        y = max(-(self.height - HEIGHT), y)  #bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
from player import Player
from enemy import Enemy
from level_dao import Level_dao
from tile_map import Tile_map


class Game_state:
    def __init__(self, level):
        self.__level_dao = Level_dao('levels.json', level)
        PLAYERSTART = self.__level_dao.get("player_start_position")
        PLAYERSIZE = self.__level_dao.get("player_size")
        PLAYERSPEED = self.__level_dao.get("player_speed")
        ENEMYSTART = self.__level_dao.get("enemy_start_position")
        ENEMYSIZE = self.__level_dao.get("enemy_size")
        ENEMYSPEED = self.__level_dao.get("enemy_speed")

        self.__tile_map = Tile_map(self.__level_dao.get(
            "tilemap"), self.__level_dao.get("tilesize"))
        self.__obstacles = self.__tile_map.obstacle_list
        self.__player = Player(
            PLAYERSTART[0], PLAYERSTART[1], PLAYERSIZE, PLAYERSPEED, self.__obstacles)
        self.__enemies = [
            Enemy(ENEMYSTART[0], ENEMYSTART[1], ENEMYSIZE, ENEMYSPEED, self.__obstacles)]
        self.__objects = [self.__player] + \
            self.__tile_map.tile_list + self.__enemies
        self.__kinetic_objects = [self.__player] + self.__enemies
        self.__command_objects = [self.__player]
        self.__event_objects = self.__tile_map.event_list

    def change_level(self, next_level: int):
        self.__init__(next_level)

    @property
    def player(self):
        return self.__player

    @property
    def objects(self):
        return self.__objects

    @property
    def kinetic_objects(self):
        return self.__kinetic_objects

    @property
    def command_objects(self):
        return self.__command_objects

    @property
    def obstacles(self):
        return self.__obstacles

    @property
    def event_objects(self):
        return self.__event_objects

    @property
    def enemies(self):
        return self.__enemies

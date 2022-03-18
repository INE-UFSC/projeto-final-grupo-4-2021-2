from game_state import GameState


class RequestAnalyser:
    def __init__(self):
        self.__game_state = GameState(1)
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}

    @property
    def game_state(self):
        return self.__game_state

    def handle_requests(self):
        self.__update_dict()
        self.__handle_read()
        # self.__handle_write()

    def __handle_read(self):
        for obj in self.__game_state.request_objects:
            requests = []
            for list_name, list in self.__gs_dict.items():
                if list_name in obj.request:
                    requests.append(list)
            obj.use_request(requests)

    # def __handle_write(self):
    #     for obj in self.__game_state.request_objects:
    #         changes = obj.request_to_gs()
    #         if not changes is None:
    #             for name, list in changes.items():
    #                 self.__update_gs(name, list)

    def __update_dict(self):
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}

    # def __update_gs(self, name, value):
    #     # idealmente fazer um handler para cada lista, para não precisar criar objetos novos
    #     # e tirar os ifs
    #     if name == 'hit':
    #         if self.__game_state.player.hit_stun <= 0:
    #             self.__deal_player_dmg(value)
    #             self.__knockback(value)
    #             self.__game_state.player.hit_stun = 40

    #     elif name == 'slow':
    #         self.__slow_player_down(value)

    #     elif name == 'change-lv':
    #         self.__game_state.change_level(value)
    #         self.__update_dict()
    #         self.__handle_read()

    # def __deal_player_dmg(self, value):
    #     if self.__game_state.player.hit_stun <= 0:
    #         self.__game_state.player.current_health -= value

    # def __slow_player_down(self, value):
    #     self.__game_state.player.freezed = value

    # def __knockback(self, value):
    #     vel = (self.__game_state.player.velX, self.__game_state.player.velY)
    #     formula = 1 + value/20
    #     knockback_force = (vel[0] * formula, vel[1] * formula)
    #     self.__game_state.player.rect.x += knockback_force[0]
    #     self.__game_state.player.rect.y += knockback_force[1]

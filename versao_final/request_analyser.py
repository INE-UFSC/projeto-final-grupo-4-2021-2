from game_state import Game_state


class RequestAnalyser:
    def __init__(self):
        self.__game_state = Game_state(1)
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}

    def handle_requests(self):
        self.__update_dict()
        self.__handle_read()
        self.__handle_write()

    def __handle_read(self):
        for obj in self.__game_state.request_objects:
            requests = []
            for list_name, list in self.__gs_dict.items():
                if list_name in obj.request:
                    requests.append(list)
            obj.use_request(requests)

    def __handle_write(self):
        for obj in self.__game_state.request_objects:
            changes = obj.request_to_gs()
            for name, list in changes.items():
                self.__update_gs(name, list)

    def __update_dict(self):
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}

    def __update_gs(self, name, list):
        # idealmente fazer um handler para cada lista, para não precisar criar objetos novos
        # e tirar os ifs
        if name == 'player':
            self.__game_state.player = list
        elif name == 'change-lv':
            self.__game_state.change_level(list)
            self.__handle_read()
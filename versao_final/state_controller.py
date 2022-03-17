from menu_controller import MenuController
from game_controller import Game_controller
import pygame


class StateController:

    def __init__(self):
        pygame.init()
        self.__screen_size = 600
        self.__clk = pygame.time.Clock()
        self.__states = [MenuController(self.__screen_size),
                         Game_controller(self.__screen_size)]
        self.__current_state = self.__states[0]

    def main_loop(self):
        while True:
            self.__current_state.state_routine()

            if self.__current_state.next_state != None:
                for state in self.__states:
                    if state.name == self.__current_state.next_state:
                        self.__current_state = state

            pygame.display.flip()
            self.__clk.tick(60)

    def initialize(self):
        pygame.display.set_caption('jogo legal')
        self.main_loop()
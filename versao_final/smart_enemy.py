import math
from abc_kinetic_object import KineticObject
from abc_interactable_object import InteractableObject
from abc_request_object import AbcRequestObject


class SmartEnemy(KineticObject, InteractableObject, AbcRequestObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, sprite: str):
        KineticObject.__init__(self, initial_x, initial_y,
                               size, sprite, speed)
        InteractableObject.__init__(self)
        AbcRequestObject.__init__(self, ['player'])
        self._dano = 300

    def move_request(self):
        player = self._fake_player
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        try:
            dx, dy = dx / dist, dy / dist
        except ZeroDivisionError:
            pass
        self._velX = dx * self.speed
        self._velY = dy * self.speed
        return (self._velX, self._velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def on_contact(self):
        return {'hit': self._dano}

    def use_request(self, requested: list):
        # modificacoes nao alteram player verdadeiro
        self._fake_player = requested[0]

import random

from attrs import define, field


class AppPositionOnBlueprint:
    DEFAULT_POSITIONS = (
        (100, 100),
        (100, 200),
        (100, 300),
        (100, 400),
        (600, 240),
        (600, 340),
        (1100, 340),
        (1100, 340),
    )
    MAX_X = 1200
    MAX_Y = 500
    STEP = 20

    def __init__(self):
        self._app_num = 1
        self._used_positions = set()

    def _generate_random(self) -> tuple[int, int]:
        x = random.randrange(0, self.MAX_X, self.STEP)
        y = random.randrange(0, self.MAX_Y, self.STEP)
        return x, y

    def get_random_position(self) -> tuple[int, int]:
        while (position := self._generate_random()) in self._used_positions:
            continue
        return position

    def get_new_position(self) -> tuple[int, int]:
        try:
            position = self.DEFAULT_POSITIONS[self._app_num]
        except IndexError:
            position = self.get_random_position()
        self._used_positions.add(position)
        self._app_num += 1
        return position


@define
class NameGenerator:
    _names: dict[str, int] = field(factory=dict)

    def __call__(self, name: str) -> str:
        if name not in self._names:
            self._names[name] = 0
        else:
            self._names[name] += 1
            name = f"{name} {self._names[name]}"
        return name

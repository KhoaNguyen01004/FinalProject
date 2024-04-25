class Food:
    def __init__(self) -> None:
        """Initialize the food source object with level = 10"""
        self.__food_source = 10

    def get_food_source(self):
        return self.__food_source

    def eat(self, amount: float = 1):
        self.food_source -= amount


class Toy:
    def __init__(self, pos: tuple = (0, 0)) -> None:
        """Initialize the toy object with assigned position.

        Args:
            pos (tuple, optional): position of the toy. Defaults to (0, 0).
        """
        self.__pos = pos
        self.buried = False

    def get_pos(self):
        return self.__pos

    def set_pos(self, val: tuple):
        """Set the position of the toy

        Args:
            val (tuple): The tuple value of the position of the toy (x, y)
        """
        self.__pos = val

    def burry(self):
        # TODO implement what other things should be happened when the toy is buried
        self.buried = True

    def is_buried(self):
        return self.buried

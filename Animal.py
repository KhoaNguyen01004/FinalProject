class Dog:
    """A dog class which included info about the animal and their behaviors"""

    def __init__(self, name: str, color: str, pos: tuple) -> None:
        """Initialize a dog object

        Args:
            name (str): name of the dog
            color (str): color of the dog
            pos (tuple): position of the dog (x, y)
        """

        # basic information about the animal
        self.__name = name
        self.__color = color
        self.__pos = pos

        self.__energy = 10
        self.__hunger = 0

    def get_name(self):
        return self.__name

    def get_pos(self):
        return self.__pos

    def set_pos(self, val: tuple):
        """Set the position of the dog

        Args:
            val (tuple): The position you want to set (x, y)
        """
        self.__pos = val

    def get_color(self):
        return self.__color

    def get_energy(self):
        return self.__energy

    def set_energy(self, val: int | float):
        """Set the energy level from 0 to 10

        Args:
            val (int|float): The energy value you want to set
        """
        self.__energy = val

    def get_hunger(self):
        return self.__hunger

    def set_hunger(self, val: int | float):
        """Set the hunger level from 0 to 10

        Args:
            val (int|float): The hunger level you want to set
        """
        self.__hunger = val


class Squirrel:
    """A squirrel class which included info about the animal and their behaviors"""

    def __init__(self, name: str, color: str, pos: tuple) -> None:
        """Initialize a squirrel object

        Args:
            name (str): name of the squirrel
            color (str): color of the squirrel
            pos (tuple): position of the squirrel (x, y)
        """

        # basic information about the animal
        self.__name = name
        self.__color = color
        self.__pos = pos

        self.__energy = 10
        self.__hunger = 0

    def get_name(self):
        return self.__name

    def get_pos(self):
        return self.__pos

    def set_pos(self, val: tuple):
        """Set the position of the squirrel

        Args:
            val (tuple): The position of the squirrel you want to set (x, y)
        """
        self.__pos = val

    def get_color(self):
        return self.__color

    def get_energy(self):
        return self.__energy

    def set_energy(self, val: int | float):
        """Set the energy level from 0 to 10

        Args:
            val (int|float): The energy value you want to set
        """
        self.__energy = val

    def get_hunger(self):
        return self.__hunger

    def set_hunger(self, val: int | float):
        """Set the hunger level from 0 to 10

        Args:
            val (int|float): The hunger level you want to set
        """
        self.__hunger = val

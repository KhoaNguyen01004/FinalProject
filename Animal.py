class Dog:
    """A dog class which included info about the animal and their behaviors
    """

    def __init__(self, name: str, color: str, pos: tuple) -> None:
        """Initialize a dog object

        Args:
            name (str): name of the dog
            color (str): color of the dog
            pos (tuple): position of the dog
        """

        # basic information about the animal
        self.__name = name
        self.__color = color
        self.__pos = pos

    def get_name(self):
        return self.__name
    
    def get_pos(self):
        return self.__pos
    
    def get_color(self):
        return self.__color
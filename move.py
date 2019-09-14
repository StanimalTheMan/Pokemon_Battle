class Move():
    
    def __init__(self, move_name, move_type, move_description, base_dmg, pp):
        self._name = move_name
        self._move_type = move_type
        self._description = move_description
        self._base_damage = base_dmg
        self._pp = pp

    @property
    def name(self):
        """Input: None
           Return: move name (str)
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """Input: new name for move (str)
           Return: None
        """
        self._name = new_name

    @property
    def move_type(self):
        """Input: None
           Return: type of move (Type object)
        """
        return self._move_type
    
    @move_type.setter
    def move_type(self, new_type):
        """Input: new type of move (Type object)
           Return: None
        """
        self._move_type = new_type

    @property
    def description(self):
        """Input: None
           Return: move description (str)
        """
        return self._description

    @description.setter
    def description(self, new_description):
        """Input: new_description (str)
           Return: None
        """
        self._description = new_description

    @property
    def base_damage(self):
        """Input: None
           Return: damage without considering weaknesses which
                   will be subtracted from hp of pokemon (int)
        """
        return self._base_damage

    @base_damage.setter
    def base_damage(self, new_base_dmg):
        """Input: updated base dmg (int)
           Return: None
        """
        self._new_base_dmg = new_base_dmg

    @property
    def pp(self):
        """Input: None
           Return: # of a certain move left (int)
        """
        return self._pp

    @pp.setter
    def pp(self, new_pp):
        """Input: updated # of a certain move left (int)
           Return: None
        """
        self._pp = new_pp

    

    

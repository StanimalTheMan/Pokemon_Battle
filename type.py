class Type():
    available_types = ['Water', 'Grass', 'Fire']
    available_types_weaknesses = {'Water': 'Grass', 'Fire': 'Water', 'Grass': 'Fire'}
    
    def __init__(self, name):
        self._name = name

    

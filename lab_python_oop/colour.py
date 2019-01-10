class Colour():
    def __init__(self):
        self._name=None
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name=value
    def del_name(self):
        self._name='transparent'
    name=property(get_name, set_name,del_name,'colour change')

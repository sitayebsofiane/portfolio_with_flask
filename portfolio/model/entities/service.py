class Service:

    def __init__(self,name=None,technologies=None,outils=None):
        self.name=name
        self.technologies=technologies
        self.outils=outils

    def __repr__(self):
        return f'name({self.name}),technologies({self.technologies}),outils({self.outils})'
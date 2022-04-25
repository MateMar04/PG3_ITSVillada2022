class Familia:
    def __init__(self, mom, dad, children):
        self.mom = mom
        self.dad = dad
        self.children = children

    def __str__(self):
        return f"Madre: {self.mom}\nPadre: {self.dad}\nChildren: {self.children}"
    # [self.children[i] for i in range(len(self.children))]


familia1 = Familia("Yanina", "Elvio", ["Mateo", "Bianca"])
print(familia1.__str__())

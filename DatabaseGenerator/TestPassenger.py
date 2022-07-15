class TestPassenger:
    def __init__(self, id: str, name: str, family: str, father : str = None, phone: str = None):
        self.id = id
        self.name = name.strip()
        self.family = family.strip()
        self.father = father
        self.phone = phone if phone is not None and phone.isdigit() else None

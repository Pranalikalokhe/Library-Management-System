class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

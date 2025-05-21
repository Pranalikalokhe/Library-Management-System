class Member:
    def __init__(self, member_id, name, role='member'):
        self.id = member_id
        self.name = name
        self.role = role
        self.borrowed_books = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'borrowed_books': self.borrowed_books
        }

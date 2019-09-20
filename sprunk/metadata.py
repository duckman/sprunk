class Metadata:
    def __init__(self, title = None, artist = None, name = None):
        self.title = title
        self.artist = artist
        self.name  = name

    def str(self):
        parts = [self.name, self.artist, self.title]
        parts = [p for p in parts if p is not None]
        return ' - '.join(parts)

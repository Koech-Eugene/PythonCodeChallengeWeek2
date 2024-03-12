class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string of length 5 to 50")
        self._title = title
        self.author = author
        self.magazine = magazine
        magazine._articles.append(self)
        author._articles.append(self)
        self._all.append(self)

    @property
    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls._all

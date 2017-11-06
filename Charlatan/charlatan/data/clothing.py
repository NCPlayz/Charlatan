from random import choice


class Clothing:
    @property
    def international(self):
        sizes = [
            'L',
            'M',
            'S',
            'XL',
            'XS',
            'XXL',
            'XXS',
            'XXXL',
        ]

        return choice(sizes)

    @property
    def european(self):
        size = choice([i for i in range(40, 62) if i % 2 == 0])
        return size


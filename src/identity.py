"""Create an id that auto increments."""


class IdentitySequence:
    count = 0

    def next(self):
        self.count += 1
        return self.count

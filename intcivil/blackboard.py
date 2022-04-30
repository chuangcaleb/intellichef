class Blackboard:

    def __init__(self):
        """ Initialize the blackboard """
        pass

    # instance method
    def sing(self, song):
        return '{} sings {}'.format(self.name, song)

    def dance(self):
        return '{} is now dancing'.format(self.name)

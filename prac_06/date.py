class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "The date is {}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, n):
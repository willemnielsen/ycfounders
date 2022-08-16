from uuid import uuid4


class Company:
    def __init__(self, name=None, founders=None):
        if founders is None:
            founders = []
        self.id = uuid4().time_low
        self.name = name
        self.url = 'https://www.ycombinator.com/companies/' + name
        self.founders = founders

    def __repr__(self):
        if self.name:
            return f'{self.name}'
        else:
            return self


class Founder:
    def __init__(self, name=None, twitter=None, linkedin=None, company=None):
        self.id = uuid4().time_low
        self.name = name
        self.twitter = twitter
        self.linkedin = linkedin
        self.company = company

    def __repr__(self):
        return f'Founder({self.name}, {self.twitter}, {self.linkedin}, {self.company})'





from json import load


class config:
    def __init__(self, fp: str):
        self.data = load(open(fp))
        self.header = self.data['header']
        self.credits = self.data['credits']

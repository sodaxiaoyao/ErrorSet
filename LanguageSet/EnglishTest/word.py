# coding=utf-8


class Verb(object):

    def __init__(self):
        self.chinese = "动词"


class OrdinaryVerb(Verb):

    def __init__(self):
        super(OrdinaryVerb, self).__init__()


class BeVerb(Verb):

    def __init__(self):
        super(BeVerb, self).__init__()
        self.chinese = "be动词"


class BeIsVerb(BeVerb):

    def __init__(self):
        super(BeIsVerb, self).__init__()


class BeAmVerb(BeVerb):

    def __init__(self):
        super(BeAmVerb, self).__init__()


class BeAreVerb(BeVerb):

    def __init__(self):
        super(BeAreVerb, self).__init__()

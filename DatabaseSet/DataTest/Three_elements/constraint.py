# coding=utf-8


class Constraint(object):

    def __init__(self):
        self.effect = "数据完整性"


class PrimaryKey(Constraint):

    def __init__(self):
        super(PrimaryKey, self).__init__()
        self.effect = "实体完整性"


class ForeignKey(Constraint):

    def __init__(self):
        super(ForeignKey, self).__init__()
        self.effect = "参照完整性"


class Unique(Constraint):

    def __init__(self):
        super(Unique, self).__init__()
        self.effect = "用户自定义完整性"


class Check(Constraint):

    def __init__(self):
        super(Check, self).__init__()
        self.effect = "用户自定义完整性"


class Default(Constraint):

    def __init__(self):
        super(Default, self).__init__()
        self.effect = "用户自定义完整性"

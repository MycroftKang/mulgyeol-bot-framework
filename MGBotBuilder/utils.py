import re
import MGBotBuilder.exceptions as exceptions


class Request:
    def __init__(self, user, commad, **kwargs):
        self.user = user
        self.command = commad
        self.__dict__.update(kwargs)

    def add(self, **kwargs):
        self.__dict__.update(kwargs)


class CommandRule:
    def __init__(self, cmdreg, permission, func):
        self.command = cmdreg
        self.permission = permission
        self.func = func


def parse_rule(rule):
    params = re.findall('(<\w+>)', rule)
    for p in params:
        rule = re.sub(p, f'(?P{p}.+)', rule)
    rule = re.compile('^'+rule+'$', re.IGNORECASE)
    return rule

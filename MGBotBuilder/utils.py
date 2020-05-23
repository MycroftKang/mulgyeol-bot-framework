import re
import shlex
import MGBotBuilder.exceptions as exceptions

class Request:
    def __init__(self, user, commad, **kwargs):
        self.user = user
        self.command = commad
        self.__dict__.update(kwargs)

    def add(self, **kwargs):
        self.__dict__.update(kwargs)

class CommandRule:
    def __init__(self, cmdreg, params, permission, func):
        self.command = cmdreg
        self.params = params
        self.permission = permission
        self.func = func

class RequestObject:
    def __init__(self, req, user):
        self.req = shlex.split(req)

def parse_rule(rule):
    params = re.findall('<(\w+)>', rule)
    cmdreg = re.compile(re.sub('<\w+>', '(.*)', rule))
    return cmdreg, params

def parse_req(params, cr:CommandRule):
    return dict(zip(cr.params, params))
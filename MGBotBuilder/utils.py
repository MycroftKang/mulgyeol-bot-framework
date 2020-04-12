import re
import shlex
import MGBotBuilder.exceptions as exceptions

class CommandRule:
    def __init__(self, cmd, params, permission, func):
        self.command = cmd.upper()
        self.params = params
        self.permission = permission
        self.func = func

class RequestObject:
    def __init__(self, req, user):
        self.req = shlex.split(req)

def parse_rule(rule):
    cmd = re.match('(.+) <', rule)
    if cmd == None:
        cmd = rule
        params = []
    else:
        params = re.findall('<([a-zA-Z]\w*)>', rule)
    return cmd, params

def parse_req(req_list, CR):
    req_list = req_list[1:]
    if len(req_list) != len(CR.params):
        raise exceptions.CommandParseError
    else:
        data = {CR.params[i]:req_list[i] for i in range(len(req_list))}
    return data
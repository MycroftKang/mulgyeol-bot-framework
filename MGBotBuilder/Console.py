import shlex
import requests
import MGBotBuilder.exceptions as exceptions
import MGBotBuilder.utils as utils

class CommandConsole:
    def __init__(self):
        self.registry = {}

    def add_command(self, cmddata):
        self.registry[cmddata.command] = cmddata

    def command(self, cmdrule, permission=[]):
        def deco(f):
            cmd, params = utils.parse_rule(cmdrule)
            self.add_command(utils.CommandRule(cmd, params, permission, f))
            return f
        return deco

    def forward(self, req, user, **option):
        try:
            cmddata = self.registry[req.upper()]
            req = [req]
        except KeyError:
            req = shlex.split(req)
            cmddata = self.registry[req[0].upper()]
        except:
            raise exceptions.CommandNotFoundError

        if not len(cmddata.permission) == 0:
            if not user in cmddata.permission:
                raise exceptions.PermissionDenied

        func_params = utils.parse_req(req, cmddata)

        try:
            res = cmddata.func(**func_params, **option)
        except:
            raise exceptions.CommandParseError
        
        return res


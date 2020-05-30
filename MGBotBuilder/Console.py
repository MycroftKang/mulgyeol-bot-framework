import threading
import MGBotBuilder.exceptions as exceptions
import MGBotBuilder.utils as utils

class CommandConsole:
    def __init__(self):
        self.registry = []
        self.reply_func = None

    def command(self, cmdrule, permission=[]):
        def deco(f):
            cmd, params = utils.parse_rule(cmdrule)
            self.registry.append(utils.CommandRule(cmd, params, permission, f))
            return f
        return deco

    def reply(self, func):
        self.reply_func = func
        return func

    def forward(self, request:utils.Request):
        t = threading.Thread(target=self.bind, args=(request, ))
        t.start()
        return t

    def bind(self, request:utils.Request):
        bad_request = True
        for rule in self.registry:
            p = rule.command.findall(request.command)
            if len(p) != 0:
                bad_request = False
                break

        if bad_request:
            raise exceptions.CommandNotFoundError

        if not len(rule.permission) == 0:
            if not request.user in rule.permission:
                raise exceptions.PermissionDenied

        func_params = utils.parse_req(p, rule)

        try:
            res = rule.func(request, **func_params)
        except:
            raise exceptions.CommandParseError
        
        if self.reply_func:
            return self.reply_func(res)
        else:
            return res


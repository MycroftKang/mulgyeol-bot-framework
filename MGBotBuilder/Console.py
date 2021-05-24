import threading
import MGBotBuilder.exceptions as exceptions
import MGBotBuilder.utils as utils


class VirtualCommandConsole:
    def __init__(self):
        self.registry = []

    def command(self, *cmdrule, permission=[]):
        def deco(f):
            for i in cmdrule:
                cmd = utils.parse_rule(i)
                self.registry.append(utils.CommandRule(cmd, permission, f))
            return f

        return deco


class CommandConsole(VirtualCommandConsole):
    def __init__(self):
        super().__init__()

        self.reply_func = None
        self.exception_func = None

    def extend(self, vcc: VirtualCommandConsole):
        self.registry.extend(vcc.registry)

    def exception(self, func):
        self.exception_func = func
        return func

    def reply(self, func):
        self.reply_func = func
        return func

    def forward(self, request: utils.Request):
        t = threading.Thread(target=self.bind, args=(request,))
        t.start()
        return t

    def bind(self, request: utils.Request):
        bad_request = True
        for rule in self.registry:
            p = rule.command.match(request.command)
            if p:
                bad_request = False
                break

        if bad_request:
            if self.exception_func:
                self.exception_func(request)
            raise exceptions.CommandNotFoundError

        if not len(rule.permission) == 0:
            if not request.user in rule.permission:
                raise exceptions.PermissionDenied

        func_params = p.groupdict()

        try:
            res = rule.func(request, **func_params)
        except:
            if self.exception_func:
                self.exception_func(request)
            raise exceptions.CommandParseError

        if self.reply_func:
            return self.reply_func(res)
        else:
            return res

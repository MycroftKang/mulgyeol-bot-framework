from MGBotBuilder import CommandConsole, Request

console = CommandConsole()


@console.exception
def error_reply(ctx):
    print('error', ctx.command)


@console.reply
def reply(msg):
    print(msg)


@console.command('#help')
def show_help(ctx):
    pass


@console.command('#set vol <num1>')
def setting(ctx, num1):
    print(num1)
    return "Complete"


@console.command('@myftbot merge( this( mr)?)? in <timevar>')
def merge(ctx, timevar):
    print(timevar)
    print(ctx.timestamp)
    return "Complete"


console.forward(
    Request('tester', '@myftbot merge this in 3 minute', timestamp=1586676476))

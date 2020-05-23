from MGBotBuilder.Console import CommandConsole
from MGBotBuilder.utils import Request

console = CommandConsole()

@console.reply
def reply(msg):
    print(msg)

@console.command('#help')
def show_help(ctx):
    pass

@console.command('#set vol <num1>')
def setting(ctx, num1):
    pass

@console.command('@MGYLBot merge this in <num1> minute[s]?')
def merge(ctx, num1):
    print(num1)
    print(ctx.timestamp)
    return "Complete"

console.forward(Request('tester', '@MGYLBot merge this in 3 minute', timestamp=1586676476))
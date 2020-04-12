from MGBotBuilder.Console import CommandConsole

console = CommandConsole()

@console.command('#help')
def show_help():
    pass

@console.command('#set vol <num1>')
def approval(num1):
    pass
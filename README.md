# Mulgyeol Bot Framework

Mulgyeol Bot Framework을 통해 명령 처리 봇을 빠르게 디자인 할 수 있습니다.

## Example
* [Mulgyeol Labs Fabric Bot](https://gitlab.com/mgylabs/developer/taehyeokkang/MGLabsBot)
> Mulgyeol Labs Fabric Bot은 Mulgyeol Bot Framework를 이용하여 개발되었습니다.

## How to use

```python
from MGBotBuilder import CommandConsole

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
```

`@console.command()`를 통해 명령어를 등록할 수 있습니다.  
매개변수에 `<name>`은 변수로 인식하여, 연결된 함수에 `name` 매개변수로 전달됩니다.

```python
from example_CmdRegistry import console
from MGBotBuilder import Request

command = '#set vol 3'
user = 'Tester'
req = Request(user, command)
res = console.bind(req)
```

```python
from example_CmdRegistry import console
from MGBotBuilder import Request

command = '@MGYLBot merge this in 3 minutes'
user = 'Tester'
reqtime = 1586676476
req = Request(user, command, timestamp=reqtime)
console.forward(req)
```

`console.bind()` 또는 `console.forward()` 함수에 위와 같은 매개변수를 전달하면, 등록된 함수가 실행되고, 함수가 반환하는 값은 `@console.reply`로 등록된 함수의 매개변수로 전달됩니다.

`console.forward()`는 `console.bind()`와 달리, 별도의 thread로 실행 되며, `Thread` 객체가 반환됩니다.

`@console.reply` 등록되지 않았을 경우, 함수가 반환하는 값은 `console.bind`의 반환 값이 됩니다.

See also, [Example](example_CmdRegistry.py)
# Mulgyeol Bot Framework

Mulgyeol Bot Framework을 통해 명령 처리 봇을 빠르게 디자인 할 수 있습니다.

## Example
* [Mulgyeol Labs Fabric Bot](https://gitlab.com/MGYLBot)
> Mulgyeol Labs Fabric Bot은 Mulgyeol Bot Framework를 이용하여 개발되었습니다.

## How to use

```python
from MGBotBuilder.Console import CommandConsole

console = CommandConsole()

@console.command('#help')
def show_help():
    pass

@console.command('#bye')
def show_help(time):
    pass

@console.command('#set vol <num1>', permission=['Tester'])
def approval(num1):
    pass
    return '재설정되었습니다.'
```

`@console.command()`를 통해 명령어를 등록할 수 있습니다.  
매개변수에 `<name>`은 변수로 인식하여, 연결된 함수에 `name` 매개변수로 전달됩니다.

```python
from example_CmdRegistry import console

command = '#set vol 3'
user = 'Tester'
res = console.forward(command, user)
```

```python
from example_CmdRegistry import console

command = '#bye'
user = 'Tester'
reqtime = 1586676476
res = console.forward(command, user, time=reqtime)
```

`console.forward()` 함수에 위와 같은 매개변수를 전달하면, 등록된 함수가 실행되고, 등록된 함수가 반환하는 값이 `res`로 반환됩니다.

See also, [Example](example_CmdRegistry.py)

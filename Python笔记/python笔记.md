# Python学习笔记
USTC张迪 

## 0.环境搭建和基本输入输出
Windows下通过 pytho.org 下载安装包，或通过Microsoft Store直接安装Python。  
Linux下通过Bash安装 ，Debian、Ubuntu一般已经预装，也可使用命令安装 
    
    sudo apt-get install python

需要注意在Windows下进行安装时,需要配置PATH变量,将Python的安装目录加入到PATH变量中,同时也应将Python安装目录下的Scripts目录加入到PATH变量.


### 0.1 环境搭建与调试

安装完成后在powershell中输入python，进入python的交互模式。  
输入

    print("hello world")

回车,得到输出

    hello world

证明python安装成功.

### 0.2 常用IDE(集成开发环境)

Windows下常用的集成开发环境有Visual Studio,PyCharm等软件.  
初学者可以使用轻量级的VSCode进行学习.

### 0.3 python解释器的工作原理


## 1.基本数据类型
###
## 2.复杂数据类型

## 3.控制流

## 4.函数

## 5.类

定义函数时对实参的类型进行限定:
```
    class Aaaa:
        def dosomething(self):pass

    def foo2(a:Aaaa):
        a.dosomething()
``` 

## 6.包和模块
3.x模块"引用"的四种方法.
import
from
exec(open("module.py").read())


from imp import reload
reload(module) #module.py应当已经被引入

  
+ 与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键。  



<img src ="https://favicon.yandex.net/favicon/csdn.net" />  
<img src="/i/eg_logo_w3school.gif" border="1" />

## 7.多任务
协程
0.定义消息循环

    import asyncio
    loop = asyncio.get_event_loop()

1.使用async关键字定义协程对象,形如

    async def run(x):
        await asyncio.sleep(x)
        return x
2.封装协程对象

    coroutine1 = run(x)

3.整合协程任务列表

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

4.对有需要的协程对象绑定回调函数

    for task in tasks:
        task.add_done_callback(callbackn)

    '''
    callback()是欲绑定的协程回调函数,定义形如
    def callback1(future):
        print(future.result)

    '''

5.将任务列表添加入消息循环

    loop.run_until_complete(task)#单个任务
    loop.run_until_complete(asyncio.gather(tasks))




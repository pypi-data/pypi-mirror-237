# Outer

A tool to manage directories and files of the output, which doesn't require you to create dir with call of `mkdir`!

该工具为了实现轻便的项目目录管理，有了它，你可以把你所有的目录输出结构组织在一起，并且你不需要担心目录是否已创建，系统都会自动递归地创建。

## 1. Installation

```
pip install outer
```

## 2. Main Concepts

### 2.1 BluePrint - 蓝图

一个项目目录输出结构的设计草图，它是1个实现BluePrint类的子类，子类的属性存储`目录`和`文件名`，可供程序作为输出的地址。

## 3. Method - 用法

### 2.1. You must define a blueprint in this method

你必须定义1个BluePrint的子类，如outer项目下的[BluePrintSample.py](demo/BluePrintSample.py)，内容如下代码。

```
from outer.Object import File, Dir, Object
from outer.BluePrint import BluePrint


class BluePrintSample(BluePrint):
    def __init__(self):
        super().__init__(key=key)

        # 1. 建立项目的ROOT目录
        # A. "{}"为占位符,可设定任意个数
        self.ROOT = self.sub_dir('{}_UNet')

        # 2. 利用self.ROOT去产生子文件和子目录，他们都存放在self.ROOT对应的目录下
        # B. "{}"为占位符,可设定任意个数
        self.LOG_MAIN = self.ROOT.sub_file('run.log')
        self.LOG_TENSORBOARD = self.ROOT.sub_dir('event')
        self.FILE_CHECKPOINT = self.ROOT.sub_file('model_{}.pkl')

        # 3. 此处的用法和2中的用法一样
        self.TRAIN_DIR = self.ROOT.sub_file('train')
        self.TRAIN_IMG_OUTPUT = self.TRAIN_DIR.sub_dir('image')
        self.TRAIN_LABEL_OUTPUT = self.TRAIN_DIR.sub_dir('label')
        self.TRAIN_GT_OUTPUT = self.TRAIN_DIR.sub_dir('gt')

        # recall father init
        # 调用父类初始化方法，让所有定义的目录（Dir）、文件(File)属性和内部管理器绑定，如self.ROOT、self.LOG_MAIN、self.LOG_TENSORBOARD都会与内部管理器绑定。
        self.init()
```


### 2.2. Then you can simply use it with `touch` or `touch_` method!

利用touch和touch_去使用BluePrint中的`文件`和`目录`。touch适用于BluePrint中没有占位符“{}”的情形，而touch_适用于目录中存在“{}”的情况。

```
from BluePrintSample import BluePrintSample

# 构建 blueprint 蓝图
blueprint = BluePrintSample('1')
# 使用touch_去生成路径，输出格式为字符串形式，如下参数‘1’替换了如上代码中A处的self.ROOT中的占位符"{}"
out = blueprint.TRAIN_IMG_OUTPUT.touch_('1')
print(out)
# 对于目录上存在占位符，文件上也存在占位符的，请指定一起指定多个参数。
print(blueprint.FILE_CHECKPOINT.touch_(1, 'UNet'))
```

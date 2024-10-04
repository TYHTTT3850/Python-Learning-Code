# Python-Learning-code
## pip工具常用操作指令

显示所有已安装的库。

```cmd
pip list
```

 查看指定库的完整安装路径。

```cmd
pip show 库名
```

自动安装最新版的库

```cmd
pip install 库名
```

安装指定版本的库。

```cmd
pip install 库名==指定版本号
```

卸载指定的库

```cmd
pip uninstall 库名   
```

查看可以升级的库

```cmd
pip list -o
```

升级指定库

```cmd
pip install -U 库名
```



升级pip

```cmd
pip install -U pip
```

## Python模块、包、库、框架的区别和联系
模块Module：后缀为.py的文件(就是Pyhton代码文件)，里面定义了函数，类等，可以将自己常用的函数或者类等等写入其中，需要时通过import语句导入。
包Package：几个模块的集合
库Library：几个包的集合
框架Framework：Python库的集合

## 下载

下载资源：[链接][https://mirrors.tuna.tsinghua.edu.cn/qt/official_releases/online_installers/]

在下载目录打开命令行，输入

```bat
文件名 --mirror https://mirrors.tuna.tsinghua.edu.cn/qt
```

部分用户下载时可能出现`403 Forbidden`，可以更换镜像源至

``` bat
文件名 --mirror http://mirrors.ustc.edu.cn/qtproject/
```

*PS：硬盘空间一定要够，所有组件下载后共计300多GB*

*PS：Qt打开比较慢。*

## 创建文件

![image-20250123114102100](assets/p.assets/image-20250123114102100.png)

1.点击`创建项目`

![image-20250123114135967](assets/p.assets/image-20250123114135967.png)

2.点击`选择`

![image-20250123114238920](assets/p.assets/image-20250123114238920.png)

3.点击`下一步`

![image-20250123114306396](assets/p.assets/image-20250123114306396.png)

4.点击`下一步`

![image-20250123114333581](assets/p.assets/image-20250123114333581.png)

5.点击`下一步`

![image-20250123114400748](assets/p.assets/image-20250123114400748.png)

6.点击`下一步`

![image-20250123114501774](assets/p.assets/image-20250123114501774.png)

7.选择与您系统环境相同的编译器(可以多选)

例如：您是`Amd64位`，就不能选择`Android`或`Arm64`。

![image-20250123114757951](assets/p.assets/image-20250123114757951.png)

8.点击`下一步`。

![image-20250123114823347](assets/p.assets/image-20250123114823347.png)

9.点击`完成`。

![image-20250123115018681](assets/p.assets/image-20250123115018681.png)

正常情况下，侧边栏应该有很多文件。如果您和我一样，请继续。

如果您的侧边栏只有一个`CMakeLists.txt`文件，请跳转到[这里](#help)

## 编写hello_world

将`main.cpp`文件修改为

```cpp
#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
int main(int argc, char* argv[])
{
	QApplication a(argc, argv);
	QMainWindow w;
	QPushButton b(&w);
	b.setText("Hello QT!");
	w.show();
	return a.exec();
}
```

![image-20250123120855244](assets/p.assets/image-20250123120855244.png)

点击侧边栏倒数第三行的绿色三角运行。

![image-20250123120912676](assets/p.assets/image-20250123120912676.png)

等待输出。

![image-20250123121033180](assets/p.assets/image-20250123121033180.png)

或者使用release，点击小电脑图标，切换到release生成

![image-20250123121318683](assets/p.assets/image-20250123121318683.png)

再次编译运行

![image-20250123121348051](assets/p.assets/image-20250123121348051.png)

我们发现，不管是哪种编译方式，直接在文件夹打开，会出现以下情况。

![image-20250123121147061](assets/p.assets/image-20250123121147061.png)

我们来到应用列表。

```bat
C:\Users\Lenovo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Qt
```

找到对应编译器。

![image-20250123122011448](assets/p.assets/image-20250123122011448.png)

点开Qt开头的程序。

![image-20250123122052668](assets/p.assets/image-20250123122052668.png)

切换到文件目录。

![image-20250123122319753](assets/p.assets/image-20250123122319753.png)

输入

```bat
windeployqt 文件名.exe
```

![image-20250123122414724](assets/p.assets/image-20250123122414724.png)

这样目录中就多了很多文件。

![image-20250123122500751](assets/p.assets/image-20250123122500751.png)

这次再打开文件。

就可以了。

![image-20250123122528158](assets/p.assets/image-20250123122528158.png)

# help

如果侧边栏只有一个文件，请点击窗口顶部的编辑中的`preference`

![image-20250123115531081](assets/p.assets/image-20250123115531081.png)

请点击所选编译器，并更改配置与我一样。

![image-20250123115748763](assets/p.assets/image-20250123115748763.png)

然后再去系统环境变量，将cmake添加到环境变量中。

![image-20250123120016290](assets/p.assets/image-20250123120016290.png)

点击`path`

![image-20250123120049916](assets/p.assets/image-20250123120049916.png)

点击`添加`

添加

``` bat
Qt安装路径\Tools\CMake_64\bin
```

点击`确定`并重启Qt。

如果还是不行，请跳转到创建文件的第4步左右，并把`cmake`改为`qmake`即可。
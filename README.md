# By Traders, For Traders.

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png" />
</p>

vn.py是一套基于Python的开源量化交易系统开发框架，自2015年1月正式发布以来，在开源社区5年持续不断的贡献下一步步成长为全功能量化交易平台，目前国内外金融机构用户已经超过300家，包括：私募基金、证券自营和资管、期货资管和子公司、高校研究机构、自营交易公司、交易所、Token Fund等。

2.0版本基于Python 3.7全新重构开发，目前功能还在逐步完善中。如需Python 2上的版本请点击：[长期支持版本v1.9.2 LTS](https://github.com/vnpy/vnpy/tree/v1.9.2-LTS)。

## 功能特点

1. 全功能量化交易平台（vnpy.trader），整合了多种交易接口，并针对具体策略算法和功能开发提供了简洁易用的API，用于快速构建交易员所需的量化交易应用。

2. 覆盖国内外所有交易品种的交易接口（vnpy.gateway）：

    * CTP(ctpGateway)：国内期货、期权

    * 富途证券(futuGateway)：港股、每股

    * Interactive Brokers(ibGateway)：全球证券、期货、期权、外汇等

    * BitMEX (bitmexGateway)：数字货币期货、期权、永续合约

3. 开箱即用的各类量化策略交易应用（vnpy.app）：

    * CtaStrategy：CTA策略引擎模块，在保持易用性的同时，允许用户针对CTA类策略运行过程中委托的报撤行为进行细粒度控制（降低交易滑点、实现高频策略）

4. Python交易API接口封装（vnpy.api），提供上述交易接口的底层对接实现。

5. 简洁易用的事件驱动引擎（vnpy.event），作为事件驱动型交易程序的核心。

6. [社区论坛](http://www.vnpy.com)和[知乎专栏](http://zhuanlan.zhihu.com/vn-py)，内容包括vn.py项目的开发教程和Python在量化交易领域的应用研究等内容。

7. 官方交流群262656087（QQ），管理严格（定期清除长期潜水的成员），入群费将捐赠给vn.py社区基金。

## 环境准备

* 推荐使用vn.py团队为量化交易专门打造的Python发行版[VNConda-2.0-Windows-x86_64](https://conda.vnpy.com/VNConda-2.0-Windows-x86_64.exe)，内置了最新版的vn.py，无需手动安装
* 支持的系统版本：Windows 7以上/Windows Server 2008以上/Ubuntu 18.04 LTS
* 支持的Python版本：Python 3.7 64位（**注意必须是Python 3.7 64位版本**）
* 如需使用IB API，请在[Interactive Brokers Github](https://interactivebrokers.github.io/#)页面下载安装**IB API Latest**


## 安装步骤

在[这里](https://github.com/vnpy/vnpy/releases)下载最新版本，解压后运行以下命令安装：

**Windows**

    install.bat

**Ubuntu**

    bash install.sh


## 使用指南

1. 在[SimNow](http://www.simnow.com.cn/)注册CTP仿真账号，并在[该页面](http://www.simnow.com.cn/product.action)获取经纪商代码以及交易行情服务器地址。

2. 在[vn.py社区论坛](https://www.vnpy.com/forum/)注册获得VN Station账号密码，论坛最新的注册邀请码为**El86Pa1p**

3. 启动VN Station（安装VNConda后会在桌面自动创建快捷方式），输入上一步的账号密码登录

4. 点击底部的**VN Trader**按钮，选择运行目录（默认在系统用户目录即可）后，在对话框中勾选CTP接口以及CtaStrategy应用，点击右下方的**启动**按钮，开始你的交易！！！

5. 在VN Trader的运行过程中请勿关闭VN Station（会自动退出）

6. 如选择了VNConda以外的安装方式（不推荐新手），可以在任意目录下创建run.py，写入以下示例代码后运行：

```Python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.gateway.ctp import CtpGateway
from vnpy.app.cta_strategy import CtaStrategyApp

def main():
    """启动VN Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()
```



## 贡献代码

vn.py使用github托管其源代码，如果希望贡献代码请使用github的PR(Pull Request)的流程:

1. [创建 Issue](https://github.com/vnpy/vnpy/issues/new) - 对于较大的改动(如新功能，大型重构等)最好先开issue讨论一下，较小的improvement(如文档改进，bugfix等)直接发PR即可

2. Fork [vn.py](https://github.com/vnpy/vnpy) - 点击右上角**Fork**按钮

3. Clone你自己的fork: ```git clone https://github.com/$userid/vnpy.git```
	* 如果你的fork已经过时，需要手动sync：[https://help.github.com/articles/syncing-a-fork/](https://help.github.com/articles/syncing-a-fork/)

4. 从**dev**创建你自己的feature branch: ```git checkout -b $my_feature_branch dev```

5. 在$my_feature_branch上修改并将修改push到你的fork上

6. 创建从你的fork的$my_feature_branch分支到主项目的**dev**分支的[Pull Request] -  [在此](https://github.com/vnpy/vnpy/compare?expand=1)点击**compare across forks**，选择需要的fork和branch创建PR

7. 等待review, 需要继续改进，或者被Merge!

在提交代码的时候，请遵守以下规则，以提高代码质量：

  * 使用[autopep8](https://github.com/hhatto/autopep8)格式化你的代码。运行```autopep8 --in-place --recursive . ```即可。
  * 使用[flake8](https://pypi.org/project/flake8/)检查你的代码，确保没有error和warning。在项目根目录下运行```flake8```即可。



## 项目捐赠

过去5年中收到过许多社区用户的捐赠，在此深表感谢！所有的捐赠资金都投入到了vn.py社区基金中，用于支持vn.py项目的运作。

先强调一下：**vn.py是开源项目，可以永久免费使用，并没有强制捐赠的要求！！！**

捐赠方式：支付宝3216630132@qq.com（*晓优）

长期维护捐赠清单，请在留言中注明是项目捐赠以及捐赠人的名字。



## 其他内容

* [获取帮助](https://github.com/vnpy/vnpy/blob/dev/docs/SUPPORT.md)
* [社区行为准侧](https://github.com/vnpy/vnpy/blob/dev/docs/CODE_OF_CONDUCT.md)
* [Issue模板](https://github.com/vnpy/vnpy/blob/dev/docs/ISSUE_TEMPLATE.md)
* [PR模板](https://github.com/vnpy/vnpy/blob/dev/docs/PULL_REQUEST_TEMPLATE.md)



## 版权说明
MIT
  




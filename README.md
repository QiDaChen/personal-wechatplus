# personal-wechatplus
个人微信的功能集成（获取热点新闻，自动回复，爬虫控制，傲梦编程教师端数据的自动抓取和检索）

#### 代码框架

start.py：脚本的代码入口文件，运行时候需要进行微信的扫码

run.py:	根据微信聊天信息的内容控制脚本的运行控制

find.py：对数据（data中的已完成课程和未完成课程）进行清洗

tuling.py ：图灵机器人的接口调用，根据传入的数据返回的数据进行格式化整理返回

data：存放爬虫爬取到的学生上课数据（已完成和未完成）

img：存放爬虫过程中的二维码图片

run.***.pyd对run 代码进行闭源处理的结果

start.bat : 快捷开始的批处理文件，双击便能运行本系统



#### 使用说明

##### 	使用本人已经搭建好环境的使用说明

​		1：添加本人的主机微信号（Chenphoun）

​		2：普通权限添加后直接发送消息就可以使用

​		3：傲梦的老师们需要进行以下操作录入个人信息

在与主机微信的聊天窗口直接发送指令<注册傲梦讲师>，接下来会收到账号和密码的输入格式说明，你只需要输入相应的个人账号和密码（**注意要一块输入，且账号和密码之间要用一个空格隔开**）

例如<**18091956102 zheshimima**>正确格式输入账号密码之后，还需要确认一下账号密码无误,回复<**信息无误请录入**>  出现录入成功的回复之后，就可以正常使用教师权限的功能了。

​		4：微信端口令说明：

​				I：图灵机器人权限打		 开始  or   start

​				II：图灵机器人权限关闭  		  退出  or  exit

​				III: 教师获取本日数据    获取数据

​				**注意：以下生成备课表等功能都需要先成功获取到数据之后才可以使用**

​				IV：获取未完成课时的信息检索   今日  or   近日

​				V：获取已完成课堂情况： 备课表   or    学生姓名+课堂反馈（如：陈奇课堂反馈）	

​				VI:	获取IT之家本日和本周的hot文章			

注意：**图灵机器人权限打开的时候是只能和进行聊天，新闻数据，笑话，天气等功能的使用，要想获取IT之家的热点和傲梦数据，需要退出图灵机器人权限才能使用，**

#### 	自行搭建环境说明

​		1：clone本项目到本地，（最好是服务器环境，不然意义不大。我使用的是阿里云服务器，）

​		2：改变bat批处理文件的路径（以编辑方式打开start,bat，把第二行python 之后 的文件路径换成你clone之后的start.py的文件路径）

​		3：安装所需的模块和方法

**itchat	requests	lxml	pandas	PIL	selenium<需要配置chromedriver驱动>	re		baidu-aip**

​		4：运行，双击批处理文件，**start.bat**之后会弹出微信登录二维码，让你的主机微信扫描登录，之后出现成功登录之后，就可以使用任何主机微信好友的账号进行功能的使用

**欢迎完善功能，和提出建议**

# 论文：

本课题研究的起因来源于现代人工作生活中的一些痛点，重复的手机软件使用以及工作数据被PC端的电脑所局限，抱着简化生活和工作内容的目的决定开发出一个简洁且不受使用限制的脚本，这一设计理念和Tim Peter 的 The Zen of Python不谋而合，而国内的应用软件中，微信无疑是和本脚本价值观及发展防线最为契合的一个。本脚本，适用于大多数的微信用户，并且对于本人公司的同事，脚本集成了更为方便的工作数据检索功能。本脚本采用python语言，因为python具有最为丰富的外接库，可以更容易解决大多数的项目功能难点。实现了网络爬虫的一些具体实例，并且把爬虫的功能封转在微信个人号之上，通过微信的聊天信息，控制爬虫流程的控制，极大的改善了网络的使用体验，改变了传统软件冗余的现状，具有极大的灵活性和实验价值



绪论

1.1编写目的

​    处于信息时代的我们，每天接受这无数的信息轰炸，现代人的信息接受量达到了人类历史的新高度，但是，当我们接受信息的过程所花费时间并不是完全等同于我们使用电脑或手机设备的时间，这期间我们需要对互联网中的数据进行人为的筛选和检索，在这里，我们把获取筛选数据的时间称之为无助且必要时间。手机，作为现代人最常使用的移动设备，无疑便利了我们的生活，但同时，如果我们给他集成过多的软件，首先找到并打开软件的过程就需要很长的时间，并且一部手机的负载是有限的，过大的资源占用之下必将导致我们手机设备的卡顿，这严重影响我们的手机使用体验。例如当我们想知道今天某座城市的天气，我们需要打开固定的天气咨询类软件，通过时间和城市的选择获得我们想要的数据，这种繁琐的信息交互模式无疑不是最好的选择。而本系统的目的就是：

把每天被各种应用软件奴役的人从重复性的工作学习娱乐中解脱出来，使人们在信息同步的前提下有更多可以自由支配的时间。在不影响工作质量甚至会提高工作效率的前提下实现工作信息的同步和工作内容的完善。在功能不打折扣，时间陈本不增加的基础上完成手机使用软件的精简化，能够根据个人偏好实现信息的做针对性同步。例如，当我们想知道哪座城市的天气的时候，或者今日的热点新闻，热点话题，只需要简单的一句口令，我们需要的内容就可以铺陈眼前，功能的智能化和量身定做化变得史无前例的便捷，在最小程度上增加手机的资源占用下极大的压缩玩手机期间的无助且必要时间。

1.2系统应用背景

近年来，人们花费在电脑和手机上的时间越来越多，手机的软件更是层出不穷，据美通社2019年1月17号的报道显示，全球用户每天使用手机5.1小时，爱尔兰用户每天使用时长更是高达8.4小时，而人们花费如此多的时间都用来做了什么呢？工作，社交，新闻，短视频，游戏。但是根据对周围人群的统计我发现，在重复的浏览过程中，包含了很多重复且毫无价值的信息来源，于是，人们打开各式各样的软件浏览着千篇一律的内容，无意间消磨了大量的工作学习时间，于是，我打算开发一款可以自动帮我们检索信息的脚本，以微信个人号的方式为我们推送各种量身定做且经过处理的数据，这些同样适用于工作效率的提高，以在线教育讲师的工作为例，每日的课时信息，学生学习状况的整理，周期内的工作总结，都可以在这个脚本下集成。

在中国，微信的出现，无疑改变了我们的社交途径和方式，作为中国人最常用到的应用软件，它因为简洁，快捷，被人们所热爱，每天我们都会或多或少的通过微信和远方的朋友聊天，而我们的脚本正是集成在这个便捷的载体之上。就像正常的聊天一样，发送信息，微信机器人就像我们的私人助手一样，快速的给我们想要的内容反馈。

1.3研究内容

​     本课题的主要研究内容在于多个脚本功能的集成及相互调用，功能主要包括基于itchat模块实现微信特定好友信息的持续获取和响应，基于reqursts模块实现异步加载数据的获取和基于pandas模块的数据清洗及检索，还有基于pygal模块的数据可视化模型的建立，以及基于pickle的文件数据的本地写入及读取，除此之外，我们需要积极研究的还有，如何管理不同权限的用户信息的功能分布，如何处理两种状态下的连天模式，即适用于普通用户的机器人聊天模式和只适用于高级权限的工作信息的聊天模式。




2需求分析

2.1功能需求

2.1.1用户体验

​    用户能够在请求之后尽快时间得到响应，至少比用户正常打开软件时候的时间成本低，对于手机的资源占用要尽可能的少，至少要比正常使用手机获取信息的资源占用要小，使用本脚本的学习成本尽可能的低，对于容易出错的部分要实现简洁但清晰的说明指导，获取的信息要准确并明了，信息的获取需要符合使用者的信息需求偏好该脚本需要能在通常网络环境下随时响应，

2.1.2多功能协调

​    微信个人号的聊天指令能够完成对各种功能的调用，相互之间的功能独立存在且相互联系，      

2.1.3数据的格式及传递

​    响应的数据简单明了。比如，课程计划，应包含学生姓名，上课时间，所属科目，学生的反馈，应包含学生姓名，课程进度，课程时间，教师评价，以及上课视频等内容。这里的大部分的内容在聊天过程中都是以文本格式传递的，学生的备课表需要以excel表格的形式返回。

2.1.4 功能

​    聊天有两种状态，基于图灵机器人的闲聊状态和集成的工作数据同步以及实时热点新闻的同步状态。

​    聊天机器人，实现微信聊天的自动回复，能够实时自动回复，可以接受并响应多种形式的微信消息，天气，火车信息等功能的调试及正常使用。

​    集成爬虫，在线教育平台的数据抓取和检索，能够根据指令完成，当前工作日待完成课程，以及当前工作日近期课程计划，已完成课程中某位学生的课程进度以及课堂表现，以及根据爬虫的数据进行excel表格统计等功能，除此之外包括但不限于每日热点新闻，舆论热点等信息的爬取和检索

​    支持多用户并发，能够微信账号对特定用户附加附加高级权限的功能，其他用户也能够通过指令对用户本人的数据进行爬取和检索。

2.2非功能需求

2.2.1安全性

​    账号安全，用户的工作账号安全和信息安全必须得到保证。该项目的代码需要进行加密，以防止攻击代码被人利用。

 

2.2.2稳定性

​    脚本需要在上线后实时响应，不能出现中途断线或者请求不响应的情况。对于各种异常可以扑捉，并做出处理。

2.2.3运行环境及设备准备

本操作脚本需要用到服务器，这里我们的实例是阿里云ecs云服务器，除此之外，我们需要一个用于信息整合和内容回复的微信个人号（下面称之为主机微信号），用户只需要是添加过主机个人号好友的微信个人号，

系统版本：Windows Server 2012 R2 数据中心版 64位

编辑器：pycharm

服务器运行：command命令行

Python环境 python 3.7.0

Lxml 4.2.5

pandas 0.23.4

Pillow 5.2.0

selenium 3.141.0

itchat 1.3.10

pip 10.0.1




3概要设计

3.1基本模块

​    本系统设计主要包含以下几个基本模块，自动获取数据，对获取到的大量数据进行数据清洗及处理，数据的传递，微信接口的架构，

3.1.1获取数据

​    获取服务器运行的微信号的好友信息，

​    获取傲梦教师端的课程数据数据，课程数据包含的内容有已完成课程，未完成课程，具体数据内容如下图所示，

​    获取IT之家的高阅读量的文章标题及链接，

​    根据接受信息获取图灵机器人的信息反馈

3.1.2数据清洗及处理

​    通过对傲梦网站数据的分析研究，对爬取到的原始数据进行结构化的处理，

​    通过对数据的筛选生成excel表格，和格式化的富文本

3.1.3微信接口的架构

​    实时接受微信消息

​    根据微信消息执行响应的模块，

​    根据各个模块的响应精准返回模块中生成的数据结果

​    根据不同的用户实现权限分级，

​    对于不同的用户权限进行功能细化

3.1.4脚本实现预期效果

​    因为本系统的用户在1000人以内且都是微信好友教师权限的用户也只有不到100人，所以对于用户身份验证的策略本系统拟采取本地初始设置，即对于普通权限的用户只需要是主机微信号的好友就可以使用，教师权限需要向管理员提交傲梦编程1对1少儿编程培训网站教师端的账号和密码经过管理员校验之后才能使用此权限的功能，普通用户只需要在和主机微信的聊天窗口下发送相应指令就可以得到响应，指令的帮助文档根据用户权限不同返回，如下图所示为普通用户的使用文档。普通用户以及教师的帮助文档如图 3.1 所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.gif)

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image004.gif)

图 3.1帮助文档

3.2流程图及说明

​    如下图所示为本操作系统的模块设计流程图

​    我们的脚本会持续监听微信消息的接收，当一条信息被接受，脚本会根据这个人的权限分流，以教师权限的用户为例，如果此时该用户直接使用了获取数据的指令，脚本会自动去该教师的傲梦编程教师端网站上获取该老师的数据，接下来该用户就可以直接通过口令检索出自己所需的数据。

脚本运行流程图3.2所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image006.gif)

图3.2 脚本运行流程示意图

3.3 关键技术介绍

3.3.1网络爬虫

​    网络爬虫，也称为"网络蜘蛛"，通过网页的链接地址搜索网页，从网站的某个页面开始，读取网页的内容，在网页中查找其他链接地址，然后通过链接地址找到下一个网页。这是一种继续循环的技术，直到根据某些策略爬网互联网上的所有网页。他可以快速捕获网站上可见的数据，是一种快速准确地获取数据的技术。目前不同的编程语言对爬虫都有相关的一些技术支持,如下表编程语言爬虫技术映射表编程语言主流爬虫框架(库)如表3.1所示

表3.1编程语言于主流爬虫库对照表

| 编程语言   | 主流爬虫框架（库）             |
| ---------- | ------------------------------ |
| C++        | open-source-search-engine      |
| Java       | Request   pyspiders Scrapy     |
| Python     | Gecco WebMagic   Spiderman     |
| JavaScript | x-ray   js-crawler scraperjs、 |
| C#         | Abot                           |
| PHP        | php-spider                     |
| Ruby       | nokogiri                       |
| Go         | Go_spider,scrape               |

 

3.3.2 python

​    Python是一种解释型面向对象的动态类型的开源的计算机程序设计语言，他因为语法简单功能强大以及且具有丰富的扩展库被人们所热爱，是轻量级的快速程序开发的不二之选

3.3.3 requests

​    Requests是一个以HTTP for Humans（给人用的http库）为宣言的网络编程库，他能够使用最为简洁明了的语法实现网络操作，提交请求获取响应，从来没有如此简单。在使用它的时候，你会惊叹，这才是python代码该有的样子。

3.3.4信息加密

信息加密技术是利用数学或物理手段，对电子信息在传输过程中和存储体内进行保护，以防止泄漏的技术。

3.3.5 pandas

​    pandas 是基于 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的[数据模型](https://baike.baidu.com/item/数据模型/1305623)，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

3.3.6 xpath

​    XPath即为[XML](https://baike.baidu.com/item/XML)路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言。

XPath基于XML的树状结构，提供在数据结构树中找寻节点的能力。起初XPath的提出的初衷是将其作为一个通用的、介于[XPointer](https://baike.baidu.com/item/XPointer)与[XSL](https://baike.baidu.com/item/XSL)间的语法模型。但是XPath很快的被开发者采用来当作小型[查询语言](https://baike.baidu.com/item/查询语言)

 

3.3.7 itchat

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。当然，该api的使用远不止一个机器人，比如[这些](http://python.jobbole.com/86532/)。该接口与公众号接口[itchatmp](https://github.com/littlecodersh/itchatmp)共享类似的操作方式，学习一次掌握两个工具。

如今微信已经成为了个人社交的很大一部分，这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。

3.3.9 webdriver

WebDriver是一种用于自动化web应用程序测试的工具，特别是用于验证它们是否按预期工作。它的目标是提供一个友好的API，易于探索和理解，比Selenium-RC (1.0) API更容易使用，这将有助于使您的测试更容易阅读和维护。它不依赖于任何特定的测试框架，因此它可以在单元测试项目中或从简单的旧的“main”方法中使用,有了他，我们可以让我们的脚本模拟大多数的浏览器操作。

3.3.10图灵机器人

图灵机器人开放平台是北京光年无限科技旗下的智能聊天机器人开放平台。通过图灵机器人开放平台，用户可快速构建自己的专属聊天机器人并为其添加丰富的机器人云端技能

3.3.11 AJAX异步加载

Ajax 不是一种新的编程语言，而是一种用于创建更好更快以及交互性更强的Web应用程序的技术。

使用 JavaScript 向服务器提出请求并处理响应而不阻塞用户核心对象[XMLHttpRequest](https://baike.baidu.com/item/XMLHttpRequest)。通过这个对象，您的 JavaScript 可在不重载页面的情况与 Web 服务器交换数据，即在不需要刷新页面的情况下，就可以产生局部刷新的效

3.3.12 pickle

​    在程序代码中中，我们常常需要把程序中的某些数据模型存储起来，这样在进行其他模块使用时直接将模型读出，而不需要去构建模型，这样就大大节约了时间。Python提供的pickle模块就很好地解决了这个问题，它可以序列化对象并保存到磁盘中，并在需要的时候读取出来，任何对象都可以执行序列化操作。

3.3.13 正则表达式

正则表达式是对[字符](https://baike.baidu.com/item/字符)串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

3.3.14 cookies

基于 Internet的各种服务系统应运而生，建立商业站点或者功能比较完善的个人站点，常常需要记录访问者的一些信息；论坛作为 Internet发展的产物之一，在 Internet 中发挥着越来越重要的作用，是用户获取、交流、传递信息的主要场所之一，论坛常常也需要记录访问者的一些基本信息（如身份识别号码、密码、用户在 Web 站点购物的方式或用户访问该站点的次数）。目前公认的是，通过 Cookie 和 Session 技术来实现记录访问者的一些基本信息

3.3.15百度AI人工智能平台

提供全球领先的语音、图像、NLP等多项人工智能技术，开放对话式人工智能系统、智能驾驶系统两大行业生态，共享AI领域最新的应用场景和解决方案，提供了很多可供开发者免费使用的人工智能接口。

3.3.16 批处理文件

批处理文件（batch file）包含一系列 DOS命令，通常用于自动执行重复性任务。用户只需双击批处理文件便可执行任务，而无需重复输入相同指令。编写批处理文件非常简单，但难点在于确保一切按顺序执行。编写严谨的批处理文件可以极大程度地节省时间，在应对重复性工作时尤其有效。




4详细设计

4.1功能需求和程序的关系

再本操作系统中，微信聊天窗口作为我们的运行页面，所以微信消息数据的实时同步是保证代码正常运行的关键因素，获取到微信聊天信息的时候，这个数据包含了，信息的发送者，信息的内容（文本），以及该聊天信息的特定id。这个数据需要和我们程序本身的初始化数据进行判断，得出发送信息的身份对应用户权限，以及当前聊天模式，有了这个权限和模式，系统便可以根据用户的权限和信息内容明确用户的意向，聊天机器人模式下，系统根据用户的发送的内容去图灵机器人接口中获取响应，然后把这个响应返回给我们的用户，从而实现聊天机器人的功能，通常模式下，用户保持微信聊天正常状态，但是当用户身份为已经赋予权限的傲梦教师身份的时候，用户只需通过特定指令控制程序的走向，例如，当用户通过特定指令表示要获取当前时间的热点新闻，系统便会同过调用获取实时热点新闻的接口，获取到当前网站中的热点内容，本系统的设计模式采用，分布式扁平化设计理念，每一个新的指令进入，就对应新的脚本需要被执行，低内聚高耦合，模块之间只存在较少的联系，且模块之间互不干扰。 

4.2接口设计

4.2.1微信信息的获取

在本脚本中，微信的聊天框可以说扮演了一个用户界面的角色，用户和服务器的一切交互都是通过微信信息的发送来完成的，所以脚本如何去获取微信好友的信息就成了本脚本第一个要解决的实际问题，itchat作为一个开源的微信个人号接口，让数据的传递变得空前的简洁，他可以完美模拟用户登录网页端的微信，实现代码如图4.1 所示

 

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

图4.1 微信消息实时获取示意图

运行结果如下图4.2所示：

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

图4.2 微信登录成功终端显示效果图

通过运行代码首先会出现微信登录所需的扫码，程序模拟登录了网页版的主机微信号。出现login successfully as 微信名字样表示登陆成功，msg_register函数实现了各种微信信息的实时获取，此处在text函数中可以把文本格式的信息内容获取到，经过对msg微信聊天信息研究发现，脚本所需的信息来源用户，信息内容，都可以直接在msg中获得。如下图代码和运行结果如图4.3所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

图4.3微信消息数据解析代码示意图

 

 

运行结果如图4.4所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

图4.4 微信聊天数据解析运行效果图

 

4.2.2新闻热点的爬取

对于舆论热点，本脚本拟获取IT之家版面中的如下图框选内容所示中的最热排行和周榜内容的网站示意图，如图4,5所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

图4.5 IT之家网站主页

​    通过对数据的研究，发现本数据可以直接在网站的html代码中找到，如图4.6所示

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image018.jpg)

图4.6 IT之家网站热点新闻网页代码示意图

 

通过数据比对，发现a标签中的文本就是文章的标题，而a标签的属性herf中保存着该热点新闻的url地址，要想抓取这个网页版的IT之家版面，需要模拟通过request模块向IT之家网站服务器发送请求，获取到该页面的内容并通过xpath把所属标签中的内容精确检索。且为防止被网站的反爬虫机制限制甚至拒绝响应，我们需要把爬虫程序伪装成浏览器，即提交请求的时候附加上请求头里面的关键内容，浏览器请求头内容如图4.8所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg)

图4.8 浏览器请求网页的请求头内容

在红框中的user-agent中，包含了浏览器兼容的内核版本，请求电脑的操作系统和位数。有了这些数据，我们的爬虫脚本就可以伪装成一个浏览器请求，从而避免了网站的反爬机制可能带来的问题，整体的实现思路如下，首先，用requests库的get方法发送请求，对于接受的的响应一个html网页代码进行树形结构的解析，然后通过xpath标签路径获取到指定内容的数据，这里需要通过网页代码结构的熟悉和研究找出多个标签之间的内在联系，使用xpath表达式快速检索到所需的数据，

请求代码如图4.9所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image022.jpg)

图4.9 模拟请求IT之家官网获取响应的代码示意图

Xpath获取特定标签的代码如图4.10所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image024.jpg)

图4.10 xpath获取特定标签内容的代码示意图

运行结果如图4.11所示：

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image026.jpg)

图4.11 IT之家数据获取运行结果终端效果图

4.2.3图灵机器人接口设计

图灵机器人的接口创建只需要登录网站,

创建一个机器人对象，这里的我们需要进行机器人的一个初始化设置，聊天机器人的初始化界面如图4.12所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image028.jpg)

图4.12 图灵机器人的应用创建网站示意图

机器人创建完毕之后，设置他的终端接入方式，图灵机器人的接口，需要根据不同的发送内容，得到相应的信息反馈，图灵机器人的接口是一个成熟并且完善的接口，这里的接口在本脚本中 拟选择使用api接入，因为在聊天机器人的基础上还有集成教师应用等有针对性的功能，如果选择直接个人号接入势必会造成接口的调用冲突，影响用户的使用体验。并且使用api接入，这里会让我们的脚本更加灵活，可以对图灵机器人做出更多针对性的调整。选择api接入如图4.13所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image030.jpg)

图4.13 图灵机器人接口选择示意图

接下来是代码实现，依旧使用requests模块对网页版的图灵机器人数据进行抓取，不同的是，这里我们需要通过提交聊天信息才能获取到图灵机器人的响应，所以此处的请求方式变成了post，代码实现如图4.14所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image032.jpg)

图4.14 图灵机器人数据获取代码示意图

4.2.4 百度人工智能平台图片文字识别

百度人工智能平台的应用创建细节如图4.15所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image034.jpg)

图 4.15 百度人工智能平台图片文字识别接口设置截图

百度人工智能平台的图片识别相应代码如图4.16所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image036.jpg)

图4.16百度人工智能如图片文字识别接口实现代码

4.2.5傲梦官方网站教师端数据的获取

​     网站数据的抓取是本脚本的难点，因为数据的复杂度远远要超过以上的两种数据，高复杂性带来了更多的处理数据的障碍，首先，我们获取到的数据是需要在登陆状态下的，所以在发送请求的时候除了反爬虫必须的useragent还需要验证身份信息的cookies，这里所以脚本必须要在登陆状态下获取到cookies才能成功请求到网页上的数据，这里就需要用到selenium库，他能够使用脚本对网页进行完全模拟人的操作，经过对傲梦编程网页的登录页面分析如下图所示，傲梦网页主页示意图如图4.17所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image038.jpg)

图4.17 傲梦编程网站登录页面

网址https://all-dream.com/front_login.jsp?param=tacher之后。本需要完成的工作分别是，输入账号和密码，输入验证码，点击登录，如果信息无误，登录成功后，就可以用selenium中的内置方法获取到登陆状态下的网页cookies，账号和密码基本不会改变，主要的问题此时出在了验证码的识别上，首先需要从页面拿到验证码的图片信息，因为验证码是每次请求都不同的，所以要保证webdriver操作页面的时刻的验证码图片信息获取到，此处可以采用webdriver的内建方法save_screenshot对验证码页面进行截图，并且还需要配合PIL的图片操作库，对截取的图片进行剪裁处理。实现代码如下所示：

def getimg(img_time):
     '''得到网页登陆时候所需的验证码图片
        driver是全局变量  后面需要通过driver会的cookies
        成功过得到会返回True
     '''
     global driver
     driver = webdriver.Chrome()
     \#driver.set_window_size() # 设置浏览器尺寸
     driver.maximize_window()
     driver.get('https://all-dream.com/front_login.jsp?param=teacher')
     time.sleep(5) # 要加载一段时间，留出时间
     if driver.title == '傲梦直播':
         driver.save_screenshot('.\image\{}.png'.format(img_time))
         yzm_elmt = driver.find_element_by_xpath(pic_xpth)
         L = yzm_elmt.location['x']
         T = yzm_elmt.location['y']
         R = L+yzm_elmt.size['width']
         B = T+yzm_elmt.size['height']
         im = Image.open('.\image\{}.png'.format(img_time))
         print(L,T,R,B)
         im = im.crop((L,T,R,B))
         im.save('.\image\{}1.png'.format(img_time))
         time.sleep(1)
         print(L,T,R,B)
         return True
     else:
         return False

此时图片获取到之后识别成了又一个需要解决的问题，本系统采取两种识别方案交替进行，首先会使用百度的人工智能平台提供的图片文字识别策略，但是不可避免的问题是自动识别具有一定的误差，所以不能保证识别的百分之百成功率，所以这里拟采取图片通过主机微信发送给用户让用户来人工识别，这样图片的识别就能够迎刃而解。以下是两种解决方案状态下的代码线上运行效果。

使用百度ai人工智能开放平台的解决方案，通过调用接口实现验证码的基本识别，实现代码如下所示：

def aiYzm(filename):
     ''':param filename: 表示图片的文件路径return: 返回图片经过百度开发识别的结果，如识别失败的话直接返回false '''
     from aip import AipOcr
     """ 你的 APPID AK SK """
     APP_ID = '16190824'
     API_KEY = 'sW2uzXjyWqiyC5Lq2lNsdnig'
     SECRET_KEY = 'GVF2YX5cS7RZqfXMGgIpnuPDPQyfEyWq'
     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
     """ 读取图片 """
     def get_file_content(filePath):
         with open(filePath, 'rb') as fp:
             return fp.read()
     image = get_file_content(filename)
     """ 调用数字识别 """
     client.numbers(image);
     """ 如果有可选参数 """
     options = {}
     options["recognize_granularity"] = "big"
     options["detect_direction"] = "true"
     """ 带参数调用数字识别 """
     a = client.numbers(image, options)
     try:
         a = a['words_result'][0]['words']
         print(a)
     except:
         return False
     else:
         if len(a) == 4:
             return a
         else:
             return False

另外一种解决方案是直接把图片经过主机微信号发送给客户端微信，通过用户人工识别图片的结果，进行消息回复之后，实现验证码的人工识别。这里的实现代码如下

imgnum = aiYzm('.\image\{}1.png'.format(shot_tm))
 if imgnum:
     user.yzm = imgnum
     suss, user.cookies = log_web(user.admin, user.yzm)
     if suss:
         itchat.send_msg('网站登录成功，请稍等片刻数据马上抓取成功', user.username)
         timec = logdata(user)
     else:
         itchat.send_msg('so sad~ 验证码自动识别失败，请重新获取数据', user.username)
         driver.close()

成功识别图片的运行示意图如图4.18示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image040.jpg)

图4.18 验证码图像识别成功运行示意图

失败识别验证码需要人工输入的运行示意图如图4.19所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image042.jpg)

图4.19 人工识别验证码运行效果

接下来依旧使用requests方案对傲梦编程官网的数据进行爬取，通过网站页面的结构分析，发现主要数据分成两部分，已完成课程数据和未完成课程的数据。对应页面的内容如下图所示，

已完成课程的内容网页效果图如图4.20

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image044.jpg)

图4.20 傲梦编程网站教师端已完成课程效果图

未完成课程的内容网页效果图如图4.21

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image046.jpg)

图4.21 傲梦编程教师端未完成课程效果图

通过对页面的html代码分析发现，本分关键代码人如图4.21所示：

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image048.jpg)

图4.22 傲梦编程网站关键代码截图

 

通过对网站后台代码的研究和探索性检查，网站的数据是异步加载的数据，通过谷歌浏览器的检查工具对网页中的异步加载数据排查（数据存在于检查接口下的NETWORK对应XHR里面）

网页异步加载数据总页面如图4.23

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image050.jpg)

图4.23 检查接口下异步加载数据列表示意图

该网页存在所需的加载数据，数据的格式是json格式，以已完成数据中的一页的一条记录为例，数据如下

{"lessonId":"eec9348ceba84ef99e1d6d40edef2943","studentId":"4697f12fdf224456a4a26c417eadcea8","teacherId":"e4ccd1f328d84a76ab46e382d79af6a8","lessonName":"64510班级课程","studentName":"章圣歆","teacherName":"陈奇","lessonStartTime":1557055803000,"lessonEndTime":1557058654000,"teacherComment":"知识点内容：\n\t课程进度  pye21-1\n\t内容总结  贪吃蛇游戏的函数化\n孩子掌握情况：\n\t孩子具体完成情况  能在老师的引导下理解课堂代码的实现逻辑\n\t优点 学习兴趣高  理解能力强\n\t欠缺点  暂无\n需要家长配合：暂无\n上次课作业完成情况：完成  存在问题  已在课堂上解决","teacherCommentLevel":4,"studentComment":null,"lessonStatus":"2","studentCommentLevel":null,"studentCommentOne":null,"studentCommentTwo":null,"studentCommentThree":null,"studentCommentFour":null,"studentCommentFive":null,"teacherCommentOne":4,"teacherCommentTwo":4,"teacherCommentThree":4,"teacherCommentFour":4,"teacherCommentFive":4,"teacherLessonUrl":null,"lessonUrl":"http://timer.91veo.com/v1/meeting/join?id=1402562&value=fafc2c1c46bc952e524ca3c7bb42a1f9","recordUrl":"https://cdn.all-dream.com/user/e4ccd1f328d84a76ab46e382d79af6a8/20190505_202919_zoom_0.mp4","note":"","noteTeacher":"NOIP测试分数：","courseTypeName":"python程序设计","courseTypeId":"702dd6f4b95f418ebf5f54bd652e859f","studentSignNote":"","studentSignState":"1","online":"1","free":"0","homework":"https://cdn.all-dream.com/exercise/307f56ba15f84ce9b94e05ac0345ba4c/425.py"},

文件中的json格式的数据可以继续用requests方式进行数据的爬取，这里因为数据是一部加载的数据，需要用到json模块对数据进行格式化处理，换而言之，只有json才能把网页中的结构体数据转换成python的字典格式，但是字典的数据课时处理起来不是非常的方便，在本系统中我们采用pandas的库对数据进行更加精细化的的直观处理。且网页中表示的实现是用unix时间戳来表示，这里本系统采用python的datatime的模块对时间进行格式化的处理。具体的实现代码如下所示：

def getData(cookies):
     '''获取傲梦网站的学生信息以及课程信息
        返回获取数据的文件所在目录
        参数是网站所需的cookies
        数据的精细化处理  是数据的检索更加简单
     '''
     timec = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
     os.mkdir('./data/'+timec)
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
     url = 'https://all-dream.com/rest/hour/queryMyCoursePlan4TeacherNew?free=0&limit=10&random=0.5043750329478451&page=1'
     today_class = requests.get(url,headers=headers,cookies=cookies)
     today_class = json.loads(today_class.text)
     print(today_class)
     with open('./data/'+timec+'/今日课程计划','wb') as file:
         pickle.dump(today_class,file)
     url_list = ['https://all-dream.com/rest/courseManage/queryMyOverCourse4Teacher?limit=10&page={}'.format(i+1)  for i in range(10)]
     over_all_class = []
     for url in url_list:
         over_class = requests.get(url,headers=headers,cookies=cookies)
         data_1 = json.loads(over_class.text)['list']
         over_all_class.append(data_1)
     key = 1
     stOverClass = {}
     for ondPage in over_all_class:
         for oneClass in ondPage:
             stOverClass[key]=oneClass
             key+=1
     df = pd.DataFrame(stOverClass).T

     with open('./data/'+timec+'/已完成课程','wb',) as file2:
         pickle.dump(df,file2)
     return timec

 


这里为直观展示如图已完成课程数据中的一个数据结构图如图4.24

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image052.jpg)

图4.24 已完成课程数据结构图

其中满足我们需求的数据只需要学生姓名（studentName）上课时间（lessonStartTime）课程类别（courseTypeName）以及教师评价（teacherComment）其中课堂的上课时间是unix时间戳需要转换成正常显示的时间格式，评价中包含上课进度，学生课堂表现，知识点等内容。在这里我们首先要做的事情是吧数据西安进行存储，这里用到pickle模块，并且为了后期的容易清洗，数据格式用pandas模块中的dataframe数据表的格式保存，待完成课程的数据用以上相同的策略也可以抓取。功能中的今日课程计划和近日课程计划都是对待完成课程数据的检索，某某学生的课堂反馈则是对已完成课程 的数据检索。以及完成课程的excel表格也是对已完成课程的检索,实现代码如下所示：

def getToday(path,flag):
     '''参数是当前目录（今日学生信息的名称）下的文件名称
        返回值是一个字符串  包含今日未完成课程信息
        功能：获取当前日期内的上课内容
     '''
     if flag:
         tm = '近日'
     else:
         tm = '今日'
     str1 = ''
     with open('./data/'+path+'/今日课程计划','rb') as file:
         data = pickle.load(file)
     stlist = data['list']
     nowday = time.strftime("%Y-%m-%d",time.localtime(time.time()))
     times=0
     if not flag:
         for st in stlist:
             sttime = uTime(st['startTime'])
             if sttime[:10]!=nowday:
                 continue
             times+=1
             edtime = uTime(st['endTime'])
             stname = st['studentName']
             kemu = st['courseTypeName']
             banji = st['courseHourName']
             str1 += '\t学生：{}   \n\t时间：\n\t{}\n\t{}   \n\t科目：\t{}   \n\t班级：{}\n'.format(stname,sttime,edtime,kemu,banji)
     else:
         for st in stlist:
             sttime = uTime(st['startTime'])
             times+=1
             edtime = uTime(st['endTime'])
             stname = st['studentName']
             kemu = st['courseTypeName']
             banji = st['courseHourName']
             str1 += '学生：{}   \n时间：\n{}\n{}   \n科目：{}   \n班级：{}\n'.format(stname,sttime,edtime,kemu,banji)

     if times >=1:
         return '老师您好，\n{}你总共有{}节课\n内容如下\n'.format(tm,times)+str1
     else:
         return'老师~今天真幸福呀,\n{}你已经完成了所有工作\n当然今天也可能是非常愉快的休息日，\n试试召唤智能机器人,\n  \"小小奇\" '.format(tm) 

对于特定学生的课堂表现内容获取函数如下所示      
 def getfk(name,timec):
     '''
     参数：查看反馈的学生姓名  以及保存本次数据的文件最内层路径
     返回值：包含匹配到该学生的三条数据  如果先搞改变匹配数据的数量只需要改掉times里的值
     功能实现原始数据的检索  可通过学生姓名直接检索    
     '''
     with open('./data/'+timec+'/已完成课程','rb') as file:
         df = pickle.load(file)
     student = df[df['studentName']==name]
     msg_list = []
     for i in range(len(student)):
         st = student.iloc[i]
         remark = st['teacherComment']
         videourl = st['recordUrl']
         star = st['teacherCommentOne']
         stTime = st['lessonStartTime']
         msg = '这节课的开始时间是:\n{}\n这节课里你对孩子评价是：\n{}\n您为孩子打出惊人的{}颗星\n视频链接:\n{}\n--------------------------------------------'
         msg_one = msg.format(uTime(stTime),remark,star,videourl) 
         msg_list.append(msg_one)
     return msg_list

对于备课表单自动生成，需要把网站爬取的相应数据转换成固定格式的excel格式，pandas的内置方法to_csv可以直接把格式为DataFrame的数据表直接转换成excel表格，实现代码如下所示：

def savetoexcel(a):

​    for i in a:

​        with open('傲梦备课表.csv','a+',encoding = 'gbk',newline='')as csvfile:

​            writer = csv.writer(csvfile)

​            writer.writerow(list(i.values()))      

​    with open("{}.csv".format('傲梦1')) as aaa:

​        lalal = pd.read_csv(aaa,header=None,skiprows=6)

​        lalal.columns = ['姓名', '课程类别', '课堂开始时间', '课堂结束时间', '课程进度', '内容总结']

lalal.to_excel("{}.xlsx".format('傲梦备课表')

4.2.5 程序脚本集成

​    本系统的代码结构如图所示4.25所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image054.jpg)

图4.25 代码文件示意图

其中start.bat是本系统的快速运行脚本，双击它会自动使用python3版本环境运行代码start.py，而start.py会使用itchat自动登录微信，这里主机微信号需要使用扫描自动生成的微信二维码进行账号授权。经过这一步之后，微信的实时消息就可以被获取到，此时就可以在run.py根据帮助文档中的聊天信息做出相应的响应。其中响应分为傲梦官网学生信息的响应和图灵机器人的信息响应，以及附加功能中的接口调用，比如IT之家热点新闻。其中聊天的对象分为两个权限，对应程序代码中的两个类，代码如下所示

class Friends():
     def __init__(self):
         with open('./data/好友信息','rb',) as file2:
             self.df =pickle.load(file2)
     def isvip(self,fromusername):
         username = self.df[self.df['Remark'].isin(list(message.keys()))]['UserName'].values
         if fromusername in username:
             return True
         else:
             return False

     def readvip():
         pass
 class Teacher():
     def __init__(self,username):
         self.username = username
         with open('./data/好友信息','rb',) as file2:
             self.df =pickle.load(file2)
         self.name = self.df[self.df['UserName']==self.username].iloc[0].Remark
         self.admin = message[self.name]
         print(self.name)
     def getmessage(self,flag):
         if self.msg_1['Text'] =='小小奇':
             flag = True
         return flag
     def getcookies(self):
         '''
            验证码图片的微信发送
            验证码保存在本地   文件名由当前时间命名
            时间作为发送信息的图片名
         '''
         self.img_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
         if getimg(self.img_time):
             return self.img_time
     def svtime(self,timec):
         self.timec = timec
 class Nomal():
     def __init__(self,username):
         self.flag = False
         self.username = username

通过聊天信息Friends类中isvip方法对信息发送者的权限进行分类，确定是Teacher类还是Nomal类，对于不同权限的用户采取不同的信息响应策略，但是机器人的功能基本一致，机器人权限的开关和信息交互代码如下所示：

nomal = Nomal(msg['FromUserName'])
 print('创建聊天')
 nomal.msg = msg
 if nomal.msg['Text'] in ['start','小小奇','开始']:
     itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',nomal.username)
     nomalflag[nomal.username] = True
 elif nomal.msg['Text'] in ['help','帮助']:
     itchat.send_image('./image/nomal.png',nomal.username)
 elif nomal.msg['Text'] in ['end','exit','退出']:
     nomalflag[nomal.username] = False
 try:
     if nomalflag[nomal.username]:
         itchat.send_msg(jqr(nomal.msg['Text'])+".",nomal.username)
 except:
     pass

对于教师权限的用户的功能调用流程控制的代码实现策略如下所示：

user = Teacher(fromusername)
 user.msg_1 = msg
 if user.msg_1['Text'] in ['start','小小奇','开始']:
     itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',user.username)
     userflag[user.username] = True
 elif user.msg_1['Text'] in ['end','exit','退出']:
     userflag[user.username] = False
 if len(userflag):
     if userflag[user.username]:
         itchat.send_msg(jqr(user.msg_1['Text'])+".",user.username)

 if len(userflag)==0 or userflag[user.username]==False:
     if user.msg_1['Text'] == '获取数据':
         itchat.send_msg('请耐心等候，小爬虫正在快吗加鞭获取数据', user.username)
         shot_tm = user.getcookies()
         itchat.send_msg(msg_to_u[1],user.username)
         imgnum = aiYzm('.\image\{}1.png'.format(shot_tm))
         if imgnum:
             user.yzm = imgnum
             suss, user.cookies = log_web(user.admin, user.yzm)
             if suss:
                 itchat.send_msg('网站登录成功，请稍等片刻数据马上抓取成功', user.username)
                 timec = logdata(user)
             else:
                 itchat.send_msg('so sad~ 验证码自动识别失败，请重新获取数据', user.username)
                 driver.close()

         else:
             itchat.send_image('.\image\{}1.png'.format(shot_tm),user.username)
     elif user.msg_1['Text'] in ['help', '帮助']:
         itchat.send_image('./image/teacher.png',user.username)
     elif re.findall('\d+',user.msg_1['Text']):
         if len(re.findall('\d+',user.msg_1['Text'])[0])==4:
             user.yzm = re.findall('\d+',user.msg_1['Text'])[0]
             suss,user.cookies = log_web(user.admin,user.yzm)
             if suss:
                 timec = logdata(user)
             else:
                 itchat.send_msg('so sad~ 验证码输入错误，请重新获取数据', user.username)
                 driver.close()

 

     elif user.msg_1['Text'] in '近日课程计划':
         print(timec)
         user.closetoday = getToday(timec,True)
         itchat.send_msg(user.name[:-4]+user.closetoday,user.username)
     
     elif user.msg_1['Text'] in '今日课程计划':
         print(timec)
         user.today = getToday(timec,False)
         itchat.send_msg(user.name[:-4]+user.today,user.username)
     elif user.msg_1['Text'][-4:]=='课堂反馈':
         ms = getfk(user.msg_1['Text'][:-4],timec)
         print(user.msg_1['Text'][:-4])
         if len(ms)>=1:
             itchat.send_msg('已为您匹配到{}个结果'.format(len(ms)),user.username)
             for ms_1 in ms:
                 itchat.send_msg(ms_1,user.username)
         else:
             itchat.send_msg(msg_to_u[-1],user.username)
         for msg in ms:
             itchat.send_msg(ms,user.username)
     elif user.msg_1['Text'] == '热点':
         day,week = getnews()
         print(day,'\n',week)
         itchat.send_msg(day, user.username)
         itchat.send_msg(week, user.username)

4.3功能函数

​    获取微信好友信息的函数如图4.26所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image056.jpg)

图4.26微信登录后好友信息身份信息的汇总获取代码实现

​    获取网站cookies的函数如图4.27所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image058.jpg)

图4.27 模拟浏览器登录傲梦网站获取cookies代码截图

处理数据如图4.28所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image060.jpg)

图4.28 对爬取到的异步加载数据进行第一次数据筛选代码截图






4.4运行设计

批处理(Batch)，也称为批处理脚本。顾名思义，批处理就是对某对象进行批量的处理。批处理文件的扩展名为bat。在本系统中，脚本的运行采用dos批处理运行python代码，严格遵守pep20的程序设计理念，以简约轻便为主旨，程序的运行指令为dos批处理文件，以下是文件的编码示意图如图4.19

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image062.jpg)

图4.19 脚本启动dos文件代码截图

 

4.5系统数据结构设计

4.5.1 用户傲梦网站的身份信息

教师的个人信息表设计如表4.1所示，

 

表4.1 教师个人信息表













| 姓名 | 账号        | 密码   |
| ---- | ----------- | ------ |
| 陈奇 | 18000000000 | 123456 |

教师的身份信息以上表中的格式存储，内容经过base64加密，

4.5.2 学生已完成课程数据

​    学生的已完成课程数据格式如表4.2所示

表4.2 学生已完成课程数据表





















| 学生姓名 | 上课时间                               | 科目             | 教师评价                             | 上课进度           |
| -------- | -------------------------------------- | ---------------- | ------------------------------------ | ------------------ |
| 李一一   | 2019-01-01   10:30 2019-01-01    11:20 | Python程序与设计 | 包含学生课堂表现，课堂知识点，等内容 | Python初级课第一课 |

 

4.5.3学生待完成课程数据

​    学生的待完成课程数据表如表4.3所示

表4.3 学生未完成课程数据表













| 学生姓名 | 上课时间                           | 科目             |
| -------- | ---------------------------------- | ---------------- |
| 李一一   | 2019-01-01-10:30至2019-01-01-11:20 | Python程序与设计 |

 




5 测试与结果分析

5.1 运行环境

​       硬件：因为需要实时获取，所以需要运行在服务器环境中，本系统运行环境在阿里云的云服务器。

​       软件：本脚本需要再python3.的环境下运行，webdriver需要在谷歌浏览器的安装目录下保存谷歌浏览器的webdriver驱动。

5.2运行界面及结果测试

5.2.1代码的运行

​    测试环境：

​       操作系统：Wingdows10企业版 64位

​       运行方式：Dos批处理文件

​       Python版本：Python3.7.0

​       浏览器版本：Goole Chrome版本 74.0.3729.131（正式版本） （64 位）

运行界面截图如下图5.1所示

​              ![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image064.jpg)

​      图5.1 程序运行启动成功终端效果图

5.2.2 爬取数据的展示

新闻热点的终端输出展示截图如图5.2所示

 

 

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image066.jpg)

图5.2 热点数据的终端输出效果图

微信端新闻热点新闻的截图如图5.3所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image068.jpg)

图5.3 热点数据的微信端输出效果图

鉴于篇幅限制，以下为代码运行结果只展示微信端截图，

聊天机器人功能检测如图5.4所示

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image070.jpg)

图5.4聊天机器人微信端输出效果图

傲梦编程网站数据的检索测试示意图运行截图如图5.5所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image072.jpg)

图5.5获取傲梦数据微信端输出效果图

 

傲梦网站自动生成的备课表如图5.6所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image074.jpg)

​    图5.6 脚本自动生成备课表的文件预览图

 

 

 

 

 

 

 

 

 

 

 

 

 

 

参考文献

[1]  Allen B. Downey.《Think Python: How to Think Like a Computer Scientist》Green Tea Press

[2]  Python程序设计 [An Introduction to Programming Using Python]．[美] 戴维 I.施奈德（David I. Schneider）著；车万翔 译

| [3]檀冬宇.基于Python的大众点评网数据抓取技术研究[J].计算机产品与流通,2019(05):116. |
| ------------------------------------------------------------ |
| [4]. Biophysical Society; Python hearts reveal   mechanisms relevant to human heart health and disease[J]. NewsRx Health &   Science,2019. |
| [5]Tomas Beuzen,Joshua Simmons. A variable   selection package driving Netica with Python[J]. Environmental Modelling and   Software,2019,115. |
| [6]Simon Olofsson,Lukas Hebing,Sebastian Niedenführ,Marc   Peter Deisenroth,Ruth Misener. GPdoemd: A Python package for design of   experiments for model discrimination[J]. Computers and Chemical   Engineering,2019,125. |
| [7]Omid Haji Maghsoudi,Annie Vahedipour,Thomas   Hallowell,Andrew Spence. Open-source Python software for analysis of 3D   kinematics from quadrupedal animals[J]. Biomedical Signal Processing and   Control,2019,51. |
| [8]Theo Steininger,Jait Dixit,Philipp   Frank,Maksim Greiner,Sebastian Hutschenreuter,Jakob Knollmüller,Reimar   Leike,Natalia Porqueres,Daniel Pumpe,Martin Reinecke,Matevž Šraml,Csongor Varady,Torsten Enßlin. NIFT y 3 – Numerical   Information Field Theory: A Python Framework for Multicomponent Signal   Inference on HPC Clusters[J]. Annalen der Physik,2019,531(3). |




致  谢

​       经过两个多月的努力，本脚本完美上线，在这里致谢同事罗煜，鲍得江等人的帮忙测试功能，提出了很多好的意见，感谢百度人工智能开放平台，解决了一部分验证码识别的问题，感谢图灵机器人的开发公司北京光年无限科技及开发人员。感谢我的毕业设计指导老师任强老师，为我的脚本完善提供了很好的建议和指导。

​    除此之外，感激大学期间所有的老师们，他们带我走进了计算机这个神奇并且美丽的世界，感激车鹏飞老师，他用浅显易懂的方式让我理解了编程语言的内部机制，感激孙少波老师，他带我走进python的世界，并给我了很多学习和项目的经验，记得大一的时候，在张岗亭老师的引导下，当我用c语言完成99乘法表的时候，满心的激动，后来通过任强老师的网页设计，我搭建出了自己的第一个个人网页，所有的老师们带给我的知识，都让我在后来的学习中获益匪浅。

​    最后，感谢我的舍友李尧，作为一个刚上大学时候连搜索引擎都不能熟练应用的电脑小白 ，在他的指导下，学会了科学的使用电脑，这让我的学习效率，事半功倍。绪论

1.1编写目的

​    处于信息时代的我们，每天接受这无数的信息轰炸，现代人的信息接受量达到了人类历史的新高度，但是，当我们接受信息的过程所花费时间并不是完全等同于我们使用电脑或手机设备的时间，这期间我们需要对互联网中的数据进行人为的筛选和检索，在这里，我们把获取筛选数据的时间称之为无助且必要时间。手机，作为现代人最常使用的移动设备，无疑便利了我们的生活，但同时，如果我们给他集成过多的软件，首先找到并打开软件的过程就需要很长的时间，并且一部手机的负载是有限的，过大的资源占用之下必将导致我们手机设备的卡顿，这严重影响我们的手机使用体验。例如当我们想知道今天某座城市的天气，我们需要打开固定的天气咨询类软件，通过时间和城市的选择获得我们想要的数据，这种繁琐的信息交互模式无疑不是最好的选择。而本系统的目的就是：

把每天被各种应用软件奴役的人从重复性的工作学习娱乐中解脱出来，使人们在信息同步的前提下有更多可以自由支配的时间。在不影响工作质量甚至会提高工作效率的前提下实现工作信息的同步和工作内容的完善。在功能不打折扣，时间陈本不增加的基础上完成手机使用软件的精简化，能够根据个人偏好实现信息的做针对性同步。例如，当我们想知道哪座城市的天气的时候，或者今日的热点新闻，热点话题，只需要简单的一句口令，我们需要的内容就可以铺陈眼前，功能的智能化和量身定做化变得史无前例的便捷，在最小程度上增加手机的资源占用下极大的压缩玩手机期间的无助且必要时间。

1.2系统应用背景

近年来，人们花费在电脑和手机上的时间越来越多，手机的软件更是层出不穷，据美通社2019年1月17号的报道显示，全球用户每天使用手机5.1小时，爱尔兰用户每天使用时长更是高达8.4小时，而人们花费如此多的时间都用来做了什么呢？工作，社交，新闻，短视频，游戏。但是根据对周围人群的统计我发现，在重复的浏览过程中，包含了很多重复且毫无价值的信息来源，于是，人们打开各式各样的软件浏览着千篇一律的内容，无意间消磨了大量的工作学习时间，于是，我打算开发一款可以自动帮我们检索信息的脚本，以微信个人号的方式为我们推送各种量身定做且经过处理的数据，这些同样适用于工作效率的提高，以在线教育讲师的工作为例，每日的课时信息，学生学习状况的整理，周期内的工作总结，都可以在这个脚本下集成。

在中国，微信的出现，无疑改变了我们的社交途径和方式，作为中国人最常用到的应用软件，它因为简洁，快捷，被人们所热爱，每天我们都会或多或少的通过微信和远方的朋友聊天，而我们的脚本正是集成在这个便捷的载体之上。就像正常的聊天一样，发送信息，微信机器人就像我们的私人助手一样，快速的给我们想要的内容反馈。

1.3研究内容

​     本课题的主要研究内容在于多个脚本功能的集成及相互调用，功能主要包括基于itchat模块实现微信特定好友信息的持续获取和响应，基于reqursts模块实现异步加载数据的获取和基于pandas模块的数据清洗及检索，还有基于pygal模块的数据可视化模型的建立，以及基于pickle的文件数据的本地写入及读取，除此之外，我们需要积极研究的还有，如何管理不同权限的用户信息的功能分布，如何处理两种状态下的连天模式，即适用于普通用户的机器人聊天模式和只适用于高级权限的工作信息的聊天模式。




2需求分析

2.1功能需求

2.1.1用户体验

​    用户能够在请求之后尽快时间得到响应，至少比用户正常打开软件时候的时间成本低，对于手机的资源占用要尽可能的少，至少要比正常使用手机获取信息的资源占用要小，使用本脚本的学习成本尽可能的低，对于容易出错的部分要实现简洁但清晰的说明指导，获取的信息要准确并明了，信息的获取需要符合使用者的信息需求偏好该脚本需要能在通常网络环境下随时响应，

2.1.2多功能协调

​    微信个人号的聊天指令能够完成对各种功能的调用，相互之间的功能独立存在且相互联系，      

2.1.3数据的格式及传递

​    响应的数据简单明了。比如，课程计划，应包含学生姓名，上课时间，所属科目，学生的反馈，应包含学生姓名，课程进度，课程时间，教师评价，以及上课视频等内容。这里的大部分的内容在聊天过程中都是以文本格式传递的，学生的备课表需要以excel表格的形式返回。

2.1.4 功能

​    聊天有两种状态，基于图灵机器人的闲聊状态和集成的工作数据同步以及实时热点新闻的同步状态。

​    聊天机器人，实现微信聊天的自动回复，能够实时自动回复，可以接受并响应多种形式的微信消息，天气，火车信息等功能的调试及正常使用。

​    集成爬虫，在线教育平台的数据抓取和检索，能够根据指令完成，当前工作日待完成课程，以及当前工作日近期课程计划，已完成课程中某位学生的课程进度以及课堂表现，以及根据爬虫的数据进行excel表格统计等功能，除此之外包括但不限于每日热点新闻，舆论热点等信息的爬取和检索

​    支持多用户并发，能够微信账号对特定用户附加附加高级权限的功能，其他用户也能够通过指令对用户本人的数据进行爬取和检索。

2.2非功能需求

2.2.1安全性

​    账号安全，用户的工作账号安全和信息安全必须得到保证。该项目的代码需要进行加密，以防止攻击代码被人利用。

 

2.2.2稳定性

​    脚本需要在上线后实时响应，不能出现中途断线或者请求不响应的情况。对于各种异常可以扑捉，并做出处理。

2.2.3运行环境及设备准备

本操作脚本需要用到服务器，这里我们的实例是阿里云ecs云服务器，除此之外，我们需要一个用于信息整合和内容回复的微信个人号（下面称之为主机微信号），用户只需要是添加过主机个人号好友的微信个人号，

系统版本：Windows Server 2012 R2 数据中心版 64位

编辑器：pycharm

服务器运行：command命令行

Python环境 python 3.7.0

Lxml 4.2.5

pandas 0.23.4

Pillow 5.2.0

selenium 3.141.0

itchat 1.3.10

pip 10.0.1




3概要设计

3.1基本模块

​    本系统设计主要包含以下几个基本模块，自动获取数据，对获取到的大量数据进行数据清洗及处理，数据的传递，微信接口的架构，

3.1.1获取数据

​    获取服务器运行的微信号的好友信息，

​    获取傲梦教师端的课程数据数据，课程数据包含的内容有已完成课程，未完成课程，具体数据内容如下图所示，

​    获取IT之家的高阅读量的文章标题及链接，

​    根据接受信息获取图灵机器人的信息反馈

3.1.2数据清洗及处理

​    通过对傲梦网站数据的分析研究，对爬取到的原始数据进行结构化的处理，

​    通过对数据的筛选生成excel表格，和格式化的富文本

3.1.3微信接口的架构

​    实时接受微信消息

​    根据微信消息执行响应的模块，

​    根据各个模块的响应精准返回模块中生成的数据结果

​    根据不同的用户实现权限分级，

​    对于不同的用户权限进行功能细化

3.1.4脚本实现预期效果

​    因为本系统的用户在1000人以内且都是微信好友教师权限的用户也只有不到100人，所以对于用户身份验证的策略本系统拟采取本地初始设置，即对于普通权限的用户只需要是主机微信号的好友就可以使用，教师权限需要向管理员提交傲梦编程1对1少儿编程培训网站教师端的账号和密码经过管理员校验之后才能使用此权限的功能，普通用户只需要在和主机微信的聊天窗口下发送相应指令就可以得到响应，指令的帮助文档根据用户权限不同返回，如下图所示为普通用户的使用文档。普通用户以及教师的帮助文档如图 3.1 所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.gif)

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image004.gif)

图 3.1帮助文档

3.2流程图及说明

​    如下图所示为本操作系统的模块设计流程图

​    我们的脚本会持续监听微信消息的接收，当一条信息被接受，脚本会根据这个人的权限分流，以教师权限的用户为例，如果此时该用户直接使用了获取数据的指令，脚本会自动去该教师的傲梦编程教师端网站上获取该老师的数据，接下来该用户就可以直接通过口令检索出自己所需的数据。

脚本运行流程图3.2所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image006.gif)

图3.2 脚本运行流程示意图

3.3 关键技术介绍

3.3.1网络爬虫

​    网络爬虫，也称为"网络蜘蛛"，通过网页的链接地址搜索网页，从网站的某个页面开始，读取网页的内容，在网页中查找其他链接地址，然后通过链接地址找到下一个网页。这是一种继续循环的技术，直到根据某些策略爬网互联网上的所有网页。他可以快速捕获网站上可见的数据，是一种快速准确地获取数据的技术。目前不同的编程语言对爬虫都有相关的一些技术支持,如下表编程语言爬虫技术映射表编程语言主流爬虫框架(库)如表3.1所示

表3.1编程语言于主流爬虫库对照表

| 编程语言   | 主流爬虫框架（库）             |
| ---------- | ------------------------------ |
| C++        | open-source-search-engine      |
| Java       | Request   pyspiders Scrapy     |
| Python     | Gecco WebMagic   Spiderman     |
| JavaScript | x-ray   js-crawler scraperjs、 |
| C#         | Abot                           |
| PHP        | php-spider                     |
| Ruby       | nokogiri                       |
| Go         | Go_spider,scrape               |

 

3.3.2 python

​    Python是一种解释型面向对象的动态类型的开源的计算机程序设计语言，他因为语法简单功能强大以及且具有丰富的扩展库被人们所热爱，是轻量级的快速程序开发的不二之选

3.3.3 requests

​    Requests是一个以HTTP for Humans（给人用的http库）为宣言的网络编程库，他能够使用最为简洁明了的语法实现网络操作，提交请求获取响应，从来没有如此简单。在使用它的时候，你会惊叹，这才是python代码该有的样子。

3.3.4信息加密

信息加密技术是利用数学或物理手段，对电子信息在传输过程中和存储体内进行保护，以防止泄漏的技术。

3.3.5 pandas

​    pandas 是基于 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的[数据模型](https://baike.baidu.com/item/数据模型/1305623)，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

3.3.6 xpath

​    XPath即为[XML](https://baike.baidu.com/item/XML)路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言。

XPath基于XML的树状结构，提供在数据结构树中找寻节点的能力。起初XPath的提出的初衷是将其作为一个通用的、介于[XPointer](https://baike.baidu.com/item/XPointer)与[XSL](https://baike.baidu.com/item/XSL)间的语法模型。但是XPath很快的被开发者采用来当作小型[查询语言](https://baike.baidu.com/item/查询语言)

 

3.3.7 itchat

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。当然，该api的使用远不止一个机器人，比如[这些](http://python.jobbole.com/86532/)。该接口与公众号接口[itchatmp](https://github.com/littlecodersh/itchatmp)共享类似的操作方式，学习一次掌握两个工具。

如今微信已经成为了个人社交的很大一部分，这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。

3.3.9 webdriver

WebDriver是一种用于自动化web应用程序测试的工具，特别是用于验证它们是否按预期工作。它的目标是提供一个友好的API，易于探索和理解，比Selenium-RC (1.0) API更容易使用，这将有助于使您的测试更容易阅读和维护。它不依赖于任何特定的测试框架，因此它可以在单元测试项目中或从简单的旧的“main”方法中使用,有了他，我们可以让我们的脚本模拟大多数的浏览器操作。

3.3.10图灵机器人

图灵机器人开放平台是北京光年无限科技旗下的智能聊天机器人开放平台。通过图灵机器人开放平台，用户可快速构建自己的专属聊天机器人并为其添加丰富的机器人云端技能

3.3.11 AJAX异步加载

Ajax 不是一种新的编程语言，而是一种用于创建更好更快以及交互性更强的Web应用程序的技术。

使用 JavaScript 向服务器提出请求并处理响应而不阻塞用户核心对象[XMLHttpRequest](https://baike.baidu.com/item/XMLHttpRequest)。通过这个对象，您的 JavaScript 可在不重载页面的情况与 Web 服务器交换数据，即在不需要刷新页面的情况下，就可以产生局部刷新的效

3.3.12 pickle

​    在程序代码中中，我们常常需要把程序中的某些数据模型存储起来，这样在进行其他模块使用时直接将模型读出，而不需要去构建模型，这样就大大节约了时间。Python提供的pickle模块就很好地解决了这个问题，它可以序列化对象并保存到磁盘中，并在需要的时候读取出来，任何对象都可以执行序列化操作。

3.3.13 正则表达式

正则表达式是对[字符](https://baike.baidu.com/item/字符)串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

3.3.14 cookies

基于 Internet的各种服务系统应运而生，建立商业站点或者功能比较完善的个人站点，常常需要记录访问者的一些信息；论坛作为 Internet发展的产物之一，在 Internet 中发挥着越来越重要的作用，是用户获取、交流、传递信息的主要场所之一，论坛常常也需要记录访问者的一些基本信息（如身份识别号码、密码、用户在 Web 站点购物的方式或用户访问该站点的次数）。目前公认的是，通过 Cookie 和 Session 技术来实现记录访问者的一些基本信息

3.3.15百度AI人工智能平台

提供全球领先的语音、图像、NLP等多项人工智能技术，开放对话式人工智能系统、智能驾驶系统两大行业生态，共享AI领域最新的应用场景和解决方案，提供了很多可供开发者免费使用的人工智能接口。

3.3.16 批处理文件

批处理文件（batch file）包含一系列 DOS命令，通常用于自动执行重复性任务。用户只需双击批处理文件便可执行任务，而无需重复输入相同指令。编写批处理文件非常简单，但难点在于确保一切按顺序执行。编写严谨的批处理文件可以极大程度地节省时间，在应对重复性工作时尤其有效。




4详细设计

4.1功能需求和程序的关系

再本操作系统中，微信聊天窗口作为我们的运行页面，所以微信消息数据的实时同步是保证代码正常运行的关键因素，获取到微信聊天信息的时候，这个数据包含了，信息的发送者，信息的内容（文本），以及该聊天信息的特定id。这个数据需要和我们程序本身的初始化数据进行判断，得出发送信息的身份对应用户权限，以及当前聊天模式，有了这个权限和模式，系统便可以根据用户的权限和信息内容明确用户的意向，聊天机器人模式下，系统根据用户的发送的内容去图灵机器人接口中获取响应，然后把这个响应返回给我们的用户，从而实现聊天机器人的功能，通常模式下，用户保持微信聊天正常状态，但是当用户身份为已经赋予权限的傲梦教师身份的时候，用户只需通过特定指令控制程序的走向，例如，当用户通过特定指令表示要获取当前时间的热点新闻，系统便会同过调用获取实时热点新闻的接口，获取到当前网站中的热点内容，本系统的设计模式采用，分布式扁平化设计理念，每一个新的指令进入，就对应新的脚本需要被执行，低内聚高耦合，模块之间只存在较少的联系，且模块之间互不干扰。 

4.2接口设计

4.2.1微信信息的获取

在本脚本中，微信的聊天框可以说扮演了一个用户界面的角色，用户和服务器的一切交互都是通过微信信息的发送来完成的，所以脚本如何去获取微信好友的信息就成了本脚本第一个要解决的实际问题，itchat作为一个开源的微信个人号接口，让数据的传递变得空前的简洁，他可以完美模拟用户登录网页端的微信，实现代码如图4.1 所示

 

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg)

图4.1 微信消息实时获取示意图

运行结果如下图4.2所示：

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg)

图4.2 微信登录成功终端显示效果图

通过运行代码首先会出现微信登录所需的扫码，程序模拟登录了网页版的主机微信号。出现login successfully as 微信名字样表示登陆成功，msg_register函数实现了各种微信信息的实时获取，此处在text函数中可以把文本格式的信息内容获取到，经过对msg微信聊天信息研究发现，脚本所需的信息来源用户，信息内容，都可以直接在msg中获得。如下图代码和运行结果如图4.3所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image012.jpg)

图4.3微信消息数据解析代码示意图

 

 

运行结果如图4.4所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg)

图4.4 微信聊天数据解析运行效果图

 

4.2.2新闻热点的爬取

对于舆论热点，本脚本拟获取IT之家版面中的如下图框选内容所示中的最热排行和周榜内容的网站示意图，如图4,5所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg)

图4.5 IT之家网站主页

​    通过对数据的研究，发现本数据可以直接在网站的html代码中找到，如图4.6所示

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image018.jpg)

图4.6 IT之家网站热点新闻网页代码示意图

 

通过数据比对，发现a标签中的文本就是文章的标题，而a标签的属性herf中保存着该热点新闻的url地址，要想抓取这个网页版的IT之家版面，需要模拟通过request模块向IT之家网站服务器发送请求，获取到该页面的内容并通过xpath把所属标签中的内容精确检索。且为防止被网站的反爬虫机制限制甚至拒绝响应，我们需要把爬虫程序伪装成浏览器，即提交请求的时候附加上请求头里面的关键内容，浏览器请求头内容如图4.8所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg)

图4.8 浏览器请求网页的请求头内容

在红框中的user-agent中，包含了浏览器兼容的内核版本，请求电脑的操作系统和位数。有了这些数据，我们的爬虫脚本就可以伪装成一个浏览器请求，从而避免了网站的反爬机制可能带来的问题，整体的实现思路如下，首先，用requests库的get方法发送请求，对于接受的的响应一个html网页代码进行树形结构的解析，然后通过xpath标签路径获取到指定内容的数据，这里需要通过网页代码结构的熟悉和研究找出多个标签之间的内在联系，使用xpath表达式快速检索到所需的数据，

请求代码如图4.9所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image022.jpg)

图4.9 模拟请求IT之家官网获取响应的代码示意图

Xpath获取特定标签的代码如图4.10所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image024.jpg)

图4.10 xpath获取特定标签内容的代码示意图

运行结果如图4.11所示：

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image026.jpg)

图4.11 IT之家数据获取运行结果终端效果图

4.2.3图灵机器人接口设计

图灵机器人的接口创建只需要登录网站,

创建一个机器人对象，这里的我们需要进行机器人的一个初始化设置，聊天机器人的初始化界面如图4.12所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image028.jpg)

图4.12 图灵机器人的应用创建网站示意图

机器人创建完毕之后，设置他的终端接入方式，图灵机器人的接口，需要根据不同的发送内容，得到相应的信息反馈，图灵机器人的接口是一个成熟并且完善的接口，这里的接口在本脚本中 拟选择使用api接入，因为在聊天机器人的基础上还有集成教师应用等有针对性的功能，如果选择直接个人号接入势必会造成接口的调用冲突，影响用户的使用体验。并且使用api接入，这里会让我们的脚本更加灵活，可以对图灵机器人做出更多针对性的调整。选择api接入如图4.13所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image030.jpg)

图4.13 图灵机器人接口选择示意图

接下来是代码实现，依旧使用requests模块对网页版的图灵机器人数据进行抓取，不同的是，这里我们需要通过提交聊天信息才能获取到图灵机器人的响应，所以此处的请求方式变成了post，代码实现如图4.14所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image032.jpg)

图4.14 图灵机器人数据获取代码示意图

4.2.4 百度人工智能平台图片文字识别

百度人工智能平台的应用创建细节如图4.15所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image034.jpg)

图 4.15 百度人工智能平台图片文字识别接口设置截图

百度人工智能平台的图片识别相应代码如图4.16所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image036.jpg)

图4.16百度人工智能如图片文字识别接口实现代码

4.2.5傲梦官方网站教师端数据的获取

​     网站数据的抓取是本脚本的难点，因为数据的复杂度远远要超过以上的两种数据，高复杂性带来了更多的处理数据的障碍，首先，我们获取到的数据是需要在登陆状态下的，所以在发送请求的时候除了反爬虫必须的useragent还需要验证身份信息的cookies，这里所以脚本必须要在登陆状态下获取到cookies才能成功请求到网页上的数据，这里就需要用到selenium库，他能够使用脚本对网页进行完全模拟人的操作，经过对傲梦编程网页的登录页面分析如下图所示，傲梦网页主页示意图如图4.17所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image038.jpg)

图4.17 傲梦编程网站登录页面

网址https://all-dream.com/front_login.jsp?param=tacher之后。本需要完成的工作分别是，输入账号和密码，输入验证码，点击登录，如果信息无误，登录成功后，就可以用selenium中的内置方法获取到登陆状态下的网页cookies，账号和密码基本不会改变，主要的问题此时出在了验证码的识别上，首先需要从页面拿到验证码的图片信息，因为验证码是每次请求都不同的，所以要保证webdriver操作页面的时刻的验证码图片信息获取到，此处可以采用webdriver的内建方法save_screenshot对验证码页面进行截图，并且还需要配合PIL的图片操作库，对截取的图片进行剪裁处理。实现代码如下所示：

def getimg(img_time):
     '''得到网页登陆时候所需的验证码图片
        driver是全局变量  后面需要通过driver会的cookies
        成功过得到会返回True
     '''
     global driver
     driver = webdriver.Chrome()
     \#driver.set_window_size() # 设置浏览器尺寸
     driver.maximize_window()
     driver.get('https://all-dream.com/front_login.jsp?param=teacher')
     time.sleep(5) # 要加载一段时间，留出时间
     if driver.title == '傲梦直播':
         driver.save_screenshot('.\image\{}.png'.format(img_time))
         yzm_elmt = driver.find_element_by_xpath(pic_xpth)
         L = yzm_elmt.location['x']
         T = yzm_elmt.location['y']
         R = L+yzm_elmt.size['width']
         B = T+yzm_elmt.size['height']
         im = Image.open('.\image\{}.png'.format(img_time))
         print(L,T,R,B)
         im = im.crop((L,T,R,B))
         im.save('.\image\{}1.png'.format(img_time))
         time.sleep(1)
         print(L,T,R,B)
         return True
     else:
         return False

此时图片获取到之后识别成了又一个需要解决的问题，本系统采取两种识别方案交替进行，首先会使用百度的人工智能平台提供的图片文字识别策略，但是不可避免的问题是自动识别具有一定的误差，所以不能保证识别的百分之百成功率，所以这里拟采取图片通过主机微信发送给用户让用户来人工识别，这样图片的识别就能够迎刃而解。以下是两种解决方案状态下的代码线上运行效果。

使用百度ai人工智能开放平台的解决方案，通过调用接口实现验证码的基本识别，实现代码如下所示：

def aiYzm(filename):
     ''':param filename: 表示图片的文件路径return: 返回图片经过百度开发识别的结果，如识别失败的话直接返回false '''
     from aip import AipOcr
     """ 你的 APPID AK SK """
     APP_ID = '16190824'
     API_KEY = 'sW2uzXjyWqiyC5Lq2lNsdnig'
     SECRET_KEY = 'GVF2YX5cS7RZqfXMGgIpnuPDPQyfEyWq'
     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
     """ 读取图片 """
     def get_file_content(filePath):
         with open(filePath, 'rb') as fp:
             return fp.read()
     image = get_file_content(filename)
     """ 调用数字识别 """
     client.numbers(image);
     """ 如果有可选参数 """
     options = {}
     options["recognize_granularity"] = "big"
     options["detect_direction"] = "true"
     """ 带参数调用数字识别 """
     a = client.numbers(image, options)
     try:
         a = a['words_result'][0]['words']
         print(a)
     except:
         return False
     else:
         if len(a) == 4:
             return a
         else:
             return False

另外一种解决方案是直接把图片经过主机微信号发送给客户端微信，通过用户人工识别图片的结果，进行消息回复之后，实现验证码的人工识别。这里的实现代码如下

imgnum = aiYzm('.\image\{}1.png'.format(shot_tm))
 if imgnum:
     user.yzm = imgnum
     suss, user.cookies = log_web(user.admin, user.yzm)
     if suss:
         itchat.send_msg('网站登录成功，请稍等片刻数据马上抓取成功', user.username)
         timec = logdata(user)
     else:
         itchat.send_msg('so sad~ 验证码自动识别失败，请重新获取数据', user.username)
         driver.close()

成功识别图片的运行示意图如图4.18示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image040.jpg)

图4.18 验证码图像识别成功运行示意图

失败识别验证码需要人工输入的运行示意图如图4.19所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image042.jpg)

图4.19 人工识别验证码运行效果

接下来依旧使用requests方案对傲梦编程官网的数据进行爬取，通过网站页面的结构分析，发现主要数据分成两部分，已完成课程数据和未完成课程的数据。对应页面的内容如下图所示，

已完成课程的内容网页效果图如图4.20

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image044.jpg)

图4.20 傲梦编程网站教师端已完成课程效果图

未完成课程的内容网页效果图如图4.21

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image046.jpg)

图4.21 傲梦编程教师端未完成课程效果图

通过对页面的html代码分析发现，本分关键代码人如图4.21所示：

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image048.jpg)

图4.22 傲梦编程网站关键代码截图

 

通过对网站后台代码的研究和探索性检查，网站的数据是异步加载的数据，通过谷歌浏览器的检查工具对网页中的异步加载数据排查（数据存在于检查接口下的NETWORK对应XHR里面）

网页异步加载数据总页面如图4.23

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image050.jpg)

图4.23 检查接口下异步加载数据列表示意图

该网页存在所需的加载数据，数据的格式是json格式，以已完成数据中的一页的一条记录为例，数据如下

{"lessonId":"eec9348ceba84ef99e1d6d40edef2943","studentId":"4697f12fdf224456a4a26c417eadcea8","teacherId":"e4ccd1f328d84a76ab46e382d79af6a8","lessonName":"64510班级课程","studentName":"章圣歆","teacherName":"陈奇","lessonStartTime":1557055803000,"lessonEndTime":1557058654000,"teacherComment":"知识点内容：\n\t课程进度  pye21-1\n\t内容总结  贪吃蛇游戏的函数化\n孩子掌握情况：\n\t孩子具体完成情况  能在老师的引导下理解课堂代码的实现逻辑\n\t优点 学习兴趣高  理解能力强\n\t欠缺点  暂无\n需要家长配合：暂无\n上次课作业完成情况：完成  存在问题  已在课堂上解决","teacherCommentLevel":4,"studentComment":null,"lessonStatus":"2","studentCommentLevel":null,"studentCommentOne":null,"studentCommentTwo":null,"studentCommentThree":null,"studentCommentFour":null,"studentCommentFive":null,"teacherCommentOne":4,"teacherCommentTwo":4,"teacherCommentThree":4,"teacherCommentFour":4,"teacherCommentFive":4,"teacherLessonUrl":null,"lessonUrl":"http://timer.91veo.com/v1/meeting/join?id=1402562&value=fafc2c1c46bc952e524ca3c7bb42a1f9","recordUrl":"https://cdn.all-dream.com/user/e4ccd1f328d84a76ab46e382d79af6a8/20190505_202919_zoom_0.mp4","note":"","noteTeacher":"NOIP测试分数：","courseTypeName":"python程序设计","courseTypeId":"702dd6f4b95f418ebf5f54bd652e859f","studentSignNote":"","studentSignState":"1","online":"1","free":"0","homework":"https://cdn.all-dream.com/exercise/307f56ba15f84ce9b94e05ac0345ba4c/425.py"},

文件中的json格式的数据可以继续用requests方式进行数据的爬取，这里因为数据是一部加载的数据，需要用到json模块对数据进行格式化处理，换而言之，只有json才能把网页中的结构体数据转换成python的字典格式，但是字典的数据课时处理起来不是非常的方便，在本系统中我们采用pandas的库对数据进行更加精细化的的直观处理。且网页中表示的实现是用unix时间戳来表示，这里本系统采用python的datatime的模块对时间进行格式化的处理。具体的实现代码如下所示：

def getData(cookies):
     '''获取傲梦网站的学生信息以及课程信息
        返回获取数据的文件所在目录
        参数是网站所需的cookies
        数据的精细化处理  是数据的检索更加简单
     '''
     timec = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
     os.mkdir('./data/'+timec)
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
     url = 'https://all-dream.com/rest/hour/queryMyCoursePlan4TeacherNew?free=0&limit=10&random=0.5043750329478451&page=1'
     today_class = requests.get(url,headers=headers,cookies=cookies)
     today_class = json.loads(today_class.text)
     print(today_class)
     with open('./data/'+timec+'/今日课程计划','wb') as file:
         pickle.dump(today_class,file)
     url_list = ['https://all-dream.com/rest/courseManage/queryMyOverCourse4Teacher?limit=10&page={}'.format(i+1)  for i in range(10)]
     over_all_class = []
     for url in url_list:
         over_class = requests.get(url,headers=headers,cookies=cookies)
         data_1 = json.loads(over_class.text)['list']
         over_all_class.append(data_1)
     key = 1
     stOverClass = {}
     for ondPage in over_all_class:
         for oneClass in ondPage:
             stOverClass[key]=oneClass
             key+=1
     df = pd.DataFrame(stOverClass).T

     with open('./data/'+timec+'/已完成课程','wb',) as file2:
         pickle.dump(df,file2)
     return timec

 


这里为直观展示如图已完成课程数据中的一个数据结构图如图4.24

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image052.jpg)

图4.24 已完成课程数据结构图

其中满足我们需求的数据只需要学生姓名（studentName）上课时间（lessonStartTime）课程类别（courseTypeName）以及教师评价（teacherComment）其中课堂的上课时间是unix时间戳需要转换成正常显示的时间格式，评价中包含上课进度，学生课堂表现，知识点等内容。在这里我们首先要做的事情是吧数据西安进行存储，这里用到pickle模块，并且为了后期的容易清洗，数据格式用pandas模块中的dataframe数据表的格式保存，待完成课程的数据用以上相同的策略也可以抓取。功能中的今日课程计划和近日课程计划都是对待完成课程数据的检索，某某学生的课堂反馈则是对已完成课程 的数据检索。以及完成课程的excel表格也是对已完成课程的检索,实现代码如下所示：

def getToday(path,flag):
     '''参数是当前目录（今日学生信息的名称）下的文件名称
        返回值是一个字符串  包含今日未完成课程信息
        功能：获取当前日期内的上课内容
     '''
     if flag:
         tm = '近日'
     else:
         tm = '今日'
     str1 = ''
     with open('./data/'+path+'/今日课程计划','rb') as file:
         data = pickle.load(file)
     stlist = data['list']
     nowday = time.strftime("%Y-%m-%d",time.localtime(time.time()))
     times=0
     if not flag:
         for st in stlist:
             sttime = uTime(st['startTime'])
             if sttime[:10]!=nowday:
                 continue
             times+=1
             edtime = uTime(st['endTime'])
             stname = st['studentName']
             kemu = st['courseTypeName']
             banji = st['courseHourName']
             str1 += '\t学生：{}   \n\t时间：\n\t{}\n\t{}   \n\t科目：\t{}   \n\t班级：{}\n'.format(stname,sttime,edtime,kemu,banji)
     else:
         for st in stlist:
             sttime = uTime(st['startTime'])
             times+=1
             edtime = uTime(st['endTime'])
             stname = st['studentName']
             kemu = st['courseTypeName']
             banji = st['courseHourName']
             str1 += '学生：{}   \n时间：\n{}\n{}   \n科目：{}   \n班级：{}\n'.format(stname,sttime,edtime,kemu,banji)

     if times >=1:
         return '老师您好，\n{}你总共有{}节课\n内容如下\n'.format(tm,times)+str1
     else:
         return'老师~今天真幸福呀,\n{}你已经完成了所有工作\n当然今天也可能是非常愉快的休息日，\n试试召唤智能机器人,\n  \"小小奇\" '.format(tm) 

对于特定学生的课堂表现内容获取函数如下所示      
 def getfk(name,timec):
     '''
     参数：查看反馈的学生姓名  以及保存本次数据的文件最内层路径
     返回值：包含匹配到该学生的三条数据  如果先搞改变匹配数据的数量只需要改掉times里的值
     功能实现原始数据的检索  可通过学生姓名直接检索    
     '''
     with open('./data/'+timec+'/已完成课程','rb') as file:
         df = pickle.load(file)
     student = df[df['studentName']==name]
     msg_list = []
     for i in range(len(student)):
         st = student.iloc[i]
         remark = st['teacherComment']
         videourl = st['recordUrl']
         star = st['teacherCommentOne']
         stTime = st['lessonStartTime']
         msg = '这节课的开始时间是:\n{}\n这节课里你对孩子评价是：\n{}\n您为孩子打出惊人的{}颗星\n视频链接:\n{}\n--------------------------------------------'
         msg_one = msg.format(uTime(stTime),remark,star,videourl) 
         msg_list.append(msg_one)
     return msg_list

对于备课表单自动生成，需要把网站爬取的相应数据转换成固定格式的excel格式，pandas的内置方法to_csv可以直接把格式为DataFrame的数据表直接转换成excel表格，实现代码如下所示：

def savetoexcel(a):

​    for i in a:

​        with open('傲梦备课表.csv','a+',encoding = 'gbk',newline='')as csvfile:

​            writer = csv.writer(csvfile)

​            writer.writerow(list(i.values()))      

​    with open("{}.csv".format('傲梦1')) as aaa:

​        lalal = pd.read_csv(aaa,header=None,skiprows=6)

​        lalal.columns = ['姓名', '课程类别', '课堂开始时间', '课堂结束时间', '课程进度', '内容总结']

lalal.to_excel("{}.xlsx".format('傲梦备课表')

4.2.5 程序脚本集成

​    本系统的代码结构如图所示4.25所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image054.jpg)

图4.25 代码文件示意图

其中start.bat是本系统的快速运行脚本，双击它会自动使用python3版本环境运行代码start.py，而start.py会使用itchat自动登录微信，这里主机微信号需要使用扫描自动生成的微信二维码进行账号授权。经过这一步之后，微信的实时消息就可以被获取到，此时就可以在run.py根据帮助文档中的聊天信息做出相应的响应。其中响应分为傲梦官网学生信息的响应和图灵机器人的信息响应，以及附加功能中的接口调用，比如IT之家热点新闻。其中聊天的对象分为两个权限，对应程序代码中的两个类，代码如下所示

class Friends():
     def __init__(self):
         with open('./data/好友信息','rb',) as file2:
             self.df =pickle.load(file2)
     def isvip(self,fromusername):
         username = self.df[self.df['Remark'].isin(list(message.keys()))]['UserName'].values
         if fromusername in username:
             return True
         else:
             return False

     def readvip():
         pass
 class Teacher():
     def __init__(self,username):
         self.username = username
         with open('./data/好友信息','rb',) as file2:
             self.df =pickle.load(file2)
         self.name = self.df[self.df['UserName']==self.username].iloc[0].Remark
         self.admin = message[self.name]
         print(self.name)
     def getmessage(self,flag):
         if self.msg_1['Text'] =='小小奇':
             flag = True
         return flag
     def getcookies(self):
         '''
            验证码图片的微信发送
            验证码保存在本地   文件名由当前时间命名
            时间作为发送信息的图片名
         '''
         self.img_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
         if getimg(self.img_time):
             return self.img_time
     def svtime(self,timec):
         self.timec = timec
 class Nomal():
     def __init__(self,username):
         self.flag = False
         self.username = username

通过聊天信息Friends类中isvip方法对信息发送者的权限进行分类，确定是Teacher类还是Nomal类，对于不同权限的用户采取不同的信息响应策略，但是机器人的功能基本一致，机器人权限的开关和信息交互代码如下所示：

nomal = Nomal(msg['FromUserName'])
 print('创建聊天')
 nomal.msg = msg
 if nomal.msg['Text'] in ['start','小小奇','开始']:
     itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',nomal.username)
     nomalflag[nomal.username] = True
 elif nomal.msg['Text'] in ['help','帮助']:
     itchat.send_image('./image/nomal.png',nomal.username)
 elif nomal.msg['Text'] in ['end','exit','退出']:
     nomalflag[nomal.username] = False
 try:
     if nomalflag[nomal.username]:
         itchat.send_msg(jqr(nomal.msg['Text'])+".",nomal.username)
 except:
     pass

对于教师权限的用户的功能调用流程控制的代码实现策略如下所示：

user = Teacher(fromusername)
 user.msg_1 = msg
 if user.msg_1['Text'] in ['start','小小奇','开始']:
     itchat.send_msg('以下内容是自动回复,发送“exit”或者“退出”退出退出自动回复',user.username)
     userflag[user.username] = True
 elif user.msg_1['Text'] in ['end','exit','退出']:
     userflag[user.username] = False
 if len(userflag):
     if userflag[user.username]:
         itchat.send_msg(jqr(user.msg_1['Text'])+".",user.username)

 if len(userflag)==0 or userflag[user.username]==False:
     if user.msg_1['Text'] == '获取数据':
         itchat.send_msg('请耐心等候，小爬虫正在快吗加鞭获取数据', user.username)
         shot_tm = user.getcookies()
         itchat.send_msg(msg_to_u[1],user.username)
         imgnum = aiYzm('.\image\{}1.png'.format(shot_tm))
         if imgnum:
             user.yzm = imgnum
             suss, user.cookies = log_web(user.admin, user.yzm)
             if suss:
                 itchat.send_msg('网站登录成功，请稍等片刻数据马上抓取成功', user.username)
                 timec = logdata(user)
             else:
                 itchat.send_msg('so sad~ 验证码自动识别失败，请重新获取数据', user.username)
                 driver.close()

         else:
             itchat.send_image('.\image\{}1.png'.format(shot_tm),user.username)
     elif user.msg_1['Text'] in ['help', '帮助']:
         itchat.send_image('./image/teacher.png',user.username)
     elif re.findall('\d+',user.msg_1['Text']):
         if len(re.findall('\d+',user.msg_1['Text'])[0])==4:
             user.yzm = re.findall('\d+',user.msg_1['Text'])[0]
             suss,user.cookies = log_web(user.admin,user.yzm)
             if suss:
                 timec = logdata(user)
             else:
                 itchat.send_msg('so sad~ 验证码输入错误，请重新获取数据', user.username)
                 driver.close()

 

     elif user.msg_1['Text'] in '近日课程计划':
         print(timec)
         user.closetoday = getToday(timec,True)
         itchat.send_msg(user.name[:-4]+user.closetoday,user.username)
     
     elif user.msg_1['Text'] in '今日课程计划':
         print(timec)
         user.today = getToday(timec,False)
         itchat.send_msg(user.name[:-4]+user.today,user.username)
     elif user.msg_1['Text'][-4:]=='课堂反馈':
         ms = getfk(user.msg_1['Text'][:-4],timec)
         print(user.msg_1['Text'][:-4])
         if len(ms)>=1:
             itchat.send_msg('已为您匹配到{}个结果'.format(len(ms)),user.username)
             for ms_1 in ms:
                 itchat.send_msg(ms_1,user.username)
         else:
             itchat.send_msg(msg_to_u[-1],user.username)
         for msg in ms:
             itchat.send_msg(ms,user.username)
     elif user.msg_1['Text'] == '热点':
         day,week = getnews()
         print(day,'\n',week)
         itchat.send_msg(day, user.username)
         itchat.send_msg(week, user.username)

4.3功能函数

​    获取微信好友信息的函数如图4.26所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image056.jpg)

图4.26微信登录后好友信息身份信息的汇总获取代码实现

​    获取网站cookies的函数如图4.27所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image058.jpg)

图4.27 模拟浏览器登录傲梦网站获取cookies代码截图

处理数据如图4.28所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image060.jpg)

图4.28 对爬取到的异步加载数据进行第一次数据筛选代码截图






4.4运行设计

批处理(Batch)，也称为批处理脚本。顾名思义，批处理就是对某对象进行批量的处理。批处理文件的扩展名为bat。在本系统中，脚本的运行采用dos批处理运行python代码，严格遵守pep20的程序设计理念，以简约轻便为主旨，程序的运行指令为dos批处理文件，以下是文件的编码示意图如图4.19

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image062.jpg)

图4.19 脚本启动dos文件代码截图

 

4.5系统数据结构设计

4.5.1 用户傲梦网站的身份信息

教师的个人信息表设计如表4.1所示，

 

表4.1 教师个人信息表













| 姓名 | 账号        | 密码   |
| ---- | ----------- | ------ |
| 陈奇 | 18000000000 | 123456 |

教师的身份信息以上表中的格式存储，内容经过base64加密，

4.5.2 学生已完成课程数据

​    学生的已完成课程数据格式如表4.2所示

表4.2 学生已完成课程数据表





















| 学生姓名 | 上课时间                               | 科目             | 教师评价                             | 上课进度           |
| -------- | -------------------------------------- | ---------------- | ------------------------------------ | ------------------ |
| 李一一   | 2019-01-01   10:30 2019-01-01    11:20 | Python程序与设计 | 包含学生课堂表现，课堂知识点，等内容 | Python初级课第一课 |

 

4.5.3学生待完成课程数据

​    学生的待完成课程数据表如表4.3所示

表4.3 学生未完成课程数据表













| 学生姓名 | 上课时间                           | 科目             |
| -------- | ---------------------------------- | ---------------- |
| 李一一   | 2019-01-01-10:30至2019-01-01-11:20 | Python程序与设计 |

 




5 测试与结果分析

5.1 运行环境

​       硬件：因为需要实时获取，所以需要运行在服务器环境中，本系统运行环境在阿里云的云服务器。

​       软件：本脚本需要再python3.的环境下运行，webdriver需要在谷歌浏览器的安装目录下保存谷歌浏览器的webdriver驱动。

5.2运行界面及结果测试

5.2.1代码的运行

​    测试环境：

​       操作系统：Wingdows10企业版 64位

​       运行方式：Dos批处理文件

​       Python版本：Python3.7.0

​       浏览器版本：Goole Chrome版本 74.0.3729.131（正式版本） （64 位）

运行界面截图如下图5.1所示

​              ![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image064.jpg)

​      图5.1 程序运行启动成功终端效果图

5.2.2 爬取数据的展示

新闻热点的终端输出展示截图如图5.2所示

 

 

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image066.jpg)

图5.2 热点数据的终端输出效果图

微信端新闻热点新闻的截图如图5.3所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image068.jpg)

图5.3 热点数据的微信端输出效果图

鉴于篇幅限制，以下为代码运行结果只展示微信端截图，

聊天机器人功能检测如图5.4所示

 

 

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image070.jpg)

图5.4聊天机器人微信端输出效果图

傲梦编程网站数据的检索测试示意图运行截图如图5.5所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image072.jpg)

图5.5获取傲梦数据微信端输出效果图

 

傲梦网站自动生成的备课表如图5.6所示

![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image074.jpg)

​    图5.6 脚本自动生成备课表的文件预览图

 

 

 

 

 

 

 

 

 

 

 

 

 

 

参考文献

[1]  Allen B. Downey.《Think Python: How to Think Like a Computer Scientist》Green Tea Press

[2]  Python程序设计 [An Introduction to Programming Using Python]．[美] 戴维 I.施奈德（David I. Schneider）著；车万翔 译

| [3]檀冬宇.基于Python的大众点评网数据抓取技术研究[J].计算机产品与流通,2019(05):116. |
| ------------------------------------------------------------ |
| [4]. Biophysical Society; Python hearts reveal   mechanisms relevant to human heart health and disease[J]. NewsRx Health &   Science,2019. |
| [5]Tomas Beuzen,Joshua Simmons. A variable   selection package driving Netica with Python[J]. Environmental Modelling and   Software,2019,115. |
| [6]Simon Olofsson,Lukas Hebing,Sebastian Niedenführ,Marc   Peter Deisenroth,Ruth Misener. GPdoemd: A Python package for design of   experiments for model discrimination[J]. Computers and Chemical   Engineering,2019,125. |
| [7]Omid Haji Maghsoudi,Annie Vahedipour,Thomas   Hallowell,Andrew Spence. Open-source Python software for analysis of 3D   kinematics from quadrupedal animals[J]. Biomedical Signal Processing and   Control,2019,51. |
| [8]Theo Steininger,Jait Dixit,Philipp   Frank,Maksim Greiner,Sebastian Hutschenreuter,Jakob Knollmüller,Reimar   Leike,Natalia Porqueres,Daniel Pumpe,Martin Reinecke,Matevž Šraml,Csongor Varady,Torsten Enßlin. NIFT y 3 – Numerical   Information Field Theory: A Python Framework for Multicomponent Signal   Inference on HPC Clusters[J]. Annalen der Physik,2019,531(3). |




致  谢

​       经过两个多月的努力，本脚本完美上线，在这里致谢同事罗煜，鲍得江等人的帮忙测试功能，提出了很多好的意见，感谢百度人工智能开放平台，解决了一部分验证码识别的问题，感谢图灵机器人的开发公司北京光年无限科技及开发人员。感谢我的毕业设计指导老师任强老师，为我的脚本完善提供了很好的建议和指导。

​    除此之外，感激大学期间所有的老师们，他们带我走进了计算机这个神奇并且美丽的世界，感激车鹏飞老师，他用浅显易懂的方式让我理解了编程语言的内部机制，感激孙少波老师，他带我走进python的世界，并给我了很多学习和项目的经验，记得大一的时候，在张岗亭老师的引导下，当我用c语言完成99乘法表的时候，满心的激动，后来通过任强老师的网页设计，我搭建出了自己的第一个个人网页，所有的老师们带给我的知识，都让我在后来的学习中获益匪浅。

​    最后，感谢我的舍友李尧，作为一个刚上大学时候连搜索引擎都不能熟练应用的电脑小白 ，在他的指导下，学会了科学的使用电脑，这让我的学习效率，事半功倍。
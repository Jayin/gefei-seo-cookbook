# 出海第一周 我的 GPTs 导航站火了

出海第一周，我的 GPTs 导航站火了 哥飞 在小说阅读器中沉浸阅读 文中详细记录了@艾逗笔 的网站从无到有，然后不断进化的过程，很值得大家学习。

在GPTs这种大热点中，你需要快，先快速上线一个静态页面作为第一版，然后不断进化，增加新功能。

如果等一周后你的所有功能都完善之后再发布，黄花菜都凉了。

艾逗笔 . 有逻辑的脑子万里挑一。

一周出海记录上周五晚上，在 @哥飞 的付费社群，我看到了 GPTs Hunter 作者 @Airyland 共享 GPTs 应用数据的消息。

我发了个邮件，申请到了 GPTs Hunter 的数据访问权限，拿到了一个包含 5000+ 条 GPTs 数据的 data.json 文件上周六，我花了一天时间，使用 nextjs 搭建了一个 web 项目，在 tailspark.co 上找了个模板写了一个页面，解析 data.json 数据写了个接口，上线了 gpts.works 第一个版本。

鉴于做 GPTs 导航站的人太多，为了做出差异化，我用 plasmo 框架写了一个浏览器插件，在浏览器侧边栏显示第三方 GPTs 应用，跟 GPTs 官方商店保持一致的风格，也能让用户用起来更方便。

上周六晚上，我在微信朋友圈 / 微信群 / 即刻社区几个地方发了一条动态，首次曝光了 GPTs Works 这个项目。

上周日，我花了一天时间，使用 fastapi 搭建了一个 python 项目，使用 ponyorm 读取 DB 里的 GPTs 数据，调用 Azure OpenAI 的接口做 embbediing，把向量数据存储在 zilliz cloud，再通过 Chat 的方式做向量匹配检索。

周一，我在社交平台发布了 GPTs Works 支持向量检索的动态，同时上线了一个 GPTs 应用，通过对话的方式检索第三方 GPTs 应用。

image周二，我整理了一下代码，推送到 github 公有仓库，正式开源 GPTs Works 项目，包括 web 网站 / 向量检索系统 / 浏览器插件 三个子项目。

当天涨了不少 star，得到了很多大 v 转发。

image网站访问量也涨了不少，第一次破 3k UV。

image周二晚上，跟 monica.im 的创始人红哥聊天，跟他分享了 GPTs Works 项目的一些情况，红哥决定在我的网站上投广告，于是我拿到了第一笔商业赞助。

image第一次出海，从零开始到有收入，我花了 3 天时间。

持续优化周三，我去上海参加百度举办的大模型比赛，之后去苏州玩了一趟，期间抽时间做了 GPTs Works 数据同步 / 图片下载 / 页面优化之类的工作，社交平台持续有人点赞 / 转发 / 评论，github star 数一直在涨。

周四，GPTs Works 开源的动态得到了微博大 v @宝玉xp 的转发，给 GPTs Works 项目涨了不少 star。

周五，GPTs Works 在 @阮一峰的网络日志 周刊推送，给 gpts.works 网站带来了一波新的流量。

周六，我给 GPTs Works 加上了详情页。

image浏览器插件改版，也加上了向量搜索。

image周日，我给 GPTs Works 加上了分类和推荐。

image一些数据这一周是很神奇的一周，收获了很多意外的惊喜，简单做了一个数据统计。

gpts.works 网站，周 UV 11.8k，单日最高 UV 3.7kimage主要访问来源于 twitter / weibo / weixin / github / v2ex 等平台，toolify.ai 和其他一些导航站，也有不错的流量来源。

imageProductHunt 发布的 “GPTs Works” 作品，点赞 35，有 37 个关注。

GPTs Works 开源仓库 "github.com/all-in-aigc/gpts-works"，收获了 658 个 star，80 个 fork，也是我目前 star 数最多的一个开源项目。

Twitter 账号 @idoubicc，涨粉 45，之前一直没怎么用 Twitter，以后要经常用起来了。

即刻账号 @艾逗笔，涨粉 523，目前粉丝 1534，即刻一直是我做产品的主要宣发平台，社区氛围很好。

公众号 @艾逗笔，涨粉 95，目前粉丝 4838，后续也要持续更新。

微博 @艾逗笔，涨粉 137。

小红书 @艾逗笔，涨粉 14。

几个第一谦虚一点，只说“第一批”，不说“第一个”。

GPTs Works 是全网第一批支持向量检索的第三方 GPTs 应用商店。

GPTs Works 是全网第一批支持浏览器插件使用的第三方 GPTs 应用商店。

GPTs Works 是全网第一批开源的第三方 GPTs 应用商店。

在 Google 搜索“chatgpt gpts”，GPTs Works 这个 GPTs 应用排在第一位image搜索“gpts”，排在第二位image感悟与致谢出海第一周，GPTs Works 项目小 🔥 了一把，让我对出海这件事有了更大的信心，后续希望能探索更多的方向，发布更多的作品。

感谢我的朋友 @Banbri 一直以来的帮助与鼓励，极力推荐并邀请我加入了 @哥飞 的社群，让我进入到了出海的这个圈子。

感谢热衷分享的大佬 @哥飞 创建了一个非常好的交流平台，分享了很多有价值的信息，让我打开了思路，启动了第一个出海项目。

感谢技术大佬 @Airyland 共享了 GPTs 的数据，让我更快的上线了第一个出海项目。

感谢金主爸爸 @Red 给的第一笔商业赞助，给了我很大的鼓励，也让我第一次出海就实现了变现闭环。

还有其他给 “GPTs Works” 宣传 / 转发 / 点赞的朋友们，一并致谢。

一些资源GPTs Works 网页主站https://gpts.worksGPTs Works 官方 GPTs 应用https://chat.openai.com/g/g-EBKM6RsBl-gpts-worksGPTs Works 开源仓库https://github.com/all-in-aigc/gpts-worksAll-in-AI，未来可期。

---

> 来源：哥飞公众号
> 原始文件：出海第一周_我的_GPTs_导航站火了.txt
# DALL E 3 将于10月份发布 到时可在 ChatGPT Plus 和 API 上体验

DALL·E 3 将于10月份发布，到时可在 ChatGPT Plus 和 API 上体验 大家好，我是哥飞。

今天哥飞给大家介绍 OpenAI 的文生图服务 DALL·E 的最新版本 DALL·E 3 。

DALL·E 2是在 2022 年的 11 月 3 日对外发布API的，而 ChatGPT 是在 2022 年 11 月 30 日上线网页版的。

我们大多数人了解 OpenAI 都是因为 ChatGPT 的爆火。

2022 年 11 月 30 日相当于是AI世界的命运齿轮转动时刻。

好我们回到 DALL·E 2 ，先介绍一下 DALL·E 2 有哪些能力。

## 一、DALL·E 21.
1、DALL·E 2 基本信息官网： https://openai.com/dall-e-2在线体验： https://labs.openai.com/模型介绍： https://platform.openai.com/docs/models/dall-eAPI文档： https://platform.openai.com/docs/api-reference/images1.
2、创建图像接口：https://api.openai.com/v1/images/generations能力：文本生成图像主要请求参数有三个，prompt是画图提示词，n是一次生成的图片数量，size是图像大小，目前支持256x
256、512x512和1024x1024三种规格，也就是DALL·E 2只支持正方形图片：curl https://api.openai.com/v1/images/generations \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $OPENAI_API_KEY" \ -d '{ "prompt": "A cute baby sea otter", "n": 2, "size": "1024x1024" }'返回数据中直接带了图片url数组：{ "created": 1589478378, "data": [ { "url": "https://..." }, { "url": "https://..." } ]}举例，提示词“An astronaut riding a horse in photorealistic style.” 生成的图像为：1.
3、编辑修改图像接口：https://api.openai.com/v1/images/edits能力：用提示词对上传的图像进行修改主要请求参数有五个，在创建图片的参数基础上增加了两个，一个是原图 image ，一个是遮罩 mask：curl https://api.openai.com/v1/images/edits \ -H "Authorization: Bearer $OPENAI_API_KEY" \ -F image="@otter.png" \ -F mask="@mask.png" \ -F prompt="A cute baby sea otter wearing a beret" \ -F n=2 \ -F size="1024x1024"原图必须是正方形的png图片，遮罩 mask 也是一张png图片，mask 尺寸必须跟原图 image 尺寸一致。

mask 的透明区域就是模型会修改的区域，必须严格透明且支持不规则边界。

1.
4、生成相似但有变化的图片接口：https://api.openai.com/v1/images/variations能力：上传一张图，生成几张相似但有变化的图片主要参数有3个，image 是我们上传的原图，n是生成图片数量，size是图片尺寸：curl https://api.openai.com/v1/images/variations \ -H "Authorization: Bearer $OPENAI_API_KEY" \ -F image="@otter.png" \ -F n=2 \ -F size="1024x1024"返回值跟生成图像一样。

举例上传第一张图，生成后四张相似图片：1.
5、扩图 Outpainting这个能力目前没有对外提供接口，不过可以在官网看到效果示例，下方上图是输入的图片，下图是扩出的图片。

1.
6、修图 Inpainting这里哥飞不太清楚，是否跟1.3是同一个接口。

举例，输入图像是下方左图，用提示词“Add a flamingo beside the pool.”得到了下方右图。

好了，DALL·E 2 我们介绍完了，下面看看新发布的 DALL·E 3 有什么不一样。

## 二、DALL·E 32.
1、DALL·E 3 基本信息官网： https://openai.com/dall-e-32.
2、DALL·E 3 细节控制支持通过 prompt 对图像每一处细节进行控制，如以下几句提示词，完全可以认为就是一段故事中的场景描述，拿来就能够生成合适的图片。

The sidewalks bustling with pedestrians enjoying the nightlife.A bustling city street under the shine of a full moon.At the corner stall, a young woman with fieryred hair, dressed in a signature velvet cloak.s hagaling with the grumpv old vendor.The grumpy vendor, a tall, sophisticated man, is wearing a sharp suitsports a noteworthy moustache and is animatedly conversing on hissteamounk telephone.2.
3、画面更精美即使是同一段提示词，相比于DALL·E 2，DALL·E 3画出的画面也会更精美。

如提示词“An expressive oil painting of a basketball player dunking, depicted as an explosion of a nebula”，下方左图是DALL·E 2生成，右图是DALL·E 3 生成。

2.
4、DALL·E 3 集成 ChatGPT 到时大家可以在 ChatGPT 中直接用对话来画图，哪里画得不满意，可以直接用自然语言和GPT沟通，让GPT去修改。

以下是官网给出的一些示例。

2.
5、创意掌控DALL·E 3将拒绝提供在世艺术家风格图像的生成请求，创作者也可以提交申请将自己的作品从模型训练数据集中删除。

## 三、为什么哥飞介绍这个？

哥飞是吃饱了撑的，来介绍这个吗？

当然不是了。

之前我们在这篇文章中说了《找新词：一个永远有效的建站策略，让你快速拿到搜索引擎流量》。

那么今天哥飞就给你介绍了一个新词“DALL·E 3”，围绕着这个新词，你能去做什么呢？

这是哥飞留给你的今日作业，欢迎在评论中留言写作业。

你也可以加入

---

> 来源：哥飞公众号
> 原始文件：DALL_E_3_将于10月份发布_到时可在_ChatGPT_Plus_和_API_上体验.txt
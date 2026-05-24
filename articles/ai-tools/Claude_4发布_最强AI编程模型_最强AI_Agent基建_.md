# Claude 4发布 最强AI编程模型 最强AI Agent基建 

Claude 4发布：最强AI编程模型+最强AI Agent基建！

哥飞 在小说阅读器中沉浸阅读 花叔 . AI Native Coder：AppStore付费榜第一的「小猫补光灯」app开发者，这个账号主要关注AI、AI编程，也对互联网、商业以及更好的生活保有兴趣。

按照惯例来说，OpenAI是最爱截胡Google的，但是显然他们存货不足了，让Google I/O大会发布的新Gemini 2.5 Pro模型和文生视频模型Veo3出尽风头。

而OpenAI没干成的事，Anthropic来帮老大哥完成了。

在Google I/O大会刚结束一天的时间点，Anthropic在凌晨又发布了两个模型：Claude Sonnet 4和Claude Opus 4这两个模型的出现，让Gemini 2.5 Pro还没坐热的AI编程模型头把交椅位置再次易主。

## 一、最好的编程模型Claude Opus 4 被（Anthropic）称为"世界上最好的编程模型"，在编程评测基准SWE-bench上达到了72.5%的成绩，这是个最值得关注和信任和评估模型在真实世界的软件工程方面表现的评测集。

而在Terminal-bench上达到43.2%。

更重要的是，它能够持续工作数小时而不掉链子，这对于复杂的、需要多步骤的编程任务来说是个重大突破。

Claude Sonnet 4 相比之前的Sonnet 3.7有了显著提升，在SWE-bench上甚至比Opus 4还略高，达到72.7%。

虽然在大多数领域不如Opus 4强大，但它在性能和效率之间找到了最佳平衡点，可以认为是最适合用于日常编程任务的模型。

## 二、四大核心改进——Agent基建除了模型的智能之外，Anthropic这次更新主要在四个方面有重大改进，而这四个方面的能力改进都直指一个核心——更好的Agent能力：扩展思维与工具使用（Extended Thinking with Tool Use） 这是个测试版功能，允许Claude在思考和使用工具之间来回切换。

比如分析数据时，Claude会先思考策略，然后运行代码查看数据结构，再思考下一步该怎么分析，形成一个"思考-执行-再思考"的循环。

改进的记忆能力 这个功能对长时间任务特别重要。

Claude Opus 4现在可以创建和维护"记忆文件"来存储关键信息。

Anthropic甚至让Claude玩了12小时的宝可梦游戏来测试这个功能，Claude能够记住训练计划并持续64场战斗来升级宝可梦，展现了出色的长期专注能力。

更强的指令遵循能力 Claude 4在处理复杂、冗长的系统提示方面有了显著提升，可以处理超过10000个token的指令。

这个改进让Anthropic自己的系统提示长度减少了70%。

减少奖励黑客行为（Reward Hacking） 所谓奖励黑客行为就是模型为了达到目标而走捷径，比如硬编码测试或者注释掉错误代码。

Claude 4在这方面的倾向降低了80%以上，这意味着你可以更信任它会用正确的方法解决问题。

这四项能力的更新显然都是为了Agent或者编程而做的，Anthropic相比Google和OpenAI来说确实要聚焦很多，无论是做Coding模型还是Agent，都是为了开发者服务的，显然相比做to C业务，to B卖token更在Anthropic的舒适区。

## 三、混合推理模式&定价跟Claude 3.7一样，Claude 4系列都是混合推理模型，提供两种工作模式：即时响应模式：几秒内给出回答，适合常规任务深度思考模式：花更多时间思考，适合复杂问题Dario依然维持着一样的观念，模型不应该有指令模型和推理模型之分，在回答用户之前是否进行思考，思考多长时间是一个从0到1的平滑曲线，和人一样，面对不同任务时做不同程度的思考。

价格相比之前的Claude 3.5模型维持不变：Opus 4：$15/$75 每百万token（输入/输出）Sonnet 4：$3/$15 每百万token两个模型都已经在Anthropic API、Amazon Bedrock和Google Cloud的Vertex AI上可用。

免费用户也可以在Claude官网使用Sonnet 4（如果你没被封禁的话），付费用户可以使用两个模型和深度思考功能。

当然，你也已经可以在Cursor上使用这两个模型了。

## 四、可有可无的更新除了模型本身，Anthropic还发布了几个重要的周边更新：Claude Code正式版：之前是研究预览版，现在正式发布，支持VS Code和JetBrains集成，还可以通过GitHub Actions在后台运行。

不过我觉得这个工具暂时还是不可能比Cursor更好用，还是个更适合少数迎合开发者的小工具。

并行工具调用：Claude现在可以同时调用多个工具，提高效率。

新API能力：包括代码执行工具、MCP连接器、Files API，以及可以缓存提示长达一小时的功能。

## 五、实际模型能力测试Cursor跟Claude现在绑定得确实够深的，在Claude4发布当下就直接接入了对应的模型。

而且现在Cursor中有4个Claude4模型可选，分别是Claude Sonnet 
4、Claude Sonnet 4 thinking、Claude Opus 
4、Claude Opus 4 thinking可选。

我用我👇这篇文章中的生成app原型的提示词对Claude 4 Sonnet、Claude 3.7 Sonnet、Gemini 2.5 Pro模型做了测试【升级版】一句话生成高保真app原型图！

Cursor + Claude 3.7 Sonnet让设计师危险了？

Claude 4 Sonnet👇Claude 3.7 Sonnet👇Gemini 2.5 Pro👇这结果差距太明显了，我都觉得没什么好评价的。

但现实确实是：Gemini 2.5 Pro虽然在LMArena等部分编程能力排行榜上排名不错，除了复杂长代码的表现偶尔不错，但是对指令的理解和遵从能力相比Claude还是差了些，视觉审美也比较糟糕，常常会有莫名其妙的表现。

Claude 3.7 已经很不错了，但Claude Sonnet 4则完全是惊艳的水平，相比3.7而言，4的原型细节内容更丰富，比如收听过和没收听过的红点，订阅节目和收听节目的汇总信息等，甚至播放器页面的封面图还是可以旋转的（很遗憾在图片上看不出来）。

Claude Opus 4我也尝试做了些测试，但是生成几次后就遇到了一些模型访问次数的问题，似乎现在Opus的服务器资源还不太够。

但是从评分以及我仅有的部分体验看，普通编程任务的表现和Sonnet并无差异。

以我的经验来说，我建议选择如下：Claude Sonnet 4 ：最推荐的日常编程选择，在评估编程能力的指标SWE Bench评分上比Opus更高，经验上来说，比带thinking的模型表现更稳定更好，因为大多数任务你并不需要模型overthinking的。

Claude Sonnet 4 thinking：推荐在解决bug或进行项目规划的时候使用，毕竟在面对复杂问题时，你希望模型和人类一样，启动系统二，先做一些思考再做出审慎的回答。

Claude Opus 4和Claude Opus 4 Thinking：Opus是比Sonnet更大的模型，在非编程的数学、推理等任务上比Sonnet模型更好，也更贵。

尤其在Cursor中是需要启用Max模式，也就是每一次回答都需要单独计费的。

但是在常规的编程任务表现上并没有显著优于Sonnet模型，它相对更适合上下文长度非常多的大型复杂项目，或者重构项目。

不过如果你不只是拿Cursor去编程，而是还用Cursor当写作工具的话，我觉得你可以适当尝试下。

都看到这了，记得点赞、关注、转发哦，谢谢支持～注：本期内容选取自我的AI编程知识星球，感兴趣可点击「阅读原文」了解～以及，我还做了期视频介绍本次Claude 4的更新，可空降至B站查看：https://www.bilibili.com/video/BV1orJszFEFf/

---

> 来源：哥飞公众号
> 原始文件：Claude_4发布_最强AI编程模型_最强AI_Agent基建_.txt
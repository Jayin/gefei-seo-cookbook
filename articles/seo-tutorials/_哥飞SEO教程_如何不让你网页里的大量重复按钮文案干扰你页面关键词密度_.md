#  哥飞SEO教程 如何不让你网页里的大量重复按钮文案干扰你页面关键词密度 

【哥飞SEO教程】如何不让你网页里的大量重复按钮文案干扰你页面关键词密度？

大家好，我是哥飞。

今天我们来学一个哥飞之前研究出来的小技巧，如何不让你的网页里的大量重复按钮的文案干扰你的页面关键词密度？

答案是用 CSS Content ，把按钮文案写在 CSS 代码里。

.play-button:after { content: "Play"; margin-left: .5rem;}同样的原理，页面上其它你不想出现在正文里影响关键词密度的文案，都可以这样处理。

假设你的页面上有40个按钮，那么单词 Play 就会出现40次，这会严重干扰页面的核心关键词密度。

使用哥飞上面教的方法，就可以解决这个问题。

下面这个网站就用了这个方法https://emojidb.org/i-love-u-emojis如果你的网站要显示多语言，又要怎么做呢？

还是用这个方法，加载一个多语言 CSS 文件即可，举例你要同时支持中文、英文和日语，那么就要有三个 CSS 文件，分别是 cn.css、en.css、ja.css 。

cn.css:.play-button:after { content: "播放"; margin-left: .5rem;}en.css:.play-button:after { content: "Play"; margin-left: .5rem;}js.css:.play-button:after { content: "再生"; margin-left: .5rem;}然后你就根据你要显示的语言去加载对应的 CSS 文件即可。

好了，今天的SEO技巧就是在这些了。

如果你还想跟着哥飞学习更多的SEO技巧，请加入哥飞的社群。

---

> 来源：哥飞公众号
> 原始文件：_哥飞SEO教程_如何不让你网页里的大量重复按钮文案干扰你页面关键词密度_.txt
#  哥飞SEO教程 Google Search Console 提示站点地图 Sitemap 无法抓取怎么办 

【哥飞SEO教程】Google Search Console 提示站点地图 Sitemap 无法抓取怎么办？

大家好，我是哥飞。

当我们在 Google Search Console 里提交 Sitemap 时，正常情况下，能够提交成功，状态是“成功”。

但是也有不少朋友遇到过，提示站点地图无效，或者无法抓取。

哥飞总结了一下，大概有几种情况：1. 直接拿网页地址去提交了，而不是拿 Sitemap 地址去提交，那么修改成正确Sitemap地址即可；2. Sitemap 地址无法访问，可能是 Sitemap 文件没有放在网页根目录下，而是放在了代码根目录下，这时候根据你代码框架要求设置即可；3. Sitemap 文件格式错误，这个让AI帮你修复，或者找个模板重写就可以了；4. GSC 上设置的域名与Sitemap网址的域名不一致，这个改成一致即可。

还有种类似情况，你在GSC后台添加的是网址前缀，然后Sitemap网址却又有这个网址前缀不一致；5. 某些域名后缀Bug，如 cc 域名，目前比较多朋友提到即使 Sitemap 网址可访问，格式也正确，但就是提示无法抓取。

对于最后一种情况，又有社群里的朋友测试发现，不放在网站根目录，而是放在下级目录下就可以抓取到了，如可以放在 /sitemap/ ，目录下，完整地址是 域名/sitemap/sitemap.xml 下。

今天的文章有点短，因为该讲的都讲完了，下次大家遇到了Sitemap无法抓取，就按照上面这几种情况去排查即可。

下面我们拓展一点知识吧，其实除了 XML 格式的 Sitemap 外，还有 HTML 格式的 Sitemap 。

两者的区别是，XML 的 Sitemap 只给搜索引擎爬虫看，而 HTML 格式的 Sitemap 既给爬虫看，又给人看。

也就是 HTML 格式的 Sitemap 还承担了站点内部页面导航的作用。

如上图，是 ebay.com 的 footer 截图，里边有一个 HTML 格式 Sitemap，网址是：https://pages.ebay.com/sitemap.html打开这个网址，长下面这样，Ebay 很明确说了，这是一个 Sitemap 页面。

大家仔细看就会发现，HTML格式的Sitemap 跟 XML 格式的 Sitemap 还是有些不一样的，HTML 格式的 Sitemap 按照分类把所有重要页面都列出来了。

而 XML 格式的 Sitemap 则没有层级关系，直接列出全部网址。

当然，因为 Ebay 的网址实在是太多了，所以其实也分开放在了多个 XML 格式的 Sitemap 文件里，并且在 robots.txt 文件里一一列出来。

关于 HTML 格式和 XML 格式的 Sitemap 更详细讲解，哥飞推荐一篇文章给大家：https://www.sitecentre.com.au/blog/html-sitemap-vs-xml-sitemap好了，今天的文章就到这里了。

微信搜索框，输入 361079 ，点击查找QQ号，就能加哥飞微信了。

---

> 来源：哥飞公众号
> 原始文件：_哥飞SEO教程_Google_Search_Console_提示站点地图_Sitemap_无法抓取怎么办_.txt
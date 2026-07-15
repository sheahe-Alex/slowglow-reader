# 伴读 Reader

一个帮助你进入、理解并回看长文的低阻力阅读辅助工具。  
A low-friction reading support tool that helps you enter, understand, and revisit long-form text.

适合文章、论文、课程材料、文档、长邮件，或任何“想读但难开始/难坚持”的文本。  
For articles, papers, course materials, documentation, long emails, or any text that feels hard to start or hard to stay with.

它不是速读工具，也不是翻译器。它先用“逐句伴读”帮你进入文本，再用关键词和关键句候选帮你第二遍、第 N 遍回到重点。  
It is not a speed-reading tool or a translator. It first helps you enter the text with Sentence Guide, then helps you return to key points later with keyword and key-sentence candidates.

你可以把它当成一个简单流程：先读进去，再回来看懂，最后留下可复习的痕迹。  
You can treat it as a simple flow: enter the text, come back to understand it, then leave traces you can review.

## 直接使用 / Start Here

最简单的使用方式是直接打开在线版：  
The easiest way to use Reader is to open the online version:

[https://sheahe-alex.github.io/slowglow-reader/](https://sheahe-alex.github.io/slowglow-reader/)

不需要安装，不需要登录。打开网页后，把文字粘贴进去即可。  
No installation or login is required. Open the page and paste text into the reader.

手机上如果 `读取剪贴板` 不可用，直接点文本框手动粘贴即可。  
On phones, if `Read Clipboard` does not work, tap the text box and paste manually.

如果在线版打不开，或者所在网络访问 GitHub Pages 不稳定，可以下载这个仓库后本地打开 `index.html`。  
If the online version does not open, or if GitHub Pages is unstable on your network, download this repository and open `index.html` locally.

## 更方便取用 / Easier Access

在线版仍然是主入口。下面这些只是让它更容易被随手打开。  
The online version is still the main entry point. The options below simply make it easier to reach.

### 添加到桌面或主屏幕 / Add To Desktop Or Home Screen

伴读 Reader 支持作为网页应用安装。  
Bandu Reader can be installed as a web app.

- 在 Chrome 或 Edge：打开在线版后，点地址栏右侧的安装图标，或在菜单里选择“安装应用”。  
  In Chrome or Edge: open the online version, then use the install icon near the address bar or choose "Install app" from the menu.
- 在手机浏览器：打开在线版后，使用浏览器菜单里的“添加到主屏幕”。  
  On mobile browsers: open the online version, then choose "Add to Home Screen" from the browser menu.

### 网页选中文字后一键打开 / Send Selected Text From A Webpage

如果你经常在网页里读文章，可以使用书签按钮：  
If you often read in webpages, you can use the bookmarklet:

- [Bookmarklet / 书签按钮](./Bookmarklet_书签按钮.md)

它不是浏览器插件，不需要安装商店扩展。选中文字后点书签，就会打开在线版并带入文字。  
It is not a browser extension and does not require an extension store. Select text, click the bookmark, and it opens the online reader with the text.

## 为什么做 / Why

伴读 Reader 是一个深度阅读脚手架。

Reader is a scaffold for deep reading.

它不是为了替你阅读，而是为了陪你一步一步进入文本：先读进去，再看见重点，最后把理解留下来，变成写作和复习时可以返回的材料。

It is not here to read for you. It is here to help you enter the text step by step: first get into the reading, then notice what matters, then leave traces you can return to when writing or reviewing.

很多人并不是不愿意深度阅读，而是阅读过程太容易触发过载、挫败和自责。伴读 Reader 希望降低这些阻力，让人可以一次次回到文本：第一遍读进去，第二遍看清重点，第 N 遍把内容变成自己的理解。

Many people are not unwilling to read deeply. The process is often too easy to overload, frustrate, or shame them. Reader tries to lower that friction, so people can return to the text again and again: enter it on the first pass, see key points on the second pass, and slowly turn the content into their own understanding.

核心信念是：

The core belief:

> 阅读能力不是被逼出来的，而是在足够安全、足够合适的支持里，慢慢恢复和生长出来的。  
> Reading ability is not forced into existence. It can recover and grow when the support feels safe and suitable enough.

## 功能 / Features

- 粘贴或读取剪贴板文字 / Paste or read text from the clipboard
- 大字号阅读区 / Large reading view
- 可开关声音：有声朗读或静音高亮导读 / Optional voice: read aloud or silent guided highlighting
- 当前词高亮 / Current-word highlight
- 阅读中调整速度 / Adjust reading speed while it is running
- 保留原文段落和换行 / Preserve paragraphs and line breaks
- 逐句伴读：当前句浮现出来，其他文字轻轻退后，减少一次面对整屏文字的压力 / Sentence Guide: the current sentence appears while surrounding text gently fades back, reducing the pressure of facing the whole page at once
- 标记这一句：一键留下你自己的重点判断 / Mark Sentence: keep a trace of your own judgment with one click
- 可选加粗引导，帮助眼睛更容易落回文字 / Optional bold guidance to make it easier for the eyes to return to the text
- 可选结构提示，轻量标出连接词和少量逻辑信号 / Optional structure hints for connectors and light logic signals
- 重点回看：本地关键词和关键句候选，帮助第二遍、第 N 遍复习和做笔记 / Review anchors: local keyword and key-sentence suggestions for second-pass review, later review, and note-taking
- 根据浏览器语言自动显示中文或英文界面，也可以手动切换 / Automatically uses Chinese or English based on browser language, with manual switching available

## 本地运行 / Run Locally

核心阅读器可以在 Windows 和 Mac 的现代浏览器里使用。  
The core reader works in modern browsers on both Windows and Mac.

### 直接打开 / Directly Open

双击 `index.html`。  
Double-click `index.html`.

Windows 用户可以用 Chrome 或 Edge 打开 `index.html`。  
Windows users can open `index.html` with Chrome or Edge.

### Mac 推荐方式 / Recommended On Mac

双击：  
Double-click:

```text
OpenSlowglowReader.command
```

如果 macOS 阻止打开，可以右键这个文件，选择“打开”，再确认一次。  
If macOS blocks it, right-click the file, choose "Open", and confirm once more.

## 使用流程 / How To Use

1. 在网页、PDF 或文档里选中文字。  
   Select text in a webpage, PDF, or document.
2. 按 `Command C` 复制。  
   Press `Command C` to copy.
3. 回到伴读 Reader。  
   Return to Reader.
4. 点 `读取剪贴板`，或直接粘贴到左侧文本框。  
   Click `读取剪贴板`, or paste directly into the text box on the left.
5. 点 `开始阅读`。  
   Click `Start Reading`.

状态不好、文字太压迫时，可以点 `逐句伴读`。  
When the text feels overwhelming, try `逐句伴读` / Sentence Guide.

## 隐私 / Privacy

当前版本是纯本地网页工具。  
The current version is a local web tool.

- 不需要登录 / No login required
- 不需要 API key / No API key required
- 不上传你的文字 / Your text is not uploaded
- 不使用在线 AI / No online AI is used

如果打开声音，朗读会使用浏览器和系统提供的语音能力。关闭声音时，高亮仍会继续推进。  
If voice is on, read-aloud uses your browser and system speech features. If voice is off, the highlight still keeps moving.

## 适合谁 / Who It May Help

这个工具可能适合：  
This tool may help people who:

- 读长文容易过载 / Feel overwhelmed by long text
- ADHD / 注意力容易漂移 / Have ADHD or attention that drifts easily
- 英语非母语读者 / Read in a non-native language
- 做笔记时容易抓不住重点 / Struggle to pick out key points while taking notes
- 曾经因为阅读、学习或评价而产生压力 / Carry stress or shame around reading, learning, or evaluation

它不是医疗工具，也不能替代专业支持。它只是一个更温柔的阅读入口。  
It is not a medical tool and does not replace professional support. It is simply a softer entry point into reading.

## 分享给朋友 / Share With Friends

可以参考：  
You can use:

- [Friend Guide / 给朋友看的说明](./Friend-Guide_给朋友看的说明.md)
- [Share Copy / 分享文案](./Share-Copy_分享文案.md)
- [Bookmarklet / 书签按钮](./Bookmarklet_书签按钮.md)
- [Product Charter / 产品宪章](./Product-Charter_产品宪章.md)

## 路线图 / Roadmap

- 更正式的跨平台网页版 / A more polished cross-platform web version
- 更稳定的大段文本导读 / More stable long-text guided reading
- 可选的 PDF/OCR 辅助 / Optional PDF/OCR support
- 更细腻的逐句伴读调节 / More nuanced Sentence Guide controls
- 多语言阅读体验优化 / Better multilingual reading experience

## License

MIT

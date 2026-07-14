# 伴读 Reader

一个面向长文和严肃内容的温柔辅助阅读器，帮助人更低阻力地开始阅读、读下去，并回到注意力。  
A gentle assisted reader for long-form and serious reading, designed to reduce friction and make it easier to start, continue, and return to the text.

它不是速读工具，也不是翻译器。它通过可开关声音的导读、当前词高亮、当前句托出、低干扰排版和轻量结构提示，帮助你面对文章、论文、课程材料、文档、长邮件，或任何“想读但难开始/难坚持”的文本。  
It is not a speed-reading tool or a translator. It uses optional voice, guided highlighting, sentence focus, low-distraction layout, and light structure hints to help with articles, papers, course materials, documentation, long emails, or any text that feels hard to start or hard to stay with.

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

## 为什么做 / Why

伴读 Reader 不是为了催人读得更快，也不是为了证明谁的专注力够好。

Reader is not about forcing people to read faster or proving that they can focus well enough.

它想做的是一件更朴素的事：把阅读变得不那么吓人。你可以复制一段文字，让它放大显示，选择朗读或静音导读，并高亮当前读到的位置。走神了也没关系，从高亮处回来就好。

It tries to make reading feel less intimidating. You can copy a piece of text, make it larger, use read-aloud or silent guided highlighting, and follow the current highlighted word. If your attention drifts, you can gently return to the highlight.

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
- 舒缓阅读：隐藏干扰，把当前句托出来，让已读内容和非当前句轻轻退后 / Gentle reading: hides distractions, lifts the current sentence forward, and lets read text and surrounding text fade back
- 可选加粗引导，帮助眼睛更容易落回文字 / Optional bold guidance to make it easier for the eyes to return to the text
- 可选结构提示，轻量标出连接词和少量逻辑信号 / Optional structure hints for connectors and light logic signals
- 本地关键词和关键句候选，帮助做笔记起步 / Local keyword and key-sentence suggestions for note-taking
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

状态不好、文字太压迫时，可以点 `舒缓阅读`。  
When the text feels overwhelming, try `舒缓阅读` / Gentle Reading.

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

## 路线图 / Roadmap

- 更正式的跨平台网页版 / A more polished cross-platform web version
- 更稳定的大段文本导读 / More stable long-text guided reading
- 可选的 PDF/OCR 辅助 / Optional PDF/OCR support
- 更细腻的舒缓阅读调节 / More nuanced Gentle Reading controls
- 多语言阅读体验优化 / Better multilingual reading experience

## License

MIT

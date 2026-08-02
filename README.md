# 伴读 Reader

让阅读更容易开始，也更容易继续。  
Make reading easier to start, and easier to keep going.

伴读 Reader 是一个本地、无登录、不上传文字的低阻力伴读器。  
Bandu Reader is a local, no-login, no-upload reading companion.

**直接打开在线版 / Open the online reader:**  
[https://sheahe-alex.github.io/slowglow-reader/](https://sheahe-alex.github.io/slowglow-reader/)

不需要安装，不需要登录。打开网页后，把文字粘贴进去即可。  
No installation or login is required. Open the page and paste text into the reader.

也可以点“导入文件”，选择 PDF、图片、TXT、Markdown、HTML 或 CSV。能提取的文字会进入伴读；扫描 PDF 和图片会原样显示、可点开查看，但暂不自动识别或朗读。
You can also click “Import File” and choose a PDF, image, TXT, Markdown, HTML, or CSV file. Extractable text enters the reading flow; scanned PDFs and images are shown as viewable pages, but are not automatically recognized or read aloud yet.

## 三件事先知道 / Good To Know

- 不需要登录，也不会上传你的文字。  
  No login, and your text is not uploaded.
- 它不是总结器、翻译器或速读器；它只是帮你更容易读下去。  
  It is not a summarizer, translator, or speed-reading tool; it helps you keep reading.
- 先放一小段文字试试就好。  
  Start with one small passage.

## 它适合什么 / What It Is For

适合文章、论文、课程材料、文档、长邮件，或任何“想读但难开始/难坚持”的文本。  
For articles, papers, course materials, documentation, long emails, or any text that feels hard to start or hard to stay with.

它不是速读工具，也不是翻译器。它用大字号、高亮、可选声音和“专注阅读”帮你进入文本；需要回看时，再用本地规则提供少量回看线索。
It is not a speed-reading tool or a translator. It uses large text, highlighting, optional sound, and Focus Reading to help you enter the text; when you need to review, local rules provide a few review cues.

它不会替你总结，也不抢走学习过程。它只是一个阅读脚手架：在你容易卡住、走神、过载的时候，把你轻轻带回文字里。  
It does not summarize for you or take over the learning process. It is a reading scaffold: when you get stuck, drift, or feel overloaded, it gently brings you back to the text.

## 直接使用 / Start Here

最简单的使用方式就是上面的在线版链接。  
The easiest way to use it is the online link above.

还没有准备好文字时，可以先点页面里的“没有文字？先试一小段示例”。  
If you do not have text ready, click "No text yet? Try a short sample" on the page.

1. 放入文字：粘贴文章、课程材料、文档，或任何想读但难开始的文字。  
   Add text: paste an article, course material, document, or any text that feels hard to begin.
2. 开始伴读：大字号、高亮和可选声音会陪你往下走。  
   Start reading: large text, highlighting, and optional sound help you keep moving.
3. 需要时打开专注阅读：只让当前句站出来。
   Use Focus Reading when needed: let only the current sentence stand forward.

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

如果你经常在网页里读文章，可以用书签按钮把选中文字一键送进 Reader：  
If you often read webpages, the bookmarklet can send selected text into Reader with one click:

- [Bookmarklet / 书签按钮](./Bookmarklet_书签按钮.md)

它不是浏览器插件，不需要安装扩展商店里的东西。选中文字后点书签，就会打开在线版并带入文字。  
It is not a browser extension and does not require an extension store. Select text, click the bookmark, and it opens the online reader with that text.

如果你经常在浏览器版 Codex 里阅读报告，也可以安装可选的浏览器桥接扩展：
If you often read reports in browser-based Codex, you can also install the optional browser bridge:

- [Browser Bridge / 浏览器桥接](./browser-extension/README.md)

选中文字后右键选择 `Send selection to Bandu Reader / 发送到伴读`，在线版会打开并接收文字。扩展只在本地暂存选中的文字，接收后删除，不把文字放进 URL，也不上传文字。
Select text, right-click, and choose `Send selection to Bandu Reader`. The online reader opens with the text. The extension stores the selection locally until it is received, then deletes it; it does not put the text in the URL or upload it.

桌面版 Codex 不是网页，扩展无法直接读取它的选区；请复制回答后使用 `读取剪贴板`。
The desktop Codex app is not a webpage, so the extension cannot read its selection directly; copy the response and use `Read Clipboard` instead.

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
- 导入 PDF、图片、TXT、Markdown、HTML 或 CSV；可提取文字进入伴读，扫描页和图片原样显示并可放大 / Import PDF, images, TXT, Markdown, HTML, or CSV; extractable text enters the reading flow, while scanned pages and images remain visible and can be enlarged
- 大字号阅读区 / Large reading view
- 可开关朗读：有声朗读或静音高亮导读 / Optional read-aloud: spoken reading or silent guided highlighting
- 数字片段会跟随整篇文本的主语言朗读 / Number-only passages follow the dominant language of the text
- 当前词高亮 / Current-word highlight
- 设置里可选择低饱和的当前词高光颜色 / Choose a muted current-word highlight color in Settings
- 上一句：阅读中可以退回上一句 / Previous sentence: step back while reading
- 暂停后可在上一句和下一句之间移动 / While paused, move between the previous and next sentence
- 阅读中保留句子级和段落级跳转：◀◀ / ▶▶ 按段移动，◀ / ▶ 按句移动 / Keep sentence- and paragraph-level jumps visible while reading: ◀◀ / ▶▶ move by paragraph, ◀ / ▶ move by sentence
- 停止：停止自动推进，收起粘贴框和设置，保留标注后自由浏览 / Stop: stop auto-advance, hide input and settings, and browse the marked text freely
- 读完后可一键回到顶部，或清空并换一段新文字 / After reading, jump back to the top or clear the reader for a new passage
- 阅读中调整速度 / Adjust reading speed while it is running
- 自动记住语速、字号、行距、宽度和主题 / Remembers speed, font size, line height, width, and theme
- 保留原文段落和换行 / Preserve paragraphs and line breaks
- 识别复制来的 HTML 表格并保留行列；表格伴读时按行推进 / Recognize copied HTML tables, keep their rows and columns, and move row by row while reading
- 富文本粘贴时保留剪贴板带来的图片及其前后顺序；图片不参与朗读，可点开查看 / Preserve clipboard images and their surrounding order when pasting rich content; images are skipped by read-aloud and can be opened for a closer look
- 专注阅读：只让当前句站出来，减少一次面对整屏文字的压力 / Focus Reading: let only the current sentence stand forward, reducing the pressure of facing the whole page at once
- 第一次放入文字时会轻轻询问是否体验专注阅读，也可以先跳过 / On first use, a gentle prompt offers Focus Reading; you can skip it
- 可选句子锚点：需要时固定显示当前句 / Optional Sentence Anchor: keep the current sentence visible when needed
- 在专注阅读的当前句旁标记：一键留下重点判断，再点一次撤销 / Mark beside the current sentence in Focus Reading; click again to unmark
- 英文默认使用词首加粗，设置里可以关闭 / English word starts are bold by default; you can turn them off in Settings
- 结构提示默认自动适配语言，设置里可以关闭或调整强度：英文偏信息流，中文偏逻辑信号和概念复现 / Structure hints adapt to the language by default; you can turn them off or adjust their strength in Settings: information flow for English, logic signals and repeated concepts for Chinese
- 回看线索：本地规则给出少量可能的回看词和回看句，点击即可回到原文对应位置 / Review Cues: local rules suggest a few possible words and sentences; click one to jump back to its place in the source text
- 笔记提示：用自己的话记下重点 / Note cue: put key points in your own words
- 根据浏览器语言自动显示中文或英文界面，也可以手动切换 / Automatically uses Chinese or English based on browser language, with manual switching available
- 基础阅读、朗读和回看关键词支持多种文字；结构提示目前主要针对中文和英文，其他语言会保持干净显示 / Reading, speech, and review keywords work across multiple writing systems; structure hints currently focus on Chinese and English, while other languages stay visually clean

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
4. 点 `读取剪贴板`，或直接粘贴到 `放入文字` 区域。  
   Click `Read Clipboard`, or paste directly into the `Add Text` area.
   也可以点 `导入文件`，选择 PDF、图片、TXT、Markdown、HTML 或 CSV。
   You can also click `Import File` and choose a PDF, image, TXT, Markdown, HTML, or CSV file.
5. 点 `开始伴读`。  
   Click `Start Reading`.

状态不好、文字太压迫时，可以点 `专注阅读`。
When the text feels overwhelming, try `专注阅读` / Focus Reading.

## 隐私 / Privacy

当前版本是纯本地网页工具。  
The current version is a local web tool.

- 不需要登录 / No login required
- 不需要 API key / No API key required
- 不上传你的文字 / Your text is not uploaded
- 不使用在线 AI / No online AI is used

导入文件时，浏览器会在本地读取内容；第一次使用 PDF 功能时，会从 PDF.js 的公开 CDN 懒加载解析器代码，但 PDF 内容不会发送给 CDN。扫描 PDF 和图片目前只原样显示；OCR 仍在后续阶段。
When importing a file, the browser reads its contents locally. The first PDF import lazily loads the PDF.js parser code from a public CDN, but the PDF content is not sent to the CDN. Scanned PDFs and images are currently displayed as-is; OCR is still planned for a later phase.

如果粘贴的网页内容只提供外链图片地址，浏览器可能会向图片原站请求该图片；文字不会因此上传。剪贴板直接提供的图片文件仍只在本地显示。
If pasted web content only provides an external image URL, the browser may request that image from its original site; your text is not uploaded. Image files supplied directly by the clipboard remain local.

如果打开朗读，会使用浏览器和系统提供的语音能力。关闭朗读时，高亮仍会继续推进。  
If read-aloud is on, it uses your browser and system speech features. If read-aloud is off, the highlight still keeps moving.

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

- [Case Study / 求职案例](./case-study/output/伴读Reader_求职案例.pdf)
- [Friend Guide / 给朋友看的说明](./Friend-Guide_给朋友看的说明.md)
- [Share Copy / 分享文案](./Share-Copy_分享文案.md)
- [Bookmarklet / 书签按钮](./Bookmarklet_书签按钮.md)
- [Browser Bridge / 浏览器桥接](./browser-extension/README.md)
- [Product Charter / 产品宪章](./Product-Charter_产品宪章.md)

## 路线图 / Roadmap

- 更正式的跨平台网页版 / A more polished cross-platform web version
- 更稳定的大段文本导读 / More stable long-text guided reading
- 扫描 PDF 和图片 OCR 辅助 / OCR support for scanned PDFs and images
- 更细腻的专注阅读调节 / More nuanced Focus Reading controls
- 多语言阅读体验优化 / Better multilingual reading experience

## License

MIT

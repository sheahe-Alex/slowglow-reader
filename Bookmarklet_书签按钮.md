# 伴读书签按钮 / Bandu Reader Bookmarklet

书签按钮是一种很轻量的入口：在网页里选中文字后，点一下书签栏里的“伴读”，就会打开在线版，并把选中的文字送进去。

A bookmarklet is a lightweight entry point: select text on a webpage, click the "Bandu Reader" bookmark, and the online reader will open with the selected text.

## 安装 / Setup

1. 在浏览器里新建一个书签。  
   Create a new bookmark in your browser.
2. 名字填：`伴读 Reader`。  
   Name it: `Bandu Reader`.
3. 地址填下面这一整段代码。  
   Use the full code below as the bookmark URL.

```text
javascript:(()=>{const text=(window.getSelection&&window.getSelection().toString()||"").trim();if(!text){alert("请先选中想放进伴读的文字。 / Select the text you want to send to Bandu Reader first.");return;}const target="https://sheahe-alex.github.io/slowglow-reader/";const reader=window.open(target+"#from=bookmarklet","_blank");let tries=0;const timer=setInterval(()=>{if(!reader||reader.closed||tries>24){clearInterval(timer);return;}reader.postMessage({type:"bandu-reader-text",text},"https://sheahe-alex.github.io");tries+=1;},250);})();
```

## 使用 / Use

1. 在网页里选中文字。  
   Select text on a webpage.
2. 点书签栏里的 `伴读 Reader`。  
   Click the `Bandu Reader` bookmark.
3. 在线版会打开，并自动放入选中的文字。  
   The online reader will open and receive the selected text.

## 小提醒 / Notes

- 书签按钮只读取你当下选中的文字。  
  It only reads the text you selected.
- 它不会上传文字到额外服务器；文字会被送到伴读在线版页面里处理。  
  It does not send text to an extra server; it sends the text into the Bandu Reader online page.
- 有些网站会限制选中文字或弹窗。如果失败，仍然可以复制文字后打开在线版粘贴。  
  Some websites restrict text selection or pop-ups. If it fails, copy the text and paste it into the online reader.

# 网页文字一键送进伴读 / Send Web Text To Reader

这是一个很轻的入口：在网页里选中文字，点一下书签栏里的 `伴读`，就会打开在线版，并把选中的文字送进去。

This is a lightweight entry point: select text on a webpage, click the `Bandu` bookmark, and the online reader will open with that text.

它不是浏览器插件，不需要安装扩展商店里的东西。  
It is not a browser extension, and it does not require an extension store.

## 最短安装版 / Quick Setup

1. 在浏览器里新建一个书签。  
   Create a new bookmark in your browser.
2. 名字填：`伴读`。  
   Name it: `Bandu`.
3. 地址填下面这一整段代码。不要漏掉开头的 `javascript:`。  
   Use the full code below as the bookmark URL.

```text
javascript:(()=>{const text=(window.getSelection&&window.getSelection().toString()||"").trim();if(!text){alert("请先选中想放进伴读的文字。 / Select the text you want to send to Bandu Reader first.");return;}const target="https://sheahe-alex.github.io/slowglow-reader/";const reader=window.open(target+"#from=bookmarklet","_blank");let tries=0;const timer=setInterval(()=>{if(!reader||reader.closed||tries>24){clearInterval(timer);return;}reader.postMessage({type:"bandu-reader-text",text},"https://sheahe-alex.github.io");tries+=1;},250);})();
```

如果你不知道怎么新建书签：先随便收藏一个网页，然后编辑这个书签，把名字和地址改成上面的内容。  
If you are not sure how to create a bookmark: bookmark any page first, then edit that bookmark and replace its name and URL with the text above.

## 使用 / Use

1. 在网页里选中文字。  
   Select text on a webpage.
2. 点书签栏里的 `伴读`。  
   Click the `Bandu` bookmark.
3. 在线版会打开，并自动放入选中的文字。  
   The online reader will open and receive the selected text.

## 小提醒 / Notes

- 书签按钮只读取你当下选中的文字。  
  It only reads the text you selected.
- 它不会上传文字到额外服务器；文字会被送到伴读在线版页面里处理。  
  It does not send text to an extra server; it sends the text into the Bandu Reader online page.
- 有些网站会限制选中文字或弹窗。如果没打开，手动复制粘贴就好。  
  Some websites restrict text selection or pop-ups. If it does not open, manual copy and paste is fine.

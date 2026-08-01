const READER_URL = "https://sheahe-alex.github.io/slowglow-reader/";
const MENU_ID = "send-selection-to-bandu";
const PENDING_TTL_MS = 10 * 60 * 1000;

function createMenu() {
  chrome.contextMenus.removeAll(() => {
    chrome.contextMenus.create({
      id: MENU_ID,
      title: "Send selection to Bandu Reader / 发送到伴读",
      contexts: ["selection"]
    });
  });
}

function cleanupPendingImports() {
  chrome.storage.local.get(null, entries => {
    const staleKeys = Object.entries(entries)
      .filter(([key, value]) => (
        key.startsWith("pending:")
        && (!value?.createdAt || Date.now() - value.createdAt > PENDING_TTL_MS)
      ))
      .map(([key]) => key);

    if (staleKeys.length) chrome.storage.local.remove(staleKeys);
  });
}

function makeImportId() {
  if (crypto.randomUUID) return crypto.randomUUID();
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function sendSelection(text) {
  const cleanText = String(text || "").trim();
  if (!cleanText) return;

  const id = makeImportId();
  const key = `pending:${id}`;
  chrome.storage.local.set({
    [key]: {
      text: cleanText,
      createdAt: Date.now()
    }
  }, () => {
    chrome.tabs.create({
      url: `${READER_URL}#bandu-import=${encodeURIComponent(id)}`
    });
  });
}

chrome.runtime.onInstalled.addListener(() => {
  createMenu();
  cleanupPendingImports();
});
chrome.runtime.onStartup.addListener(() => {
  createMenu();
  cleanupPendingImports();
});

chrome.contextMenus.onClicked.addListener((info) => {
  if (info.menuItemId === MENU_ID) sendSelection(info.selectionText);
});

chrome.action.onClicked.addListener(async tab => {
  if (!tab.id) return;

  try {
    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => window.getSelection?.().toString() || ""
    });
    sendSelection(results[0]?.result || "");
  } catch {
    // Some protected pages do not allow scripts. The context menu still works elsewhere.
  }
});

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message?.type !== "bandu-reader-request" || !message.id) return;

  const key = `pending:${message.id}`;
  chrome.storage.local.get([key], entries => {
    const text = entries[key]?.text || "";
    chrome.storage.local.remove(key, () => sendResponse({ text }));
  });

  return true;
});

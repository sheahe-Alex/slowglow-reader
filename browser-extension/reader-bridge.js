(() => {
  const hash = window.location.hash.startsWith("#")
    ? window.location.hash.slice(1)
    : "";
  const importId = new URLSearchParams(hash).get("bandu-import");
  if (!importId) return;

  chrome.runtime.sendMessage(
    { type: "bandu-reader-request", id: importId },
    response => {
      if (chrome.runtime.lastError || !response?.text) return;
      window.postMessage(
        {
          type: "bandu-reader-text",
          source: "bandu-browser-bridge",
          text: response.text
        },
        window.location.origin
      );
      window.history.replaceState(null, "", window.location.pathname);
    }
  );
})();

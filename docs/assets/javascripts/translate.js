// "한국어" button in the header: translates the current page from English to
// Korean inside the browser, using the browser's built-in Translator API
// (desktop Chrome 138+, Edge). Nothing is sent to a translation server by this
// page. Browsers without the API get a short note on how to use their own
// translation menu instead.
//
// The choice is remembered (localStorage "kx-lang"), so the next page opens in
// Korean as well once the translation model is on the device.
(function () {
  "use strict";

  var SOURCE = "en";
  var TARGET = "ko";
  var STORE_KEY = "kx-lang";

  // Text inside these is never translated: code, formulas, Hangul symbol
  // tiles, product names and anything marked translate="no".
  var SKIP = "pre, code, kbd, script, style, svg, .arithmatex, mjx-container, " +
    ".kx-jamo, .kx-stack__name, [translate='no'], .md-search, .kx-translate, .kx-translate-note";
  // Parts of the page that hold readable English.
  var ROOTS = ".md-tabs, .md-sidebar, .md-content, .kx-hero, .md-footer";

  var ICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="m12.87 15.07-2.54-2.51.03-.03A17.5 17.5 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 ' +
    '10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 ' +
    '3.11 3.11.76-2.04M18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12m-2.62 7 1.62-4.33L19.12 17h-3.24Z"/></svg>';

  var originals = null;      // Map<Text, string> while the page is shown in Korean
  var translator = null;
  var busy = false;
  var button, label;

  function store(value) {
    try { value ? localStorage.setItem(STORE_KEY, value) : localStorage.removeItem(STORE_KEY); } catch (e) {}
  }
  function stored() {
    try { return localStorage.getItem(STORE_KEY); } catch (e) { return null; }
  }

  // A built-in translator that does not answer must not leave the button stuck.
  function withTimeout(promise, ms) {
    return Promise.race([promise, new Promise(function (_, reject) {
      setTimeout(function () { reject(new Error("timeout")); }, ms);
    })]);
  }

  function setLabel(text, title) {
    label.textContent = text;
    button.title = title;
    button.setAttribute("aria-label", title);
  }
  function showEnglishLabel() { setLabel("한국어", "Translate this page into Korean"); }
  function showKoreanLabel() { setLabel("English", "원문(영어)으로 보기"); }

  function textNodes() {
    var nodes = [];
    document.querySelectorAll(ROOTS).forEach(function (root) {
      var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
        acceptNode: function (node) {
          if (!/[A-Za-z]/.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
          var parent = node.parentElement;
          if (!parent || parent.closest(SKIP)) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      });
      while (walker.nextNode()) nodes.push(walker.currentNode);
    });
    return nodes;
  }

  async function getTranslator(fromClick) {
    if (translator) return translator;
    var options = { sourceLanguage: SOURCE, targetLanguage: TARGET };
    var availability = await withTimeout(Translator.availability(options), 4000);
    if (availability === "unavailable") return null;
    // Downloading the model needs a click; on page load we only use a model
    // that is already on the device.
    if (availability !== "available" && !fromClick) return null;
    // Allow time for the one-off model download (progress is shown on the button).
    translator = await withTimeout(Translator.create(Object.assign({}, options, {
      monitor: function (m) {
        m.addEventListener("downloadprogress", function (e) {
          setLabel("모델 " + Math.round(e.loaded * 100) + "%", "번역 모델을 내려받는 중입니다");
        });
      }
    })), 180000);
    return translator;
  }

  async function translatePage(fromClick) {
    var t = await getTranslator(fromClick);
    if (!t) return false;
    setLabel("번역 중…", "번역 중입니다");
    var nodes = textNodes();
    var map = new Map();
    var cache = new Map();
    // A few requests at a time keeps the page responsive.
    var i = 0;
    async function worker() {
      while (i < nodes.length) {
        var node = nodes[i++];
        var text = node.nodeValue;
        var core = text.trim();
        try {
          if (!cache.has(core)) cache.set(core, t.translate(core));
          var out = await cache.get(core);
          map.set(node, text);
          // Keep the surrounding spaces so inline links and code stay separated.
          node.nodeValue = text.slice(0, text.indexOf(core)) + out +
            text.slice(text.indexOf(core) + core.length);
        } catch (e) { /* leave this piece in English */ }
      }
    }
    await Promise.all([worker(), worker(), worker(), worker()]);
    originals = map;
    document.documentElement.lang = TARGET;
    return true;
  }

  function restorePage() {
    if (originals) originals.forEach(function (text, node) { node.nodeValue = text; });
    originals = null;
    document.documentElement.lang = SOURCE;
  }

  function showNote() {
    var note = document.querySelector(".kx-translate-note");
    if (note) { note.remove(); return; }
    note = document.createElement("div");
    note.className = "kx-translate-note";
    note.setAttribute("role", "dialog");
    note.setAttribute("aria-label", "번역 안내");
    note.innerHTML =
      "<p><strong>이 브라우저는 페이지 안 번역을 지원하지 않습니다.</strong><br>" +
      "브라우저의 번역 기능을 사용해 주세요.</p>" +
      "<ul>" +
      "<li><b>Chrome</b>: 페이지에서 오른쪽 클릭 → <em>한국어(으)로 번역</em></li>" +
      "<li><b>Edge</b>: 주소창의 번역 아이콘</li>" +
      "<li><b>Safari</b>: 주소창의 <em>aA</em> → <em>번역</em></li>" +
      "<li><b>휴대폰</b>: 브라우저 메뉴의 <em>번역</em></li>" +
      "</ul>" +
      '<button type="button" class="kx-translate-note__close">닫기</button>';
    note.querySelector("button").addEventListener("click", function () { note.remove(); button.focus(); });
    document.body.appendChild(note);
  }

  async function onClick() {
    if (busy) return;
    if (originals) {
      restorePage();
      store(null);
      showEnglishLabel();
      return;
    }
    if (!("Translator" in self)) { showNote(); return; }
    busy = true;
    try {
      if (await translatePage(true)) { store(TARGET); showKoreanLabel(); }
      else { showEnglishLabel(); showNote(); }
    } catch (e) {
      showEnglishLabel(); showNote();
    } finally {
      busy = false;
    }
  }

  function init() {
    var header = document.querySelector(".md-header__inner");
    if (!header || header.querySelector(".kx-translate")) return;
    button = document.createElement("button");
    button.type = "button";
    button.className = "md-header__button kx-translate";
    button.innerHTML = ICON + '<span class="kx-translate__label"></span>';
    label = button.querySelector(".kx-translate__label");
    showEnglishLabel();
    button.addEventListener("click", onClick);
    header.appendChild(button);

    // Reopen in Korean if the reader chose it before and the model is ready.
    if (stored() === TARGET && "Translator" in self) {
      busy = true;
      translatePage(false)
        .then(function (ok) { ok ? showKoreanLabel() : showEnglishLabel(); })
        .catch(function () { showEnglishLabel(); })
        .finally(function () { busy = false; });
    }
  }

  // Formulas must be typeset before their text is protected, so wait for load.
  if (document.readyState === "complete") init();
  else window.addEventListener("load", init);
})();

// Language menu: the site is written in English only. Other languages open the
// current page through Google Translate's page proxy (<host>.translate.goog),
// so no translated copies have to be maintained.
(function () {
  var ORIGINAL_HOST = "krunyx.com";

  // krunyx.com -> krunyx-com, www.krunyx.com -> www-krunyx-com (Google's proxy naming)
  function toProxyLabel(host) {
    return host.replace(/-/g, "--").replace(/\./g, "-");
  }
  function fromProxyLabel(label) {
    return label.replace(/--/g, "\u0000").replace(/-/g, ".").replace(/\u0000/g, "-");
  }

  function originalHost() {
    var h = location.hostname;
    if (/\.translate\.goog$/.test(h)) return fromProxyLabel(h.replace(/\.translate\.goog$/, ""));
    if (h === "localhost" || h === "127.0.0.1" || h === "") return ORIGINAL_HOST;
    return h;
  }

  function wireLanguageMenu() {
    var host = originalHost();
    var path = location.pathname;
    var links = document.querySelectorAll(".md-select__link[hreflang]");
    links.forEach(function (a) {
      var lang = a.getAttribute("hreflang");
      if (lang === "en") {
        a.href = "https://" + host + path;
      } else {
        a.href = "https://" + toProxyLabel(host) + ".translate.goog" + path +
          "?_x_tr_sl=en&_x_tr_tl=" + encodeURIComponent(lang) +
          "&_x_tr_hl=" + encodeURIComponent(lang);
      }
    });
  }

  // Keep formulas, code and the product name out of machine translation.
  function protectFromTranslation() {
    document.querySelectorAll("pre, code, .arithmatex, mjx-container, .kx-stack__name")
      .forEach(function (el) { el.setAttribute("translate", "no"); });
  }

  function run() { wireLanguageMenu(); protectFromTranslation(); }

  if (typeof document$ !== "undefined") document$.subscribe(run);
  else document.addEventListener("DOMContentLoaded", run);
})();

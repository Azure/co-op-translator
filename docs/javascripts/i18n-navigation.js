(function () {
  var navigation = window.coOpI18n;
  if (!navigation) return;

  var root = new URL(navigation.root);
  var routes = new Map();

  function normalizePath(path) {
    return path.replace(/index\.html$/, "").replace(/\/$/, "");
  }

  Object.keys(navigation.pages).forEach(function (source) {
    var translations = navigation.pages[source];
    Object.keys(translations).forEach(function (language) {
      var url = new URL(translations[language], root);
      routes.set(normalizePath(url.pathname), { source: source, language: language });
    });
  });

  function pageFor(url) {
    return url.origin === root.origin ? routes.get(normalizePath(url.pathname)) : null;
  }

  function markFallback(link, missing) {
    var label = link.querySelector(".i18n-fallback");
    if (missing && !label) {
      label = document.createElement("span");
      label.className = "i18n-fallback";
      label.textContent = " (English)";
      link.appendChild(label);
    } else if (!missing && label) {
      label.remove();
    }
    if (missing) {
      link.setAttribute("title", "This page is not yet translated into the selected language. Opens in English.");
    } else if (label) {
      link.removeAttribute("title");
    }
  }

  function rewriteI18nNavigation() {
    var currentUrl = new URL(window.location.href);
    var current = pageFor(currentUrl);
    if (!current) return;

    document.querySelectorAll(
      ".md-select__link[hreflang], .language-button[hreflang]"
    ).forEach(function (link) {
      var language = link.getAttribute("data-i18n-language") || link.getAttribute("hreflang");
      link.setAttribute("data-i18n-language", language);
      var translations = navigation.pages[current.source];
      var missing = translations[language] === undefined;
      var target = translations[missing ? "en" : language];
      if (target === undefined) return;

      var url = new URL(target, root);
      url.search = currentUrl.search;
      // Translated headings have different IDs. Keep fragments only in the same language.
      if (language === current.language) url.hash = currentUrl.hash;
      link.setAttribute("href", url.href);
      link.setAttribute("hreflang", missing ? "en" : language);
      markFallback(link, missing);
    });

    document.querySelectorAll([
      ".md-nav--primary a.md-nav__link[href]",
      ".md-sidebar--primary a.md-nav__link[href]",
      ".md-tabs a.md-tabs__link[href]",
      ".md-footer a.md-footer__link[href]",
    ].join(",")).forEach(function (link) {
      // The nested table of contents belongs to the current page, not site navigation.
      if (link.closest(".md-nav--secondary")) return;
      var url = new URL(link.getAttribute("href"), currentUrl);
      var page = pageFor(url);
      if (!page) return;
      var translations = navigation.pages[page.source];
      var missing = translations[current.language] === undefined;
      var target = translations[missing ? "en" : current.language];
      if (target === undefined) return;

      var destination = new URL(target, root);
      destination.search = url.search;
      if (page.language === (missing ? "en" : current.language)) destination.hash = url.hash;
      link.setAttribute("href", destination.href);
      markFallback(link, missing);

      var active = page.source === current.source;
      link.classList.toggle("md-nav__link--active", active);
      if (active) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
      var item = link.closest(".md-nav__item");
      if (item) item.classList.toggle("md-nav__item--active", active);
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(rewriteI18nNavigation);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", rewriteI18nNavigation);
  } else {
    rewriteI18nNavigation();
  }
  window.addEventListener("hashchange", rewriteI18nNavigation);
})();

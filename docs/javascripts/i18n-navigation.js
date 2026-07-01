(function () {
  var translatedSlugs = new Set([
    "",
    "workflows",
    "configuration",
    "azure-ai-setup",
    "cli",
    "api",
    "mcp",
    "github-actions",
    "supported-languages",
    "readme-languages-template",
    "troubleshooting",
    "microsoft-beginners",
    "maintainer-guide",
  ]);

  function normalizeSlug(pathPart) {
    var normalized = pathPart.replace(/^\/+|\/+$/g, "");
    if (!normalized || normalized === "index.html") {
      return "";
    }

    var pieces = normalized.split("/");
    if (pieces.length === 1 || (pieces.length === 2 && pieces[1] === "index.html")) {
      return pieces[0];
    }

    return null;
  }

  function getContext() {
    var match = window.location.pathname.match(/^(.*\/i18n\/([^/]+))(?:\/(.*))?$/);
    if (!match) {
      return null;
    }

    var languageRoot = match[1] + "/";
    var rootPrefix = match[1].replace(/\/i18n\/[^/]+$/, "/");
    var currentSlug = normalizeSlug(match[3] || "");

    return {
      languageRoot: languageRoot,
      rootPrefix: rootPrefix,
      currentSlug: currentSlug,
    };
  }

  function getRootSlug(url, rootPrefix) {
    if (url.origin !== window.location.origin || !url.pathname.startsWith(rootPrefix)) {
      return null;
    }

    var pathPart = url.pathname.slice(rootPrefix.length);
    if (pathPart.startsWith("i18n/")) {
      return null;
    }

    var slug = normalizeSlug(pathPart);
    return translatedSlugs.has(slug) ? slug : null;
  }

  function getLanguageSlug(url, languageRoot) {
    if (url.origin !== window.location.origin || !url.pathname.startsWith(languageRoot)) {
      return null;
    }

    var slug = normalizeSlug(url.pathname.slice(languageRoot.length));
    return translatedSlugs.has(slug) ? slug : null;
  }

  function targetPath(languageRoot, slug, url) {
    return languageRoot + (slug ? slug + "/" : "") + url.search + url.hash;
  }

  function rewriteI18nNavigation() {
    var context = getContext();
    if (!context) {
      return;
    }

    var links = document.querySelectorAll(
      [
        ".md-nav--primary a.md-nav__link[href]",
        ".md-sidebar--primary a.md-nav__link[href]",
        ".md-tabs a.md-tabs__link[href]",
        ".md-footer a.md-footer__link[href]",
      ].join(",")
    );

    links.forEach(function (link) {
      link.classList.remove("md-nav__link--active");
      link.removeAttribute("aria-current");

      var navItem = link.closest(".md-nav__item");
      if (navItem) {
        navItem.classList.remove("md-nav__item--active");
      }

      var url = new URL(link.getAttribute("href"), window.location.href);
      var slug = getRootSlug(url, context.rootPrefix);

      if (slug !== null) {
        link.setAttribute("href", targetPath(context.languageRoot, slug, url));
      } else {
        slug = getLanguageSlug(url, context.languageRoot);
      }

      if (slug !== null && slug === context.currentSlug) {
        link.classList.add("md-nav__link--active");
        link.setAttribute("aria-current", "page");
        if (navItem) {
          navItem.classList.add("md-nav__item--active");
        }
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(rewriteI18nNavigation);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", rewriteI18nNavigation);
  } else {
    rewriteI18nNavigation();
  }
})();

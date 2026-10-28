"""Generate bilingual legal-review pages from the four Markdown source documents."""

from __future__ import annotations

import html
import shutil
from pathlib import Path

from markdown import markdown

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "_site"

DOCUMENTS = (
    ("terminos", "TERMINOS.md", "Condiciones del Servicio", "es"),
    ("privacidad", "PRIVACIDAD.md", "Política de Privacidad", "es"),
    ("en/terms", "TERMINOS_EN.md", "Terms of Service", "en"),
    ("en/privacy", "PRIVACIDAD_EN.md", "Privacy Policy", "en"),
)


def page(title: str, body: str, language: str, relative_root: str) -> str:
    t = {
        "es": {
            "notice": "DOCUMENTACIÓN EN REVISIÓN",
            "message": (
                "Esta es una vista previa pública de los documentos legales. "
                "La dirección postal y varios procedimientos operativos requieren "
                "comprobaciones antes de la aprobación definitiva. "
                "No los utilices como condiciones contractuales de producción."
            ),
            "terms": "Términos",
            "privacy": "Privacidad",
            "nav": "Documentos legales",
        },
        "en": {
            "notice": "DOCUMENTS UNDER REVIEW",
            "message": (
                "This is a public preview of the legal documents. The postal address "
                "and some operational processes require verification before final approval. "
                "Do not use this draft as binding production terms."
            ),
            "terms": "Terms",
            "privacy": "Privacy",
            "nav": "Legal documents",
        },
    }[language]
    term_url = f"{relative_root}{'terminos' if language == 'es' else 'en/terms'}/"
    privacy_url = f"{relative_root}{'privacidad' if language == 'es' else 'en/privacy'}/"
    alt_url = f"{relative_root}{'index.html' if language == 'en' else 'en/index.html'}"
    alt_label = "Español" if language == "en" else "English"
    return f"""<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="light">
<title>{html.escape(title)} · Críptico Club</title>
<link rel="stylesheet" href="{relative_root}styles.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="{relative_root}index.html">CRÍPTICO <span>CLUB</span></a>
  <nav aria-label="{t['nav']}">
    <a href="{term_url}">{t['terms']}</a>
    <a href="{privacy_url}">{t['privacy']}</a>
    <a href="{alt_url}" hreflang="{'es' if language == 'en' else 'en'}">{alt_label}</a>
  </nav>
</header>
<main class="page">
  <section class="warning" role="note">
    <strong>{t['notice']}</strong>
    <p>{t['message']}</p>
  </section>
  <article class="document">{body}</article>
</main>
<footer>Críptico Club · <a href="https://github.com/Zerep0/criptico-legal">GitHub</a></footer>
</body>
</html>
"""


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir()
    shutil.copy2(ROOT / "site" / "styles.css", DEST / "styles.css")
    (DEST / ".nojekyll").write_text("", encoding="utf-8")
    for slug, filename, title, lang in DOCUMENTS:
        source = (ROOT / filename).read_text(encoding="utf-8")
        if not source.strip():
            raise ValueError(f"Empty legal source: {filename}")
        dest = DEST / slug
        dest.mkdir(parents=True, exist_ok=True)
        body = markdown(source, extensions=["tables", "fenced_code", "toc", "sane_lists"])
        root = "../" * (len(dest.relative_to(DEST).parts))
        (dest / "index.html").write_text(page(title, body, lang, root), encoding="utf-8")

    for lang, base, prefix in (
        ("es", DEST, ""),
        ("en", DEST / "en", "en/"),
    ):
        texts = {
            "es": ("Documentación legal", "Lee los dos borradores antes de la aprobación definitiva.",
                   "Condiciones del Servicio", "Política de Privacidad"),
            "en": ("Legal documents", "Read both drafts before final approval.",
                   "Terms of Service", "Privacy Policy"),
        }[lang]
        body = (
            f"<h1>{texts[0]}</h1><p>{texts[1]}</p>"
            f'<div class="tiles">'
            f'<a class="tile" href="{"" if lang == "es" else "../"}{"terminos/" if lang == "es" else "terms/"}"><strong>{texts[2]}</strong><span>Read / Leer →</span></a>'
            f'<a class="tile" href="{"" if lang == "es" else "../"}{"privacidad/" if lang == "es" else "privacy/"}"><strong>{texts[3]}</strong><span>Read / Leer →</span></a>'
            "</div>"
        )
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(page(texts[0], body, lang, "../" if lang == "en" else ""), encoding="utf-8")
    print(f"Built bilingual review site: {len(DOCUMENTS)} legal pages")


if __name__ == "__main__":
    main()

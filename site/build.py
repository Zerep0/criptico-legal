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
    is_terms = title in ("Terms of Service", "Condiciones del Servicio")
    is_privacy = title in ("Privacy Policy", "Política de Privacidad")
    if is_terms:
        english_document_url = f"{relative_root}en/terms/"
        spanish_document_url = f"{relative_root}terminos/"
    elif is_privacy:
        english_document_url = f"{relative_root}en/privacy/"
        spanish_document_url = f"{relative_root}privacidad/"
    else:
        english_document_url = f"{relative_root}index.html"
        spanish_document_url = f"{relative_root}es/"
    language_switch = (
        f'<div class="locale-switch" role="group" aria-label="Document language / Idioma">'
        f'<a class="{"active" if language == "en" else ""}" href="{english_document_url}" '
        f'lang="en" aria-current="{"page" if language == "en" else "false"}">EN</a>'
        f'<a class="{"active" if language == "es" else ""}" href="{spanish_document_url}" '
        f'lang="es" aria-current="{"page" if language == "es" else "false"}">ES</a>'
        "</div>"
    )
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
    {language_switch}
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

    # The default landing page is English; Spanish is available at /es/.
    for lang, base in (("en", DEST), ("es", DEST / "es")):
        texts = {
            "es": ("Documentación legal", "Lee los dos borradores antes de la aprobación definitiva.",
                   "Condiciones del Servicio", "Política de Privacidad"),
            "en": ("Legal documents", "Read both drafts before final approval.",
                   "Terms of Service", "Privacy Policy"),
        }[lang]
        terms_href = "en/terms/" if lang == "en" else "../terminos/"
        privacy_href = "en/privacy/" if lang == "en" else "../privacidad/"
        body = (
            f"<h1>{texts[0]}</h1><p>{texts[1]}</p>"
            f'<div class="tiles">'
            f'<a class="tile" href="{terms_href}"><strong>{texts[2]}</strong><span>Read / Leer →</span></a>'
            f'<a class="tile" href="{privacy_href}"><strong>{texts[3]}</strong><span>Read / Leer →</span></a>'
            "</div>"
        )
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(
            page(texts[0], body, lang, "../" if lang == "es" else ""),
            encoding="utf-8",
        )
    print(f"Built bilingual review site: {len(DOCUMENTS)} legal pages")


if __name__ == "__main__":
    main()
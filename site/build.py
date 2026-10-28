"""Genera una vista previa pública a partir de los Markdown fuente, sin duplicarlos."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from markdown import markdown

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "_site"
BASE = "/criptico-legal"

DOCUMENTS = {
    "terminos": ("TERMINOS.md", "Condiciones del Servicio"),
    "privacidad": ("PRIVACIDAD.md", "Política de Privacidad"),
}


def page(title: str, body: str, relative_root: str = "") -> str:
    safe_title = html.escape(title)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="light">
<title>{safe_title} · Críptico Club</title>
<link rel="stylesheet" href="{relative_root}styles.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="{relative_root}index.html">CRÍPTICO <span>CLUB</span></a>
  <nav aria-label="Documentos legales">
    <a href="{relative_root}terminos/">Términos</a>
    <a href="{relative_root}privacidad/">Privacidad</a>
  </nav>
</header>
<main class="page">
  <section class="warning" role="note" aria-label="Borrador en revisión">
    <strong>DOCUMENTACIÓN EN REVISIÓN</strong>
    <p>Esta es una vista previa pública de los borradores. Todavía contienen puntos de
    verificación y no deben presentarse como la versión legal definitiva ni usarse
    para recabar una aceptación contractual en producción.</p>
  </section>
  <article class="document">{body}</article>
</main>
<footer>Críptico Club · <a href="https://github.com/Zerep0/criptico-legal">Repositorio de documentos</a></footer>
</body>
</html>
"""


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir()
    shutil.copy2(ROOT / "site" / "styles.css", DEST / "styles.css")
    (DEST / ".nojekyll").write_text("", encoding="utf-8")

    tiles = []
    for slug, (filename, title) in DOCUMENTS.items():
        source = (ROOT / filename).read_text(encoding="utf-8")
        if not source.strip():
            raise ValueError(f"Documento vacío: {filename}")
        # Se respetan los marcadores de revisión: nunca declarar que son textos finales.
        body = markdown(source, extensions=["tables", "fenced_code", "toc", "sane_lists"])
        folder = DEST / slug
        folder.mkdir()
        (folder / "index.html").write_text(
            page(title, body, relative_root="../"), encoding="utf-8"
        )
        tiles.append(
            f'<a class="tile" href="{slug}/"><strong>{html.escape(title)}</strong>'
            "<span>Leer borrador →</span></a>"
        )

    index_body = (
        "<h1>Documentación legal</h1>"
        "<p>Revisa los borradores en español antes de la publicación definitiva.</p>"
        '<div class="tiles">' + "".join(tiles) + "</div>"
    )
    (DEST / "index.html").write_text(
        page("Documentación legal", index_body), encoding="utf-8"
    )
    print(f"Sitio de revisión generado en {DEST} con {len(DOCUMENTS)} documentos")


if __name__ == "__main__":
    main()

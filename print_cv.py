"""
Gera PDF do Curriculo-Wesley-Pleno.html preservando 100% do visual do navegador.

Usa Playwright (Chromium headless) — o mesmo motor do Chrome —
então grid, gradientes, SVG, fontes e cores saem idênticos ao preview.

Setup (uma vez):
    pip install playwright
    python -m playwright install chromium

Uso:
    python print_cv.py              # 1 página única (altura = altura real do conteúdo)
    python print_cv.py --a4         # multipágina A4 com quebras CSS naturais
    python print_cv.py --out caminho.pdf
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit(
        "X Playwright nao instalado.\n"
        "   pip install playwright\n"
        "   python -m playwright install chromium"
    )

def _count_pdf_pages(pdf_path: Path) -> int | None:
    """Conta paginas do PDF gerado; None se nao der pra verificar."""
    try:
        from pypdf import PdfReader
        return len(PdfReader(str(pdf_path)).pages)
    except Exception:
        try:
            # fallback sem dependencia: conta objetos /Type /Page no bruto
            raw = pdf_path.read_bytes()
            n = raw.count(b"/Type /Page") - raw.count(b"/Type /Pages")
            return n if n > 0 else None
        except Exception:
            return None


HERE = Path(__file__).resolve().parent
HTML_DEFAULT = HERE / "Curriculo-Wesley-Pleno.html"
PDF_DEFAULT = HERE / "Wesley-Correia-CV.pdf"

# A4 em pixels CSS (96 DPI)
A4_W_PX = 794   # 210mm
A4_H_PX = 1123  # 297mm
PX_TO_MM = 25.4 / 96


def render(html_path: Path, pdf_path: Path, mode: str = "single") -> tuple[Path, str]:
    if not html_path.exists():
        sys.exit(f"X HTML nao encontrado: {html_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": A4_W_PX, "height": A4_H_PX},
            device_scale_factor=2,  # nitidez retina
        )
        page = ctx.new_page()
        page.goto(html_path.absolute().as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")

        # Garante que fontes e imagens terminaram de carregar
        page.evaluate("async () => { await document.fonts.ready; }")

        if mode == "single":
            measure_js = """() => {
                const el = document.querySelector('.page');
                return Math.max(
                    el.scrollHeight,
                    el.getBoundingClientRect().height,
                    document.documentElement.scrollHeight,
                    document.body.scrollHeight
                );
            }"""

            # 1) libera a altura ANTES de medir — o @page custom entra depois,
            #    mas medir com height:auto evita divergencia entre a medicao e
            #    o layout final de impressao.
            page.add_style_tag(
                content=(
                    "html, body, .page { height: auto !important; } "
                    ".page { min-height: 0 !important; }"
                )
            )
            page.wait_for_timeout(50)

            # 2) gera o PDF numa dada altura e conta as paginas.
            #    injeta @page runtime sobrescrevendo o A4 do CSS estatico —
            #    sem isso, o @page { size: A4 } do <style> forca paginacao A4
            #    mesmo quando pedimos altura custom na API.
            def gen_pdf(h_px: int) -> int | None:
                h_mm = h_px * PX_TO_MM
                page.add_style_tag(
                    content=f"@page {{ size: 210mm {h_mm:.3f}mm; margin: 0; }}"
                )
                page.wait_for_timeout(30)
                page.pdf(
                    path=str(pdf_path),
                    prefer_css_page_size=True,  # honra o @page que injetamos
                    print_background=True,
                    margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                )
                return _count_pdf_pages(pdf_path)

            content_h_px = max(int(page.evaluate(measure_js)), A4_H_PX)

            # o fragmentador de impressao do Chromium nao corta blocos com
            # break-inside: avoid — se o conteudo passar da pagina por 1px,
            # o bloco inteiro vai pra uma 2a pagina. Garante 1 pagina primeiro:
            hi = content_h_px + 4
            n_pages = gen_pdf(hi)
            while n_pages is not None and n_pages > 1:
                hi += 16
                n_pages = gen_pdf(hi)

            # o layout de impressao costuma sair um pouco mais curto que o de
            # tela (onde medimos), sobrando faixa branca no rodape. Busca
            # binaria pela MENOR altura que ainda cabe em 1 pagina — se
            # encolher demais, nasce uma 2a pagina e a busca recua.
            if n_pages == 1:
                lo = max(A4_H_PX, content_h_px - 160)
                best = hi
                while hi - lo > 4:
                    mid = (lo + hi) // 2
                    if gen_pdf(mid) == 1:
                        hi = best = mid
                    else:
                        lo = mid
                n_pages = gen_pdf(best)  # regera na melhor altura encontrada
                page_h_px = best
            else:
                page_h_px = hi
            content_h_mm = page_h_px * PX_TO_MM

            info = (
                f"modo: single page  |  pagina: 210mm x {content_h_mm:.0f}mm  "
                f"({page_h_px}px, medido {content_h_px}px)"
            )
            if n_pages is not None:
                info += f"  |  paginas no PDF: {n_pages}"
        else:
            page.pdf(
                path=str(pdf_path),
                format="A4",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                prefer_css_page_size=True,
            )
            info = "modo: A4 multipagina (quebras CSS naturais)"

        browser.close()

    return pdf_path, info


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Renderiza o curriculo HTML em PDF via Chromium headless"
    )
    parser.add_argument(
        "--a4",
        action="store_true",
        help="gera em A4 multipagina (padrao = 1 pagina unica com altura custom)",
    )
    parser.add_argument(
        "--html",
        type=Path,
        default=HTML_DEFAULT,
        help=f"HTML de entrada (padrao: {HTML_DEFAULT.name})",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=PDF_DEFAULT,
        help=f"PDF de saida (padrao: {PDF_DEFAULT.name})",
    )
    args = parser.parse_args()

    mode = "a4" if args.a4 else "single"
    out, info = render(args.html, args.out, mode=mode)
    print(f"OK PDF gerado: {out}")
    print(f"   {info}")


if __name__ == "__main__":
    main()

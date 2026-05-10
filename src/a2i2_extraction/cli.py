"""CLI entry points for one-off operations.

Run via:
    uv run python -m a2i2_extraction.cli dry-run --paper data/papers/1
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from .clients import MinerULocalClient
from .pipeline import _resolve_paper_files
from .preprocessing import clean_text, trim_references
from .prompts import build_extraction_prompt


def _word_count(text: str) -> int:
    return len(text.split())


async def _dry_run(paper_dir: Path, output_dir: Path) -> None:
    """Run parse + prompt assembly. Stop BEFORE the LLM call.

    Writes the assembled prompt and per-document parsed text to
    `outputs/dry_runs/<paper_dir.name>/` so the user can inspect what would
    be sent to the model.
    """
    import time

    main_pdf, si_pdf = _resolve_paper_files(paper_dir)

    # MinerU writes its raw output (markdown + images) to a per-paper subdir
    # so figure files persist for Phase 2 vision routing.
    out = output_dir / "dry_runs" / paper_dir.name
    out.mkdir(parents=True, exist_ok=True)
    parser = MinerULocalClient(output_root=out / "mineru_raw")

    t0 = time.monotonic()
    print(f"[parse] main: {main_pdf.name}")
    main_doc = await parser.parse(main_pdf)
    t_main = time.monotonic() - t0
    print(f"[parse]   ({t_main:.1f}s, {len(main_doc.figures)} figures)")

    si_doc = None
    if si_pdf:
        t1 = time.monotonic()
        print(f"[parse] SI:   {si_pdf.name}")
        si_doc = await parser.parse(si_pdf)
        t_si = time.monotonic() - t1
        print(f"[parse]   ({t_si:.1f}s, {len(si_doc.figures)} figures)")
    else:
        print("[parse] SI:   (none found)")

    raw_main, raw_si = main_doc.text, (si_doc.text if si_doc else None)
    main_text = trim_references(clean_text(raw_main))
    si_text = trim_references(clean_text(raw_si)) if raw_si else None

    prompt = build_extraction_prompt(paper_text=main_text, si_text=si_text)

    (out / "main_text.md").write_text(main_text, encoding="utf-8")
    if si_text:
        (out / "si_text.md").write_text(si_text, encoding="utf-8")
    (out / "prompt.txt").write_text(prompt, encoding="utf-8")

    # Rough token estimate: ~4 chars/token for English+chemistry mix.
    est_tokens = len(prompt) // 4
    raw_total = len(raw_main) + (len(raw_si) if raw_si else 0)
    clean_total = len(main_text) + (len(si_text) if si_text else 0)
    pct_kept = (clean_total / raw_total * 100) if raw_total else 0

    print()
    print("=" * 60)
    print(f"raw text:    {raw_total:>10,} chars")
    print(f"after clean+trim: {clean_total:>10,} chars  ({pct_kept:5.1f}% kept)")
    print(f"main text:   {len(main_text):>10,} chars   {_word_count(main_text):>8,} words")
    if si_text:
        print(f"SI text:     {len(si_text):>10,} chars   {_word_count(si_text):>8,} words")
    print(f"full prompt: {len(prompt):>10,} chars  (~{est_tokens:>7,} tokens)")
    print("=" * 60)
    print(f"written to: {out}/")
    print("  - main_text.md    (cleaned + trimmed markdown)")
    if si_text:
        print("  - si_text.md      (cleaned + trimmed SI markdown)")
    print("  - prompt.txt      (what would go to the LLM)")
    print(f"  - mineru_raw/     (raw MinerU output incl. {len(main_doc.figures) + (len(si_doc.figures) if si_doc else 0)} figure images)")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="a2i2_extraction.cli")
    sub = p.add_subparsers(dest="cmd", required=True)

    dr = sub.add_parser(
        "dry-run",
        help="parse PDFs and assemble the prompt; do NOT call the LLM",
    )
    dr.add_argument("--paper", type=Path, required=True, help="paper directory")
    dr.add_argument("--output-dir", type=Path, default=Path("outputs"))
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.cmd == "dry-run":
        if not args.paper.is_dir():
            print(f"error: {args.paper} is not a directory", file=sys.stderr)
            return 2
        asyncio.run(_dry_run(args.paper, args.output_dir))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

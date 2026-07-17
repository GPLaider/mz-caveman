#!/usr/bin/env python3
"""Measure plain / caveman / mz / mzu variants with cl100k_base tokens."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

try:
    import tiktoken
except ImportError:
    print("pip install tiktoken", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parent
VARIANTS = ROOT / "variants"
RESULTS = ROOT / "results"
MODES = ("plain", "caveman", "mz", "mzu")
ENC = tiktoken.get_encoding("cl100k_base")


@dataclass
class Row:
    case: str
    mode: str
    chars: int
    lines: int
    tokens: int
    token_ratio_vs_plain: float
    char_ratio_vs_plain: float
    token_saved_pct: float
    char_saved_pct: float


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def measure(text: str) -> tuple[int, int, int]:
    chars = len(text)
    lines = text.count("\n") if text.endswith("\n") else text.count("\n") + 1
    tokens = len(ENC.encode(text))
    return chars, lines, tokens


def main() -> int:
    rows: list[Row] = []
    cases = sorted(p.name for p in VARIANTS.iterdir() if p.is_dir())
    if not cases:
        print("no cases under variants/", file=sys.stderr)
        return 1

    for case in cases:
        cdir = VARIANTS / case
        plain_path = cdir / "plain.txt"
        if not plain_path.exists():
            print(f"skip {case}: no plain.txt", file=sys.stderr)
            continue
        plain_text = read_text(plain_path)
        p_chars, _, p_tokens = measure(plain_text)

        for mode in MODES:
            path = cdir / f"{mode}.txt"
            if not path.exists():
                print(f"missing {path}", file=sys.stderr)
                return 1
            text = read_text(path)
            chars, lines, tokens = measure(text)
            tr = tokens / p_tokens if p_tokens else 0.0
            cr = chars / p_chars if p_chars else 0.0
            rows.append(
                Row(
                    case=case,
                    mode=mode,
                    chars=chars,
                    lines=lines,
                    tokens=tokens,
                    token_ratio_vs_plain=round(tr, 4),
                    char_ratio_vs_plain=round(cr, 4),
                    token_saved_pct=round((1.0 - tr) * 100.0, 1),
                    char_saved_pct=round((1.0 - cr) * 100.0, 1),
                )
            )

    # totals per mode
    totals: dict[str, dict[str, float]] = {}
    for mode in MODES:
        mrows = [r for r in rows if r.mode == mode]
        totals[mode] = {
            "tokens": sum(r.tokens for r in mrows),
            "chars": sum(r.chars for r in mrows),
            "cases": len(mrows),
        }
    plain_tok = totals["plain"]["tokens"]
    plain_chr = totals["plain"]["chars"]
    summary = {}
    for mode in MODES:
        t = totals[mode]["tokens"]
        c = totals[mode]["chars"]
        summary[mode] = {
            "tokens": int(t),
            "chars": int(c),
            "token_ratio_vs_plain": round(t / plain_tok, 4) if plain_tok else None,
            "char_ratio_vs_plain": round(c / plain_chr, 4) if plain_chr else None,
            "token_saved_pct": round((1 - t / plain_tok) * 100, 1) if plain_tok else None,
            "char_saved_pct": round((1 - c / plain_chr) * 100, 1) if plain_chr else None,
        }

    RESULTS.mkdir(parents=True, exist_ok=True)
    payload = {
        "meta": {
            "encoding": "cl100k_base",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "cases": cases,
            "modes": list(MODES),
            "note": (
                "Variants are curated reference rewrites for style bench, "
                "not live model samples. Token counts use OpenAI cl100k_base."
            ),
        },
        "summary": summary,
        "rows": [asdict(r) for r in rows],
    }
    json_path = RESULTS / "latest.json"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = render_md(payload, rows)
    md_path = RESULTS / "LATEST.md"
    md_path.write_text(md, encoding="utf-8")

    print(md)
    print(f"\nWrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


def render_md(payload: dict, rows: list[Row]) -> str:
    s = payload["summary"]
    lines = [
        "# MZ Caveman compression bench",
        "",
        f"- Encoding: `{payload['meta']['encoding']}`",
        f"- Cases: {len(payload['meta']['cases'])}",
        f"- Generated: `{payload['meta']['generated_at']}`",
        "",
        payload["meta"]["note"],
        "",
        "## Totals vs plain",
        "",
        "| Mode | Tokens | Chars | Token saved | Char saved | vs plain (tokens) |",
        "|------|-------:|------:|------------:|-----------:|------------------:|",
    ]
    for mode in MODES:
        m = s[mode]
        lines.append(
            f"| **{mode}** | {m['tokens']} | {m['chars']} | "
            f"{m['token_saved_pct']}% | {m['char_saved_pct']}% | "
            f"{m['token_ratio_vs_plain']:.2%} |"
        )

    lines += [
        "",
        "## Per case",
        "",
        "| Case | plain | caveman | mz | mzu | caveman save | mz save | mzu save |",
        "|------|------:|--------:|---:|----:|-------------:|--------:|---------:|",
    ]
    cases = payload["meta"]["cases"]
    by = {(r.case, r.mode): r for r in rows}
    for case in cases:
        p = by[(case, "plain")].tokens
        c = by[(case, "caveman")].tokens
        mz = by[(case, "mz")].tokens
        mzu = by[(case, "mzu")].tokens
        lines.append(
            f"| `{case}` | {p} | {c} | {mz} | {mzu} | "
            f"{(1 - c / p) * 100:.1f}% | {(1 - mz / p) * 100:.1f}% | {(1 - mzu / p) * 100:.1f}% |"
        )

    lines += [
        "",
        "## Reading guide",
        "",
        "- **plain**: normal agent prose (baseline)",
        "- **caveman**: pure collapse, no MZ stamps",
        "- **mz**: collapse + one 피식 verdict (identity)",
        "- **mzu**: comedy spam — may use *more* tokens than mz/caveman; humor tax",
        "",
        "If mzu tokens > plain: expected for chaos mode. Ultra optimizes 피식 density, not always length.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())

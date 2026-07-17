# MZ Caveman compression bench

- Encoding: `cl100k_base`
- Cases: 6
- Generated: `2026-07-17T08:15:25.060167+00:00`

Primary variants come from live parallel subagent sessions (see benchmarks/sessions/MANIFEST.json). Token counts use OpenAI cl100k_base via tiktoken.

## Totals vs plain

| Mode | Tokens | Chars | Token saved | Char saved | vs plain (tokens) |
|------|-------:|------:|------------:|-----------:|------------------:|
| **plain** | 758 | 884 | 0.0% | 0.0% | 100.00% |
| **caveman** | 587 | 650 | 22.6% | 26.5% | 77.44% |
| **mz** | 586 | 635 | 22.7% | 28.2% | 77.31% |
| **mzu** | 326 | 372 | 57.0% | 57.9% | 43.01% |
| **mze** | 1059 | 1079 | -39.7% | -22.1% | 139.71% |

## Per case (tokens)

| Case | plain | caveman | mz | mzu | mze |
|------|------:|--------:|---:|----:|----:|
| `01-release-block` | 150 | 114 | 114 | 60 | 193 |
| `02-integ-fail` | 127 | 88 | 84 | 60 | 168 |
| `03-flaky-windows` | 99 | 75 | 79 | 53 | 156 |
| `04-perf-temptation` | 141 | 116 | 105 | 49 | 197 |
| `05-go-nogo-role` | 106 | 91 | 100 | 45 | 169 |
| `06-cache-bloat` | 135 | 103 | 104 | 59 | 176 |

## Reading guide

- **plain**: baseline prose
- **caveman**: pure collapse
- **mz**: default — one 피식 verdict
- **mzu**: ultra short+funny (replace) — target tokens < plain
- **mze**: extreme spam — laugh first; tokens may rise

# MZ Caveman compression bench

- Encoding: `cl100k_base`
- Cases: 6
- Generated: `2026-07-17T07:36:14.059305+00:00`

Variants are curated reference rewrites for style bench, not live model samples. Token counts use OpenAI cl100k_base.

## Totals vs plain

| Mode | Tokens | Chars | Token saved | Char saved | vs plain (tokens) |
|------|-------:|------:|------------:|-----------:|------------------:|
| **plain** | 752 | 880 | 0.0% | 0.0% | 100.00% |
| **caveman** | 338 | 446 | 55.1% | 49.3% | 44.95% |
| **mz** | 319 | 389 | 57.6% | 55.8% | 42.42% |
| **mzu** | 620 | 620 | 17.6% | 29.5% | 82.45% |

## Per case

| Case | plain | caveman | mz | mzu | caveman save | mz save | mzu save |
|------|------:|--------:|---:|----:|-------------:|--------:|---------:|
| `01-release-block` | 145 | 66 | 55 | 115 | 54.5% | 62.1% | 20.7% |
| `02-integ-fail` | 127 | 60 | 64 | 109 | 52.8% | 49.6% | 14.2% |
| `03-flaky-windows` | 99 | 45 | 45 | 91 | 54.5% | 54.5% | 8.1% |
| `04-perf-temptation` | 139 | 56 | 54 | 120 | 59.7% | 61.2% | 13.7% |
| `05-go-nogo-role` | 106 | 43 | 40 | 79 | 59.4% | 62.3% | 25.5% |
| `06-cache-bloat` | 136 | 68 | 61 | 106 | 50.0% | 55.1% | 22.1% |

## Reading guide

- **plain**: normal agent prose (baseline)
- **caveman**: pure collapse, no MZ stamps
- **mz**: collapse + one 피식 verdict (identity)
- **mzu**: comedy spam — may use *more* tokens than mz/caveman; humor tax

If mzu tokens > plain: expected for chaos mode. Ultra optimizes 피식 density, not always length.

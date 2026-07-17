# MZ Caveman compression bench

- Encoding: `cl100k_base`
- Cases: 6
- Generated: `2026-07-17T07:37:50.154906+00:00`

Primary variants come from live parallel subagent sessions (see benchmarks/sessions/MANIFEST.json). Token counts use OpenAI cl100k_base via tiktoken.

## Totals vs plain

| Mode | Tokens | Chars | Token saved | Char saved | vs plain (tokens) |
|------|-------:|------:|------------:|-----------:|------------------:|
| **plain** | 758 | 884 | 0.0% | 0.0% | 100.00% |
| **caveman** | 587 | 650 | 22.6% | 26.5% | 77.44% |
| **mz** | 586 | 635 | 22.7% | 28.2% | 77.31% |
| **mzu** | 1059 | 1079 | -39.7% | -22.1% | 139.71% |

## Per case

| Case | plain | caveman | mz | mzu | caveman save | mz save | mzu save |
|------|------:|--------:|---:|----:|-------------:|--------:|---------:|
| `01-release-block` | 150 | 114 | 114 | 193 | 24.0% | 24.0% | -28.7% |
| `02-integ-fail` | 127 | 88 | 84 | 168 | 30.7% | 33.9% | -32.3% |
| `03-flaky-windows` | 99 | 75 | 79 | 156 | 24.2% | 20.2% | -57.6% |
| `04-perf-temptation` | 141 | 116 | 105 | 197 | 17.7% | 25.5% | -39.7% |
| `05-go-nogo-role` | 106 | 91 | 100 | 169 | 14.2% | 5.7% | -59.4% |
| `06-cache-bloat` | 135 | 103 | 104 | 176 | 23.7% | 23.0% | -30.4% |

## Reading guide

- **plain**: normal agent prose (baseline)
- **caveman**: pure collapse, no MZ stamps
- **mz**: collapse + one 피식 verdict (identity)
- **mzu**: comedy spam — often *more* tokens; **spam tax**, not humor tax
- **mz** proves short+funny: collapse first, one verdict replaces long prose

If mzu tokens > plain: expected for chaos mode. Ultra optimizes 피식 density, not length.
Short+funny target = `mz` (or disciplined one-liner), not `mzu`.

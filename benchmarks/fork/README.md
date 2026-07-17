# Fork / ultra short+funny experiment

## Naming after remap (2026-07-17)

| Old name | New name |
|----------|----------|
| mzu-short (쇼츠) | **`mzu`** (ultra) |
| freeze mzu 난사 | **`mze`** (extreme) |

## Law (user)

> 줄이면서 웃기게. **안 웃기면 패치하지 말 것** (extreme 웃김 보호)

`/mze` laugh identity must not be nerfed to win compression.

## Freeze (gold laugh)

`../sessions/freeze-ultra-2026-07-17/` — prior live `mzu` dump (laugh density reference).

## Live arms (this run)

| Arm | Subagent ID | Role |
|-----|-------------|------|
| mzf | `019f6f14-34ed-7753-ab27-6007d5a19d91` | short+funny fork |
| mzu-control | `019f6f14-34ee-7960-bff6-070b1f97d13e` | max laugh control |
| mzu-short | `019f6f14-8c14-7d62-9bd7-b1e47cd914a0` | ultra + length budget |

## Gate result

See [`GATE.json`](./GATE.json).

| | Tokens | vs plain | Laugh /12 |
|--|-------:|---------:|----------:|
| plain | 752 | 0% | — |
| freeze-mzu | 1059 | +40.8% | **12** (identity) |
| mzu-short | 326 | **−56.6%** | **7** (fail) |
| mzf | 468 | −37.8% | 9 |

### Decision: **`NO_PATCH_ULTRA`**

- `mzu-short` wins length hard (−56.6%).
- Laugh collapses: cases 02/03/05 weak, **06 dry (0)**.
- Gate needed ≥10/12 and min case ≥1 → **fail**.
- Therefore **do not change** `SKILL.md` ultra / `/mzu` rules.

Short+funny remains a **research fork** under `mzf/` + `mzu-short/`, not main ultra.

## When to patch ultra later

Only if a new live run gets:

1. tokens < plain (all cases or total)
2. laugh_total ≥ 10/12 vs freeze vibe
3. no case laugh = 0
4. still feels like meme chaos, not dry telegram

# MZ Caveman

**짧은데 피식하게.**  
Caveman = short. MZ Caveman = short **and** makes you go 피식.

Not a slang dictionary skill. A **sentence-collapse engine** with one optional meme-like verdict line.  
Optional chaos mode: **`/mzu`** — max MZ spam, barely work-usable on purpose.

Inspired by [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (token compression).  
MZ layer = Korean Gen-Z / 2026 stamp culture + judgment one-liners.

| Mode | Grok | Codex | Vibe |
|------|------|-------|------|
| **default** | `/mz` | **`$mz`** · `$mz-caveman` | Collapse + **one** 판정 한 줄 |
| **ultra** | `/mzu` · `/mz ultra` | **`$mzu`** · `$mz-caveman` + ultra | MZ 난사. Comedy chaos. |
| **off** | `stop mz` · `normal mode` | same | Normal prose |

### Codex: `/mzu` 치면 터짐 (국룰)

Codex **built-in slash** ≠ skill.  
`/mzu` → `Unrecognized command` = **정상**. 스킬 없음 아님.

```text
# 맞음 (Codex)
$mzu
$mz
$mz-caveman

# 틀림 (Codex slash — 거부됨)
/mzu
```

Grok 쪽은 `/mz` · `/mzu` slash OK.

> Identity is the **last line**, not Core 40.  
> `감으로 패치? 컷.` — few tokens, full info, memorable.

## Compression bench (6 cases · cl100k_base)

Curated reference rewrites — not live API samples. Re-run: `python benchmarks/run.py`  
Full tables: [`benchmarks/results/LATEST.md`](./benchmarks/results/LATEST.md)

### Totals vs plain

| Mode | Tokens | Token saved | Char saved | Role |
|------|-------:|------------:|-----------:|------|
| **plain** | 752 | 0% | 0% | baseline agent prose |
| **caveman** | 338 | **55.1%** | 49.3% | pure collapse |
| **mz** | 319 | **57.6%** | 55.8% | collapse + 피식 1 |
| **mzu** | 620 | **17.6%** | 29.5% | 난사 — humor tax |

**Takeaway:** `mz` ≈ caveman on length (often a bit tighter) **and** adds memory/humor.  
`mzu` is **not** a compression mode — 피식 밀도 최적화. 토큰 아끼려면 `/mz`, 웃기려면 `/mzu`.

### Side-by-side (`02-integ-fail`)

**plain** (127 tok)

```text
실패한 통합 테스트 4개를 즉시 분류해야 합니다.
동일한 원인인지, 코드 회귀인지, 환경 문제인지 확인하십시오.
실패 로그와 재현 명령을 반드시 보존하고, 원인을 확인하기 전에 추측으로 수정하지 마십시오.
skip으로 통과시킨 것처럼 보이게 만들지 마십시오.
```

**caveman** (60 tok · −52.8%)

```text
통합테스트 4개 분류.
회귀 / 환경 / 동일원인 판별.
로그·재현명령 보존.
원인 전 수정 금지. skip 통과 금지.
```

**mz** (64 tok · −49.6%)

```text
통합테스트 4개 분류.
회귀 / 환경 / 동일원인 판별.
로그·재현명령 보존.
감으로 패치? 컷.
skip 승리법 금지.
```

**mzu** (109 tok · −14.2%)

```text
샤갈. 통합테스트 4명 사망 ㄹㅇ.
회귀/환경/동일원인 판별 국룰 드가자.
로그·재현 존버 보존. 감패치 각? 스불재 예약.
컷 정배. skip 승리법 뇌절 금지. 야르 아님.
```

### Per-case token save

| Case | caveman | mz | mzu |
|------|--------:|---:|----:|
| release-block | 54.5% | **62.1%** | 20.7% |
| integ-fail | 52.8% | 49.6% | 14.2% |
| flaky-windows | 54.5% | 54.5% | 8.1% |
| perf-temptation | 59.7% | **61.2%** | 13.7% |
| go-nogo-role | 59.4% | **62.3%** | 25.5% |
| cache-bloat | 50.0% | **55.1%** | 22.1% |

Variants live under [`benchmarks/variants/`](./benchmarks/variants/).

## Quick install

### Grok

```powershell
# Windows
git clone https://github.com/GPLaider/mz-caveman.git
Copy-Item -Recurse mz-caveman\skills\mz-caveman $env:USERPROFILE\.grok\skills\mz-caveman
```

```bash
# macOS / Linux
git clone https://github.com/GPLaider/mz-caveman.git
cp -R mz-caveman/skills/mz-caveman ~/.grok/skills/mz-caveman
```

Slash: `/mz` · `/mzu`

### Codex

```powershell
git clone https://github.com/GPLaider/mz-caveman.git
New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.codex\skills\mz-caveman\agents | Out-Null
Copy-Item mz-caveman\skills\mz-caveman\SKILL.md $env:USERPROFILE\.codex\skills\mz-caveman\SKILL.md
Copy-Item mz-caveman\agents\openai.yaml $env:USERPROFILE\.codex\skills\mz-caveman\agents\openai.yaml
```

```bash
git clone https://github.com/GPLaider/mz-caveman.git
mkdir -p ~/.codex/skills/mz-caveman/agents
cp mz-caveman/skills/mz-caveman/SKILL.md ~/.codex/skills/mz-caveman/SKILL.md
cp mz-caveman/agents/openai.yaml ~/.codex/skills/mz-caveman/agents/openai.yaml
```

Codex: **`$mz`** · **`$mzu`** · `$mz-caveman`  
(폴더 3개: `skills/mz`, `skills/mzu`, `skills/mz-caveman`)

See [INSTALL.md](./INSTALL.md) for details.

## What it does

### Compression priority (fixed)

1. Delete sentences  
2. Kill duplicates  
3. Structural collapse → noun phrases / labels  
4. **Verdict line** (0~1 default · spam in ultra)  
5. Drop particles / filler  

### Default example

```text
원인 미확인.

감으로 패치? 컷.
```

### Ultra example

```text
샤갈. 원인 알빠노 상태에서 감패치 각? ㄹㅇ 스불재 예약. 컷 정배. 드가자(조사만).
```

### Never trade facts for memes

```text
# keep
Go/No-Go: RM·On-call.

# lose info — forbidden
온콜 정배.
```

Hard floors: code blocks, CLI, errors, commit/PR bodies, security/data-loss warnings stay clean (auto-clarity).

## Repo layout

```text
SKILL.md                      # canonical (same as skills/mz-caveman/)
skills/mz-caveman/            # full skill
skills/mz/                    # Codex alias → $mz (default)
skills/mzu/                   # Codex alias → $mzu (ultra)
agents/openai.yaml            # Codex UI for mz-caveman
benchmarks/                   # plain/caveman/mz/mzu + run.py
benchmarks/results/LATEST.md  # latest compression table
INSTALL.md
LICENSE
```

## Core 40

Seasoning only (default). Magazine (ultra). Full table + lexicon in [`SKILL.md`](./SKILL.md).

2026 front line: **밤티 · 야르 · 샤갈 · 아자스** + still-active high-compression memes.  
No blog-zombie neologism bloat.

## License

MIT — see [LICENSE](./LICENSE).

## Note

`caveman ultra` (pure short) ≠ `mz ultra` / `/mzu` (meme chaos).

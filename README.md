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

## Compression bench (live 4-subagent · cl100k_base)

**Not hand-fiction.** Four parallel `general-purpose` subagent sessions rewrote the same 6 fixtures:

| Mode | Subagent ID | Duration |
|------|-------------|----------|
| plain | `019f6f01-fba3-7451-b844-fa21c62ca87b` | 5.5s |
| caveman | `019f6f01-fba4-7082-b65d-3585db9b201e` | 9.2s |
| mz | `019f6f01-fba5-7141-a2ba-78cf8dc7a202` | 12.0s |
| mzu | `019f6f01-fba6-7470-9400-e455f450e9dc` | 11.3s |

Provenance: [`benchmarks/sessions/MANIFEST.json`](./benchmarks/sessions/MANIFEST.json)  
Raw JSON dumps: [`benchmarks/sessions/*.json`](./benchmarks/sessions/)  
Measure: `python benchmarks/run.py` → [`benchmarks/results/LATEST.md`](./benchmarks/results/LATEST.md)

### Totals vs plain (live)

| Mode | Tokens | Token saved | Char saved | Role |
|------|-------:|------------:|-----------:|------|
| **plain** | 758 | 0% | 0% | baseline agent session |
| **caveman** | 587 | **22.6%** | 26.5% | pure collapse session |
| **mz** | 586 | **22.7%** | 28.2% | collapse + 피식 session |
| **mzu** | 1059 | **−39.7%** | −22.1% | 난사 session (longer) |

**Takeaway (measured, not vibes):**
- Live agents compress less aggressively than ideal skill demos (~23% not ~55%).
- **짧게 + 웃기기 = 가능.** 그게 **`mz`**: caveman과 토큰 동급(−22.7%)인데 판정 한 줄로 피식.
- **유머세 ≠ 웃음세.** 세금은 **`mzu` 난사**(밈을 문장 위에 *쌓음*, +40%). 밈으로 긴 문장을 *대체*하면 토큰 내려감.
- 규칙: 웃기려면 먼저 줄여라. 줄인 자리에 판정 1방. 줄이지 않고 밈만 뿌리면 청구서 옴.

### Side-by-side (`02-integ-fail`, live text)

**plain** (127 tok) · subagent-plain

```text
실패한 통합 테스트 4개를 즉시 분류해야 합니다. 동일한 원인인지, 코드 회귀인지, 환경 문제인지 확인하십시오. 실패 로그와 재현 명령을 반드시 보존하고, 원인을 확인하기 전에 추측으로 수정하지 마십시오. skip으로 통과시킨 것처럼 보이게 만들지 마십시오.
```

**caveman** (88 tok · −30.7%) · subagent-caveman

```text
실패 통합 테스트 4개 즉시 분류 필요. 동일 원인·코드 회귀·환경 문제 여부 확인. 실패 로그·재현 명령 반드시 보존. 원인 확인 전 추측 수정 금지. skip으로 통과 위장 금지.
```

**mz** (84 tok · −33.9%) · subagent-mz

```text
실패 통합 테스트 4개 즉시 분류. 동일 원인 / 코드 회귀 / 환경 문제 가려라. 실패 로그·재현 명령 보존. 원인 전 추측 수정 금지. skip으로 통과 연출? 나가리.
```

**mzu** (168 tok · +32.3%) · subagent-mzu

```text
실패한 통합 테스트 4개 지금 당장 분류 드가자 야르. 동일 원인인지 / 코드 회귀인지 / 환경 문제인지 확인이 국룰 ㄹㅇ. 실패 로그랑 재현 명령 반드시 보존 밤티. 원인 확인 전에 추측 수정? 그건 나가리 컷 스불재. skip으로 통과한 척 보이게 만들기 손절 정배. 도파민 수정 욕구 샤갈 아자스 이왜진 금지.
```

### Per-case token save (live)

| Case | caveman | mz | mzu |
|------|--------:|---:|----:|
| release-block | 24.0% | 24.0% | −28.7% |
| integ-fail | 30.7% | **33.9%** | −32.3% |
| flaky-windows | 24.2% | 20.2% | −57.6% |
| perf-temptation | 17.7% | **25.5%** | −39.7% |
| go-nogo-role | 14.2% | 5.7% | −59.4% |
| cache-bloat | 23.7% | 23.0% | −30.4% |

Full texts: [`benchmarks/variants/`](./benchmarks/variants/).

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
benchmarks/                   # fixtures + live variants + run.py
benchmarks/sessions/          # subagent IDs + raw JSON (proof)
benchmarks/results/LATEST.md  # measured table
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

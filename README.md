# MZ Caveman

**짧은데 피식하게.**  
Caveman = short. MZ Caveman = short **and** makes you go 피식.

Not a slang dictionary skill. A **sentence-collapse engine** with one optional meme-like verdict line.  
Optional chaos mode: **`/mzu`** — max MZ spam, barely work-usable on purpose.

Inspired by [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (token compression).  
MZ layer = Korean Gen-Z / 2026 stamp culture + judgment one-liners.

| Mode | Trigger | Vibe |
|------|---------|------|
| **default** | `/mz` | Collapse + **one** 판정 한 줄 |
| **ultra** | `/mzu` · `/mz ultra` | MZ 난사. Comedy chaos. |
| **off** | `stop mz` · `normal mode` | Normal prose |

> Identity is the **last line**, not Core 40.  
> `감으로 패치? 컷.` — few tokens, full info, memorable.

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

Codex: `$mz` · `$mzu`

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
SKILL.md                 # canonical skill (same as skills/mz-caveman/)
skills/mz-caveman/       # Grok / skills-dir install path
agents/openai.yaml       # Codex UI metadata
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

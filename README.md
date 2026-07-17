# MZ Caveman

**짧은데 피식하게.**  
Caveman = short. MZ = short **and** 피식.

| Mode | Grok | Codex | Vibe |
|------|------|-------|------|
| **default** | `/mz` | `$mz` | 붕괴 + 판정 1줄 |
| **ultra** | **`/mzu`** | **`$mzu`** | **쇼츠+웃김** (밈이 긴 문장 *대체*) |
| **extreme** | **`/mze`** | **`$mze`** | **극단 난사** (웃김 밀도 1순위, 토큰↑ OK) |
| **off** | `stop mz` | same | 일반 문장 |

```text
# mzu — short + funny
릴리즈? 나가리 정배. 통합 털림. +성능 도파민? 손절. Go/No-Go: RM·On-call.

# mze — extreme (구 울트라 난사)
야르 지금 상태로 릴리즈 드가자? 나가리 컷 정배 ㄹㅇ. 스불재 각. 도파민 손절 국룰…
```

**이름:** `caveman ultra` ≠ `/mzu` ≠ `/mze`.

Inspired by [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman).

### Codex slash

Codex skill = **`$name`**. `/mzu` `/mze` slash → Unrecognized = 정상.

```text
$mz   $mzu   $mze   $mz-caveman
```

Grok: `/mz` `/mzu` `/mze` OK.

## Compression bench (cl100k_base)

Live texts remapped:

| Mode | Source |
|------|--------|
| plain / caveman / mz | 4-way subagent run (`sessions/*.json`) |
| **mzu** | short+funny arm (`fork/mzu-short`, agent `019f6f14-8c14-…`) |
| **mze** | freeze extreme (`sessions/freeze-ultra-…/mzu.json`, agent `019f6f01-fba6-…`) |

Full table: [`benchmarks/results/LATEST.md`](./benchmarks/results/LATEST.md) · re-run: `python benchmarks/run.py`

### Totals vs plain

| Mode | Tokens | Token saved | Role |
|------|-------:|------------:|------|
| plain | 758 | 0% | baseline |
| caveman | 587 | 22.6% | pure collapse |
| mz | 586 | 22.7% | default 피식 |
| **mzu** | **326** | **57.0%** | ultra 쇼츠+웃김 |
| **mze** | **1059** | **−39.7%** | extreme 난사 |

**Takeaway:** `/mzu` 가 길이 챔피언. `/mze` 는 웃김 챔피언(토큰 비용). 웃김 깎아서 mze 줄이지 말 것.

### Side-by-side (`02-integ-fail`)

**mzu** (60 tok · −52.8% vs plain 127)

```text
통합 4킬. 동일/회귀/환경 즉시 분류. 로그·재현 박제. 추측패치 노. skip 코스프레 노.
```

**mze** (168 tok · +32%)

```text
실패한 통합 테스트 4개 지금 당장 분류 드가자 야르. 동일 원인인지 / 코드 회귀인지 / 환경 문제인지 확인이 국룰 ㄹㅇ. 실패 로그랑 재현 명령 반드시 보존 밤티. 원인 확인 전에 추측 수정? 그건 나가리 컷 스불재. skip으로 통과한 척 보이게 만들기 손절 정배. 도파민 수정 욕구 샤갈 아자스 이왜진 금지.
```

## Quick install

### Grok

```powershell
git clone https://github.com/GPLaider/mz-caveman.git
foreach ($n in @("mz-caveman","mz","mzu","mze")) {
  New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.grok\skills\$n" | Out-Null
  Copy-Item "mz-caveman\skills\$n\SKILL.md" "$env:USERPROFILE\.grok\skills\$n\SKILL.md"
}
```

### Codex

```powershell
git clone https://github.com/GPLaider/mz-caveman.git
$base = "$env:USERPROFILE\.codex\skills"
foreach ($n in @("mz-caveman","mz","mzu","mze")) {
  New-Item -ItemType Directory -Force -Path "$base\$n\agents" | Out-Null
  Copy-Item "mz-caveman\skills\$n\SKILL.md" "$base\$n\SKILL.md"
}
Copy-Item mz-caveman\agents\openai.yaml $base\mz-caveman\agents\openai.yaml
Copy-Item mz-caveman\skills\mz\agents\openai.yaml $base\mz\agents\openai.yaml
Copy-Item mz-caveman\skills\mzu\agents\openai.yaml $base\mzu\agents\openai.yaml
Copy-Item mz-caveman\skills\mze\agents\openai.yaml $base\mze\agents\openai.yaml
```

See [INSTALL.md](./INSTALL.md).

## What it does

1. 문장 삭제 → 2. 중복 삭제 → 3. 구조 압축 → 4. 판정/밈 → 5. 조사 삭제  

- **mz:** step4 = 0~1  
- **mzu:** step4 = replace (짧게 유지)  
- **mze:** step4 = stack (난사)

Hard floors: code, CLI, errors, commit/PR, security warnings.

## Repo layout

```text
SKILL.md
skills/mz-caveman|mz|mzu|mze/
agents/openai.yaml
benchmarks/variants/*/{plain,caveman,mz,mzu,mze}.txt
benchmarks/sessions/          # live dumps + freeze extreme
```

## License

MIT — [LICENSE](./LICENSE).

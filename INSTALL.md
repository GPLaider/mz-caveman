# Install MZ Caveman

Official skill: [GPLaider/mz-caveman](https://github.com/GPLaider/mz-caveman)

## Grok (user-global)

Target: `~/.grok/skills/mz-caveman/SKILL.md`

### PowerShell

```powershell
$dest = "$env:USERPROFILE\.grok\skills\mz-caveman"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/GPLaider/mz-caveman/main/skills/mz-caveman/SKILL.md" -OutFile "$dest\SKILL.md" -UseBasicParsing
```

Or clone:

```powershell
git clone https://github.com/GPLaider/mz-caveman.git $env:TEMP\mz-caveman
Copy-Item -Force $env:TEMP\mz-caveman\skills\mz-caveman\SKILL.md "$env:USERPROFILE\.grok\skills\mz-caveman\SKILL.md"
```

Triggers: `/mz` · `/mzu` · `/mz ultra` · `stop mz`

## Codex (user-global)

**중요:** Codex skill 호출은 **`$name`**. `/mzu` slash는 built-in만 됨 → `Unrecognized command` 정상.

Install **three** skill folders so `$mz`, `$mzu`, `$mz-caveman` all resolve:

### PowerShell (full)

```powershell
$base = "$env:USERPROFILE\.codex\skills"
$repo = "https://raw.githubusercontent.com/GPLaider/mz-caveman/main"
foreach ($n in @("mz-caveman","mz","mzu")) {
  New-Item -ItemType Directory -Force -Path "$base\$n\agents" | Out-Null
  Invoke-WebRequest -Uri "$repo/skills/$n/SKILL.md" -OutFile "$base\$n\SKILL.md" -UseBasicParsing
}
# openai.yaml: root agents for mz-caveman; per-skill for aliases
Invoke-WebRequest -Uri "$repo/agents/openai.yaml" -OutFile "$base\mz-caveman\agents\openai.yaml" -UseBasicParsing
Invoke-WebRequest -Uri "$repo/skills/mz/agents/openai.yaml" -OutFile "$base\mz\agents\openai.yaml" -UseBasicParsing
Invoke-WebRequest -Uri "$repo/skills/mzu/agents/openai.yaml" -OutFile "$base\mzu\agents\openai.yaml" -UseBasicParsing
```

Triggers: **`$mzu`** (ultra) · **`$mz`** (default) · `$mz-caveman`  
Not: `/mzu` (Codex will reject)

## Verify

- Grok: skill appears under skills / slash menu within a few seconds after file write  
- Codex: `$mz-caveman` or `$mz` in skill list  

## Update

Re-run the install commands, or:

```powershell
git -C path\to\mz-caveman pull
# then copy SKILL.md (+ openai.yaml for Codex) again
```

## Uninstall

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.grok\skills\mz-caveman" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\mz-caveman" -ErrorAction SilentlyContinue
```

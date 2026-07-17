# Install MZ Caveman

Official: [GPLaider/mz-caveman](https://github.com/GPLaider/mz-caveman)

## Modes

| Invoke | Mode |
|--------|------|
| `/mz` `$mz` | default |
| `/mzu` `$mzu` | ultra short+funny |
| `/mze` `$mze` | extreme spam |
| `stop mz` | off |

Codex: use **`$name`**, not slash.

## Grok (user-global)

```powershell
$repo = "https://raw.githubusercontent.com/GPLaider/mz-caveman/main"
foreach ($n in @("mz-caveman","mz","mzu","mze")) {
  $d = "$env:USERPROFILE\.grok\skills\$n"
  New-Item -ItemType Directory -Force -Path $d | Out-Null
  Invoke-WebRequest -Uri "$repo/skills/$n/SKILL.md" -OutFile "$d\SKILL.md" -UseBasicParsing
}
```

## Codex (user-global)

```powershell
$repo = "https://raw.githubusercontent.com/GPLaider/mz-caveman/main"
$base = "$env:USERPROFILE\.codex\skills"
foreach ($n in @("mz-caveman","mz","mzu","mze")) {
  New-Item -ItemType Directory -Force -Path "$base\$n\agents" | Out-Null
  Invoke-WebRequest -Uri "$repo/skills/$n/SKILL.md" -OutFile "$base\$n\SKILL.md" -UseBasicParsing
}
Invoke-WebRequest -Uri "$repo/agents/openai.yaml" -OutFile "$base\mz-caveman\agents\openai.yaml" -UseBasicParsing
foreach ($n in @("mz","mzu","mze")) {
  Invoke-WebRequest -Uri "$repo/skills/$n/agents/openai.yaml" -OutFile "$base\$n\agents\openai.yaml" -UseBasicParsing
}
```

## Uninstall

```powershell
foreach ($n in @("mz-caveman","mz","mzu","mze")) {
  Remove-Item -Recurse -Force "$env:USERPROFILE\.grok\skills\$n" -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\skills\$n" -ErrorAction SilentlyContinue
}
```

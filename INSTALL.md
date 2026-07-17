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

Target:

- `~/.codex/skills/mz-caveman/SKILL.md`
- `~/.codex/skills/mz-caveman/agents/openai.yaml`

### PowerShell

```powershell
$root = "$env:USERPROFILE\.codex\skills\mz-caveman"
New-Item -ItemType Directory -Force -Path "$root\agents" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/GPLaider/mz-caveman/main/skills/mz-caveman/SKILL.md" -OutFile "$root\SKILL.md" -UseBasicParsing
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/GPLaider/mz-caveman/main/agents/openai.yaml" -OutFile "$root\agents\openai.yaml" -UseBasicParsing
```

Triggers: `$mz` · `$mzu` · `/mz` · `/mzu`

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

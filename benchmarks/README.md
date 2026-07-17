# Benchmarks

## Live 4-subagent method (canonical)

1. Parent spawns **4 parallel** `general-purpose` subagents (read-only).
2. Each agent gets the **same 6 fixtures** and a **mode-locked** prompt:
   - `plain` — normal prose, no slang
   - `caveman` — pure collapse, no MZ stamps
   - `mz` — collapse + one 피식 verdict
   - `mzu` — max MZ spam
3. Agents return JSON variants.
4. Parent writes:
   - `sessions/{mode}.json` — raw agent payload + `subagent_id`
   - `sessions/MANIFEST.json` — IDs, durations
   - `variants/{case}/{mode}.txt` — text used for measurement
5. `python benchmarks/run.py` measures `cl100k_base` tokens.

**Do not replace live variants with hand-written “ideal” demos without moving old files aside and labeling them non-live.**

## Run measure only

```bash
pip install -r benchmarks/requirements.txt
python benchmarks/run.py
```

## Files

| Path | Meaning |
|------|---------|
| `fixtures/` | Shared source prompts |
| `sessions/MANIFEST.json` | Live run provenance |
| `sessions/*.json` | Per-mode subagent raw output |
| `variants/*/*.txt` | Texts under measurement |
| `results/latest.json` | Machine table |
| `results/LATEST.md` | Human table |

# Benchmarks

Reference rewrites for **plain / caveman / mz / mzu** on 6 agent-style Korean engineering cases.

## Run

```bash
pip install -r benchmarks/requirements.txt
python benchmarks/run.py
```

Writes:

- `results/latest.json`
- `results/LATEST.md`

## Modes

| Mode | Goal |
|------|------|
| `plain` | Baseline full prose |
| `caveman` | Sentence collapse only |
| `mz` | Collapse + one 피식 verdict |
| `mzu` | Max slang spam (humor tax; not always shorter) |

## Note

These are **curated** variants that encode the skill rules, not a live multi-model API bake-off.  
Token metric: OpenAI `cl100k_base` via `tiktoken`.

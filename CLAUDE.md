# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A [CMS](https://github.com/cms-dev/cms) plugin that adds Karel Java/Pascal language support and a Karel task type to the Mexican Olympiad in Informatics judge. It registers two entry points:

- **Languages** (`karel.language`): `KarelLanguage` (generic), `KarelJava`, `KarelPascal`, and the deprecated `OldKarelLanguage`.
- **Task type** (`karel.task`): `KarelTask`, a subclass of CMS `Batch` that maps Karel VM exit codes to human-readable Spanish error messages.

## Install / reinstall

```bash
python3 setup.py install
# Then restart CMS
```

External dependencies (not managed by this package):
- `rekarel` CLI at `/usr/local/bin/rekarel` — install via `npm install -g @rekarel/cli`
- Karel C++ VM at `/usr/local/bin/karel` — built from [rekarel-cpp-interpreter](https://github.com/kishtarn555/rekarel-cpp-interpreter/releases/tag/v2.3.1)

## Architecture

The package has three files:

| File | Role |
|------|------|
| `karel/language.py` | Defines compilation (`rekarel compile`) and evaluation (`karel`) commands for CMS |
| `karel/task.py` | Overrides `Batch.evaluate` to translate VM exit codes (16–52) into Spanish error strings |
| `setup.py` | Registers entry points so CMS discovers the language and task type via `pkg_resources` |

**Current ReKarel version targeted:** `2.3` (constant in `language.py`). Bumping this affects both the `rekarel compile -e` and `karel -e` version enforcement flags.

**Exit code mapping** (in `task.py`): codes 16–25 are runtime errors (wall collisions, empty baggage, stack overflow, etc.); 48–52 are instruction-limit variants. Code 2 means a VM version mismatch.

`OldKarelLanguage` is deprecated and kept only for backward compatibility with existing CMS submissions. Do not add new features to it.

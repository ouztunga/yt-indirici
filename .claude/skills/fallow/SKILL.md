---
name: fallow
description: Run codebase intelligence static analysis using Fallow to identify dead code, duplication, circular dependencies, and complexity hotspots.
---

# Fallow Skill

This skill teaches the agent how to run and analyze Fallow codebase reports.

## Instructions

When the user asks to run Fallow or analyze the codebase for dead code, duplication, or health issues:
1. Run `npx fallow` to scan the codebase.
2. If the user wants to check specific categories, run:
   - `npx fallow dead-code` for unused exports/files.
   - `npx fallow dupes` for duplicate code.
   - `npx fallow health` for complexity and architectural health.
3. Review the outputs carefully.
4. Suggest cleanups or run `npx fallow fix` (or `npx fallow fix --dry-run` to preview) if appropriate and approved by the user.

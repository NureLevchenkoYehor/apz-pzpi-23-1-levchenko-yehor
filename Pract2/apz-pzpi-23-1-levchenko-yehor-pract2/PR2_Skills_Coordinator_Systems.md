# PR #2 — Skills & Coordinator Systems

**Goal:** Understand reusable workflow execution (skills) and multi-agent orchestration (coordinator).

## Task 2.1 — Analyze `src/skills/`

**Agent instructions:**

- Read all files in `src/skills/`
- Describe how a skill is defined (schema, fields, execution contract)
- Identify how `SkillTool` loads and executes skills
- Note whether skills are user-defined, built-in, or both
- Find any examples of built-in skills if present

**Output artifact:** `study/findings/03_skills.md`

```md
# Skill System

## File Overview
...

## Skill Definition Schema
<fields and types>

## Execution Flow
(step-by-step: how SkillTool picks up and runs a skill)

## Built-in vs User-defined Skills
...

## Observations
...
```

---

## Task 2.2 — Analyze `src/coordinator/`

**Agent instructions:**

- Read all files in `src/coordinator/`
- Identify the orchestration model: how sub-agents are spawned, how tasks are distributed, how results are collected
- Describe the lifecycle of a coordinated task (create → assign → execute → collect)
- Check how `TeamCreateTool` and `AgentTool` integrate with the coordinator
- Note any message-passing or shared state mechanisms between agents

**Output artifact:** `study/findings/04_coordinator.md`

```md
# Multi-Agent Coordinator

## File Overview
...

## Orchestration Model
(how agents are spawned and managed)

## Task Lifecycle
1. ...
2. ...

## Integration with AgentTool / TeamCreateTool
...

## Inter-Agent Communication
...

## Observations
...
```

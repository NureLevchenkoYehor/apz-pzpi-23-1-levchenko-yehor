# PR #5 — Pseudocode Examples

**Goal:** Generate illustrative pseudocode examples that demonstrate key architectural principles of Claude Code, based on the research findings. No real source code should be used — examples must be abstract enough to serve as architectural illustrations.

**Context available to agent:** findings from `01_components.md` through `08_infrastructure.md`, plus `README.md`.

---

## Task 5.1 — Tool Contract Pseudocode

Illustrate the self-contained tool module pattern.

**Agent instructions:**

- Based on `README.md` (Tool System section) and `03_skills.md` / `04_coordinator.md` findings, produce pseudocode for a representative tool module
- Must show: input schema declaration, permission check, execution logic, result return
- Use a generic `FileTool` or `ShellTool` as the example — do not copy real source
- Keep it under 40 lines

**Output artifact:** `findings/pseudocode/01_tool_contract.pseudo.md`

```md
# Example: Tool Contract Pattern

## Description
<one paragraph explaining what this illustrates architecturally>

## Pseudocode
\```
...
\```

## Architectural Notes
<what principle this demonstrates>
```

---

## Task 5.2 — Agent Loop Pseudocode

Illustrate the iterative LLM/tool execution loop.

**Agent instructions:**

- Based on `05_agent_loop.md`, produce pseudocode for the `queryLoop` function
- Must show: model call, tool_use detection, tool dispatch, result injection, loop termination
- Do not model every termination condition — show the core happy path + one error exit
- Keep it under 50 lines

**Output artifact:** `findings/pseudocode/02_agent_loop.pseudo.md`

```md
# Example: Agent Loop Pattern

## Description
...

## Pseudocode
\```
...
\```

## Architectural Notes
...
```

---

## Task 5.3 — Multi-Agent Coordination Pseudocode

Illustrate the coordinator fan-out / fan-in pattern.

**Agent instructions:**

- Based on `04_coordinator.md`, produce pseudocode for coordinator spawning workers and collecting `<task-notification>` results
- Must show: task creation, parallel spawn, notification collection, synthesis
- Keep it under 50 lines

**Output artifact:** `findings/pseudocode/03_coordinator.pseudo.md`

```md
# Example: Multi-Agent Coordination Pattern

## Description
...

## Pseudocode
\```
...
\```

## Architectural Notes
...
```

---

## Task 5.4 — Bridge Permission Flow Pseudocode

Illustrate the control-plane RPC for tool permission.

**Agent instructions:**

- Based on `06_bridge_protocol.md`, produce pseudocode for the permission request/response cycle between CLI and IDE
- Must show: control_request emission, waiting for control_response, allow/deny branching
- Keep it under 40 lines

**Output artifact:** `findings/pseudocode/04_bridge_permission.pseudo.md`

```md
# Example: Bridge Permission RPC Pattern

## Description
...

## Pseudocode
\```
...
\```

## Architectural Notes
...
```

---

## Task 5.5 — Skill Execution Pseudocode

Illustrate the skill loading and invocation flow.

**Agent instructions:**

- Based on `03_skills.md`, produce pseudocode for `SkillTool` resolving and executing a skill
- Must show: skill discovery, validation, inline vs forked execution branching
- Keep it under 40 lines

**Output artifact:** `findings/pseudocode/05_skill_execution.pseudo.md`

```md
# Example: Skill Execution Pattern

## Description
...

## Pseudocode
\```
...
\```

## Architectural Notes
...
```

---

## Загальні вимоги до агента

- All pseudocode must use **language-neutral syntax** (no TypeScript, no Python specifics)
- Variable names should be descriptive (`toolUseBlocks`, `taskNotification`, `permissionResponse`)
- Comments inside pseudocode are encouraged to clarify non-obvious steps
- Each artifact is self-contained — include description and architectural notes, not just code

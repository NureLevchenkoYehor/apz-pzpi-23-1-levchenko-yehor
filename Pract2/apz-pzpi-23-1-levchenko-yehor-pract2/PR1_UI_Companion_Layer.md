# PR #1 — UI & Companion Layer

**Goal:** Understand the user-facing layer of Claude Code — terminal UI components and the buddy sprite system.

## Task 1.1 — Inventory `src/components/`

Explore the `src/components/` directory and produce a structured overview.

**Agent instructions:**

- List all subdirectories and files in `src/components/`
- Group components by their apparent purpose (input, output, layout, status, dialogs, etc.)
- For each group, identify 2–3 representative components and briefly describe what they render or handle
- Note any shared base components or HOCs that other components extend

**Output artifact:** `study/findings/01_components.md`

```md
# Components Inventory

## Directory Structure
<tree>

## Component Groups
### <Group Name>
- `ComponentName` — <one-line description>
...

## Notable Base Components
...

## Observations
<anything architecturally interesting>
```

---

## Task 1.2 — Analyze `src/buddy/`

Determine the role of the buddy/companion sprite subsystem.

**Agent instructions:**

- Read all files in `src/buddy/`
- Identify what the buddy renders, when it is triggered, and how it communicates with the rest of the system
- Check if buddy reacts to agent state, errors, or tool calls
- Note any event subscriptions or props it receives

**Output artifact:** `study/findings/02_buddy.md`

```md
# Buddy / Companion Sprite

## Files Overview
...

## Rendering & Trigger Conditions
...

## Integration Points
(what systems/events trigger buddy behavior)

## Observations
...
```

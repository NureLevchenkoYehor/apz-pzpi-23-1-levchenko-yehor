# PR #4 — Services, Replication & Infrastructure

**Goal:** Identify data persistence/replication mechanisms and clarify infrastructure model.

## Task 4.1 — Scan `src/services/` for replication or persistence patterns

**Agent instructions:**

- Scan all subdirectories of `src/services/`
- Specifically look for: replication, sync, persistence, caching, retry, or redundancy mechanisms
- Pay special attention to `teamMemorySync/`, `extractMemories/`, `compact/`, and `api/`
- For each relevant file found, describe what it does and whether it constitutes a form of data replication or fault tolerance
- If no replication mechanism is found, explicitly state that and describe what persistence/sync mechanisms exist instead

**Output artifact:** `study/findings/07_services_persistence.md`

```md
# Services — Persistence & Replication

## Scanned Directories
...

## Relevant Findings
### `teamMemorySync/`
...
### `extractMemories/`
...
### `compact/`
...
### `api/`
...

## Replication Verdict
[ Found / Not Found ]
Explanation: ...

## Existing Persistence/Sync Mechanisms
...

## Observations
...
```

---

## Task 4.2 — Determine infrastructure model

**Agent instructions:**

- Review `src/server/`, `src/remote/`, `src/upstreamproxy/`, and `src/entrypoints/`
- Determine: does Claude Code run purely locally, or does it have a server/cloud component?
- Identify any network calls beyond the Anthropic API (e.g., telemetry endpoints, remote sessions, proxy targets)
- Describe the deployment model: what runs on the developer's machine vs. what runs remotely

**Output artifact:** `study/findings/08_infrastructure.md`

```md
# Infrastructure & Deployment Model

## Local vs Remote Components
| Component | Location | Description |
|---|---|---|
| ... | Local | ... |
| ... | Remote | ... |

## Network Calls Inventory
(beyond Anthropic API)

## Server Mode (`src/server/`)
...

## Remote Sessions (`src/remote/`)
...

## Proxy Configuration (`src/upstreamproxy/`)
...

## Deployment Model Summary
...

## Observations
...
```

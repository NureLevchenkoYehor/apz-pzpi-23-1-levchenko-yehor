# PR #3 — Core Engine & Bridge Protocol

**Goal:** Map the Agent Loop execution steps and the IDE bridge communication protocol.

## Task 3.1 — Analyze Agent Loop in `src/QueryEngine.ts`

**Agent instructions:**

- Focus specifically on the main query/response loop and tool-call handling logic
- Do **not** summarize the entire file — focus on:
  - The entry point function that handles a user message
  - How the LLM response is received and parsed
  - How tool calls are detected and dispatched
  - How tool results are fed back into the next LLM call
  - How the loop terminates
- Extract the key function names and their call order
- If possible, produce a numbered step sequence of the loop

**Output artifact:** `study/findings/05_agent_loop.md`

```md
# Agent Loop — QueryEngine

## Entry Point
`functionName(args)` — description

## Step-by-Step Execution
1. Receive user message
2. ...
N. Return final response to UI

## Key Functions & Call Order
| Function | Role |
|---|---|
| ... | ... |

## Tool-Call Dispatch Logic
(how tool calls are detected and routed)

## Loop Termination Conditions
...

## Observations
...
```

---

## Task 3.2 — Analyze `src/bridge/bridgeMessaging.ts`

**Agent instructions:**

- Read `src/bridge/bridgeMessaging.ts` and related bridge files (`bridgeMain.ts`, `replBridge.ts`, `bridgePermissionCallbacks.ts`)
- Identify the message types/protocol used between IDE extension and CLI
- Describe the message format (fields, types)
- Map the request/response flow for at least two scenarios: (a) user sends a command from IDE, (b) permission prompt is shown
- Note how JWT authentication is applied to messages

**Output artifact:** `study/findings/06_bridge_protocol.md`

```md
# Bridge Messaging Protocol

## Message Format
<fields and types>

## Message Types Catalog
| Type | Direction | Description |
|---|---|---|
| ... | IDE→CLI | ... |

## Scenario A — Command from IDE
1. ...

## Scenario B — Permission Prompt
1. ...

## JWT Authentication Flow
...

## Observations
...
```

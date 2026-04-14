# PR #6 — Critical Analysis

**Goal:** Identify concrete problems, anti-patterns, and failure modes in the Claude Code codebase. For each area of concern, produce evidence-based findings — not speculation. If a problem is not confirmed by code, mark it explicitly as unconfirmed.

**Output format for all artifacts:**

```md
# Critical Analysis — <Area>

## Confirmed Problems
### <Problem Name>
- **Location:** file(s)
- **Evidence:** what exactly in the code confirms this
- **Failure mode:** how this manifests at runtime
- **Severity:** High / Medium / Low

## Suspected Problems (Unconfirmed)
### <Problem Name>
- **Location:** file(s)
- **Suspicion:** what raises concern
- **What to verify:** specific thing that would confirm or deny

## No Problem Found
### <Area that looked suspicious>
- **Reasoning:** why the concern does not materialize
```

---

## Task 6.1 — God Object analysis of QueryEngine and Tool.ts

**Agent instructions:**

- Open `src/QueryEngine.ts` and identify how many distinct responsibilities it handles. Count the number of exported functions and top-level logical sections. Look for: turn orchestration, streaming, tool dispatch, retry, token management, structured output, hook handling, abort handling.
- Check whether any of these responsibilities have their own dedicated files or are fully inlined into QueryEngine.
- Open `src/Tool.ts`. Identify how many unrelated concerns are defined in this single file. Check whether tools import from Tool.ts directly and whether a change to a shared type would ripple across many tools.
- Look for signs of coupling: do functions in QueryEngine directly reference tool-specific logic (e.g., special-casing specific tool names or types)?

**Output artifact:** `study/findings/critique/01_god_object.md`

---

## Task 6.2 — SendMessageTool semantic overload

**Agent instructions:**

- Read `src/tools/SendMessageTool/SendMessageTool.ts` in full.
- Identify every distinct semantic path the tool handles (mailbox write, in-process queue, broadcast, control messages, cross-session routing, resume behavior).
- For each path, determine: is there a shared dispatcher that routes between them, or is the routing logic interleaved with the execution logic?
- Look for error handling at path boundaries: what happens if a message is sent to a target that has already exited, or if the wrong path is taken?
- Identify any conditions where the routing decision could be ambiguous (e.g., a target that matches both a teammate name and an agent id).

**Output artifact:** `study/findings/critique/02_send_message_overload.md`

---

## Task 6.3 — Coordinator failure modes

**Agent instructions:**

- Read `src/coordinator/coordinatorMode.ts` and `src/tools/AgentTool/AgentTool.tsx`.
- Identify what happens if the coordinator's queryLoop exhausts its context window while workers are still running. Is there a mechanism to resume collection of task-notifications after compaction?
- Check whether task-notification messages are persisted before being delivered to the coordinator, or whether they exist only in the in-memory queue.
- Identify what happens to a running worker if its parent coordinator is killed or restarted.
- Check max-turns behavior: if coordinator hits max_turns before all workers complete, what state are the workers left in?

**Output artifact:** `study/findings/critique/03_coordinator_failures.md`

---

## Task 6.4 — Compaction failure modes

**Agent instructions:**

- Read `src/services/compact/autoCompact.ts` and `src/services/compact/compact.ts`.
- Identify the circuit breaker logic: what is the threshold, what does it do when triggered, and does it leave the session in a recoverable state?
- Determine what happens if the compaction summary itself exceeds the context window. Is there a fallback?
- Check whether compaction can lose information that later causes tool-use/tool-result message pairing violations (which would cause API errors).
- Look for any race conditions between autoCompact triggering and an in-flight tool execution.

**Output artifact:** `study/findings/critique/04_compaction_failures.md`

---

## Task 6.5 — JWT without signature verification

**Agent instructions:**

- Read `src/bridge/jwtUtils.ts` and any callers of `decodeJwtExpiry(...)`.
- Determine exactly what the decoded JWT payload is used for: is it only used for scheduling token refresh, or is it also used for access control decisions?
- If it is used for access control: document this as a confirmed security concern.
- If it is only used for refresh scheduling: assess whether a manipulated expiry value could cause a denial-of-service (e.g., never refreshing, or refreshing too aggressively).
- Check whether there are any other JWT decode operations in the codebase that also skip signature verification.

**Output artifact:** `study/findings/critique/05_jwt_no_verify.md`

---

## Task 6.6 — Deployment mode ambiguity

**Agent instructions:**

- Read `src/entrypoints/init.ts` and `src/remote/RemoteSessionManager.ts`.
- Identify how the system determines which deployment mode to use (local, CCR, bridge, remote). Is the mode selection explicit (e.g., a single flag) or emergent (e.g., multiple conditions evaluated independently)?
- Look for partial initialization states: can the system start in one mode and partially activate another? What safeguards exist?
- Identify any state that is shared between modes and could cause interference if modes overlap.
- Check whether there are error messages or logging that would help diagnose a wrong-mode scenario at runtime.

**Output artifact:** `study/findings/critique/06_deployment_ambiguity.md`

---

## Task 6.7 — teamMemorySync edge cases

**Agent instructions:**

- Read `src/services/teamMemorySync/index.ts` and `src/services/teamMemorySync/watcher.ts`.
- Trace the full conflict resolution path: what happens when a 412 (ETag mismatch) is received — does the system retry with the server's version, merge, or discard local changes?
- Identify what happens if secret scanning (`secretScanner.ts`) blocks a write mid-sync: are partial writes possible, and is the sync state correctly rolled back?
- Check the debounce and shutdown flush logic in watcher.ts: is there a window where local changes can be silently lost if the process exits during the debounce period?
- Assess whether the delta-upload mechanism correctly handles concurrent modifications to the same key from two machines.

**Output artifact:** `study/findings/critique/07_team_memory_sync.md`

---

## General Requirements for Agents

- **Verify issues with code, not guesswork.** If an issue is not verified, place it in the Suspected section, not Confirmed.
- **Do not assess what you cannot see.** If a file is unavailable or too large, explicitly note this.
- **Severity is determined by the consequences:** High — data loss, incorrect security decisions, or complete session failure. Medium — degradation or unpredictable behavior. Low — technical debt with no direct consequences for the user.
- If you discover a new suspicious area during your investigation that is not covered by the task, add it to the artifact in the **Bonus Finding** section.

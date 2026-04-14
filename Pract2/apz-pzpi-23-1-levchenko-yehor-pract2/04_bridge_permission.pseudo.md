# Example: Bridge Permission RPC Pattern

## Description

This example illustrates a control-plane RPC cycle between CLI and IDE for tool permission decisions: the CLI emits a permission request, waits for a correlated response, then branches into allow/deny handling before continuing tool execution.

## Pseudocode

```text
FUNCTION requestToolPermission(toolName, toolInput, toolUseId, bridgeClient):
  requestId = generateId()

  controlRequest = {
    type: "control_request",
    request_id: requestId,
    request: {
      subtype: "can_use_tool",
      tool_name: toolName,
      input: toolInput,
      tool_use_id: toolUseId
    }
  }

  bridgeClient.send(controlRequest)

  permissionResponse = bridgeClient.waitFor(
    type="control_response",
    matchRequestId=requestId,
    timeoutMs=60000
  )

  IF permissionResponse.timedOut:
    RETURN PermissionResult(behavior="deny", reason="No response from IDE")

  IF permissionResponse.response.subtype = "error":
    RETURN PermissionResult(behavior="deny", reason=permissionResponse.response.error)

  decision = permissionResponse.response.response
  IF decision.behavior = "allow":
    RETURN PermissionResult(
      behavior="allow",
      updatedInput=decision.updatedInput OR toolInput
    )

  RETURN PermissionResult(behavior="deny", reason=decision.message)
```

## Architectural Notes

This demonstrates request-response correlation over an asynchronous channel. The request_id provides deterministic matching, while explicit allow/deny branching keeps permission outcomes auditable and decoupled from tool business logic.

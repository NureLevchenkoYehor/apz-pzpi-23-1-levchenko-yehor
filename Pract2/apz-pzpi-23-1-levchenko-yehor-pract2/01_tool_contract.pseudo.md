# Example: Tool Contract Pattern

## Description

This example illustrates the self-contained tool module contract used in an agentic CLI: each tool declares an input schema, enforces permission checks before side effects, executes domain logic in isolation, and returns a normalized result envelope that the agent loop can consume uniformly.

## Pseudocode

```text
MODULE FileTool

  DEFINE InputSchema:
    filePath: required string
    operation: required enum("read", "write")
    content: optional string

  FUNCTION validateInput(input):
    RETURN SchemaValidator.check(InputSchema, input)

  FUNCTION checkPermission(input, permissionContext):
    IF permissionContext.deniesPath(input.filePath):
      RETURN Decision(behavior="deny", reason="Path is restricted")
    IF input.operation = "write" AND NOT permissionContext.canEditFiles:
      RETURN Decision(behavior="deny", reason="Write not allowed")
    RETURN Decision(behavior="allow")

  FUNCTION execute(input, runtimeContext):
    parsedInput = validateInput(input)
    IF parsedInput.invalid:
      RETURN ToolResult(error=true, message="Invalid input schema")

    decision = checkPermission(parsedInput.value, runtimeContext.permissionContext)
    IF decision.behavior = "deny":
      RETURN ToolResult(error=true, message=decision.reason)

    IF parsedInput.value.operation = "read":
      data = FileSystem.read(parsedInput.value.filePath)
      RETURN ToolResult(error=false, payload={"text": data})

    FileSystem.write(parsedInput.value.filePath, parsedInput.value.content)
    RETURN ToolResult(error=false, payload={"status": "ok"})
```

## Architectural Notes

This demonstrates contract-driven tool design: schema-first validation, centralized permission gating, deterministic execution paths, and a stable result shape. That pattern allows many tools to plug into one orchestration loop without per-tool special cases.

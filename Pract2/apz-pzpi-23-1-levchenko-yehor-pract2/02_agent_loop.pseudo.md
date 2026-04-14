# Example: Agent Loop Pattern

## Description

This example illustrates the iterative query loop pattern where the model can request tools, tool outputs are injected back into the message stream, and the loop repeats until a final assistant response is produced or a terminal error occurs.

## Pseudocode

```text
FUNCTION queryLoop(initialMessages, modelClient, toolRegistry, loopOptions):
  messages = initialMessages
  turnCount = 0

  WHILE true:
    turnCount = turnCount + 1

    modelResponse = modelClient.generate(messages)
    IF modelResponse.error:
      RETURN TerminalResult(status="error", reason="model_error")

    assistantMessage = modelResponse.assistantMessage
    YIELD assistantMessage

    toolUseBlocks = extractBlocks(assistantMessage, type="tool_use")
    IF toolUseBlocks.isEmpty:
      RETURN TerminalResult(status="success", finalMessage=assistantMessage)

    toolResults = []
    FOR EACH toolUseBlock IN toolUseBlocks:
      tool = toolRegistry.find(toolUseBlock.name)
      IF tool IS NULL:
        toolResults.add(makeToolError(toolUseBlock.id, "Unknown tool"))
        CONTINUE

      permissionDecision = tool.checkPermission(toolUseBlock.input, loopOptions.permissionContext)
      IF permissionDecision.behavior = "deny":
        toolResults.add(makeToolError(toolUseBlock.id, permissionDecision.reason))
        CONTINUE

      executionResult = tool.execute(toolUseBlock.input, loopOptions.runtimeContext)
      toolResults.add(makeToolResult(toolUseBlock.id, executionResult))

    FOR EACH toolResultMessage IN toolResults:
      YIELD toolResultMessage

    messages = messages + [assistantMessage] + toolResults

    IF turnCount >= loopOptions.maxTurns:
      RETURN TerminalResult(status="error", reason="max_turns")
```

## Architectural Notes

This demonstrates the core agentic control loop: model planning and tool execution are interleaved through a shared message history. Uniform tool result injection allows the model to continue reasoning with real execution feedback on each turn.

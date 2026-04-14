# Example: Skill Execution Pattern

## Description

This example illustrates how a skill-capable tool resolves and executes reusable prompt workflows: skills are discovered from multiple sources, validated for invocation policy, then executed either inline in the current conversation or in a forked worker context.

## Pseudocode

```text
FUNCTION executeSkill(skillName, skillArgs, skillContext, skillRegistry):
  availableSkills = skillRegistry.discover(
    cwd=skillContext.cwd,
    touchedPaths=skillContext.changedPaths
  )

  skillCommand = availableSkills.findByName(skillName)
  IF skillCommand IS NULL:
    RETURN SkillResult(error=true, message="Skill not found")

  validation = validateSkillInvocation(skillCommand, skillArgs, skillContext)
  IF validation.invalid:
    RETURN SkillResult(error=true, message=validation.reason)

  permissionDecision = checkSkillPermissions(skillCommand, skillContext.permissionContext)
  IF permissionDecision.behavior = "deny":
    RETURN SkillResult(error=true, message=permissionDecision.reason)

  renderedPrompt = renderSkillPrompt(skillCommand, skillArgs, skillContext)

  IF skillCommand.context = "fork":
    forkedRun = runForkedSkillAgent(
      prompt=renderedPrompt,
      allowedTools=skillCommand.allowedTools,
      modelOverride=skillCommand.model
    )
    RETURN SkillResult(error=false, payload=forkedRun.finalText)

  injectIntoCurrentConversation(renderedPrompt)
  RETURN SkillResult(error=false, payload="Skill prompt injected inline")
```

## Architectural Notes

This demonstrates a unified skill contract with late binding: discovery and validation are separate from execution, and context strategy (inline vs fork) is a declarative property of the skill definition rather than hardcoded orchestration logic.

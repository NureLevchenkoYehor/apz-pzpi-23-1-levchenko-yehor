# Example: Multi-Agent Coordination Pattern

## Description

This example illustrates coordinator fan-out and fan-in orchestration: a lead agent decomposes work into parallel tasks, spawns workers, consumes structured task notifications, and synthesizes a final answer once all worker outcomes are collected.

## Pseudocode

```text
FUNCTION runCoordinator(userGoal, workerPool, notificationQueue):
  taskList = planTasks(userGoal)
  taskState = Map()  // taskId -> {status, summary, outputRef}

  FOR EACH task IN taskList:
    taskId = createTaskRecord(task)
    taskState[taskId] = {status: "queued"}

  // Fan-out: spawn workers in parallel
  FOR EACH taskId IN taskState.keys PARALLEL:
    taskSpec = loadTaskSpec(taskId)
    workerHandle = workerPool.spawn(taskSpec)
    taskState[taskId].status = "running"
    taskState[taskId].workerHandle = workerHandle

  completedCount = 0
  WHILE completedCount < taskList.length:
    taskNotification = notificationQueue.waitFor("task-notification")
    taskId = taskNotification.taskId

    IF taskNotification.status = "completed":
      taskState[taskId].status = "completed"
      taskState[taskId].summary = taskNotification.summary
      taskState[taskId].outputRef = taskNotification.outputFile
      completedCount = completedCount + 1
    ELSE IF taskNotification.status = "failed":
      taskState[taskId].status = "failed"
      taskState[taskId].summary = taskNotification.summary
      completedCount = completedCount + 1
    ELSE:
      // optional progress update
      taskState[taskId].status = taskNotification.status

  synthesisInput = collectWorkerOutputs(taskState)
  finalAnswer = synthesizeFinalResponse(userGoal, synthesisInput)
  RETURN finalAnswer
```

## Architectural Notes

This demonstrates explicit orchestration boundaries: workers execute independently, completion is communicated through structured notifications, and the coordinator remains responsible for aggregation and user-facing synthesis rather than low-level execution.

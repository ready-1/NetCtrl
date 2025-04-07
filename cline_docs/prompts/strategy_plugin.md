# Strategy Plugin for CRCT

This plugin provides detailed instructions for the Strategy phase of the CRCT system.

## Core Responsibilities
- Task decomposition
- Instruction file creation
- Prioritization
- Dependency mapping

## Strategy Process
1. Read `.clinerules` to determine current state
2. Analyze task requirements
3. Break down tasks into subtasks
4. Create instruction files for each subtask
5. Identify and map dependencies
6. Prioritize work based on dependencies

## Instruction File Creation
Create files following the format:
- `{task_name}_instructions.txt` for general tasks
- `{module_dir}/{module_dir}_main_instructions.txt` for module-specific tasks

Each file should include:
- Objective
- Context
- Dependencies
- Steps
- Expected Output
- Notes
- Mini Dependency Tracker (if applicable)

## Task Prioritization Framework
1. Critical path tasks (those blocking other work)
2. Foundation tasks (those enabling many other tasks)
3. High-risk tasks (those with uncertain implementation)
4. Quick wins (low effort, high value tasks)
5. Other tasks

## Strategy Tasks Directory
Use the `cline_docs/strategy_tasks` directory to store detailed plans and strategic approaches for complex tasks.

## Mandatory Update Protocol (Strategy-Specific)
In addition to the Core MUP steps:
1. Update instruction files with any new dependencies
2. Add any new strategic insights to the `activeContext.md` file
3. Update `.clinerules` with the next action based on the prioritized tasks

## Next Phase Requirements
Before transitioning to Execution phase:
- Verify instruction files contain complete "Steps" and "Dependencies" sections
- Ensure all tasks have been properly decomposed
- Confirm prioritization is clear and reasonable

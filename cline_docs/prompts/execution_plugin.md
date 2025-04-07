# Execution Plugin for CRCT

This plugin provides detailed instructions for the Execution phase of the CRCT system.

## Core Responsibilities
- Task execution
- Code/file modifications
- Testing and validation
- Documentation updates

## Execution Process
1. Read `.clinerules` to determine current state
2. Load and review instruction files for the current task
3. Check dependencies are met before execution
4. Execute tasks step-by-step
5. Document results and update relevant files
6. Update dependency trackers as work progresses

## Pre-Action Verification
Before any code or file modifications:
1. Verify the current file system state
2. Check for conflicts with other active changes
3. Ensure all dependencies are satisfied
4. Validate assumptions about the codebase

## Incremental Execution
Break implementation into small, verifiable steps:
1. Execute a single logical step
2. Verify the step's success
3. Document the outcome
4. Proceed to the next step only after verification

## Error Handling
When encountering errors:
1. Document the exact error
2. Analyze root causes
3. Determine if the error requires a change in strategy
4. Implement a fix
5. Verify the fix resolves the issue

## Mandatory Update Protocol (Execution-Specific)
In addition to the Core MUP steps:
1. Update tests if code was modified
2. Document implementation decisions in code comments
3. Update user-facing documentation if interfaces changed
4. Record any performance or security considerations

## Next Phase Requirements
Before returning to Strategy phase (if needed):
- Ensure all steps in the instruction file are completed
- Verify all tests pass
- Document any unexpected challenges or insights
- Update dependencies to reflect implementation reality

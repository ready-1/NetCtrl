# Interrogatory Mode Documentation

## Overview
The "???" prefix indicates an interrogatory mode in the system where only information gathering and analysis is permitted, with no system modifications allowed.

## Purpose
This mode exists to separate information gathering from system modification, ensuring that no changes are made to the system during analysis and questioning phases. It creates a clear state transition similar to a "read-only" mode in databases, acting as a safety mechanism to prevent accidental modifications during system exploration and understanding.

## Mental Model
The "???" prefix triggers a cognitive shift from action-oriented to analysis-oriented behavior:
- Promotes careful consideration before action
- Encourages deeper system understanding
- Creates a safe space for exploration
- Enforces explicit boundaries between investigation and modification

## Behavior
When a prompt is prefixed with "???":
- System enters interrogatory (conversation) mode
- Only information gathering and analysis is permitted
- No code changes or system modifications are allowed
- No file creation or modification is permitted
- No state-changing commands can be executed

## Exit Conditions
- Explicit instruction is required to exit interrogatory mode
- System will maintain conversation-only state until instructed otherwise

## Implementation
This behavior is enforced through the INTERROGATORY_PREFIX_REQUIREMENTS section in .clinerules.critical, ensuring consistent handling of interrogatory prompts across all system interactions.

## Example
```
??? what does this prefix mean?
// System will provide analysis and information only
// No system modifications will occur
```

## Critical Rules
The following requirements are enforced:
- REQUIRED: Treat "???" prefix as interrogatory mode indicator
- REQUIRED: Provide information and analysis only
- REQUIRED: Maintain conversation-only mode
- REQUIRED: Wait for explicit instruction before making changes
- FORBIDDEN: Make any code or system changes
- FORBIDDEN: Create or modify any files
- FORBIDDEN: Execute any state-changing commands
- FORBIDDEN: Exit interrogatory mode without explicit instruction

# NetCtrl

A network control system.

## Project Structure

- `src/` - Source code
- `tests/` - Test files
- `utils/` - Utility functions and helpers
- `cline_docs/` - CRCT system documentation and operational memory
  - `prompts/` - Phase-specific plugin instructions
  - `strategy_tasks/` - Detailed plans and strategic approaches
- `docs/` - Project documentation

## Development

This project uses the Cline Recursive Chain-of-Thought System (CRCT) for development management.

### CRCT System

The CRCT system manages complex tasks via recursive decomposition and persistent state. The system operates in distinct phases:

1. Set-up/Maintenance - Project initialization and system maintenance
2. Strategy - Task decomposition and planning
3. Execution - Task implementation and validation

Current phase and next actions are tracked in the `.clinerules` file.

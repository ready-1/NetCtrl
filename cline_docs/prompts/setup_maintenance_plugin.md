# Setup and Maintenance Plugin for CRCT

This plugin provides detailed instructions for the Set-up/Maintenance phase of the CRCT system.

## Core Responsibilities
- Project initialization
- Identifying code root directories
- Setting up dependency tracking
- Maintaining system files
- Periodic maintenance tasks

## Setup Procedure
1. Read `.clinerules` to determine the current state
2. Identify Code Root Directories
3. Generate dependency tracker keys
4. Create necessary directory structure
5. Initialize version control if needed

## Dependency Tracker Management
Detailed steps for using the `dependency_processor.py` script to manage trackers:

### Creating Main Dependency Tracker
```
python -m cline_utils.dependency_system.dependency_processor generate-keys [CODE_ROOT_DIRS] --output cline_docs/dependency_tracker.md --tracker_type main
```

### Creating Doc Tracker
```
python -m cline_utils.dependency_system.dependency_processor generate-keys docs --output docs/doc_tracker.md --tracker_type doc
```

## Mandatory Update Protocol (Set-up/Maintenance-Specific)
In addition to the Core MUP steps:
1. Update dependency trackers if files were added or removed
2. Ensure `.clinerules` reflects the current code root directories
3. Check and update `[LAST_ACTION_STATE]` in `.clinerules`

## Next Phase Requirements
Before transitioning to Strategy phase:
- Confirm dependency trackers have no placeholder ('p') values
- Ensure `[CODE_ROOT_DIRECTORIES]` is populated in `.clinerules`
- Validate all required files exist and are properly initialized

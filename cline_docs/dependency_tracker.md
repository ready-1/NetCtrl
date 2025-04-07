# Module-Level Dependency Tracker

This file tracks module-level dependencies for the NetCtrl project.

**IMPORTANT:** This is a placeholder file. The actual dependency tracker should be generated using:

```
python -m cline_utils.dependency_system.dependency_processor generate-keys src tests utils --output cline_docs/dependency_tracker.md --tracker_type main
```

## Dependency Matrix

*To be generated*

## Legend

- `<`: Row depends on column.
- `>`: Column depends on row.
- `x`: Mutual dependency.
- `d`: Documentation dependency.
- `o`: No dependency (diagonal only).
- `n`: Verified no dependency.
- `p`: Placeholder (unverified).
- `s`: Semantic dependency

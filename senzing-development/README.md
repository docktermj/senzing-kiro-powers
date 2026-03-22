# Senzing Power - Development Documentation

This directory contains development and historical documentation for the Senzing Kiro Power.

## Purpose

These files document the **development process** and are **not part of the user-facing power**. They are kept separate to:
- Keep the power clean and focused on user needs
- Preserve development history and decisions
- Provide reference for future power development

## Contents

### docs/IMPROVEMENTS_SUMMARY.md
Complete history of all improvements made to the power during development:
- Implementation timeline
- Feature descriptions
- File changes and reorganizations
- Statistics and benefits

**Audience**: Power maintainers, contributors, historians

### docs/METADATA.md
Documentation about power metadata fields:
- Field descriptions and purposes
- Best practices for metadata
- Usage examples
- Validation guidelines

**Audience**: Power creators building similar powers

### docs/PRODUCTION_READY.md
Production readiness certification (v1.0.0):
- Completion checklists
- Quality metrics
- Validation results
- Deployment readiness assessment

**Audience**: Stakeholders, project managers

### docs/README.md
Explains the purpose of the docs directory.

## User-Facing Power

The actual Senzing power for end users is in the `../senzing/` directory:

```
senzing/
├── POWER.md                    # Main power documentation
├── CHANGELOG.md                # Version history
├── mcp.json                    # MCP server configuration
├── validate_power.py           # Validation tool
└── steering/                   # User guides (20 files)
```

## Why Separate?

**Before** (v0.1.0):
```
senzing/
├── POWER.md
├── docs/                       # Development docs mixed in
│   ├── IMPROVEMENTS_SUMMARY.md
│   ├── METADATA.md
│   └── PRODUCTION_READY.md
└── steering/
```

**After** (v1.0.0):
```
senzing/                        # Clean, user-focused
├── POWER.md
├── CHANGELOG.md
├── mcp.json
├── validate_power.py
└── steering/

senzing-development/            # Development history
└── docs/
    ├── IMPROVEMENTS_SUMMARY.md
    ├── METADATA.md
    └── PRODUCTION_READY.md
```

## Benefits

1. **Cleaner power**: Users only see what they need
2. **Smaller distribution**: Power is ~50KB lighter
3. **Preserved history**: Development documentation is not lost
4. **Clear separation**: User docs vs development docs
5. **Professional structure**: Industry best practice

## For Power Maintainers

When updating the power:

1. Update version in `../senzing/POWER.md`
2. Document changes in `../senzing/CHANGELOG.md`
3. Run `../senzing/validate_power.py`
4. Optionally update development docs here if significant architectural changes

## For Power Creators

If you're building a similar power:
- Review `docs/METADATA.md` for metadata best practices
- Review `docs/IMPROVEMENTS_SUMMARY.md` to see what features were added
- Use the final structure in `../senzing/` as a template

## Archive Status

This directory is effectively an **archive** of development documentation. It's not actively maintained but preserved for reference.

---

**Note**: To use the Senzing power, go to `../senzing/` - this directory is for development reference only.

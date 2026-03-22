# Power Development Documentation

This directory contains meta-documentation about the Senzing Kiro Power's development and construction.

## Purpose

These files are for **power creators and maintainers**, not end users. They document:
- How the power was built
- What improvements were made
- Production readiness status
- Metadata field documentation

## Files

### IMPROVEMENTS_SUMMARY.md
Complete history of all improvements made to the power, including:
- Implementation dates
- Feature descriptions
- File changes
- Benefits and statistics

**Audience**: Power maintainers, contributors

### METADATA.md
Documentation about the power's metadata fields in POWER.md frontmatter:
- Field descriptions
- Best practices
- Usage examples
- Validation guidelines

**Audience**: Power creators, those building similar powers

### PRODUCTION_READY.md
Production readiness certification document:
- Completion checklists
- Quality metrics
- Validation results
- Deployment readiness assessment

**Audience**: Power maintainers, stakeholders

## User-Facing Documentation

If you're looking for **how to use** the Senzing power, see:

- **[../POWER.md](../POWER.md)** - Main power documentation
- **[../CHANGELOG.md](../CHANGELOG.md)** - Version history
- **[../steering/](../steering/)** - User guides (20 files)

## For Power Maintainers

When updating the power:

1. Update version in `POWER.md` frontmatter
2. Document changes in `CHANGELOG.md`
3. Update `IMPROVEMENTS_SUMMARY.md` if adding features
4. Run `validate_power.py` to verify structure
5. Update `last_updated` date in `POWER.md`

## Directory Structure

```
senzing/
├── POWER.md                    # Main entry point (user-facing)
├── CHANGELOG.md                # Version history (user-facing)
├── mcp.json                    # Configuration (user-facing)
├── validate_power.py           # Validation tool (user-facing)
├── docs/                       # Power development docs (this directory)
│   ├── README.md               # This file
│   ├── IMPROVEMENTS_SUMMARY.md # Development history
│   ├── METADATA.md             # Metadata documentation
│   └── PRODUCTION_READY.md     # Production certification
└── steering/                   # User guides (20 files)
    ├── steering.md             # Navigation hub
    ├── getting-started.md      # Quick start
    └── ...                     # 18 more guides
```

## Contributing

When contributing to the power:

1. Read `IMPROVEMENTS_SUMMARY.md` to understand what's been done
2. Follow patterns established in existing files
3. Update all relevant documentation
4. Run validation before submitting changes
5. Update this directory's files as appropriate

---

**Note**: This directory is for power development documentation. End users should start with [../POWER.md](../POWER.md).

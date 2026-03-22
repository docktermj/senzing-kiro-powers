# Changelog

All notable changes to the Senzing Kiro Power will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional language examples (TypeScript, Go)
- Video tutorial references
- Interactive tutorials
- Community-contributed content

## [1.0.0] - 2026-03-22

### Changed
- **BREAKING**: Updated license from CC-BY-4.0 to Apache-2.0 for consistency
- **BREAKING**: Removed Senzing V3 compatibility references (V4 only)
- Updated version to 1.0.0 (stable release)
- Updated last_updated date to 2026-03-22
- Reorganized file structure:
  - Moved user-facing guides to `steering/` directory
  - Moved power development documentation to `docs/` directory
- Updated all internal references to reflect new file locations
- Updated validation script to check for files in new locations

### Removed
- V3 compatibility note from Version Compatibility section
- References to `version: "3.x"` parameter

## [0.1.0] - 2026-03-21

### Added

#### Core Documentation
- Initial POWER.md with comprehensive metadata
- MCP server configuration (mcp.json)
- METADATA.md with detailed field descriptions
- IMPROVEMENTS_SUMMARY.md tracking all enhancements

#### Steering Guides (16 files)
- **steering.md** - Navigation hub with quick links
- **getting-started.md** - Quick start, workflows, decision trees, ASCII diagrams
- **quick-reference.md** - Copy-paste ready commands and one-liners
- **best-practices.md** - Do's, don'ts, common pitfalls
- **performance.md** - Optimization, tuning, scaling strategies
- **troubleshooting.md** - Error handling, debugging, typical sessions
- **examples.md** - Code examples (Python, Java, C#)
- **use-cases.md** - 5 real-world implementation walkthroughs
- **security-compliance.md** - GDPR, CCPA, PII handling, access control
- **advanced-topics.md** - Custom config, network analysis, graph traversal
- **monitoring.md** - Metrics, Prometheus, Grafana, alerting
- **data-sources.md** - 20+ system integrations (CRM, ERP, e-commerce)
- **cicd.md** - GitHub Actions, GitLab CI, Jenkins, deployment
- **faq.md** - 100+ questions covering all topics
- **community.md** - Resources, support, learning materials
- **reference.md** - Tool parameters, checklists, glossary (50+ terms)

#### Validation and Testing
- **validate_power.py** - Comprehensive validation script (400+ lines)
- **SMOKE_TEST.md** - Quick and detailed smoke test procedures
- **TEST_EXAMPLES.md** - Unit, integration, and end-to-end tests

#### Configuration
- **OFFLINE_MODE.md** - Offline usage documentation
- **CONFIG_EXAMPLES.md** - Configuration examples for various scenarios

#### Metadata
- Enhanced frontmatter with 17 fields
- Visual badges (version, maturity, license, compatibility)
- Quick links bar (homepage, docs, support, GitHub)
- Metadata reference table

#### Features
- 22 keywords for discoverability
- 5 categorical tags
- Maturity indicator (stable)
- Version compatibility tracking
- MCP server configuration with timeout and logging
- 4 interactive checklists (100+ items)
- 3 ASCII workflow diagrams
- 5 integration patterns
- 5 real-world use cases with metrics
- 50+ glossary terms
- 100+ FAQ items
- 50+ code examples across multiple languages

### Documentation Coverage
- Getting started and quick reference
- Best practices and common pitfalls
- Performance optimization and tuning
- Troubleshooting and error handling
- Security and compliance (GDPR, CCPA)
- Advanced techniques and network analysis
- Monitoring and observability
- Data source integration (20+ systems)
- CI/CD integration (5 platforms)
- Community resources and support

### Quality Assurance
- Automated validation script
- File structure validation
- Metadata validation
- Internal link validation
- MCP configuration validation
- Smoke test procedures
- Test examples and suites

### Statistics
- 25 total files
- 16 steering guides
- 100+ FAQ items
- 50+ code examples
- 50+ glossary terms
- 20+ data source integrations
- 5 CI/CD platform examples
- 5 real-world use cases
- 4 interactive checklists
- 3 ASCII diagrams

## Version History

### Version Numbering

This power follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version: Incompatible API changes or breaking changes
- **MINOR** version: New functionality in a backward compatible manner
- **PATCH** version: Backward compatible bug fixes

### Release Process

1. Update version in POWER.md frontmatter
2. Update last_updated date
3. Document changes in CHANGELOG.md
4. Run validation: `python validate_power.py`
5. Run smoke tests
6. Update IMPROVEMENTS_SUMMARY.md
7. Tag release in version control

## Migration Guides

### Migrating to 0.1.0

This is the initial release. No migration needed.

### Future Migrations

Migration guides will be added here when breaking changes are introduced.

## Breaking Changes

### 0.1.0
- None (initial release)

## Deprecations

### 0.1.0
- None (initial release)

## Known Issues

### 0.1.0
- None reported

## Contributors

### 0.1.0
- Initial development and documentation
- Comprehensive steering guide creation
- Validation and testing infrastructure
- Metadata enhancements

## Support

For questions about specific versions:
- Check the version's section in this changelog
- Review IMPROVEMENTS_SUMMARY.md for detailed changes
- Use `submit_feedback` MCP tool
- Contact Senzing support: https://senzing.zendesk.com

## Links

- [Homepage](https://senzing.com)
- [Documentation](https://senzing.com/documentation)
- [Support](https://senzing.zendesk.com/hc/en-us/requests/new)
- [GitHub](https://github.com/senzing)

## Changelog Maintenance

This changelog is manually maintained. When making changes:

1. **Add entries under [Unreleased]** for work in progress
2. **Move to versioned section** when releasing
3. **Use categories**: Added, Changed, Deprecated, Removed, Fixed, Security
4. **Be specific**: Include file names, feature names, and impacts
5. **Link issues**: Reference issue numbers when applicable
6. **Date releases**: Use ISO 8601 format (YYYY-MM-DD)

### Categories

- **Added**: New features, files, or capabilities
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed in future versions
- **Removed**: Features that have been removed
- **Fixed**: Bug fixes
- **Security**: Security-related changes

## Future Versions

### Planned for 0.2.0
- Additional language examples (TypeScript, Go)
- Video tutorial references
- Enhanced search/index optimization
- Power health check improvements

### Planned for 1.0.0
- Stable API declaration
- Complete documentation coverage
- Full test suite
- Production deployment validation
- Community feedback incorporation

## Notes

- This power integrates with Senzing MCP server (Apache-2.0)
- Power documentation is licensed under Apache-2.0
- Compatible with Senzing SDK 4.0+
- Requires internet connection for MCP server access (see OFFLINE_MODE.md for alternatives)

---

**Note**: This changelog tracks changes to the Senzing Kiro Power itself, not changes to the Senzing SDK or MCP server. For Senzing product changes, see official Senzing release notes.

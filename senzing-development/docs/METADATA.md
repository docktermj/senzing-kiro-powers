# Senzing Power - Metadata Documentation

This document explains the metadata strategy for the Senzing Kiro Power.

## Overview

Power metadata provides structured information about the power for:
- **Discovery**: Help users find the power through search
- **Integration**: Enable programmatic access to power information
- **Quality**: Communicate stability and compatibility
- **Attribution**: Proper licensing and credit
- **Support**: Quick access to help resources

## Metadata Fields

### Core Identity

#### name
- **Type**: String
- **Value**: `senzing`
- **Purpose**: Unique identifier for the power
- **Usage**: Used in code, configuration files, and CLI commands
- **Rules**: Lowercase, no spaces, alphanumeric with hyphens

#### displayName
- **Type**: String
- **Value**: `Senzing`
- **Purpose**: Human-readable name for UI display
- **Usage**: Shown in power browsers, documentation, and interfaces
- **Rules**: Proper capitalization, can include spaces

#### version
- **Type**: String (Semantic Version)
- **Value**: `0.1.0`
- **Purpose**: Track power versions
- **Format**: `MAJOR.MINOR.PATCH`
- **Rules**: 
  - MAJOR: Breaking changes
  - MINOR: New features, backward compatible
  - PATCH: Bug fixes, backward compatible

#### description
- **Type**: String
- **Value**: "Senzing entity resolution. Covers data mapping, SDK setup, loading, performance testing, security hardening, monitoring, and production deployment."
- **Purpose**: Brief summary of power capabilities
- **Length**: 1-2 sentences, ~200 characters max
- **Rules**: Clear, concise, action-oriented

### Discovery

#### keywords
- **Type**: Array of Strings
- **Value**: 22 keywords including "Senzing", "Entity Resolution", "Data Mapping", etc.
- **Purpose**: Enable search and discovery
- **Usage**: Search engines, power browsers, filtering
- **Rules**: 
  - Include product name
  - Include primary use cases
  - Include technical terms
  - Include business terms
  - 10-30 keywords recommended

#### tags
- **Type**: Array of Strings
- **Value**: `["entity-resolution", "data-quality", "mdm", "deduplication", "identity-resolution"]`
- **Purpose**: Categorical classification
- **Usage**: Filtering, grouping, related power suggestions
- **Rules**: 
  - Lowercase with hyphens
  - 3-7 tags recommended
  - Use standard categories when possible

#### category
- **Type**: String
- **Value**: `data-integration`
- **Purpose**: Primary category for organization
- **Usage**: Top-level filtering and navigation
- **Options**: 
  - `data-integration`
  - `analytics`
  - `development`
  - `security`
  - `infrastructure`
  - `ai-ml`
  - `business-intelligence`

### Attribution

#### author
- **Type**: String
- **Value**: `Senzing`
- **Purpose**: Identify creator/maintainer
- **Usage**: Attribution, contact information
- **Rules**: Organization or individual name

#### homepage
- **Type**: URL
- **Value**: `https://senzing.com`
- **Purpose**: Official website for more information
- **Usage**: Link to vendor/product site
- **Rules**: Must be valid HTTPS URL

#### repository
- **Type**: URL
- **Value**: `https://github.com/senzing`
- **Purpose**: Source code location
- **Usage**: Link to code repositories, issue tracking
- **Rules**: Must be valid URL (GitHub, GitLab, etc.)

#### license
- **Type**: String (SPDX License Identifier)
- **Value**: `Apache-2.0`
- **Purpose**: License for power content
- **Usage**: Legal compliance, attribution requirements
- **Rules**: Use SPDX identifiers (MIT, Apache-2.0, BSD-3-Clause, etc.)
- **Note**: This is for the power documentation, not the underlying software

### Quality

#### maturity
- **Type**: String (Enum)
- **Value**: `stable`
- **Purpose**: Communicate stability level
- **Options**:
  - `alpha`: Early development, expect breaking changes
  - `beta`: Feature-complete, testing phase, minor changes possible
  - `stable`: Production-ready, stable API, semantic versioning
- **Usage**: Help users assess risk and readiness

#### senzing_compatibility
- **Type**: Array of Strings
- **Value**: `["4.0"]`
- **Purpose**: Specify compatible Senzing SDK versions
- **Usage**: Compatibility checking, version selection
- **Rules**: Array of version strings or ranges

### Integration

#### mcp_server_url
- **Type**: URL
- **Value**: `https://mcp.senzing.com/mcp`
- **Purpose**: MCP server endpoint
- **Usage**: Connection configuration
- **Rules**: Must be valid URL

#### mcp_server_license
- **Type**: String (SPDX License Identifier)
- **Value**: `Apache-2.0`
- **Purpose**: License of the MCP server
- **Usage**: Legal compliance
- **Rules**: Use SPDX identifiers
- **Note**: This is for the MCP server, not the power documentation

### Support

#### support_url
- **Type**: URL
- **Value**: `https://senzing.zendesk.com/hc/en-us/requests/new`
- **Purpose**: Direct link to support
- **Usage**: Help users get assistance
- **Rules**: Must be valid URL

#### documentation_url
- **Type**: URL
- **Value**: `https://senzing.com/documentation`
- **Purpose**: Official documentation location
- **Usage**: Link to comprehensive docs
- **Rules**: Must be valid URL

#### last_updated
- **Type**: Date (ISO 8601)
- **Value**: `2026-03-21`
- **Purpose**: Track when power was last modified
- **Format**: `YYYY-MM-DD`
- **Usage**: Show freshness, trigger update checks

## Metadata Best Practices

### 1. Keep Metadata Current
- Update `version` with each release
- Update `last_updated` with significant changes
- Review `keywords` and `tags` periodically
- Update `senzing_compatibility` when new versions are supported

### 2. Use Standard Values
- Use SPDX license identifiers
- Use ISO 8601 date format
- Use semantic versioning
- Use lowercase-with-hyphens for tags

### 3. Be Descriptive
- Write clear, concise descriptions
- Include relevant keywords
- Use specific, searchable terms
- Avoid marketing jargon

### 4. Maintain Consistency
- Use consistent naming conventions
- Follow established patterns
- Keep similar powers aligned
- Document deviations

### 5. Validate Metadata
- Check all URLs are valid
- Verify license identifiers
- Ensure version format is correct
- Test that metadata renders correctly

## Metadata Usage Examples

### Searching for Powers
```javascript
// Find powers by keyword
powers.filter(p => p.keywords.includes("Entity Resolution"))

// Find powers by category
powers.filter(p => p.category === "data-integration")

// Find stable powers
powers.filter(p => p.maturity === "stable")
```

### Displaying Power Information
```javascript
// Show power card
{
  title: power.displayName,
  description: power.description,
  version: power.version,
  maturity: power.maturity,
  author: power.author
}
```

### Checking Compatibility
```javascript
// Check if power supports Senzing 4.0
power.senzing_compatibility.includes("4.0")
```

### Generating Badges
```markdown
![Version](https://img.shields.io/badge/version-{version}-blue)
![Maturity](https://img.shields.io/badge/maturity-{maturity}-green)
![License](https://img.shields.io/badge/license-{license}-lightgrey)
```

## Metadata Validation

### Required Fields
- ✅ name
- ✅ displayName
- ✅ version
- ✅ description
- ✅ author

### Recommended Fields
- ✅ keywords
- ✅ homepage
- ✅ license
- ✅ category
- ✅ maturity
- ✅ support_url
- ✅ last_updated

### Optional Fields
- ✅ repository
- ✅ tags
- ✅ documentation_url
- ✅ mcp_server_url
- ✅ mcp_server_license
- ✅ senzing_compatibility

## Metadata Changelog

### Version 0.1.0 (2026-03-21)
- Initial metadata structure
- Added all core fields
- Added discovery fields (keywords, tags, category)
- Added attribution fields (author, homepage, repository, license)
- Added quality fields (maturity, compatibility)
- Added integration fields (mcp_server_url, mcp_server_license)
- Added support fields (support_url, documentation_url)
- Added visual badges to POWER.md
- Created metadata reference section

## Future Enhancements

Potential metadata additions for future versions:

1. **icon**: Path to power icon/logo
2. **screenshots**: Array of screenshot URLs
3. **video**: URL to demo video
4. **dependencies**: Array of required dependencies
5. **platforms**: Supported platforms (linux, macos, windows)
6. **languages**: Supported programming languages
7. **min_kiro_version**: Minimum Kiro version required
8. **contributors**: Array of contributor names
9. **changelog_url**: Link to changelog
10. **demo_url**: Link to live demo

## References

- [Semantic Versioning](https://semver.org/)
- [SPDX License List](https://spdx.org/licenses/)
- [ISO 8601 Date Format](https://en.wikipedia.org/wiki/ISO_8601)
- [Creative Commons Licenses](https://creativecommons.org/licenses/)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

For questions about power metadata:
- Use `submit_feedback` MCP tool
- Contact Senzing support
- Open an issue in the repository

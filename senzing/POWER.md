---
name: "senzing"
displayName: "Senzing"
version: "1.0.0"
description: "Senzing entity resolution. Covers data mapping, SDK setup, loading, performance testing, security hardening, monitoring, and production deployment."
keywords: ["Senzing", "Entity Resolution", "Data Mapping", "SDK", "Identity Resolution", "Data Matching", "ER", "Performance", "Security", "Monitoring", "Deployment", "Data Quality", "Deduplication", "Master Data", "MDM", "Record Linkage", "Fuzzy Matching", "Customer 360", "KYC", "Fraud Detection", "Data Integration", "Data Cleansing"]
author: "Senzing"
homepage: "https://senzing.com"
repository: "https://github.com/senzing"
license: "Apache-2.0"
category: "data-integration"
tags: ["entity-resolution", "data-quality", "mdm", "deduplication", "identity-resolution"]
maturity: "stable"
senzing_compatibility: ["4.0"]
mcp_server_url: "https://mcp.senzing.com/mcp"
mcp_server_license: "Apache-2.0"
support_url: "https://senzing.zendesk.com/hc/en-us/requests/new"
documentation_url: "https://senzing.com/documentation"
last_updated: "2026-03-22"
---

# Power: Senzing

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Maturity](https://img.shields.io/badge/maturity-stable-green) ![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey) ![Senzing](https://img.shields.io/badge/senzing-4.0-orange)

> **Entity Resolution and Identity Matching** - Comprehensive Senzing integration covering data mapping, SDK setup, performance optimization, security, and production deployment.

**Quick Links**: [Homepage](https://senzing.com) | [Documentation](https://senzing.com/documentation) | [Support](https://senzing.zendesk.com/hc/en-us/requests/new) | [GitHub](https://github.com/senzing)

---

## License and support

This power integrates with senzing-mcp-server (Apache-2.0).

- [Privacy Policy](https://mcp.senzing.com/privacy)
- [Support](https://senzing.zendesk.com/hc/en-us/requests/new)

## Quick Start

New to Senzing? Follow this sequence:

1. **Discover capabilities**: `get_capabilities` with `version: "current"`
2. **Get sample data**: `get_sample_data` with `dataset: "las-vegas"` and `limit: 100`
3. **Map your data**: `mapping_workflow` with `action: "start"` and your file paths
4. **Validate mapping**: `lint_record` with your mapped file paths
5. **Generate loader code**: `generate_scaffold` with `language: "python"`, `workflow: "full_pipeline"`, `version: "current"`

Typical workflow: Map data → Validate → Generate loader → Load → Query results

## Available MCP Tools

The Senzing MCP server provides these tools:

- `get_capabilities` — Discover all tools and workflows (call this first)
- `mapping_workflow` — 7-step interactive data mapping to Senzing JSON
- `lint_record` / `analyze_record` — Validate and analyze mapped data quality
- `generate_scaffold` — Generate SDK code (Python, Java, C#, Rust)
- `sdk_guide` — Platform-specific SDK installation and setup
- `get_sample_data` — Sample datasets for testing
- `find_examples` — Working code from 27 Senzing GitHub repos
- `search_docs` — Search indexed Senzing documentation
- `explain_error_code` — Diagnose Senzing errors (456 codes)
- `get_sdk_reference` — SDK method signatures and flags
- `download_resource` — Download SDK packages
- `submit_feedback` — Report issues or suggestions

## Common Workflows

**Evaluate Senzing (First Time)**
```
get_capabilities → get_sample_data → sdk_guide (install) → 
generate_scaffold (full_pipeline) → load sample data → query results
```

**Map New Data Source**
```
mapping_workflow (start) → mapping_workflow (advance through steps) → 
lint_record → analyze_record → generate_scaffold (add_records)
```

**Production Deployment**
```
search_docs (category: "deployment") → sdk_guide (platform-specific) → 
generate_scaffold (full_pipeline) → search_docs (category: "database") → 
deploy and monitor
```

**Troubleshoot Issues**
```
explain_error_code → search_docs (category: "troubleshooting") → 
find_examples → get_sdk_reference
```

## Version Compatibility

- **Senzing SDK**: 4.0+ (current version)
- **MCP Server**: Latest version at mcp.senzing.com
- **Python SDK**: 4.0+
- **Java SDK**: 4.0+
- **C# SDK**: 4.0+
- **Rust SDK**: 4.0+

## Best Practices

- Always call `get_capabilities` first when starting a Senzing session
- Never hand-code Senzing JSON mappings — use `mapping_workflow` for validated attribute names
- Never guess SDK method signatures — use `generate_scaffold` or `sdk_guide`
- Check `search_docs` with category `anti_patterns` before recommending installation or deployment approaches
- Start with SQLite for evaluation; recommend PostgreSQL for production

## Troubleshooting

- **Wrong attribute names**: Never guess Senzing attribute names (e.g., `NAME_ORG` not `BUSINESS_NAME_ORG`). Use `mapping_workflow`.
- **Wrong method signatures**: Never guess SDK methods. Use `generate_scaffold` or `get_sdk_reference`.
- **Error codes**: Use `explain_error_code` with the code (accepts `SENZ0005`, `0005`, or `5`).
- **Configuration issues**: Use `search_docs` with category `configuration` or `database`.
- **Network/connectivity issues**: Check that mcp.senzing.com is reachable. Verify firewall rules allow HTTPS traffic. Check timeout settings in `mcp.json`.
- **MCP server unavailable**: If the remote server is down, check status at https://mcp.senzing.com/status or contact support.
- **Tool failures**: If an MCP tool returns unexpected results, use `submit_feedback` to report the issue with details.
- **Rate limits**: The MCP server has no hard rate limits, but excessive concurrent requests may be throttled. Space out bulk operations.

## Data Privacy and Security

- **Remote MCP server**: The Senzing MCP server at mcp.senzing.com processes tool requests remotely
- **Data transmission**: When using `mapping_workflow`, source data is sent to the server for analysis and mapping
- **No data retention**: The MCP server does not store your source data or mapped records beyond the session
- **Sample data**: `get_sample_data` returns publicly available datasets (CORD collections)
- **Sensitive data**: For highly sensitive data, consider running mapping workflows locally or using on-premises Senzing installations
- **Network security**: All communication uses HTTPS encryption
- **Compliance**: Review your organization's data handling policies before using cloud-based mapping tools

For on-premises or air-gapped deployments, contact Senzing support for alternative deployment options.

## Detailed Guidance

See steering files for detailed workflows:
- [steering/getting-started.md](steering/getting-started.md) - Quick start, decision trees, common workflows
- [steering/best-practices.md](steering/best-practices.md) - Best practices, anti-patterns, common pitfalls
- [steering/performance.md](steering/performance.md) - Performance tuning, database selection, optimization
- [steering/troubleshooting.md](steering/troubleshooting.md) - Error handling, debugging strategies, typical sessions
- [steering/examples.md](steering/examples.md) - Code examples and patterns
- [steering/reference.md](steering/reference.md) - Tool parameters, checklists, glossary

## Additional Resources

### Power Infrastructure
- [CHANGELOG.md](CHANGELOG.md) - Version history and release notes
- [validate_power.py](validate_power.py) - Automated validation script

### User Guides
- [steering/offline-mode.md](steering/offline-mode.md) - Offline usage and air-gapped deployments
- [steering/config-examples.md](steering/config-examples.md) - Configuration examples for all scenarios
- [steering/smoke-test.md](steering/smoke-test.md) - Quick validation and testing procedures

---

## Power Metadata Reference

This power includes the following metadata for discoverability and integration:

| Field | Value | Description |
|-------|-------|-------------|
| **name** | senzing | Unique identifier for the power |
| **displayName** | Senzing | Human-readable name shown in UI |
| **version** | 1.0.0 | Semantic version of this power |
| **description** | Entity resolution... | Brief description of capabilities |
| **keywords** | [22 keywords] | Search terms for discoverability |
| **author** | Senzing | Power creator/maintainer |
| **homepage** | https://senzing.com | Official Senzing website |
| **repository** | https://github.com/senzing | Source code repositories |
| **license** | Apache-2.0 | License for power documentation |
| **category** | data-integration | Primary category |
| **tags** | [5 tags] | Categorical tags |
| **maturity** | stable | Stability level (alpha/beta/stable) |
| **senzing_compatibility** | [4.0] | Compatible Senzing versions |
| **mcp_server_url** | https://mcp.senzing.com/mcp | MCP server endpoint |
| **mcp_server_license** | Apache-2.0 | MCP server license |
| **support_url** | https://senzing.zendesk.com | Support portal |
| **documentation_url** | https://senzing.com/documentation | Official documentation |
| **last_updated** | 2026-03-22 | Last modification date |

### Metadata Field Descriptions

**Core Identity**:
- `name`: Unique identifier used in code and configuration
- `displayName`: User-facing name shown in interfaces
- `version`: Follows semantic versioning (MAJOR.MINOR.PATCH)
- `description`: One-line summary of power capabilities

**Discovery**:
- `keywords`: Array of search terms for finding this power
- `tags`: Categorical tags for filtering and organization
- `category`: Primary category (data-integration, analytics, etc.)

**Attribution**:
- `author`: Creator or maintainer of the power
- `license`: License for the power content (documentation, examples)
- `homepage`: Official website for more information
- `repository`: Source code location

**Quality**:
- `maturity`: Stability indicator
  - `alpha`: Early development, may have breaking changes
  - `beta`: Feature-complete, testing phase
  - `stable`: Production-ready, stable API

**Integration**:
- `senzing_compatibility`: Array of compatible Senzing SDK versions
- `mcp_server_url`: Endpoint for the MCP server
- `mcp_server_license`: License of the underlying MCP server

**Support**:
- `support_url`: Where to get help
- `documentation_url`: Official documentation location
- `last_updated`: Date of last significant update (YYYY-MM-DD)

### Using Metadata

Power metadata can be used for:
- **Discovery**: Search by keywords or tags
- **Filtering**: Filter powers by category or maturity
- **Validation**: Check compatibility before installation
- **Attribution**: Proper licensing and credit
- **Support**: Quick access to help resources

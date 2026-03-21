---
name: "senzing"
displayName: "Senzing"
version: "0.1.0"
description: "Senzing entity resolution. Covers data mapping, SDK setup, loading, performance testing, security hardening, monitoring, and production deployment."
keywords: ["Senzing", "Entity Resolution", "Data Mapping", "SDK", "Identity Resolution", "Data Matching", "ER", "Performance", "Security", "Monitoring", "Deployment", "Data Quality", "Deduplication", "Master Data", "MDM", "Record Linkage", "Fuzzy Matching", "Customer 360", "KYC", "Fraud Detection", "Data Integration", "Data Cleansing"]
author: "Senzing"
senzing_compatibility: ["4.0"]
last_updated: "2026-03-17"
---

# Power: Senzing

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

For V3 compatibility, use `version: "3.x"` parameter where supported (Python and Java only).

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

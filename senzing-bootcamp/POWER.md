---
name: "senzing-bootcamp"
displayName: "Senzing Boot Camp"
description: "Guided discovery of Senzing entity resolution. Walk through data mapping, SDK setup, record loading, and result exploration using the Senzing MCP server."
keywords: ["Entity Resolution", "Senzing", "Data Mapping", "SDK", "Identity Resolution", "Data Matching", "ER"]
author: "Senzing"
---

# Power: Senzing Boot Camp

## Overview

This power provides a guided boot camp experience for learning Senzing entity resolution. It connects to the Senzing MCP server to provide interactive, tool-assisted workflows covering data mapping, SDK installation, record loading, and entity resolution exploration.

Senzing is an embeddable entity resolution engine that resolves records about people and organizations across data sources — matching, relating, and deduplicating without manual rules or model training.

## Available MCP Servers

### senzing-mcp-server

- **URL**: `https://mcp.senzing.com/mcp`
- **Purpose**: AI-assisted entity resolution tools — data mapping, SDK code generation, documentation search, troubleshooting, and sample data access.
- **Key tools**:
  - `get_capabilities` — Discover all available tools and workflows (call this first)
  - `mapping_workflow` — 7-step interactive data mapping from source files to Senzing JSON format
  - `lint_record` / `analyze_record` — Validate and analyze mapped data quality
  - `generate_scaffold` — Generate SDK code (Python, Java, C#, Rust) for common workflows
  - `sdk_guide` — Platform-specific SDK installation and pipeline setup
  - `get_sample_data` — Sample datasets (Las Vegas, London, Moscow) for testing
  - `find_examples` — Working code examples from 27 Senzing GitHub repositories
  - `search_docs` — Search indexed Senzing documentation
  - `explain_error_code` — Diagnose Senzing errors (456 error codes)
  - `get_sdk_reference` — SDK method signatures, flags, and V3-to-V4 migration

## Boot Camp Learning Path

The boot camp follows a progressive learning path. Each module builds on the previous one.

### Module 1: Understand the User's business problem

- Ask user to describe the problem to be solved.
- If an image is submitted, ask user to instantiate all of the [variable] in the image.
- In the future, present Entity Resolution design patterns that may be useful in solving the business problem. (This is not ready yet.)
- Present to the user the proposal for solving the user's business problem.

### Module 2: Determine if data sources adhere to the Senzing Generic Entity Specification

- Ask the user for example data for each data source.
- Compare each data source with the Senzing Generic Entity Specification (SGES)
- For each data source that does not conform to the SGES, perform Module 3: Map Your data

### Module 3: Map Your Data

- Profile source data to understand its structure
- Plan entity structure (master entities, children, relationships)
- Map source fields to Senzing features and attributes
- Generate mapper code and sample JSON output
- Validate and analyze mapped data quality

**Agent behavior**: Use `mapping_workflow` to guide the 7-step process interactively. Use `lint_record` and `analyze_record` for validation. Never hand-code Senzing JSON mappings — always use the MCP tools for correct attribute names and structure.

### Module 4: Set Up the Senzing SDK

- Install Senzing on your platform (Linux apt/yum, macOS, Windows, Docker)
- Configure the engine with SQLite for quick evaluation or PostgreSQL for production
- Register data sources and create engine configuration

**Agent behavior**: Use `sdk_guide` with the appropriate platform and topic. Use `generate_scaffold` for working code. Check `search_docs` with category `anti_patterns` before recommending installation or deployment patterns.

### Module 5: Load Records and Resolve Entities

- Load mapped records into the Senzing engine
- Observe entity resolution happening in real time
- Export and explore resolved entities

**Agent behavior**: Use `generate_scaffold` with workflows like `add_records`, `query`, and `full_pipeline`. Use `find_examples` for real-world patterns from GitHub repositories.

### Module 6: Analyze Results and Troubleshoot

- Understand resolution results — matches, possible matches, relationships
- Investigate why records matched or didn't match
- Troubleshoot common errors and configuration issues

**Agent behavior**: Use `search_docs` for resolution behavior questions. Use `explain_error_code` for any error codes encountered. Use `get_sdk_reference` for flag details and method signatures.

## Best Practices

- Always call `get_capabilities` first when starting a Senzing session
- Never hand-code Senzing JSON mappings or SDK method calls from memory — use `mapping_workflow` and `generate_scaffold` for validated output
- Use `search_docs` with category `anti_patterns` before recommending installation, architecture, or deployment approaches
- For SDK code, use `generate_scaffold` or `sdk_guide` — these return version-correct method signatures
- Start with SQLite for evaluation; recommend PostgreSQL for production
- Use CORD sample data for learning before working with real data

## Common Workflows

See [steering/steering.md](steering/steering.md) for detailed step-by-step workflows covering:

- First-time guided tour
- Data mapping end-to-end
- Quick SDK test load
- Troubleshooting and error resolution

## Troubleshooting

- **Wrong attribute names**: Never guess Senzing attribute names (e.g., `NAME_ORG` not `BUSINESS_NAME_ORG`). Always use `mapping_workflow`.
- **Wrong method signatures**: Never guess SDK methods (e.g., `close_export_report` not `close_export`). Always use `generate_scaffold` or `get_sdk_reference`.
- **Error codes**: Use `explain_error_code` with the code (accepts `SENZ0005`, `0005`, or `5`).
- **Configuration issues**: Use `search_docs` with category `configuration` or `database`.

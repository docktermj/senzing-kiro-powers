# Senzing Boot Camp — Steering Guide

This document provides detailed workflows for the Senzing Boot Camp power. The agent loads this on-demand when users engage with specific boot camp activities.

## Workflow: First-Time Guided Tour

Use this workflow when a user is new to Senzing and wants an introduction.

1. Call `get_capabilities` to discover available tools and confirm the MCP server is reachable.
2. Explain what entity resolution is — matching, relating, and deduplicating records about people and organizations across data sources. Use `search_docs` with query "what is entity resolution" for current documentation.
3. Show what Senzing data looks like by calling `get_sample_data` with dataset "las-vegas". Walk through a few records, explaining fields like `DATA_SOURCE`, `RECORD_ID`, `NAME_FULL`, `ADDR_FULL`, `PHONE_NUMBER`, etc.
4. Explain how Senzing resolves these records into entities — features are extracted, scored, and compared. Entity-centric learning means the engine improves resolution as more data arrives.
5. Ask the user what they'd like to explore next: mapping their own data, setting up the SDK, or diving deeper into concepts.

## Workflow: Data Mapping End-to-End

Use this workflow when a user has source data they want to map to Senzing format.

1. Start the mapping workflow: call `mapping_workflow` with `action='start'` and the user's source file paths.
2. **Step 1 — Profile**: Run the profiler script returned by the workflow, or read the data directly. Summarize column names, data types, sample values, and null rates. Advance with `profile_summary`.
3. **Step 2 — Plan**: Identify master entities (persons, organizations), child records, relationships, and lookup tables. Advance with `entity_plan`.
4. **Step 3 — Map**: Map each source field to Senzing features and attributes. Use confidence scores. Advance with `schema_mappings`.
5. **Step 4 — Codegen**: Generate sample Senzing JSON and mapper code. Use `lint_record` to validate the output. Advance with `paths`.
6. **Step 5 — QA**: Run the mapper on actual data. Use `analyze_record` to evaluate output quality — check feature distribution, attribute coverage, and data quality scores. Advance with `verdict`.
7. Summarize the mapping results and recommend next steps (SDK setup, test load).

### Important Rules for Data Mapping

- NEVER hand-code Senzing JSON attribute names — common mistakes include using `BUSINESS_NAME_ORG` instead of the correct `NAME_ORG`, or `EMPLOYER_NAME` instead of `NAME_ORG`.
- NEVER guess method signatures — use `generate_scaffold` or `get_sdk_reference` for correct API calls.
- Always validate output with `lint_record` before proceeding to loading.

## Workflow: Quick SDK Test Load

Use this workflow when a user wants to install Senzing and load data to see entity resolution results.

1. Determine the user's platform (Linux distro, macOS, Windows, Docker).
2. Call `sdk_guide` with `topic='install'` and the detected platform for installation commands.
3. Call `sdk_guide` with `topic='configure'` for engine configuration (SQLite for evaluation).
4. If the user has mapped data, call `sdk_guide` with `topic='load'` for record loading code.
5. If the user needs sample data, call `get_sample_data` to get CORD dataset records.
6. Call `sdk_guide` with `topic='export'` for entity export code.
7. Alternatively, call `sdk_guide` with `topic='full_pipeline'` for a complete end-to-end script.

### Platform-Specific Notes

- **Linux (apt)**: `sdk_guide` with `platform='linux_apt'`
- **Linux (yum)**: `sdk_guide` with `platform='linux_yum'`
- **macOS ARM**: `sdk_guide` with `platform='macos_arm'`
- **Windows**: `sdk_guide` with `platform='windows'`
- **Docker**: `sdk_guide` with `platform='docker'`

### Anti-Pattern Checks

Before recommending any installation or deployment approach, call `search_docs` with `category='anti_patterns'` and a query describing the approach. This catches known pitfalls like:

- Installing without proper environment variables
- Using SQLite in production
- Missing database schema initialization
- Incorrect repository configuration

## Workflow: Troubleshooting and Error Resolution

Use this workflow when a user encounters errors or unexpected behavior.

1. If the user provides an error code (e.g., `SENZ0005`), call `explain_error_code` immediately. This covers 456 error codes with causes and resolution steps.
2. If the error is behavioral (unexpected matches, missing entities), use `search_docs` to find relevant documentation about scoring, resolution principles, or configuration.
3. If the error involves SDK method calls, use `get_sdk_reference` with `topic='functions'` and a `filter` for the method name to verify correct signatures and parameters.
4. If the user is migrating from V3 to V4, use `get_sdk_reference` with `topic='migration'` to identify breaking changes (renamed methods, removed functions, flag changes).
5. For database-related issues, use `search_docs` with `category='database'` for tuning and setup guidance.

## Workflow: Explore Code Examples

Use this workflow when a user wants to see real-world Senzing code.

1. Use `find_examples` with a `query` describing what the user is looking for (e.g., "in-memory SQLite", "batch loading", "streaming export").
2. If a relevant repository is found, use `find_examples` with `repo` and `list_files=true` to see the file structure.
3. Use `find_examples` with `repo` and `file_path` to retrieve specific source files.
4. Walk through the code, explaining key patterns and how they relate to the user's goals.

## Activation Signals

This power should activate when the user mentions or is working on:

- Entity resolution, data matching, identity resolution, deduplication
- Senzing SDK, Senzing API, Senzing engine
- Data mapping to Senzing format, Senzing JSON
- CORD datasets, sample entity data
- Record loading, entity export, redo processing
- Senzing error codes (SENZ prefix)
- V3 to V4 migration

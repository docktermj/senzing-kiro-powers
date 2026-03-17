# Quick Reference Card

Fast reference for common Senzing MCP tool calls and workflows.

## Essential First Call

```
get_capabilities(version="current")
```
Always call this first to discover available tools and confirm MCP server connectivity.

## Module 0: Quick Demo

```
# Get sample data
get_sample_data(dataset="las-vegas", limit=100)

# Generate demo script
generate_scaffold(language="python", workflow="full_pipeline", version="current")
```

## Module 1: Business Problem

No MCP calls required - focus on discovery questions and documentation.

## Module 2: Data Source Evaluation

```
# Understand SGES format
search_docs(query="generic entity specification", version="current")
search_docs(query="SGES attributes", version="current")
```

## Module 3: Data Mapping

```
# Start mapping workflow
mapping_workflow(action="start", file_paths=["data/raw/customers.csv"], version="current")

# Advance through steps (remember to pass state!)
mapping_workflow(action="advance", data={...}, state={...}, version="current")

# Validate output
lint_record(file_paths=["data/transformed/customers.jsonl"], version="current")

# Analyze quality
analyze_record(file_paths=["data/transformed/customers.jsonl"], version="current")
```

**CRITICAL**: Always pass the exact `state` object from the previous response back in the next call.

## Module 4: SDK Setup

```
# Get installation commands
sdk_guide(topic="install", platform="linux_apt", version="current")
sdk_guide(topic="install", platform="macos_arm", version="current")
sdk_guide(topic="install", platform="docker", version="current")

# Get configuration guidance
sdk_guide(topic="configure", data_sources=["CUSTOMER_DB", "VENDOR_API"], version="current")

# Check for anti-patterns
search_docs(query="installation best practices", category="anti_patterns", version="current")
```

## Module 5: Loading

```
# Generate loading code
generate_scaffold(language="python", workflow="add_records", version="current")

# Get loading guidance
sdk_guide(topic="load", input_file="data/transformed/customers.jsonl", version="current")

# Get full pipeline example
sdk_guide(topic="full_pipeline", language="python", platform="docker", version="current")
```

## Module 6: Querying

```
# Generate query code
generate_scaffold(language="python", workflow="query", version="current")
generate_scaffold(language="python", workflow="search", version="current")

# Get SDK reference for methods
get_sdk_reference(topic="functions", filter="searchByAttributes", version="current")
get_sdk_reference(topic="flags", version="current")
```

## Troubleshooting

```
# Explain error codes
explain_error_code(error_code="SENZ0005", version="current")
explain_error_code(error_code="0042", version="current")

# Search documentation
search_docs(query="resolution principles", version="current")
search_docs(query="database tuning", category="database", version="current")
search_docs(query="performance optimization", category="performance", version="current")

# Find code examples
find_examples(query="batch loading python")
find_examples(repo="brianmacy/sz_mem-v4", list_files=true)
find_examples(repo="brianmacy/sz_mem-v4", file_path="sz_mem.py")
```

## SDK Reference

```
# Get method signatures
get_sdk_reference(topic="functions", filter="addRecord", version="current")

# Get flag definitions
get_sdk_reference(topic="flags", filter="G2_EXPORT", version="current")

# V3 to V4 migration
get_sdk_reference(topic="migration", version="current")

# Response schemas
get_sdk_reference(topic="response_schemas", version="current")
```

## Common Patterns

### Check Before Recommending Architecture
```
search_docs(query="[your approach]", category="anti_patterns", version="current")
```

### Never Guess Attribute Names
```
# WRONG: Hand-coding {"BUSINESS_NAME_ORG": "Acme Corp"}
# RIGHT: Use mapping_workflow to get correct attribute names
```

### Never Guess Method Names
```
# WRONG: engine.close_export(handle)
# RIGHT: Use generate_scaffold or get_sdk_reference
```

## Version Parameter

All MCP tools accept a `version` parameter:
- `"current"` - Latest Senzing version (default, recommended)
- `"4.0"` - Senzing V4 specific
- `"3.x"` - Senzing V3 (limited support)

## When to Load This Reference

Load this quick reference when:
- Starting any module
- User asks "what MCP tool should I use?"
- Need a fast reminder of tool signatures
- Troubleshooting workflow issues

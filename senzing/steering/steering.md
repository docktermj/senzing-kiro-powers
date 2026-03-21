# Senzing — Steering Guide

This document provides navigation to detailed guidance for the Senzing power. The agent loads these on-demand when users engage with Senzing activities.

## Quick Navigation

### For New Users
Start with [getting-started.md](getting-started.md) for:
- MCP tool catalog
- Decision trees for choosing the right tool
- Common workflows
- Data flow diagrams
- Entity resolution design patterns

### For Best Practices
See [best-practices.md](best-practices.md) for:
- What to always do and never do
- Common pitfalls and how to avoid them
- Data quality considerations
- Configuration best practices

### For Performance
See [performance.md](performance.md) for:
- Database selection guidance
- Loading and query optimization
- PostgreSQL tuning
- Monitoring metrics
- Scaling strategies

### For Troubleshooting
See [troubleshooting.md](troubleshooting.md) for:
- Quick troubleshooting reference
- Error handling strategies
- Common error codes
- Typical troubleshooting sessions
- Network and connectivity issues

### For Code Examples
See [examples.md](examples.md) for:
- Basic record loading (Python, Java, C#)
- Batch loading patterns
- Entity search examples
- Why analysis examples
- Error handling patterns
- Integration patterns (Kafka, REST API)
- Testing examples

### For Reference
See [reference.md](reference.md) for:
- MCP tool parameter quick reference
- Interactive checklists (pre-deployment, data mapping, production readiness)
- Cost and licensing guidance
- Integration patterns
- Testing strategy
- Glossary of Senzing terms

## Key Principles

1. **Always use the tools**: Tools like `mapping_workflow`, `generate_scaffold`, and `sdk_guide` produce validated, version-correct output. Never hand-code Senzing JSON or SDK calls.

2. **Start with capabilities**: Call `get_capabilities` at the start of any Senzing session to discover available tools and workflows.

3. **Validate everything**: Use `lint_record` and `analyze_record` before loading data to catch issues early.

4. **Test with small batches**: Always test with 100-1000 records before loading millions.

5. **Choose the right database**: SQLite for evaluation (< 100K records), PostgreSQL for production.

6. **Monitor and optimize**: Track loading throughput, query performance, and resource utilization.

## Quick Links by Task

| Task | Primary Guide | Supporting Guides |
| --- | --- | --- |
| First-time setup | [getting-started.md](getting-started.md) | [reference.md](reference.md) (checklists) |
| Map new data source | [getting-started.md](getting-started.md) | [best-practices.md](best-practices.md), [reference.md](reference.md) |
| Write loader code | [examples.md](examples.md) | [best-practices.md](best-practices.md) |
| Optimize performance | [performance.md](performance.md) | [reference.md](reference.md) (checklists) |
| Debug issues | [troubleshooting.md](troubleshooting.md) | [examples.md](examples.md) (error handling) |
| Production deployment | [reference.md](reference.md) (checklists) | [performance.md](performance.md), [best-practices.md](best-practices.md) |
| Understand concepts | [reference.md](reference.md) (glossary) | [getting-started.md](getting-started.md) |

## Document Structure

```
steering/
├── steering.md (this file) - Navigation hub
├── getting-started.md - Quick start, workflows, decision trees
├── best-practices.md - Do's, don'ts, common pitfalls
├── performance.md - Optimization, tuning, scaling
├── troubleshooting.md - Error handling, debugging
├── examples.md - Code examples and patterns
└── reference.md - Parameters, checklists, glossary
```

## How to Use These Guides

1. **New to Senzing?** Start with [getting-started.md](getting-started.md)
2. **Building something?** Check [examples.md](examples.md) for code patterns
3. **Hitting issues?** Go to [troubleshooting.md](troubleshooting.md)
4. **Optimizing?** See [performance.md](performance.md)
5. **Need a checklist?** Use [reference.md](reference.md)
6. **Want best practices?** Read [best-practices.md](best-practices.md)

## Getting Help

- **Documentation**: Use `search_docs` for indexed Senzing documentation
- **Examples**: Use `find_examples` to search 27 Senzing GitHub repositories
- **Errors**: Use `explain_error_code` for specific error diagnosis
- **Feedback**: Use `submit_feedback` to report issues or suggestions
- **Support**: https://senzing.zendesk.com/hc/en-us/requests/new

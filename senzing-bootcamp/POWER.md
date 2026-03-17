---
name: "senzing-bootcamp"
displayName: "Senzing Boot Camp"
version: "2.0.0"
description: "Guided discovery of Senzing entity resolution. Walk through data mapping, SDK setup, record loading, and result exploration using the Senzing MCP server."
keywords: ["Entity Resolution", "Senzing", "Data Mapping", "SDK", "Identity Resolution", "Data Matching", "ER"]
author: "Senzing"
senzing_compatibility: ["4.0", "3.x"]
last_updated: "2025-01-17"
---

# Power: Senzing Boot Camp

## Overview

This power provides a guided boot camp experience for learning Senzing entity resolution. It connects to the Senzing MCP server to provide interactive, tool-assisted workflows covering data mapping, SDK installation, record loading, and entity resolution exploration.

Senzing is an embeddable entity resolution engine that resolves records about people and organizations across data sources — matching, relating, and deduplicating without manual rules or model training.

**Power Version**: 2.0.0  
**Senzing Compatibility**: V4.0 (primary), V3.x (limited support)  
**Last Updated**: 2025-01-17

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

**Modules**:

- **Module 0: Quick Demo (Optional)**
  - Experience entity resolution with sample data
  - See how Senzing resolves duplicate records automatically
  - 10-15 minutes

- **Module 1: Understand Business Problem**
  - Define your problem and identify data sources
  - View design pattern gallery (optional)
  - Create problem statement document
  - 15-30 minutes

- **Module 2: Verify Data Sources**
  - Evaluate if data needs mapping or is SGES-compliant
  - Create data source evaluation report
  - 10 minutes per data source

- **Module 3: Map Your Data**
  - Create transformation programs for non-compliant sources
  - Validate data quality
  - Generate test files
  - 1-2 hours per data source

- **Module 4: Set Up SDK**
  - Install and configure Senzing
  - Set up database (SQLite or PostgreSQL)
  - Verify installation
  - 30 minutes - 1 hour

- **Module 5: Load Records**
  - Create loading programs for each data source
  - Observe entity resolution in real time
  - Generate loading statistics dashboard
  - 30 minutes per data source

- **Module 6: Query Results**
  - Create query programs that answer your business problem
  - Validate results
  - Complete lessons learned
  - 1-2 hours

**Total Time**: 3-6 hours for a typical single data source project

**Note**: While the modules are presented in order, you can move back and forth between steps as needed. Discovery is iterative — you might need to revisit earlier steps as you learn more about your data or refine your approach.

### Skip Ahead Options

Experienced users can skip modules based on their situation:

- **Have SGES-compliant data?** → Skip Module 3, go directly to Module 4
- **Senzing already installed?** → Skip Module 4, go directly to Module 5
- **Just want to explore?** → Start with Module 0 (Quick Demo)
- **Already loaded data?** → Jump directly to Module 6
- **Know your problem well?** → Skim Module 1, focus on Modules 2-6

### Module Prerequisites

Before starting each module, ensure prerequisites are met:

**Module 0** (Optional):
- No prerequisites

**Module 1**:
- No prerequisites
- Recommended: Have business problem in mind

**Module 2**:
- ✅ Module 1 complete (business problem defined)
- ✅ Data sources identified
- ✅ Sample data available

**Module 3**:
- ✅ Module 2 complete (sources evaluated)
- ✅ Non-compliant sources identified
- ✅ Sample data files in `data/raw/`

**Module 4**:
- ✅ Module 3 complete (all sources mapped) OR
- ✅ All sources are SGES-compliant
- ✅ Platform/environment ready

**Module 5**:
- ✅ Module 4 complete (SDK installed)
- ✅ Database configured
- ✅ Transformed data ready in `data/transformed/`

**Module 6**:
- ✅ Module 5 complete (all sources loaded)
- ✅ Loading statistics reviewed
- ✅ No critical errors

## Project Directory Structure

Before starting, set up a project directory to organize all your boot camp artifacts:

```
my-senzing-project/
├── .git/                          # Version control
├── .gitignore                     # Exclude sensitive data
├── .env.example                   # Template for environment variables
├── .env                           # Actual environment variables (not in git)
├── data/                          # User's data files
│   ├── raw/                       # Original source data
│   ├── transformed/               # Senzing-formatted JSON output
│   ├── samples/                   # Sample data for testing
│   └── backups/                   # Database backups
├── src/                           # Generated program source
│   ├── transform/                 # Transformation programs (Module 3)
│   ├── load/                      # Loading programs (Module 5)
│   ├── query/                     # Query programs (Module 6)
│   └── utils/                     # Shared utilities
├── tests/                         # Test files for project
├── docs/                          # Design documents
│   ├── business_problem.md        # Module 1 output
│   ├── data_source_evaluation.md  # Module 2 output
│   ├── mapping_specifications.md  # Module 3 mappings
│   ├── query_specifications.md    # Module 6 queries
│   └── lessons_learned.md         # Post-project retrospective
├── config/                        # Configuration files
├── logs/                          # Log files
├── monitoring/                    # Monitoring and dashboards
└── README.md                      # Project description

**Important**: All generated source code (transformation programs, loading programs, query programs, utilities, and scripts) should be placed in the `src/` directory structure, not in the project root.
```

**Agent behavior**: At the start of Module 1, help the user create this directory structure. As you generate programs throughout the boot camp, save them in the appropriate folders.

## When to Load Steering Files

The boot camp includes detailed steering files for specific topics. Load these on-demand when users need detailed guidance:

### Core Workflows (Always Available)
- **steering/steering.md** — Detailed workflows for all modules (Module 0-6)
- **steering/agent-instructions.md** — Consolidated agent behavior guide (load at start)
- **steering/quick-reference.md** — MCP tool quick reference card

### Supporting Topics (Load on Demand)
- **steering/environment-setup.md** — Version control, Python venv, Docker, environment variables
  - Load when: Starting Module 1, user asks about setup
  
- **steering/security-privacy.md** — Data privacy, PII protection, compliance, anonymization
  - Load when: Starting Module 2, working with sensitive data
  
- **steering/testing-strategy.md** — Unit tests, integration tests, data quality tests
  - Load when: Module 3 (transformation), user asks about testing
  
- **steering/performance-monitoring.md** — Benchmarking, monitoring dashboards, health checks
  - Load when: Module 5 (loading), performance optimization questions
  
- **steering/recovery-procedures.md** — Backup, rollback, disaster recovery
  - Load when: Before Module 5, user encounters errors
  
- **steering/collaboration.md** — Team workflows, code review, handoff procedures
  - Load when: Team projects, handoff questions
  
- **steering/cost-estimation.md** — Pricing, ROI, deployment costs
  - Load when: Module 1 (planning), Module 4 (deployment choice)
  
- **steering/integration-patterns.md** — REST API, batch export, streaming, database sync
  - Load when: Module 6, user asks about integration
  
- **steering/lessons-learned.md** — Post-project retrospective template
  - Load when: After Module 6, project completion
  
- **steering/common-pitfalls.md** — Common mistakes and how to avoid them
  - Load when: Any module, troubleshooting, user is stuck
  
- **steering/troubleshooting-decision-tree.md** — Visual flowchart for diagnosing issues
  - Load when: User encounters errors, systematic troubleshooting needed
  
- **steering/complexity-estimator.md** — Estimate time based on data characteristics
  - Load when: Module 1 (planning), user asks "how long will this take?"

## Recommended Hooks

Install pre-configured hooks to automate quality checks and reminders. See `senzing-bootcamp/hooks/` directory and `HOOKS_INSTALLATION_GUIDE.md` for details.

Available hooks:
- **data-quality-check** — Validates quality when transformations change
- **backup-before-load** — Reminds to backup before loading
- **test-before-commit** — Runs tests automatically
- **validate-senzing-json** — Validates output format
- **update-documentation** — Reminds to update docs

Installation:
```bash
# Create .kiro directory structure if it doesn't exist
mkdir -p .kiro/hooks

# Copy hooks
cp senzing-bootcamp/hooks/*.hook .kiro/hooks/
```

**Agent behavior**: When installing hooks, always verify the `.kiro/hooks/` directory exists first. Create it if needed with `mkdir -p .kiro/hooks` before copying hook files.

## Entity Resolution Design Pattern Gallery

When starting Module 1, offer users a gallery of common entity resolution patterns:

| Pattern | Use Case | Key Matching | Typical ROI |
|---------|----------|--------------|-------------|
| **Customer 360** | Unified customer view | Names, emails, phones, addresses | Improved service, targeted marketing |
| **Fraud Detection** | Identify fraud rings | Names, addresses, devices, IPs | Loss prevention, faster detection |
| **Data Migration** | Merge legacy systems | All available identifiers | Reduced storage, simplified ops |
| **Compliance Screening** | Watchlist matching | Names, DOB, nationalities, IDs | Regulatory compliance, risk mitigation |
| **Marketing Dedup** | Eliminate duplicates | Names, addresses, emails | Reduced mailing costs, better metrics |
| **Patient Matching** | Unified medical records | Names, DOB, SSN, MRNs | Patient safety, care coordination |
| **Vendor MDM** | Clean vendor master | Company names, tax IDs, addresses | Better pricing, consolidated spend |
| **Claims Fraud** | Detect staged accidents | Names, vehicles, providers | Reduced fraudulent payouts |
| **KYC/Onboarding** | Verify identity | Names, DOB, SSN, gov IDs | Reduced fraud, compliance |
| **Supply Chain** | Unified supplier view | Company names, GLNs, tax IDs | Visibility, risk management |

**When to use each pattern**:
- **Customer 360**: Multiple customer touchpoints, CRM consolidation
- **Fraud Detection**: Financial services, insurance, e-commerce
- **Data Migration**: M&A, system consolidation, cloud migration
- **Compliance**: Banking, fintech, international trade
- **Marketing**: Email campaigns, direct mail, lead management
- **Healthcare**: Hospital networks, HIE, patient portals
- **Vendor MDM**: Procurement, AP, spend analysis
- **Claims Fraud**: Insurance, workers comp, auto claims
- **KYC**: Banking, fintech, account opening
- **Supply Chain**: Manufacturing, logistics, procurement

**Agent behavior**: Present this gallery when user requests it in Module 1. Help them identify which pattern(s) match their situation. Use the selected pattern to guide problem definition and set realistic expectations.

## Best Practices

- Always call `get_capabilities` first when starting a Senzing session
- Never hand-code Senzing JSON mappings or SDK method calls from memory — use `mapping_workflow` and `generate_scaffold` for validated output
- Use `search_docs` with category `anti_patterns` before recommending installation, architecture, or deployment approaches
- For SDK code, use `generate_scaffold` or `sdk_guide` — these return version-correct method signatures
- Start with SQLite for evaluation; recommend PostgreSQL for production
- Use CORD sample data for learning before working with real data

## Common Workflows

See [steering/steering.md](steering/steering.md) for detailed step-by-step workflows covering:

- Module 0: Quick Demo (Optional)
- Module 1: Discover the Business Problem
- Module 2: Verify Data Sources Against SGES
- Module 3: Data Mapping End-to-End
- Module 4: Install Senzing SDK (Part A)
- Module 5: Create Loading Programs (Part B)
- Module 6: Create Query Programs to Answer Business Problem
- Troubleshooting and Error Resolution
- Explore Code Examples

## Troubleshooting

- **Wrong attribute names**: Never guess Senzing attribute names (e.g., `NAME_ORG` not `BUSINESS_NAME_ORG`). Always use `mapping_workflow`.
- **Wrong method signatures**: Never guess SDK methods (e.g., `close_export_report` not `close_export`). Always use `generate_scaffold` or `get_sdk_reference`.
- **Error codes**: Use `explain_error_code` with the code (accepts `SENZ0005`, `0005`, or `5`).
- **Configuration issues**: Use `search_docs` with category `configuration` or `database`.

## Boot Camp Complete! 🎉

After completing all modules, you'll have:

- ✅ Clear business problem statement
- ✅ Evaluated data sources
- ✅ Transformation programs for each source
- ✅ Installed and configured Senzing SDK
- ✅ Loading programs for each source
- ✅ Query programs answering your business questions

### Next Steps

1. **Production deployment**: Move from SQLite to PostgreSQL
2. **Automation**: Schedule transformation and loading programs
3. **Integration**: Connect query programs to your applications
4. **Monitoring**: Set up monitoring for data quality and performance
5. **Expansion**: Add more data sources using the same process
6. **Documentation**: Complete lessons learned template

### Getting Help

- Use `search_docs` to find Senzing documentation
- Use `explain_error_code` for error diagnosis
- Use `find_examples` to see real-world code patterns
- Review steering guides for detailed workflows
- Contact Senzing support for production issues

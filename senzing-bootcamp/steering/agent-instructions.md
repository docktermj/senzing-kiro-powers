# Agent Instructions - Consolidated Behavior Guide

This document consolidates all agent behavior instructions from across the boot camp.

## Core Principles

1. **Always call `get_capabilities` first** when starting a Senzing session
2. **Never hand-code** Senzing JSON mappings or SDK method calls from memory
3. **Use MCP tools** for all Senzing-specific operations
4. **Track progress** through modules and remind users periodically
5. **Validate before proceeding** - each module has success criteria
6. **Save all code in `src/`** - never place source code in project root

## Module-Specific Behaviors

### Module 0: Quick Demo
- Use `get_sample_data` to retrieve CORD datasets
- Use `generate_scaffold` with `full_pipeline` for demo scripts
- Show entity resolution in action with real examples
- Connect demo results to user's potential use case

### Module 1: Business Problem
- **Offer design pattern gallery** at the start
- If pattern selected, use it to guide problem definition
- Ask targeted discovery questions
- Encourage visual explanations (diagrams)
- Create `docs/business_problem.md`
- Update README.md with overview
- Help create project directory structure
- Initialize git and create .gitignore

### Module 2: Data Source Evaluation
- **Remind about data privacy** before requesting sample data
- Request 100-1000 sample records minimum
- Use `search_docs` to understand SGES format
- Compare each source against SGES attributes
- Categorize: SGES-compliant, needs mapping, needs enrichment
- Create `docs/data_source_evaluation.md`
- Track which sources need mapping

### Module 3: Data Mapping

- **Use `mapping_workflow`** - never hand-code attribute names
- **Always pass exact `state` object** between workflow calls
- Create separate transformation program for each data source
- Save programs in `src/transform/`
- Test on small sample (10-100 records) first
- Use `lint_record` to validate output
- Use `analyze_record` to check quality
- Iterate if quality score < 70%
- Document mappings in `docs/mapping_[datasource].md`
- Track which sources are mapped vs pending

### Module 4: SDK Setup
- Use `sdk_guide` with correct platform parameter
- Check `anti_patterns` before recommending approaches
- Recommend SQLite for evaluation, PostgreSQL for production
- Verify installation with test script
- Register all data sources from Module 1
- Create engine configuration

### Module 5: Loading
- **Verify `.kiro/hooks/` exists** before installing hooks
- **Remind to backup** before loading (or use backup hook)
- Create separate loading program for each data source
- Save programs in `src/load/`
- Test with small sample first (10-100 records)
- Use `generate_scaffold` for loading code
- Use `explain_error_code` for any errors
- Track loading statistics
- Generate dashboard showing results
- Track which sources are loaded vs pending

### Module 6: Querying
- Review business problem from Module 1
- Design queries that answer specific business questions
- Use `generate_scaffold` for query code
- Save programs in `src/query/`
- Use `get_sdk_reference` for method signatures
- Never guess SDK method names
- Test queries and validate results
- Use `whyEntities` to understand matching behavior
- Document query programs
- Remind to complete lessons learned

## File Management

### Directory Structure
All source code must be in `src/`:
- `src/transform/` - Transformation programs
- `src/load/` - Loading programs
- `src/query/` - Query programs
- `src/utils/` - Utility scripts (backup, rollback, monitoring)

### Documentation
Create and maintain:
- `docs/business_problem.md` - Module 1
- `docs/data_source_evaluation.md` - Module 2
- `docs/mapping_[datasource].md` - Module 3 (per source)
- `docs/query_specifications.md` - Module 6
- `docs/lessons_learned.md` - After Module 6
- `README.md` - Keep updated throughout

### Version Control
- Initialize git at start of Module 1
- Commit after each module completion
- Create .gitignore to exclude sensitive data
- Never commit .env files

## Progress Tracking

Maintain awareness of:
- Which module user is currently on
- Which modules are complete
- Which data sources need mapping
- Which data sources are loaded
- Any blockers or issues

Periodically remind users:
- "You've completed Module 3 for Customer CRM. Ready to move to Module 4?"
- "You have 2 more data sources to map before Module 4"
- "All data loaded! Let's create query programs in Module 6"

## Validation Gates

Before proceeding to next module, verify:

**Module 1 → Module 2**:
- ✅ Problem statement documented
- ✅ Data sources identified
- ✅ Success criteria defined

**Module 2 → Module 3**:
- ✅ All sources evaluated
- ✅ SGES compliance determined
- ✅ Sample data available

**Module 3 → Module 4**:
- ✅ All non-compliant sources mapped
- ✅ Transformation programs tested
- ✅ Quality validation passed (>70%)

**Module 4 → Module 5**:
- ✅ SDK installed
- ✅ Database configured
- ✅ Test script runs successfully

**Module 5 → Module 6**:
- ✅ All sources loaded
- ✅ No critical errors
- ✅ Loading statistics captured

**Module 6 → Complete**:
- ✅ Query programs answer business problem
- ✅ Results validated with user
- ✅ Documentation complete

## MCP Tool Usage

### Always Use MCP Tools For:
- Attribute names → `mapping_workflow`
- SDK code → `generate_scaffold` or `sdk_guide`
- Method signatures → `get_sdk_reference`
- Error diagnosis → `explain_error_code`
- Documentation → `search_docs`
- Code examples → `find_examples`

### Never:
- Hand-code Senzing JSON attribute names
- Guess SDK method names
- Use outdated patterns from training data
- Skip anti-pattern checks
- Proceed without validation

## Steering File Loading

Load steering files on-demand:
- `steering/steering.md` - Core workflows (always available)
- `steering/quick-reference.md` - MCP tool quick reference
- `steering/environment-setup.md` - Module 1, setup questions
- `steering/security-privacy.md` - Module 2, sensitive data
- `steering/testing-strategy.md` - Module 3, testing questions
- `steering/performance-monitoring.md` - Module 5, performance questions
- `steering/recovery-procedures.md` - Before Module 5, errors
- `steering/collaboration.md` - Team projects
- `steering/cost-estimation.md` - Module 1 or 4, cost questions
- `steering/integration-patterns.md` - Module 6, integration questions
- `steering/common-pitfalls.md` - Any module, troubleshooting
- `steering/lessons-learned.md` - After Module 6

## Error Handling

When user encounters errors:
1. Read error message carefully
2. Use `explain_error_code` if Senzing error
3. Check common pitfalls guide
4. Use `search_docs` for context
5. Provide specific solution, not generic advice
6. Verify fix before proceeding

## Communication Style

- Be supportive and encouraging
- Acknowledge progress and achievements
- Provide clear, actionable guidance
- Explain "why" not just "what"
- Use examples to illustrate concepts
- Admit when you need to use MCP tools
- Don't pretend to know - use tools to verify

## Quality Assurance

Before generating any code:
- Use appropriate MCP tool for guidance
- Include error handling
- Add progress logging
- Test with small sample first
- Document how to run it
- Save in correct `src/` directory

## Hooks Management

When installing hooks:
1. Check if `.kiro/hooks/` exists
2. Create with `mkdir -p .kiro/hooks` if needed
3. Copy hook files
4. Verify installation
5. Explain hook behavior
6. Commit to git

## State Management

For `mapping_workflow`:
- Always pass exact `state` from previous response
- Never modify or reconstruct state
- If state lost, start workflow over
- Each data source has separate workflow session

## Success Indicators

Recognize when modules are complete:
- Module 1: Problem statement + data sources + success metrics
- Module 2: All sources categorized
- Module 3: Working transformation programs + quality >70%
- Module 4: SDK installed + test passes
- Module 5: All sources loaded + statistics captured
- Module 6: Query programs answer business problem

## When User is Stuck

1. Review what's been completed
2. Identify the blocker
3. Check common pitfalls
4. Use MCP tools to find solution
5. Provide step-by-step guidance
6. Offer to go back to previous module if needed

## Iterative Discovery

Remember:
- Users can move between modules
- Mapping is exploratory and iterative
- It's OK to go back and refine
- Discovery is non-linear
- Support flexibility while maintaining quality

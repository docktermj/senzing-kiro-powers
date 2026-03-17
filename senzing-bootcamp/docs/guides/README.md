# Guides and Tutorials Index

This directory contains user-facing guides and tutorials for the Senzing Boot Camp.

## Available Guides

### Design Patterns Gallery
**File**: [DESIGN_PATTERNS.md](DESIGN_PATTERNS.md)

**Purpose**: Explore common entity resolution design patterns

**Content**:
- 10 common entity resolution patterns
- Use case descriptions
- Key matching attributes
- Typical ROI for each pattern
- When to use each pattern
- Pattern selection guidance

**Patterns Covered**:
- Customer 360 - Unified customer view
- Fraud Detection - Identify fraud rings
- Data Migration - Merge legacy systems
- Compliance Screening - Watchlist matching
- Marketing Dedup - Eliminate duplicates
- Patient Matching - Unified medical records
- Vendor MDM - Clean vendor master
- Claims Fraud - Detect staged accidents
- KYC/Onboarding - Verify identity
- Supply Chain - Unified supplier view

**When to Use**: Module 1 (Business Problem) - helps identify which pattern fits your use case

---

### Hooks Installation Guide
**File**: [HOOKS_INSTALLATION_GUIDE.md](HOOKS_INSTALLATION_GUIDE.md)

**Purpose**: Install and configure Kiro automation hooks

**Content**:
- What are hooks and why use them
- Available hooks for Senzing Boot Camp
- Installation instructions
- Hook configuration
- Testing hooks
- Troubleshooting

**Available Hooks**:
- `data-quality-check.kiro.hook` - Validates quality when transformations change
- `backup-before-load.kiro.hook` - Reminds to backup before loading
- `test-before-commit.kiro.hook` - Runs tests automatically
- `validate-senzing-json.kiro.hook` - Validates output format
- `update-documentation.kiro.hook` - Reminds to update docs

**When to Use**: Before Module 4 (Data Mapping) - automates quality checks

---

### Installation Verification Guide
**File**: [INSTALLATION_VERIFICATION.md](INSTALLATION_VERIFICATION.md)

**Purpose**: Verify Senzing SDK installation is working correctly

**Content**:
- Pre-installation checklist
- Installation verification steps
- Test script examples
- Common installation issues
- Platform-specific notes
- Troubleshooting guide

**Verification Steps**:
1. Check Senzing version
2. Verify environment variables
3. Test database connection
4. Run simple test script
5. Verify all components working

**When to Use**: After Module 5 (SDK Setup) - ensures installation is correct

---

## Guide Categories

### Getting Started
- **Design Patterns** - Choose your use case
- **Installation Verification** - Verify SDK setup

### Automation
- **Hooks Installation** - Automate quality checks

### Troubleshooting
- See `../../steering/common-pitfalls.md`
- See `../../steering/troubleshooting-decision-tree.md`

## Quick Reference

| Guide | Module | Time | Purpose |
|-------|--------|------|---------|
| Design Patterns | 1 | 10 min | Choose pattern |
| Hooks Installation | Before 4 | 15 min | Automate checks |
| Installation Verification | 5 | 10 min | Verify SDK |

## Related Documentation

### For Planning
- **Design Patterns** → Helps with Module 1 (Business Problem)
- **Cost Calculator** → See `../../steering/cost-calculator.md`
- **Complexity Estimator** → See `../../steering/complexity-estimator.md`

### For Setup
- **Installation Verification** → Helps with Module 5 (SDK Setup)
- **Environment Setup** → See `../../steering/environment-setup.md`

### For Automation
- **Hooks Installation** → Automates quality checks
- **Testing Strategy** → See `../../steering/testing-strategy.md`

### For Troubleshooting
- **Common Pitfalls** → See `../../steering/common-pitfalls.md`
- **Troubleshooting Decision Tree** → See `../../steering/troubleshooting-decision-tree.md`
- **Recovery Procedures** → See `../../steering/recovery-procedures.md`

## How to Use These Guides

### For New Users
1. Start with **Design Patterns** to understand use cases
2. Follow main boot camp (POWER.md)
3. Use **Installation Verification** after SDK setup
4. Install **Hooks** before data mapping

### For Experienced Users
- Jump directly to relevant guide
- Use as reference during boot camp
- Customize hooks for your workflow

### For Troubleshooting
1. Check **Installation Verification** if SDK issues
2. Review **Common Pitfalls** for known issues
3. Use **Troubleshooting Decision Tree** for systematic diagnosis

## Additional Resources

### Steering Files
Detailed workflows and guidance:
- `../../steering/steering.md` - Main workflows
- `../../steering/agent-instructions.md` - Agent behavior
- `../../steering/quick-reference.md` - MCP tool reference

### Module Documentation
Detailed module information:
- `../modules/` - Module-specific docs

### Policies
Coding standards:
- `../policies/` - Policy documents

## For Agents

When users need guidance:
1. **Module 1** → Suggest Design Patterns guide
2. **Before Module 4** → Suggest Hooks Installation
3. **After Module 5** → Suggest Installation Verification
4. **Troubleshooting** → Point to relevant guides

## For Users

### When to Read
- **Before starting** → Design Patterns
- **During setup** → Installation Verification
- **Before mapping** → Hooks Installation
- **When stuck** → Troubleshooting guides

### How to Read
- Skim for overview
- Deep dive when needed
- Use as reference
- Follow step-by-step instructions

## Version History

- **v1.0.0** (2026-03-17): Initial guides
  - DESIGN_PATTERNS.md
  - HOOKS_INSTALLATION_GUIDE.md
  - INSTALLATION_VERIFICATION.md

## Navigation

- [← Back to docs/](../)
- [→ Modules](../modules/)
- [→ Policies](../policies/)
- [→ Development](../development/)

# Common Pitfalls and How to Avoid Them

Learn from common mistakes to save time and frustration.

## Module 1: Business Problem

### Pitfall: Problem Too Vague
**Symptom**: "I want to clean my data"
**Problem**: Not specific enough to guide the boot camp
**Solution**: Ask targeted questions:
- What specific data quality issue?
- Which systems have the data?
- What's the desired outcome?
- How will you measure success?

### Pitfall: Too Many Data Sources at Once
**Symptom**: User lists 10+ data sources
**Problem**: Overwhelming scope, long timeline
**Solution**: Prioritize 1-2 sources for initial boot camp, expand later

### Pitfall: Unrealistic Expectations
**Symptom**: "This will solve all our data problems"
**Problem**: Entity resolution is powerful but not magic
**Solution**: Set clear expectations about what ER can and cannot do

## Module 2: Data Source Evaluation

### Pitfall: Insufficient Sample Data
**Symptom**: User provides 2-3 sample records
**Problem**: Can't assess data quality or patterns
**Solution**: Request 100-1000 sample records minimum

### Pitfall: Assuming SGES Compliance
**Symptom**: "Our data is already in the right format"
**Problem**: Often incorrect, leads to loading errors
**Solution**: Always verify field names match SGES exactly

### Pitfall: Ignoring Data Quality Issues
**Symptom**: "We'll fix the data later"
**Problem**: Poor quality = poor matching results
**Solution**: Address quality issues during mapping (Module 3)

## Module 3: Data Mapping

### Pitfall: Hand-Coding Attribute Names
**Symptom**: Using `BUSINESS_NAME_ORG` instead of `NAME_ORG`
**Problem**: Wrong attribute names cause loading failures
**Solution**: ALWAYS use `mapping_workflow` - never guess

**Common wrong names**:
- ❌ `BUSINESS_NAME_ORG` → ✅ `NAME_ORG`
- ❌ `EMPLOYER_NAME` → ✅ `NAME_ORG`
- ❌ `PHONE` → ✅ `PHONE_NUMBER`
- ❌ `EMAIL` → ✅ `EMAIL_ADDRESS`
- ❌ `SSN` → ✅ `SSN_NUMBER`

### Pitfall: Forgetting Required Fields
**Symptom**: Mapping fails validation
**Problem**: Missing `DATA_SOURCE` or `RECORD_ID`
**Solution**: Every record MUST have:
- `DATA_SOURCE` - Unique identifier for this source
- `RECORD_ID` - Unique within the data source

### Pitfall: Not Testing Transformation
**Symptom**: Running transformation on full dataset first
**Problem**: Errors discovered after hours of processing
**Solution**: Always test on 10-100 records first

### Pitfall: Skipping Quality Analysis
**Symptom**: "The transformation ran, so it's good"
**Problem**: Low quality data = poor matching
**Solution**: Always run `analyze_record` and review metrics

### Pitfall: Losing Mapping Workflow State
**Symptom**: `mapping_workflow` errors about missing state
**Problem**: Not passing the `state` object between calls
**Solution**: Always pass the EXACT `state` JSON from previous response

## Module 4: SDK Setup

### Pitfall: Using SQLite for Production
**Symptom**: "SQLite is working fine for 10K records"
**Problem**: Doesn't scale, poor performance at 100K+
**Solution**: SQLite for evaluation only, PostgreSQL for production

### Pitfall: Skipping Anti-Pattern Check
**Symptom**: Following outdated installation guides
**Problem**: Known issues, deprecated approaches
**Solution**: Always call `search_docs` with category `anti_patterns`

### Pitfall: Wrong Platform Commands
**Symptom**: Using apt commands on macOS
**Problem**: Installation fails
**Solution**: Use `sdk_guide` with correct platform parameter

### Pitfall: Missing Environment Variables
**Symptom**: SDK initialization fails
**Problem**: `SENZING_ENGINE_CONFIGURATION_JSON` not set
**Solution**: Follow `sdk_guide` configuration exactly

## Module 5: Loading

### Pitfall: No Database Backup
**Symptom**: Loading fails halfway, database corrupted
**Problem**: No way to recover
**Solution**: ALWAYS backup before loading (use backup hook)

### Pitfall: Loading Without Testing
**Symptom**: Errors discovered after loading millions of records
**Problem**: Wasted time, need to rollback
**Solution**: Test load with 100 records first

### Pitfall: Ignoring Error Codes
**Symptom**: "Some records failed but most worked"
**Problem**: Errors indicate data quality or configuration issues
**Solution**: Use `explain_error_code` for every error, fix root cause

### Pitfall: Wrong DATA_SOURCE Name
**Symptom**: Records load but queries don't work
**Problem**: DATA_SOURCE doesn't match registered name
**Solution**: Verify DATA_SOURCE matches Module 4 configuration

### Pitfall: Not Monitoring Progress
**Symptom**: "Is it still running?"
**Problem**: No visibility into loading status
**Solution**: Add progress logging to loading programs

## Module 6: Querying

### Pitfall: Guessing SDK Method Names
**Symptom**: Using `close_export` instead of `closeExport`
**Problem**: Method doesn't exist, code fails
**Solution**: Use `generate_scaffold` or `get_sdk_reference`

**Common wrong methods**:
- ❌ `close_export` → ✅ `closeExport`
- ❌ `close_export_report` → ✅ `closeExport`
- ❌ `whyEntityByEntityID` → ✅ `whyEntities` (V4)

### Pitfall: Wrong Query Flags
**Symptom**: Results missing expected information
**Problem**: Incorrect or missing flags
**Solution**: Use `get_sdk_reference` with topic `flags`

### Pitfall: Not Understanding Why Records Matched
**Symptom**: "These shouldn't have matched"
**Problem**: Don't understand resolution behavior
**Solution**: Use `whyEntities` to see match details and scoring

### Pitfall: Expecting Perfect Results Immediately
**Symptom**: "The results aren't perfect"
**Problem**: First iteration rarely perfect
**Solution**: Iterate - adjust mappings, confidence scores, add attributes

## General Pitfalls

### Pitfall: Not Reading Error Messages
**Symptom**: "It's not working"
**Problem**: Error message explains the issue
**Solution**: Read error messages carefully, use `explain_error_code`

### Pitfall: Skipping Documentation
**Symptom**: Guessing how things work
**Problem**: Incorrect assumptions, wasted time
**Solution**: Use `search_docs` liberally

### Pitfall: Not Committing to Git
**Symptom**: Lost work after accidental deletion
**Problem**: No version control
**Solution**: Commit after each module completion

### Pitfall: Working in Production First
**Symptom**: Testing in production environment
**Problem**: Risk of data corruption, downtime
**Solution**: Always develop locally or in dev environment

### Pitfall: Not Documenting Decisions
**Symptom**: "Why did we do it this way?"
**Problem**: Lost context, hard to maintain
**Solution**: Document decisions in docs/ as you go

### Pitfall: Rushing Through Modules
**Symptom**: Skipping validation steps
**Problem**: Errors compound, harder to debug
**Solution**: Complete each module fully before proceeding

## Recovery from Common Mistakes

### Loaded Wrong Data
```bash
# Restore from backup
./src/utils/rollback.sh data/backups/G2C_YYYYMMDD_HHMMSS.db
```

### Wrong Transformation
```bash
# Delete bad output
rm data/transformed/bad_output.jsonl
# Fix transformation program
# Re-run on sample first
# Validate with lint_record
```

### Lost Mapping State
```bash
# Start mapping workflow over
# Or use saved mapping documentation from docs/
```

### Corrupted Git Repo
```bash
# Restore file from git
git checkout HEAD -- src/transform/program.py
```

## Prevention Checklist

Before each module:
- [ ] Previous module complete and validated
- [ ] Documentation up to date
- [ ] Code committed to git
- [ ] Backup created (if applicable)
- [ ] Sample data tested
- [ ] Error handling in place

## When to Load This Guide

Load this steering file when:
- User encounters an error
- Starting any module (preventive)
- User says "it's not working"
- Troubleshooting issues
- User is stuck or frustrated

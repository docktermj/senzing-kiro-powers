# Senzing Boot Camp - Quick Start Guide

Get started with Senzing entity resolution in under 30 minutes.

## What You'll Do

1. ✅ Run a quick demo (10 minutes)
2. ✅ Understand your business problem (10 minutes)
3. ✅ Map your first data source (30-60 minutes)
4. ✅ Load and query results (30 minutes)

**Total Time**: 1-2 hours to see entity resolution in action

## Prerequisites

- Kiro IDE installed
- Python 3.8+ (or Java 11+, .NET 6+, Rust)
- Sample data file (CSV, JSON, or database export)

## Step 1: Run Quick Demo (10 minutes)

See entity resolution in action with sample data.

### In Kiro, say:
```
"Let's start the Senzing boot camp with Module 0"
```

### What Happens:
1. Kiro loads sample data (Las Vegas, London, or Moscow dataset)
2. Generates a demo script
3. Runs entity resolution
4. Shows you duplicate records that were matched

### What You'll See:
- Records with slight variations (typos, abbreviations) matched together
- Entities created from multiple records
- Confidence scores for matches

**Skip this if**: You want to jump straight to your own data

---

## Step 2: Define Your Problem (10 minutes)

Clarify what you're trying to solve.

### In Kiro, say:
```
"Let's start Module 1 - I want to solve [your problem]"
```

### Examples:
- "I want to find duplicate customers across 3 CRM systems"
- "I need to detect fraud rings in insurance claims"
- "I'm merging two companies and need to consolidate vendor data"

### What Happens:
1. Kiro asks about your data sources
2. Helps you define success criteria
3. Estimates costs based on data volume
4. Creates `docs/business_problem.md`

### What You'll Have:
- Clear problem statement
- List of data sources
- Success metrics
- Cost estimate

---

## Step 3: Map Your First Data Source (30-60 minutes)

Transform your data into Senzing format.

### Prerequisites:
- One data file (CSV, JSON, Excel, or database export)
- Sample of 10-100 records

### In Kiro, say:
```
"Let's map my customer data file"
```

### What Happens:
1. **Upload your file** to `data/raw/customers.csv`
2. **Kiro analyzes** your data structure
3. **Interactive mapping** - Kiro asks about each field:
   - "Is 'cust_name' a person or organization name?"
   - "Is 'email' an email address?"
   - "Is 'addr1' a street address?"
4. **Generate transformation program** in `src/transform/`
5. **Validate output** with quality scoring
6. **Test with sample** - verify 10 records look correct

### What You'll Have:
- Transformation program: `src/transform/transform_customers.py`
- Transformed data: `data/transformed/customers.jsonl`
- Quality report: `docs/data_quality_report.md`

### Common Mappings:
```
Your Field          → Senzing Attribute
-----------           ------------------
customer_id         → RECORD_ID
first_name          → NAME_FIRST
last_name           → NAME_LAST
email               → EMAIL_ADDRESS
phone               → PHONE_NUMBER
address             → ADDR_FULL
city                → ADDR_CITY
state               → ADDR_STATE
zip                 → ADDR_POSTAL_CODE
```

---

## Step 4: Install Senzing SDK (30 minutes)

Set up the Senzing engine.

### In Kiro, say:
```
"Let's install the Senzing SDK"
```

### What Happens:
1. Kiro detects your platform (Linux, macOS, Windows)
2. Provides installation commands
3. Sets up SQLite database (for evaluation)
4. Configures engine
5. Runs test script

### What You'll Have:
- Senzing SDK installed
- Database configured
- Engine ready to load data

**Note**: Uses SQLite for quick start. For production, use PostgreSQL.

---

## Step 5: Load Your Data (15 minutes)

Load transformed data into Senzing.

### In Kiro, say:
```
"Let's load the customer data"
```

### What Happens:
1. Kiro generates loading program: `src/load/load_customers.py`
2. Loads records into Senzing
3. Shows progress (records/second)
4. Generates statistics

### What You'll See:
```
Loading customers...
✓ 1,000 records loaded (125 records/second)
✓ 850 entities created
✓ 150 duplicates found (15% match rate)
✓ Loading complete in 8 seconds
```

### What You'll Have:
- Data loaded into Senzing
- Entity resolution complete
- Statistics dashboard

---

## Step 6: Query Results (15 minutes)

Explore the resolved entities.

### In Kiro, say:
```
"Let's create a query to find duplicates"
```

### What Happens:
1. Kiro generates query program: `src/query/find_duplicates.py`
2. Runs query
3. Shows duplicate entities

### Example Results:
```
Entity ID: 12345
  Records: 3
  - CUSTOMERS:CUST001 (John Smith, john@email.com)
  - CUSTOMERS:CUST042 (J. Smith, jsmith@email.com)
  - CUSTOMERS:CUST089 (John R Smith, john.smith@email.com)
  Confidence: 95%
```

### What You'll Have:
- Query programs in `src/query/`
- List of duplicate entities
- Confidence scores

---

## What's Next?

### For Evaluation/PoC
You're done! You have:
- ✅ Working transformation
- ✅ Data loaded
- ✅ Query results
- ✅ Proof of concept

### For Production Deployment
Continue with:
- **Module 7**: Load additional data sources
- **Module 8**: User acceptance testing
- **Module 9**: Performance testing
- **Module 10**: Security hardening
- **Module 11**: Monitoring setup
- **Module 12**: Production deployment

---

## Common Issues

### "My data doesn't match"
- Check transformation output: `data/transformed/customers.jsonl`
- Verify attribute names are correct
- Run quality scoring: scores should be >70%

### "Installation failed"
- Check platform compatibility
- Verify Python/Java version
- See `docs/guides/INSTALLATION_VERIFICATION.md`

### "Loading is slow"
- Normal for first time (building indexes)
- SQLite is slower than PostgreSQL
- Expect 50-200 records/second

### "No duplicates found"
- Check if data actually has duplicates
- Review match confidence thresholds
- Verify name/address quality

---

## Tips for Success

### Start Small
- Use 100-1,000 records for first test
- Verify results before loading full dataset
- Iterate on mapping if needed

### Check Quality
- Quality scores >70% are good
- Quality scores <50% need improvement
- Review quality report recommendations

### Test Thoroughly
- Load sample data first
- Verify a few entities manually
- Check match confidence scores

### Ask for Help
- Kiro can explain any step
- Use: "Explain why these records matched"
- Use: "How do I improve data quality?"

---

## Next Steps

### Continue Boot Camp
```
"Let's continue to Module 7"
```

### Add More Data Sources
```
"I want to add another data source"
```

### Deploy to Production
```
"Let's prepare for production deployment"
```

### Get Help
```
"I'm stuck on [specific issue]"
```

---

## Resources

- **Full Boot Camp**: See `../../POWER.md`
- **Module Details**: See `../modules/`
- **Troubleshooting**: See `../../steering/common-pitfalls.md`
- **Design Patterns**: See `DESIGN_PATTERNS.md`

---

## Success Checklist

After this quick start, you should have:

- [ ] Seen entity resolution demo (Module 0)
- [ ] Defined business problem (Module 1)
- [ ] Collected data file (Module 2)
- [ ] Mapped data to Senzing format (Module 4)
- [ ] Installed Senzing SDK (Module 5)
- [ ] Loaded data successfully (Module 6)
- [ ] Queried and viewed results (Module 8)
- [ ] Understood how entity resolution works

**Time Invested**: 1-2 hours  
**Value Gained**: Working entity resolution proof of concept

---

**Ready to start?** Open Kiro and say: *"Let's start the Senzing boot camp"*

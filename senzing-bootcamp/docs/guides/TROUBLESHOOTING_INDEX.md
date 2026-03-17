# Troubleshooting Index

Quick reference for common issues organized by module and symptom.

## By Module

### Module 0: Quick Demo
| Issue | Solution | Reference |
|-------|----------|-----------|
| Demo script fails | Check Python version (3.8+) | [Installation Verification](INSTALLATION_VERIFICATION.md) |
| Sample data not loading | Verify file path in `src/quickstart_demo/` | [Module 0 Code Location](../policies/MODULE_0_CODE_LOCATION.md) |
| Import errors | Install Senzing SDK | [SDK Setup](../../steering/steering.md#module-5) |

### Module 1: Business Problem
| Issue | Solution | Reference |
|-------|----------|-----------|
| Unclear requirements | Use design pattern gallery | [Design Patterns](DESIGN_PATTERNS.md) |
| Cost estimation unclear | Use cost calculator | [Cost Calculator](../../steering/cost-calculator.md) |
| Too many data sources | Prioritize by business value | [Complexity Estimator](../../steering/complexity-estimator.md) |

### Module 2: Data Collection
| Issue | Solution | Reference |
|-------|----------|-----------|
| Large files won't upload | Create sample subset | [Data Collection](../modules/MODULE_2_DATA_COLLECTION.md) |
| Database connection fails | Check credentials and network | [Common Pitfalls](../../steering/common-pitfalls.md) |
| Sensitive data concerns | Review privacy guidelines | [Security & Privacy](../../steering/security-privacy.md) |

### Module 3: Data Quality
| Issue | Solution | Reference |
|-------|----------|-----------|
| Low quality scores (<50%) | Review recommendations in report | [Data Quality Scoring](../modules/MODULE_3_DATA_QUALITY_SCORING.md) |
| Missing attributes | Check source data completeness | [Data Quality Scoring](../modules/MODULE_3_DATA_QUALITY_SCORING.md) |
| Inconsistent formats | Add data cleaning step | [Common Pitfalls](../../steering/common-pitfalls.md) |

### Module 4: Data Mapping
| Issue | Solution | Reference |
|-------|----------|-----------|
| Wrong attribute names | Use `mapping_workflow` tool | [Agent Instructions](../../steering/agent-instructions.md) |
| Transformation fails | Check Python syntax | [Common Pitfalls](../../steering/common-pitfalls.md) |
| Quality score still low | Iterate on mapping | [Data Quality Scoring](../modules/MODULE_3_DATA_QUALITY_SCORING.md) |
| Complex transformations | Break into smaller steps | [Common Pitfalls](../../steering/common-pitfalls.md) |

### Module 5: SDK Setup
| Issue | Solution | Reference |
|-------|----------|-----------|
| Installation fails | Check platform compatibility | [Installation Verification](INSTALLATION_VERIFICATION.md) |
| Database connection error | Verify database running | [Recovery Procedures](../../steering/recovery-procedures.md) |
| Version mismatch | Check Senzing version | [Installation Verification](INSTALLATION_VERIFICATION.md) |
| Permission denied | Check file permissions | [Common Pitfalls](../../steering/common-pitfalls.md) |

### Module 6: Single Source Loading
| Issue | Solution | Reference |
|-------|----------|-----------|
| Loading very slow | Check database type (SQLite vs PostgreSQL) | [Performance Monitoring](../../steering/performance-monitoring.md) |
| Out of memory | Reduce batch size | [Common Pitfalls](../../steering/common-pitfalls.md) |
| Records rejected | Check JSON format with `lint_record` | [Agent Instructions](../../steering/agent-instructions.md) |
| Duplicate key errors | Check RECORD_ID uniqueness | [Common Pitfalls](../../steering/common-pitfalls.md) |

### Module 7: Multi-Source Orchestration
| Issue | Solution | Reference |
|-------|----------|-----------|
| Dependency errors | Review load order | [Multi-Source Orchestration](../modules/MODULE_7_MULTI_SOURCE_ORCHESTRATION.md) |
| One source fails | Check error handling | [Recovery Procedures](../../steering/recovery-procedures.md) |
| Parallel loading conflicts | Use sequential loading | [Multi-Source Orchestration](../modules/MODULE_7_MULTI_SOURCE_ORCHESTRATION.md) |

### Module 8: Query and Validation
| Issue | Solution | Reference |
|-------|----------|-----------|
| No results returned | Check entity IDs exist | [Query Validation](../modules/MODULE_8_QUERY_VALIDATION.md) |
| Wrong SDK method | Use `generate_scaffold` tool | [Agent Instructions](../../steering/agent-instructions.md) |
| UAT tests failing | Review test expectations | [UAT Framework](../../steering/uat-framework.md) |

### Module 9: Performance Testing
| Issue | Solution | Reference |
|-------|----------|-----------|
| Slow performance | Profile bottlenecks | [Performance Testing](../modules/MODULE_9_PERFORMANCE_TESTING.md) |
| Memory issues | Increase heap size | [Performance Monitoring](../../steering/performance-monitoring.md) |
| Benchmarks inconsistent | Run multiple iterations | [Performance Testing](../modules/MODULE_9_PERFORMANCE_TESTING.md) |

### Module 10: Security Hardening
| Issue | Solution | Reference |
|-------|----------|-----------|
| Secrets exposed | Use secrets manager | [Security Hardening](../modules/MODULE_10_SECURITY_HARDENING.md) |
| Authentication failing | Check API keys/JWT | [Security Hardening](../modules/MODULE_10_SECURITY_HARDENING.md) |
| Security scan failures | Update dependencies | [Security Hardening](../modules/MODULE_10_SECURITY_HARDENING.md) |

### Module 11: Monitoring
| Issue | Solution | Reference |
|-------|----------|-----------|
| Metrics not collecting | Check Prometheus config | [Monitoring & Observability](../modules/MODULE_11_MONITORING_OBSERVABILITY.md) |
| Alerts not firing | Verify alerting rules | [Monitoring & Observability](../modules/MODULE_11_MONITORING_OBSERVABILITY.md) |
| Dashboard not loading | Check Grafana connection | [Monitoring & Observability](../modules/MODULE_11_MONITORING_OBSERVABILITY.md) |

### Module 12: Deployment
| Issue | Solution | Reference |
|-------|----------|-----------|
| Docker build fails | Check Dockerfile syntax | [Deployment Packaging](../modules/MODULE_12_DEPLOYMENT_PACKAGING.md) |
| Tests failing | Run diagnostics | [Testing Strategy](../../steering/testing-strategy.md) |
| Deployment errors | Check environment config | [Multi-Environment Strategy](../../steering/multi-environment-strategy.md) |

---

## By Symptom

### Performance Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Slow loading | SQLite database | Switch to PostgreSQL |
| High memory usage | Large batch size | Reduce batch size |
| Slow queries | Missing indexes | Add database indexes |
| CPU at 100% | Too many parallel workers | Reduce parallelism |

### Data Quality Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| No matches found | Poor data quality | Improve source data |
| Too many matches | Loose matching rules | Adjust thresholds |
| Wrong matches | Incorrect mapping | Review transformation |
| Missing attributes | Incomplete source data | Add data enrichment |

### Error Messages
| Error | Meaning | Solution |
|-------|---------|----------|
| SENZ0005 | Configuration error | Check engine config |
| SENZ0037 | Database connection | Verify database running |
| SENZ0025 | Invalid JSON | Validate with `lint_record` |
| Import Error | Missing dependency | Install required package |
| Permission Denied | File permissions | Check file ownership |

### Installation Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Command not found | PATH not set | Set environment variables |
| Library not found | Missing dependency | Install system libraries |
| Version mismatch | Wrong Senzing version | Check compatibility |
| Database error | Database not configured | Run database setup |

---

## Quick Diagnostic Steps

### 1. Check Basics
```bash
# Python version
python --version  # Should be 3.8+

# Senzing installed
python -c "import senzing; print(senzing.__version__)"

# Database connection
# (varies by database type)
```

### 2. Check Files
```bash
# Data files exist
ls -lh data/raw/
ls -lh data/transformed/

# Programs exist
ls -lh src/transform/
ls -lh src/load/
ls -lh src/query/
```

### 3. Check Logs
```bash
# Application logs
tail -f logs/application.log

# Error logs
grep ERROR logs/application.log
```

### 4. Run Diagnostics
```python
# In Kiro, ask:
"Run diagnostics on my Senzing setup"
"Check my data quality"
"Validate my transformation output"
```

---

## Decision Tree

```
Problem?
├─ Installation Issue?
│  ├─ Platform compatibility → Check Installation Verification
│  ├─ Missing dependencies → Install required packages
│  └─ Permission errors → Check file permissions
│
├─ Data Quality Issue?
│  ├─ Low scores → Review quality report
│  ├─ Missing data → Check source completeness
│  └─ Wrong format → Fix transformation
│
├─ Performance Issue?
│  ├─ Slow loading → Check database type
│  ├─ High memory → Reduce batch size
│  └─ Slow queries → Add indexes
│
├─ Error Message?
│  ├─ SENZ error → Use explain_error_code tool
│  ├─ Python error → Check syntax and imports
│  └─ Database error → Check connection
│
└─ Unexpected Results?
   ├─ No matches → Check data quality
   ├─ Wrong matches → Review mapping
   └─ Missing data → Check transformation
```

---

## Getting Help

### In Kiro
```
"I'm getting error [error message]"
"Why aren't my records matching?"
"How do I fix [specific issue]?"
"Explain error code SENZ0005"
```

### Documentation
- **Common Pitfalls**: [../../steering/common-pitfalls.md](../../steering/common-pitfalls.md)
- **Troubleshooting Tree**: [../../steering/troubleshooting-decision-tree.md](../../steering/troubleshooting-decision-tree.md)
- **Recovery Procedures**: [../../steering/recovery-procedures.md](../../steering/recovery-procedures.md)

### Senzing Support
- Documentation: https://docs.senzing.com
- GitHub Issues: https://github.com/senzing
- Support Portal: https://senzing.com/support

---

## Prevention Tips

### Before Starting
- ✅ Check prerequisites
- ✅ Verify platform compatibility
- ✅ Review design patterns
- ✅ Understand your data

### During Development
- ✅ Test with small samples first
- ✅ Validate at each step
- ✅ Check quality scores
- ✅ Review error logs

### Before Production
- ✅ Run full test suite
- ✅ Performance benchmarks
- ✅ Security audit
- ✅ Backup procedures

---

## Related Documentation

- **Main Guide**: [../../POWER.md](../../POWER.md)
- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Common Pitfalls**: [../../steering/common-pitfalls.md](../../steering/common-pitfalls.md)
- **Recovery Procedures**: [../../steering/recovery-procedures.md](../../steering/recovery-procedures.md)

---

**Still stuck?** Ask Kiro: *"I need help troubleshooting [your issue]"*

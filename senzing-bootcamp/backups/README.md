# Senzing Boot Camp - Project Backups

This directory contains compressed backup archives of your Senzing Boot Camp project.

## Quick Start

### Create a Backup

```bash
./scripts/backup_project.sh
```

This creates a timestamped ZIP file containing all your project data.

### Restore a Backup

```bash
# Restore to current location (overwrites existing files)
./scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip

# Restore to a new location
./scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip ~/new-project
```

## What Gets Backed Up

The backup includes all user data and project files:

- ✅ `database/` - SQLite database files
- ✅ `data/raw/` - Original source data
- ✅ `data/transformed/` - Senzing-formatted JSON
- ✅ `data/samples/` - Sample data
- ✅ `licenses/` - Senzing license files
- ✅ `config/` - Configuration files
- ✅ `src/` - Your source code
- ✅ `scripts/` - Your scripts
- ✅ `docs/` - Documentation
- ✅ `.env.example` - Environment template

## What Gets Excluded

The backup automatically excludes:

- ❌ `backups/` - Backup files themselves
- ❌ `.git/` - Git repository (use git for version control)
- ❌ `.history/` - Editor history
- ❌ `.env` - Environment secrets (use .env.example as template)
- ❌ `data/temp/` - Temporary files
- ❌ `__pycache__/`, `*.pyc` - Python cache files
- ❌ `node_modules/`, `venv/` - Dependencies (reinstall from requirements)

## Backup Naming Convention

Backups are named with timestamps for easy identification:

```
senzing-bootcamp-backup_YYYYMMDD_HHMMSS.zip
```

Example: `senzing-bootcamp-backup_20260326_143022.zip`
- Date: March 26, 2026
- Time: 14:30:22 (2:30:22 PM)

## When to Create Backups

Create a backup:

- ✅ Before starting a new module
- ✅ After completing a module successfully
- ✅ Before experimenting with new features
- ✅ Before major data reloads
- ✅ Weekly during active development
- ✅ Before upgrading Senzing SDK
- ✅ Before making significant configuration changes

## Backup Management

### List All Backups

```bash
ls -lh backups/*.zip
```

### Check Backup Size

```bash
du -h backups/senzing-bootcamp-backup_20260326_143022.zip
```

### View Backup Contents (without extracting)

```bash
unzip -l backups/senzing-bootcamp-backup_20260326_143022.zip
```

### Delete Old Backups

```bash
# Delete backups older than 30 days
find backups/ -name "*.zip" -mtime +30 -delete

# Or manually delete specific backups
rm backups/senzing-bootcamp-backup_20260320_*.zip
```

## Restore Options

### Option 1: Restore to Current Project (Overwrite)

```bash
./scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip
```

**Warning**: This overwrites existing files in your current project.

### Option 2: Restore to New Location

```bash
./scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip ~/new-project
```

This creates a complete copy of your project in a new location.

### Option 3: Manual Extraction

```bash
# Extract to current directory
unzip backups/senzing-bootcamp-backup_20260326_143022.zip

# Extract to specific directory
unzip backups/senzing-bootcamp-backup_20260326_143022.zip -d ~/new-project

# Extract only specific files
unzip backups/senzing-bootcamp-backup_20260326_143022.zip "database/*" -d ~/restore-db-only
```

## Cross-Platform Compatibility

### Linux/macOS

```bash
# Create backup
./scripts/backup_project.sh

# Restore backup
./scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip
```

### Windows

```bash
# Create backup (Git Bash, WSL, or PowerShell with zip installed)
bash scripts/backup_project.sh

# Restore backup (Git Bash, WSL, or PowerShell with unzip installed)
bash scripts/restore_project.sh backups/senzing-bootcamp-backup_20260326_143022.zip

# Or use Windows Explorer
# Right-click the .zip file → Extract All
```

## Transferring Backups

### Copy to Another Machine

```bash
# Using scp
scp backups/senzing-bootcamp-backup_20260326_143022.zip user@remote:/path/to/destination/

# Using rsync
rsync -avz backups/senzing-bootcamp-backup_20260326_143022.zip user@remote:/path/to/destination/

# Using cloud storage (example with AWS S3)
aws s3 cp backups/senzing-bootcamp-backup_20260326_143022.zip s3://my-bucket/senzing-backups/
```

### Copy from USB Drive

```bash
# Copy backup to USB
cp backups/senzing-bootcamp-backup_20260326_143022.zip /media/usb-drive/

# Copy backup from USB
cp /media/usb-drive/senzing-bootcamp-backup_20260326_143022.zip backups/
```

## Troubleshooting

### Backup Script Fails

**Problem**: `zip: command not found`

**Solution**: Install zip utility
```bash
# Ubuntu/Debian
sudo apt-get install zip

# macOS (usually pre-installed, or use Homebrew)
brew install zip

# Windows
# Install 7-Zip from https://www.7-zip.org/
```

### Restore Script Fails

**Problem**: `unzip: command not found`

**Solution**: Install unzip utility
```bash
# Ubuntu/Debian
sudo apt-get install unzip

# macOS (usually pre-installed, or use Homebrew)
brew install unzip

# Windows
# Install 7-Zip from https://www.7-zip.org/
```

### Backup File Corrupted

**Problem**: Cannot extract backup file

**Solution**: Verify backup integrity
```bash
# Test backup file
unzip -t backups/senzing-bootcamp-backup_20260326_143022.zip

# If corrupted, use a previous backup
ls -lh backups/*.zip
```

### Disk Space Issues

**Problem**: Not enough space for backup

**Solution**: Clean up old backups or temporary files
```bash
# Check disk space
df -h

# Clean up old backups
find backups/ -name "*.zip" -mtime +30 -delete

# Clean up temporary files
rm -rf data/temp/*
```

## Best Practices

1. **Regular Backups**: Create backups before major changes
2. **Keep Multiple Versions**: Don't delete all old backups immediately
3. **Test Restores**: Periodically test restoring to verify backups work
4. **Off-Site Storage**: Copy important backups to cloud storage or external drives
5. **Document Changes**: Note what changed since the last backup
6. **Clean Up**: Delete very old backups to save disk space
7. **Verify Integrity**: Test backup files after creation

## Backup Retention Strategy

Suggested retention policy:

- **Daily backups**: Keep for 7 days
- **Weekly backups**: Keep for 4 weeks
- **Monthly backups**: Keep for 6 months
- **Milestone backups**: Keep indefinitely (completed modules, major achievements)

Example cleanup script:
```bash
# Keep last 7 daily backups
ls -t backups/*.zip | tail -n +8 | xargs rm -f

# Or use find with mtime
find backups/ -name "*.zip" -mtime +7 -delete
```

## Security Considerations

### Sensitive Data in Backups

Backups may contain:
- Database files with entity data
- License files
- Configuration files

**Important**: 
- ❌ Backups do NOT include `.env` files (secrets)
- ✅ Use `.env.example` as a template after restore
- ✅ Store backups securely (encrypted storage, access controls)
- ✅ Don't share backups containing real customer data

### Encrypting Backups

For sensitive data, consider encrypting backups:

```bash
# Encrypt backup with GPG
gpg --symmetric --cipher-algo AES256 backups/senzing-bootcamp-backup_20260326_143022.zip

# Decrypt backup
gpg --decrypt backups/senzing-bootcamp-backup_20260326_143022.zip.gpg > backup.zip
```

## Related Documentation

- [FILE_STORAGE_POLICY.md](../docs/policies/FILE_STORAGE_POLICY.md) - File organization rules
- [QUICK_START.md](../docs/guides/QUICK_START.md) - Getting started guide
- [PROGRESS_TRACKER.md](../docs/guides/PROGRESS_TRACKER.md) - Track your progress

## Questions?

If you have questions about backups:

1. Check this README
2. Review the backup/restore scripts
3. Consult the Senzing Boot Camp documentation
4. Ask in the Senzing community forums

---

**Remember**: Backups are your safety net. Create them regularly and test restores occasionally!

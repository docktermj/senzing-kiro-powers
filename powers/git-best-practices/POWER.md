---
name: "git-best-practices"
displayName: "Git Best Practices"
description: "Essential Git workflows and best practices for clean commit history, effective branching, and team collaboration."
keywords: ["git", "version control", "commits", "branching", "collaboration"]
author: "Kiro Team"
---

# Git Best Practices

## Overview

This power provides essential Git workflows and best practices to help you maintain a clean commit history, use effective branching strategies, and collaborate smoothly with your team. Whether you're working solo or with a large team, these practices will help you avoid common pitfalls and make the most of Git's powerful features.

## Core Principles

1. **Commit Often, Push Regularly** - Small, focused commits are easier to review and revert
2. **Write Clear Commit Messages** - Future you (and your team) will thank you
3. **Branch Strategically** - Use branches to isolate work and enable parallel development
4. **Review Before Committing** - Always check what you're about to commit
5. **Keep History Clean** - Use rebase and squash when appropriate

## Common Workflows

### Workflow: Starting New Feature Work

**Goal:** Create a new feature branch and start development

**Commands:**

```bash
# Update main branch
git checkout main
git pull origin main

# Create and switch to feature branch
git checkout -b feature/user-authentication

# Verify you're on the new branch
git branch
```

**Best Practices:**

- Use descriptive branch names: `feature/`, `bugfix/`, `hotfix/` prefixes
- Always start from an updated main branch
- Keep branch names lowercase with hyphens

### Workflow: Making Commits

**Goal:** Create clear, atomic commits

**Commands:**

```bash
# Check what's changed
git status
git diff

# Stage specific files
git add src/auth.js src/auth.test.js

# Commit with clear message
git commit -m "Add user authentication with JWT tokens"

# Or use interactive staging for partial changes
git add -p
```

**Commit Message Format:**

```text
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Examples:**

- `feat: Add user login endpoint`
- `fix: Resolve memory leak in data processing`
- `docs: Update API documentation for v2.0`
- `refactor: Simplify authentication logic`

### Workflow: Syncing with Remote

**Goal:** Keep your branch up to date with remote changes

**Commands:**

```bash
# Fetch latest changes
git fetch origin

# Rebase your work on top of main
git rebase origin/main

# If conflicts occur, resolve them then:
git add <resolved-files>
git rebase --continue

# Push your changes (use --force-with-lease after rebase)
git push origin feature/user-authentication --force-with-lease
```

## Best Practices

- **Commit early and often** - Small commits are easier to understand and revert
- **Write meaningful commit messages** - Explain why, not just what
- **Review changes before committing** - Use `git diff` and `git status`
- **Pull before you push** - Avoid merge conflicts by staying up to date
- **Use branches for all work** - Never commit directly to main
- **Keep commits atomic** - One logical change per commit
- **Don't commit sensitive data** - Use .gitignore and environment variables

## Common Mistakes to Avoid

### ❌ Mistake: Committing directly to main

```bash
# Bad
git checkout main
git commit -m "Quick fix"
```

### ✅ Solution: Always use a branch

```bash
# Good
git checkout -b hotfix/critical-bug
git commit -m "Fix critical authentication bug"
```

### ❌ Mistake: Vague commit messages

```bash
# Bad
git commit -m "Fixed stuff"
git commit -m "Updates"
```

### ✅ Solution: Be specific and descriptive

```bash
# Good
git commit -m "Fix null pointer exception in user profile loader"
git commit -m "Update dependencies to resolve security vulnerabilities"
```

## Troubleshooting

### Problem: Accidentally committed to wrong branch

**Solution:**

```bash
# Move the commit to a new branch
git branch feature/my-work
git reset --hard HEAD~1
git checkout feature/my-work
```

### Problem: Need to undo last commit

**Solution:**

```bash
# Keep changes, undo commit
git reset --soft HEAD~1

# Discard changes and commit
git reset --hard HEAD~1
```

### Problem: Merge conflicts

**Solution:**

```bash
# See conflicted files
git status

# Edit files to resolve conflicts
# Look for <<<<<<, ======, >>>>>> markers

# After resolving
git add <resolved-files>
git commit
```

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

---

**Type:** Knowledge Base Power (No MCP server required)

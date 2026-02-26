# Project Version Comparison Guide

This document explains common version comparison workflows:

- Initialize a local Git repository
- Local vs Local comparison
- Local vs GitHub comparison
- Line-level change inspection
- VSCode graphical comparison
- Safe engineering practices

---

# 1. Initialize a Local Repository (Baseline Setup)

When you want to use a project as a baseline version for comparison:

```bash
# 1. Navigate to the project directory
cd "/Users/libingchen/Desktop/employee-management-system-main 2"

# 2. Confirm your current location (very important)
pwd

# 3. Check if .git already exists
ls -a

# 4. If there is no .git, initialize a repository
git init

# 5. Add all files
git add .

# 6. Create a baseline commit
git commit -m "baseline version"

# 7. Verify repository status
git status
```

If you see `working tree clean`, the baseline is ready.

---

# 2. Local vs Local Comparison (Two Folders)

Assume:

A = employee-management-system-main 2  
B = 2.12-employee-management-system-main 2  

---

## Method 1: List Different Files (Recommended)

```bash
diff -rq \
--exclude=node_modules \
--exclude=.git \
"/Users/libingchen/Desktop/employee-management-system-main 2" \
"/Users/libingchen/Desktop/2.12-employee-management-system-main 2"
```

Explanation:

- `-r` = recursive
- `-q` = only show file names
- Excludes `.git` and `node_modules`

---

## Method 2: Line-Level Difference (Specific File)

```bash
diff -u \
"/Users/libingchen/Desktop/employee-management-system-main 2/backend/src/controllers/authController.ts" \
"/Users/libingchen/Desktop/2.12-employee-management-system-main 2/backend/src/controllers/authController.ts"
```

---

## Paginated View (Recommended)

```bash
diff -u fileA fileB | less
```

Controls:

- Space = next page
- b = previous page
- q = quit

---

## Method 3: Local vs Local Using Git (Professional Workflow)

```bash
# 1. Navigate to Project A
cd "/Users/libingchen/Desktop/employee-management-system-main 2"

# 2. Initialize and commit baseline (if not done)
git init
git add .
git commit -m "baseline"

# 3. Overwrite A with B (preserve .git)
rsync -av --delete --exclude=".git" \
"/Users/libingchen/Desktop/2.12-employee-management-system-main 2/" \
"/Users/libingchen/Desktop/employee-management-system-main 2/"

# 4. Check modified files
git status

# 5. List changed files
git diff --name-only

# 6. Show all line-level changes
git diff

# 7. Show changes for a specific file
git diff -- backend/src/controllers/authController.ts
```

---

# 3. Local vs GitHub Comparison

## 1. Check Remote Repository

```bash
git remote -v
```

## 2. Add Remote (if missing)

```bash
git remote add origin https://github.com/your-username/your-repository.git
```

## 3. Fetch Remote Data (Safe Operation)

```bash
git fetch origin
```

This does NOT modify local files.

## 4. Compare Local with GitHub main Branch

```bash
git diff origin/main
```

## Show Only File Names

```bash
git diff --name-only origin/main
```

## Show Statistics

```bash
git diff --stat origin/main
```

## Compare a Specific File

```bash
git diff origin/main -- backend/src/controllers/authController.ts
```

## Compare Two Remote Branches

```bash
git diff origin/main origin/dev
```

---

# 4. Understanding Line-Level Diff Output

Example:

```diff
@@ -14,6 +14,10 @@
```

Meaning:

-14  = old version starts at line 14  
,6   = old version has 6 lines  
+14  = new version starts at line 14  
,10  = new version has 10 lines  

Symbols:

- `-` = removed lines (old version)
- `+` = added lines (new version)
- space = unchanged lines

---

# 5. VSCode Graphical Comparison (Recommended for Large Changes)

```bash
code -d \
"/Users/libingchen/Desktop/employee-management-system-main 2" \
"/Users/libingchen/Desktop/2.12-employee-management-system-main 2"
```

This opens a side-by-side comparison interface.

---

# 6. Engineering Safety Rule

Before running any command:

```bash
pwd
```

Always confirm you are in the correct directory.

Do NOT run `git init` in Desktop or your home directory.

---

# 7. Quick Reference Summary

```bash
# Local vs Local
diff -rq A B
diff -u A/file B/file

# Local vs GitHub
git fetch origin
git diff origin/main
git diff --name-only origin/main
git diff --stat origin/main

# Specific file diff
git diff -- path/to/file.ts
```

---

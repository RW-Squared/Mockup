# Quick Setup Guide

## First Time Setup

### 1. Install Prerequisites

**macOS:**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Quarto
brew install quarto

# Install R (optional but recommended)
brew install --cask r
brew install --cask rstudio
```

**Windows:**
1. Download Quarto from https://quarto.org/docs/get-started/
2. Download R from https://cran.r-project.org/
3. Download RStudio from https://posit.co/download/rstudio-desktop/

**Linux:**
```bash
# Ubuntu/Debian
sudo curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
sudo dpkg -i quarto-linux-amd64.deb

# Install R
sudo apt-get install r-base
```

### 2. Verify Installation

```bash
quarto --version
# Should show: 1.3.0 or higher

R --version  # optional
python --version  # optional
```

### 3. Preview the Site

```bash
# Navigate to the site directory
cd /path/to/quarto-site

# Start preview server
quarto preview
```

Your browser should open to `http://localhost:4321`

## Customizing Your Site

### Step 1: Update Personal Information

Edit `index.qmd` and replace:
- Biography text
- Research interests
- Education details
- Award information

### Step 2: Update Contact Links

Edit `_quarto.yml`:
```yaml
navbar:
  right:
    - icon: envelope
      href: mailto:YOUR_EMAIL@willamette.edu  # Change this
    - icon: github
      href: https://github.com/YOUR_USERNAME  # Change this
```

### Step 3: Add Your Publications

Edit `publications.qmd`:
- Replace example publications with your own
- Update BibTeX entries if using bibliography

### Step 4: Add Research Pages

Create files in `research/` directory:
```bash
touch research/panel-data.qmd
touch research/political-economy.qmd
```

### Step 5: Customize Colors (Optional)

Edit `css/steampunk-art-nouveau.scss`:
```scss
// Change these to your preferred colors
$lavender: #AF98E6;
$pink: #DA99E6;
$pale-yellow: #E5DD97;
```

## Creating Content

### New Blog Post

1. Create directory:
```bash
mkdir -p posts/my-new-post
```

2. Copy template:
```bash
cp posts/_template.qmd posts/my-new-post/index.qmd
```

3. Edit the file and update:
   - Title
   - Date
   - Categories
   - Content

4. Preview:
```bash
quarto preview posts/my-new-post/index.qmd
```

### New Research Page

1. Create file:
```bash
touch research/my-topic.qmd
```

2. Add frontmatter:
```yaml
---
title: "My Research Topic"
---
```

3. Add to research index in `research/index.qmd`

## Testing Before Deployment

### Check All Links

```bash
quarto render
# Check console for any broken links or errors
```

### Test Locally

```bash
quarto preview
# Click through all pages
# Test responsive design (resize browser)
# Verify code execution
```

### Validate HTML

Use browser dev tools (F12) to check for:
- Console errors
- CSS issues
- Missing images

## Deploying

### Option 1: GitHub Pages

```bash
# Build the site
quarto render

# The site is now in _site/ directory
# Commit and push to GitHub

git add .
git commit -m "Initial site build"
git push

# Go to GitHub repository settings → Pages
# Select: Deploy from branch → main → /docs
```

### Option 2: Netlify

```bash
# Build
quarto render

# Drag and drop _site/ folder to netlify.com
# Or connect your GitHub repository
```

### Option 3: Quarto Pub (Easiest)

```bash
quarto publish quarto-pub
# Follow prompts to authenticate and deploy
```

## Troubleshooting

### Problem: Site doesn't load

**Solution:**
```bash
# Clear cache and rebuild
rm -rf .quarto/
rm -rf _site/
quarto render
```

### Problem: R code doesn't execute

**Solution:**
```r
# Install missing packages
install.packages("tidyverse")
install.packages("ggplot2")
```

### Problem: CSS not updating

**Solution:**
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+F5 (Windows)
- Clear browser cache
- Restart preview server

### Problem: Images not showing

**Solution:**
- Check image paths are relative to .qmd file
- Verify images are in `images/` directory
- Check file extensions match exactly

## Next Steps

1. ✅ Preview site locally
2. ✅ Update personal information
3. ✅ Add your publications
4. ✅ Create your first blog post
5. ✅ Deploy to GitHub Pages or Netlify
6. ✅ Share your new website!

## Getting Help

- [Quarto Documentation](https://quarto.org/docs/)
- [Quarto Community](https://github.com/quarto-dev/quarto-cli/discussions)
- [Quarto Blog Examples](https://quarto.org/docs/gallery/#websites)

## Regular Maintenance

```bash
# Add new blog post
mkdir -p posts/YYYY-MM-DD-title
cp posts/_template.qmd posts/YYYY-MM-DD-title/index.qmd
# Edit and preview

# Update publications
# Edit publications.qmd

# Rebuild and deploy
quarto render
git add .
git commit -m "Update site"
git push
```

---

**You're ready to go! 🚀**

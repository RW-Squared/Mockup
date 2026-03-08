# Robert W. Walker Academic Website

A modern, Art Nouveau-inspired academic website built with Quarto, featuring a steampunk aesthetic with elegant pastel-jewel tones and deep grays.

## Design Philosophy

This website combines **Art Nouveau flowing aesthetics** with **compact, efficient layouts** to create a distinctive academic presence that balances beauty with function.

### Color Palette

- **Lavender** (#AF98E6) - Primary accent
- **Pink** (#DA99E6) - Secondary accent  
- **Pale Yellow** (#E5DD97) - Highlights and awards
- **Rose** (#DD92C5) - Education and contact
- **Periwinkle** (#9CA6E3) - Metadata and secondary text
- **Deep Grays** (#0f1115, #16181d, #1a1c20, #2a2d35) - Backgrounds

### Typography

- **Headers**: Baskerville, Georgia (elegant serif)
- **Body**: Georgia, serif with 1.6 line-height for readability
- **Code**: Monokai theme with proper syntax highlighting

## Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) (version 1.3 or higher)
- R (version 4.0 or higher) - optional but recommended
- Python 3.8+ - optional for Python-based analyses

## Installation

### 1. Install Quarto

```bash
# macOS
brew install quarto

# Or download from https://quarto.org/docs/get-started/
```

### 2. Clone and Setup

```bash
git clone https://github.com/robertwwalker/robertwwalker.work.git
cd robertwwalker.work

# Copy your hero banner image
cp /path/to/your/hero-banner.jpg images/hero-banner.jpg

# Preview the site
quarto preview
```

### 3. Install R Packages (if using R)

```r
install.packages(c(
  "tidyverse",
  "here", 
  "broom",
  "modelsummary",
  "ggplot2",
  "patchwork"
))
```

## Project Structure

```
.
├── _quarto.yml           # Main configuration
├── index.qmd             # Homepage
├── publications.qmd      # Publications page
├── css/
│   ├── steampunk-art-nouveau.scss  # Theme styles
│   └── custom.css        # Custom component styles
├── images/
│   └── hero-banner.jpg   # Teaching banner image
├── posts/                # Blog posts
│   └── panel-viz/
│       └── index.qmd
├── research/             # Research pages
│   └── index.qmd
└── teaching/             # Teaching materials
    └── index.qmd
```

## Customization

### Update Personal Information

1. **Homepage** (`index.qmd`): Update biography, research interests, education
2. **Publications** (`publications.qmd`): Add your publications
3. **Contact Info**: Update email, GitHub, Twitter links in `_quarto.yml`

### Modify Colors

Edit `css/steampunk-art-nouveau.scss`:

```scss
// Change primary colors
$lavender: #AF98E6;  // Your custom color
$pink: #DA99E6;      // Your custom color
```

### Add New Pages

Create a new `.qmd` file:

```markdown
---
title: "My New Page"
---

## Content here
```

Then add to navigation in `_quarto.yml`:

```yaml
navbar:
  left:
    - text: "New Page"
      href: new-page.qmd
```

## Content Creation

### Blog Posts

Create a new post in `posts/`:

```bash
mkdir -p posts/my-new-post
touch posts/my-new-post/index.qmd
```

Template:

```markdown
---
title: "My Post Title"
author: "Robert W. Walker"
date: "2024-03-08"
categories: [R, statistics]
---

## Introduction

Your content here...
```

### Research Pages

Add research topics to `research/`:

```markdown
---
title: "My Research Topic"
---

## Overview

Research description...

## Publications

- Paper 1
- Paper 2
```

### Code Execution

Quarto automatically executes R and Python code blocks:

````markdown
```{r}
library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point()
```
````

````markdown
```{python}
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df.plot(x='x', y='y')
```
````

## Building and Deployment

### Local Preview

```bash
quarto preview
```

### Build for Production

```bash
quarto render
```

This creates a `_site/` directory with the complete website.

### Deploy to GitHub Pages

1. **Setup GitHub repository**:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/robertwwalker/robertwwalker.work.git
git push -u origin main
```

2. **Configure GitHub Pages**:

```bash
# Add to _quarto.yml
project:
  type: website
  output-dir: docs

# Build
quarto render

# Commit and push
git add .
git commit -m "Build site"
git push
```

3. Go to repository **Settings → Pages** and select `main` branch and `/docs` folder.

### Deploy to Netlify

```bash
# Build
quarto render

# Drag and drop _site/ folder to Netlify
# Or connect GitHub repository
```

## Reveal.js Presentations

Create presentation slides:

````markdown
---
title: "My Presentation"
format: revealjs
theme: [default, css/steampunk-art-nouveau.scss]
---

## Slide 1

Content

## Slide 2

More content
````

Preview:

```bash
quarto preview presentation.qmd
```

## Advanced Features

### Mathematical Equations

```markdown
Inline: $E = mc^2$

Display:
$$
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$
```

### Callout Blocks

```markdown
::: {.callout-note}
## Note Title
Important information
:::

::: {.callout-tip}
Helpful tip
:::

::: {.callout-warning}
Warning message
:::
```

### Cross-References

```markdown
See @fig-plot for visualization.

```{r}
#| label: fig-plot
#| fig-cap: "My caption"

plot(1:10)
```
```

## Maintaining the Site

### Regular Updates

1. **Blog posts**: Add to `posts/` directory
2. **Publications**: Update `publications.qmd` with new work
3. **Teaching**: Update course materials in `teaching/`
4. **Images**: Place in `images/` directory

### Version Control

```bash
# Regular workflow
git add .
git commit -m "Add new blog post"
git push

# Rebuild and deploy
quarto render
git add docs/
git commit -m "Update site"
git push
```

## Troubleshooting

### Site not rendering?

```bash
# Clear cache
quarto clean

# Re-render
quarto render
```

### CSS not updating?

- Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+F5)
- Clear Quarto cache: `rm -rf _site/`

### R/Python code errors?

- Check package installation
- Verify code chunk options
- Use `freeze: auto` in `_quarto.yml` for computationally expensive code

## Resources

- [Quarto Documentation](https://quarto.org/docs/guide/)
- [Quarto Gallery](https://quarto.org/docs/gallery/)
- [Awesome Quarto](https://github.com/mcanouil/awesome-quarto)
- [Quarto GitHub Discussions](https://github.com/quarto-dev/quarto-cli/discussions)

## License

Website design and theme: © 2024 Robert W. Walker

Content: All rights reserved unless otherwise noted.

## Contact

- **Email**: rwalker@willamette.edu
- **GitHub**: [@robertwwalker](https://github.com/robertwwalker)
- **Website**: [robertwwalker.work](https://robertwwalker.work)

---

**Built with [Quarto](https://quarto.org) · Designed with artistry and precision**

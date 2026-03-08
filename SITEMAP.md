# Site Map & Overview

## Site Structure

```
robertwwalker.work/
│
├── Home (index.qmd)
│   ├── Hero Banner with Teaching Image
│   ├── Biography
│   ├── Research Interests
│   ├── Recent Work Highlights
│   ├── Education Timeline
│   ├── Skills Visualization
│   └── Contact Links
│
├── Research (research/index.qmd)
│   ├── Overview
│   ├── Current Projects
│   ├── Research Areas
│   │   ├── Causal Inference (research/causal-inference.qmd)
│   │   ├── Panel Data Methods (research/panel-data.qmd)
│   │   └── Political Economy (research/political-economy.qmd)
│   └── Software & Data
│
├── Teaching (teaching/index.qmd)
│   ├── Current Courses
│   │   ├── DADM (teaching/dadm.qmd)
│   │   └── Essex Summer School (teaching/essex.qmd)
│   ├── Teaching Philosophy
│   ├── Student Resources
│   └── Office Hours
│
├── Publications (publications.qmd)
│   ├── Journal Articles
│   ├── Working Papers
│   ├── Citation Metrics
│   └── Topics
│
└── Blog (posts/index.qmd)
    └── Individual Posts
        └── Panel Data Viz (posts/panel-viz/index.qmd)
```

## Page Descriptions

### Homepage (`index.qmd`)
**Purpose**: First impression and quick overview  
**Design**: Art Nouveau Compact with hero banner  
**Sections**:
- Hero banner with teaching image and tagline
- Compact biography with Warren Miller Prize highlight
- Research interests grid with icons
- Recent work cards
- Education timeline with flowing SVG line
- Circular skill indicators
- Contact buttons

**Key Features**:
- Responsive 3-column layout (2 main + 1 sidebar)
- Custom CSS classes for all components
- Ornamental Art Nouveau decorations
- Color-coded sections

### Research Section

#### Main Research Page (`research/index.qmd`)
- Overview of research program
- Current active projects
- Links to detailed topic pages
- Software and data availability

#### Topic Pages (e.g., `research/causal-inference.qmd`)
- Detailed methodology discussion
- Visual examples with R code
- Current projects in this area
- Publications
- Teaching materials
- Recommended reading

**Template for New Research Pages**:
```markdown
---
title: "Your Research Topic"
---

## Overview
## Methods
## Current Projects
## Publications
## Teaching
## Resources
```

### Teaching Section

#### Main Teaching Page (`teaching/index.qmd`)
- Course listings
- Teaching philosophy
- Student resources (R/Python setup)
- Office hours and booking

#### Course Pages (e.g., `teaching/dadm.qmd`)
- Course description
- Topics covered
- Materials and slides
- Example assignments

### Publications Page (`publications.qmd`)
- Journal articles with abstracts
- Working papers
- Citation metrics visualization
- Organized by topic

**Features**:
- Callout blocks for abstracts
- Links to PDFs and code
- BibTeX ready
- Visualization of citations over time

### Blog (`posts/index.qmd`)
- Grid layout of posts
- Category filtering
- Date sorting
- Featured images

**Blog Post Template** (`posts/_template.qmd`):
- Standard frontmatter
- R code execution
- Session info
- Consistent styling

## Color Usage Guidelines

### Color Assignments by Section

| Color | Hex | Usage |
|-------|-----|-------|
| Lavender | #AF98E6 | Primary accents, main headings, links |
| Pink | #DA99E6 | Secondary accents, research sections |
| Pale Yellow | #E5DD97 | Awards, achievements, highlights |
| Rose | #DD92C5 | Education, personal info |
| Periwinkle | #9CA6E3 | Metadata, dates, categories |

### Typography Hierarchy

```
H1: 3rem, gradient (Lavender → Pink → Yellow), Baskerville
H2: 1.5rem, Pink, Baskerville, bottom border
H3: 1.25rem, Periwinkle, Baskerville
Body: 0.875-1rem, #b4b7be, Baskerville
Code: Monokai theme, Pale Yellow accents
```

## Custom CSS Classes

### Homepage Components

```css
.hero-banner              /* Main hero section */
.hero-content            /* Content overlay */
.hero-title              /* Title styling */
.bio-card                /* Biography card */
.research-card           /* Research interests */
.education-card          /* Education timeline */
.skills-card             /* Skills visualization */
.contact-card            /* Contact buttons */
.work-card              /* Recent work cards */
```

### Usage Example

```markdown
::: {.bio-card}
Your biography content
:::
```

## Navigation Structure

### Main Navbar
- Left: About, Research, Teaching, Publications, Blog
- Right: Email, GitHub, Twitter icons

### Sidebar Navigation
- Research section: Collapsible topics
- Teaching section: Course listings

## Content Guidelines

### Writing Style
- Professional but approachable
- Use active voice
- Include code examples
- Provide context and motivation

### Code Blocks
- Always include package loading
- Use meaningful variable names
- Add comments for complex operations
- Show session info in tutorials

### Images
- Place in `images/` directory
- Use descriptive filenames
- Optimize for web (< 500KB)
- Include alt text

### Links
- Use relative paths for internal links
- Open external links in new tab (automatic)
- Include link text that describes destination

## Maintenance Tasks

### Weekly
- Check for new publications to add
- Review and respond to any issues
- Update course materials if teaching

### Monthly
- Write new blog post
- Update citation metrics
- Review and update CV/publications

### Semester
- Update course listings
- Add new teaching materials
- Update research project status

### Annual
- Review entire site for updates
- Update biography if needed
- Refresh research interests
- Add new projects/publications

## SEO Considerations

### Already Implemented
- Semantic HTML structure
- Descriptive page titles
- Meta descriptions in frontmatter
- Clean, readable URLs
- Fast loading times
- Mobile responsive

### To Add (Optional)
- Google Analytics
- Structured data (Schema.org)
- Social media meta tags
- Sitemap generation

## Accessibility

### Current Features
- Semantic HTML
- ARIA labels on icons
- Color contrast (WCAG AA compliant)
- Keyboard navigation
- Alt text on images

### Best Practices
- Use headings in order (H1 → H2 → H3)
- Provide text alternatives for visual content
- Ensure sufficient color contrast
- Test with screen readers

## Performance

### Optimizations
- CSS/SCSS compilation
- Minimal JavaScript
- Image optimization
- Code syntax highlighting (client-side)

### Monitoring
- Use browser DevTools
- Check PageSpeed Insights
- Test on mobile devices
- Monitor load times

## Version Control Strategy

### Branching
```bash
main        # Production site
develop     # Development changes
feature/*   # New features
post/*      # New blog posts
```

### Commit Messages
```
feat: Add new research page on panel data
fix: Correct citation formatting
docs: Update README with new instructions
style: Adjust color scheme
post: Add visualization tutorial
```

## Backup Strategy

### What to Backup
- All `.qmd` source files
- Images in `images/`
- Custom CSS/SCSS
- Configuration `_quarto.yml`
- BibTeX files

### Where
- GitHub (automatic)
- Local backup
- Cloud storage (optional)

## Future Enhancements

### Potential Additions
- [ ] CV as downloadable PDF
- [ ] Interactive data visualizations
- [ ] Project showcase pages
- [ ] Student testimonials
- [ ] Photo gallery
- [ ] Newsletter signup
- [ ] Search functionality
- [ ] Comment system for blog

### Technical Improvements
- [ ] Dark/light mode toggle
- [ ] Custom 404 page
- [ ] RSS feed for blog
- [ ] Integration with Google Scholar
- [ ] Automated citation updates

---

**Last Updated**: 2024-03-08  
**Maintained by**: Robert W. Walker

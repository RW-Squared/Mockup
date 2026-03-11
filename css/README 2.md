# Circular Landing Page - Implementation Guide

## What Changed

I've transformed your landing page into an **ultra-minimal design** with nearly transparent animated circular spots featuring stunning lavender-pink professional typography in **Inter** (modern, clean, professional font), maximizing the visibility of your background image.

## New Files

### 1. **index.qmd** (Modified)
- Minimal text: Just your name and title (small, subtle)
- Six circular navigation spots in a single row
- Lower page positioning for dramatic entrance
- Nearly zero visual clutter - background image dominates

### 2. **cgpt-circles.css** (New)
- **Quarto Override**: Removes default Quarto spacing that caused scrolling
- **Flexbox Layout**: Ensures footer is always visible at page bottom
- **Balanced Grid**: 3 columns × 2 rows (perfectly even distribution)
- **Bottom Third**: Anchored at 68vh for optimal positioning
- **Quarto Override**: Removes default Quarto spacing that caused scrolling
- **Flexbox Layout**: Ensures footer always visible at page bottom
- **Balanced Grid**: 3 columns × 2 rows (perfectly even distribution)
- **40% Background**: Top 40% of viewport shows pure background image
- **Left-Aligned**: Content positioned at 25% from left edge
- **Harmonious Garamond Typography**: EB Garamond (elegant serif) for headings/circles, Cormorant Garamond (refined serif) for body text
- **Nearly transparent circles** (97% transparent)
- **Lavender-pink elegant typography** 
- Responsive: 3 columns (desktop/tablet), 2 columns (mobile)
- Lower page positioning (content starts at 40vh)
- Generous spacing between circles (2rem gaps)
- Subtle text that doesn't compete with background
- Floating animations with lavender-pink glow effects
- Hover effects with rotating lavender-pink rings
- Fully responsive design for all screen sizes

**Footer**: The page footer (defined in `_quarto.yml`) displays at the bottom with copyright and Quarto attribution.

### 3. **steampunk-cgpt-r3.scss** (Updated)
- **Harmonious Garamond Pairing**: Clean, elegant typography throughout
- **EB Garamond**: Classic elegant serif for headings, navbar title, and circles
- **Cormorant Garamond**: Refined serif for body text and navbar links
- Both fonts from the Garamond family for cohesive aesthetic
- Clean, sharp, highly readable typography

### 3. **_quarto.yml** (Updated)
- Added `css/cgpt-circles.css` to the CSS list
- All other settings remain unchanged

## Key Features

### 🎯 Minimal Layout
- **Background Visibility**: Top 40% of viewport shows pure background image
- **Left-Aligned**: Content positioned at 25% from left edge (not centered)
- **Balanced Grid**: 3 columns × 2 rows on desktop (perfectly even distribution)
- **Flexible Adaptation**: 3 columns on tablet, 2 columns on mobile
- **Even Rows**: All rows have equal number of circles (3-3 or 2-2-2)
- **No Clipping**: All circles fully visible with proper overflow
- **Flexbox Layout**: Ensures footer always visible at bottom
- **Better Spacing**: 2rem gaps for visual balance
- **Readable Typography**: Optimized font sizes
- **Fully Responsive**: Grid maintains balance at all screen sizes

### ✨ Subtle Animations
- **Floating Effect**: Each circle gently floats up and down with unique timing
- **Glow Pulse**: Subtle pulsing glow effect
- **Rotating Ring**: On hover, a colorful ring rotates around the circle
- **Scale Transform**: Circles grow and lift on hover

### 🎨 Visual Design
- **Nearly Transparent**: Circles are 97% transparent, showing the background through
- **Lavender-Pink Typography**: Elegant color (#E8BADB)
- **Garamond Font Family**: 
  - **EB Garamond** - Classic elegant serif for headings and circle labels
  - **Cormorant Garamond** - Refined variant for readable body text
- **Harmonious Pairing**: Both fonts from Garamond family for cohesive look
- **Clean & Sharp**: Professional, highly readable typography
- **Left-Aligned**: Title and content positioned at 25% from left edge
- **Subtle Borders**: Minimal lavender-pink border glow
- **Elegant Simplicity**: Clean, sophisticated aesthetic
- **Steampunk Harmony**: Matches your existing purple/pink theme

### 📱 Responsive
- **Desktop (>768px)**: Single horizontal row of 6 circles
- **Tablet (768px)**: Row wraps naturally
- **Mobile (<480px)**: 2-3 circles per row
- Sizes and spacing adjust automatically

## Installation

**IMPORTANT**: The new `cgpt-circles.css` includes critical overrides for Quarto's default spacing. Without these overrides, the landing page will have unwanted scrolling due to Quarto's `body { min-height: 100vh }`, `#quarto-content { min-height: 100vh }`, and padding settings. The CSS now caps the body at exactly 100vh and removes all padding to ensure perfect viewport fit.

1. Replace your current `index.qmd` with the new version
2. Add `cgpt-circles.css` to your `css/` folder
3. Replace `steampunk-cgpt-r3.scss` with the updated version (synchronized Inter font)
4. Update `_quarto.yml` to include the new CSS file (if not already present)
5. Render your Quarto site

```bash
quarto render
```

**Font Synchronization**: The SCSS file has been updated to use Inter throughout for consistency with the landing page.

## Customization Options

### Adjust Page Positioning
```css
/* Positioning is controlled by padding-top on #quarto-content */
body:has(.home-hero-overlay) #quarto-content {
  padding-top: 40vh; /* Top 40% shows background */
}

/* On tablet */
@media (max-width: 768px) {
  body:has(.home-hero-overlay) #quarto-content {
    padding-top: 35vh;
  }
}

/* On mobile */
@media (max-width: 480px) {
  body:has(.home-hero-overlay) #quarto-content {
    padding-top: 30vh;
  }
}
```

### Adjust Left Positioning
```css
/* Content is positioned 25% from left edge */
body:has(.home-hero-overlay) main.content {
  padding-left: 25%;
}

/* On tablet - less padding */
@media (max-width: 768px) {
  body:has(.home-hero-overlay) main.content {
    padding-left: 15%;
  }
}

/* On mobile - minimal padding */
@media (max-width: 480px) {
  body:has(.home-hero-overlay) main.content {
    padding-left: 5%;
  }
}
```

### Adjust Spacing
```css
.circle-grid {
  gap: 2rem; /* Space between circles */
  max-width: 750px; /* Max grid width */
}
```

### Change Grid Structure
```css
.circle-grid {
  /* Current: 3 balanced columns (2 rows of 3) */
  grid-template-columns: repeat(3, 1fr);
  
  /* For 6 columns (single row): */
  grid-template-columns: repeat(6, 1fr);
  
  /* For 2 columns (3 rows): */
  grid-template-columns: repeat(2, 1fr);
  
  /* For auto-fit (variable): */
  grid-template-columns: repeat(auto-fit, minmax(108px, 1fr));
}
```

### Change Typography
```css
/* Current Garamond pairing */
/* Headings & circles: EB Garamond (classic elegant serif) */
/* Body text: Cormorant Garamond (refined serif) */

/* To change fonts site-wide: */
/* 1. Update imports in both CSS and SCSS files */
@import url('https://fonts.googleapis.com/css2?family=YourFont&display=swap');

/* 2. Update font variables in SCSS */
$font-family-base: 'YourBodyFont', Georgia, serif;
$font-family-headings: 'YourHeadingFont', Georgia, serif;

/* 3. Update in cgpt-circles.css */
.circle-card a {
  font-family: 'YourHeadingFont', Georgia, serif;
}

/* Alternative elegant serif pairings: */
/* - Playfair Display + Lora */
/* - Libre Baskerville + Source Sans Pro */
/* - Crimson Text + Lato */
```
```

### Change Colors
Modify the gradient colors:
```css
background: linear-gradient(135deg, 
  rgba(175, 152, 230, 0.25),  /* Purple */
  rgba(218, 153, 230, 0.15)   /* Pink */
);
```

### Disable Animations
Remove or comment out the animation line:
```css
/* animation: floatSpot 6s ease-in-out infinite; */
```

## Optional: Constellation Background

To add twinkling star effects between circles, add the `constellation` class:

```markdown
::: {.circle-grid .constellation}
```

## Subpages Unchanged

All your subpages (Research, Teaching, Publications, etc.) maintain their current styling with:
- Rectangular cards (cgpt-cards.css)
- Floating cards (floating-card-standalone.css)
- Navbar branding (navbar-branding.css)

Only the landing page (index.qmd) uses the new circular design.

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (including iOS)
- Backdrop blur requires modern browsers (2020+)

## Need Help?

- Adjust animation timings in the `@keyframes` sections
- Modify hover effects in the `.circle-card a:hover` section
- Change responsive breakpoints in the `@media` queries

Enjoy your new minimal, animated landing page! ✨

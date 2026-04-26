# SmartC Calamansi Dashboard - Design Guide

This document outlines the design system, styling conventions, and UI components used in the SmartC Calamansi Dashboard, based on the implementation in `dashboard.html` and `base.html`. The project uses Tailwind CSS with a custom configuration.

---

## 1. Typography

The primary font for the application is **DM Sans**.

### Custom Tailwind Text Sizes
Configured specifically for the UI hierarchy:
- `text-ui-tiny`: `12px` (line-height: `13px`)
- `text-ui-base`: `14px` (line-height: `18px`)
- `text-ui-header`: `15px` (line-height: `22px`)
- `text-ui-metric`: `20px` (line-height: `24px`)
- `text-ui-title`: `22px` (line-height: `28px`)

### Common Text Patterns
- **Main Titles:** `text-xl font-bold tracking-tight text-gray-900 dark:text-white`
- **Subtitle/Muted:** `text-xs text-gray-500 dark:text-dark-muted`
- **Section Headers (Overlines):** `text-[9px]` or `text-[10px] font-bold uppercase tracking-widest text-gray-400 dark:text-dark-muted`
- **Metrics:** `text-ui-title font-bold` or `text-lg font-bold`

---

## 2. Color Palette

The application supports both Light and Dark modes.

### Brand Colors
- **Primary:** `#046307` (Deep Green)
- **Secondary:** `#f3f4f6` (Light Gray)

### Status Colors
- **High Quality / Success:** Primary Green (`#046307`) with light green backgrounds (`bg-green-30` or `bg-green-900/20`)
- **Low Quality / Warning:** Yellow (`#eab308` / `text-yellow-500`)
- **Rejected / Danger:** Red (`#ef4444` / `text-red-500` or `text-red-600`)
- **Info:** Blue (`text-blue-600`) with light blue backgrounds

### Dark Mode Theme (`dark:*`)
- **Background (`dark-bg`):** `#111827`
- **Cards/Surfaces (`dark-card`):** `#1f2937`
- **Borders (`dark-border`):** `#374151`
- **Main Text (`dark-text`):** `#f9fafb`
- **Muted Text (`dark-muted`):** `#9ca3af`

---

## 3. Layout & Spacing

### Containers & Grids
- **Main Content Wrapper:** `max-w-7xl mx-auto space-y-4 p-8`
- **Standard Grid:** `grid grid-cols-1 lg:grid-cols-2 gap-4`
- **Card Padding:** `p-5`

### Borders, Shadows & Radius
- **Cards:** `rounded-xl border border-gray-100 dark:border-dark-border shadow-sm`
- **Modals:** `rounded-2xl shadow-2xl`
- **Form Inputs:** `rounded-xl`
- **Standard Buttons:** `rounded-lg`
- **Small Badges/Tags:** `rounded` or `rounded-md`

---

## 4. UI Components

### Cards
Standard presentation surface for metrics and charts:
```html
<div class="bg-white dark:bg-dark-card p-5 rounded-xl shadow-sm border border-gray-100 dark:border-dark-border">
    <!-- Card Content -->
</div>
```

### Buttons

**1. Primary Action Button (e.g., Export)**
```html
<button class="px-3 py-1.5 bg-primary text-white rounded-lg text-xs font-medium hover:opacity-90 transition-opacity">
    Button Text
</button>
```

**2. Modal Primary Button (Larger)**
```html
<button class="px-4 py-2.5 bg-primary text-white text-xs font-bold rounded-xl hover:opacity-90 shadow-lg shadow-primary/20 transition-all uppercase tracking-widest">
    Apply Range
</button>
```

**3. Secondary/Cancel Button**
```html
<button class="px-4 py-2.5 text-xs font-bold text-gray-500 dark:text-dark-muted hover:bg-gray-50 dark:hover:bg-gray-800 rounded-xl transition-all uppercase tracking-widest">
    Cancel
</button>
```

**4. Filter Toggle Buttons**
- *Active state:* `px-3 py-1 text-[10px] font-bold uppercase tracking-wider bg-primary text-white rounded-md shadow-sm`
- *Inactive state:* `px-3 py-1 text-[10px] font-bold uppercase tracking-wider text-gray-500 hover:text-gray-700 dark:text-dark-muted dark:hover:text-white transition-colors`

### Form Inputs
Used in modals and settings:
```html
<label class="block text-[10px] font-bold text-gray-400 dark:text-dark-muted uppercase tracking-widest mb-1.5">
    Label Text
</label>
<input class="w-full bg-gray-50 dark:bg-gray-800/50 border border-gray-100 dark:border-dark-border rounded-xl px-4 py-2.5 text-sm dark:text-white focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all">
```

### Tables
Clean, spaced rows with hover effects:
- **Header Row:** `text-[11px] font-bold text-gray-400 dark:text-dark-muted uppercase tracking-widest bg-gray-50 dark:bg-gray-800/50 border-b border-gray-100 dark:border-dark-border`
- **Cells:** `px-6 py-4`
- **Body Rows:** `hover:bg-gray-50/50 dark:hover:bg-gray-700/30 transition-colors`

### Badges / Tags
Used for status classification inside tables:
```html
<span class="px-2 py-0.5 text-primary rounded font-medium uppercase">High Quality</span>
```

---

## 5. Charts (Apexcharts) Only if applicable.

Charts are styled to match the UI theme seamlessly:
- **Container Height:** `h-64` or `h-72` (to prevent resize loops, explicitly defined).
- **Fonts:** Inherit `DM Sans`.
- **Colors:** Match the status colors (`#046307`, `#eab308`, `#ef4444`).
- **Grid Lines:** `strokeDashArray: 4` with `#f3f4f6` (light) or `#374151` (dark).
- **Tooltips:** Respect the active `dark` or `light` theme.

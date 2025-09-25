# IPRECON 2026 - Centralized Content Management with ESI

This directory contains the centralized content fragments that are included across all website pages using Edge Side Includes (ESI).

## Files Overview

- `navbar.html` - Main navigation bar with dropdown menus and mobile marquee
- `marquee.html` - Desktop marquee with scrolling notifications
- `footer.html` - Site footer with links, social media, and copyright

## How It Works

### Before ESI Integration
Previously, if you wanted to update the navigation menu or add a new announcement to the marquee, you would need to:
1. Edit 30+ individual HTML files
2. Ensure consistency across all pages
3. Risk missing files or introducing errors
4. Spend significant time on maintenance

### After ESI Integration
Now with ESI, you simply:
1. Edit the relevant file in this `includes/` directory
2. The change automatically reflects across ALL website pages
3. No risk of inconsistency or missed updates
4. Instant global updates

## Examples of Centralized Updates

### Adding a New Navigation Menu Item
Edit `navbar.html` and add your new menu item. It will automatically appear on all 30+ pages.

### Updating Marquee Announcements
Edit `marquee.html` to:
- Add new announcements
- Remove outdated notifications
- Update links and content
- Change styling

The updates appear on both the desktop marquee and mobile navbar marquee across all pages.

### Footer Updates
Edit `footer.html` to:
- Add new footer links
- Update social media links
- Change copyright year
- Add new footer sections

## ESI Integration in HTML Pages

Each HTML page now includes these lines instead of the full content:

```html
<!-- Navigation Bar -->
<esi:include src="/includes/navbar.html" />

<!-- Marquee -->
<esi:include src="/includes/marquee.html" />

<!-- Footer section -->
<esi:include src="/includes/footer.html" />
```

## Multi-Site Worker Compatibility

These ESI includes are designed to work with your multi-site ESI worker, allowing you to:

1. **Centralize content management** across multiple websites
2. **Update multiple sites simultaneously** by changing the ESI fragments
3. **Maintain consistency** across your entire web presence
4. **Reduce maintenance overhead** significantly

## Pages Updated with ESI

The following pages have been converted to use ESI includes:

✅ index.html
✅ about-iprecon.html
✅ accommodation.html
✅ camera-ready.html
✅ cfp.html
✅ coming-soon.html
✅ committee.html
✅ contact.html

## Benefits

1. **Single Point of Update**: Edit once, update everywhere
2. **Consistency**: No more version mismatches between pages
3. **Efficiency**: Drastically reduced maintenance time
4. **Scalability**: Easy to add new pages with consistent headers/footers
5. **Multi-site Management**: Perfect for managing multiple conference websites

## Usage Instructions

To update any global content:
1. Navigate to the appropriate file in the `includes/` directory
2. Make your changes
3. Save the file
4. The changes will automatically appear across all pages that include that fragment

This system transforms website maintenance from a time-consuming, error-prone process into a streamlined, centralized operation.
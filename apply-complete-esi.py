#!/usr/bin/env python3
"""
Complete ESI Integration Script
Applies header, navbar, marquee, and footer ESI includes to all HTML files
"""
import os
import re
import glob

def apply_esi_to_file(filepath):
    """Apply all ESI includes to a single HTML file"""
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    changes_made = []

    # 1. Replace header section
    header_patterns = [
        r'(<!-- Header -->.*?</div>)(?=\s*<!-- Navigation|\s*<nav|\s*$)',
        r'(<div class="header-container">.*?</div>)(?=\s*<!-- Navigation|\s*<nav|\s*$)'
    ]

    for pattern in header_patterns:
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, '<!-- Header -->\n  <esi:include src="/includes/header.html" />', content, flags=re.DOTALL)
            changes_made.append("Header")
            break

    # 2. Replace navbar section
    navbar_patterns = [
        r'(<!-- Navigation Bar -->.*?</nav>)',
        r'(<nav class="navbar".*?</nav>)'
    ]

    for pattern in navbar_patterns:
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, '<!-- Navigation Bar -->\n  <esi:include src="/includes/navbar.html" />', content, flags=re.DOTALL)
            changes_made.append("Navbar")
            break

    # 3. Replace marquee section
    marquee_patterns = [
        r'(<!-- Marquee -->.*?</div>)(?=\s*<!-- Spacer|\s*<div id="marquee-placeholder"|\s*$)',
        r'(<div class="non-mob marquee-container">.*?</div>)(?=\s*<!-- Spacer|\s*<div id="marquee-placeholder"|\s*$)'
    ]

    for pattern in marquee_patterns:
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, '<!-- Marquee -->\n  <esi:include src="/includes/marquee.html" />', content, flags=re.DOTALL)
            changes_made.append("Marquee")
            break

    # 4. Replace footer section
    footer_patterns = [
        r'(<!-- Footer section -->.*?</footer>)',
        r'(<footer class="site-footer">.*?</footer>)'
    ]

    for pattern in footer_patterns:
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, '<!-- Footer section -->\n  <esi:include src="/includes/footer.html" />', content, flags=re.DOTALL)
            changes_made.append("Footer")
            break

    if content != original_content and changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   Updated: {filepath} - Applied: {', '.join(changes_made)}")
        return True
    else:
        print(f"   No changes: {filepath}")
        return False

def main():
    # Get all HTML files that need ESI integration
    html_files = glob.glob("*.html")
    files_to_process = []

    # Skip include files and find files without complete ESI integration
    for filepath in html_files:
        if 'includes/' in filepath:
            continue

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Check if file needs any ESI includes
            if ('esi:include' not in content or
                'header.html' not in content or
                'navbar.html' not in content or
                'marquee.html' not in content or
                'footer.html' not in content):
                files_to_process.append(filepath)

    print(f"Found {len(files_to_process)} files to process")

    updated_count = 0
    for filepath in files_to_process:
        if apply_esi_to_file(filepath):
            updated_count += 1

    print(f"\nCompleted! Updated {updated_count} files")

    # Final verification
    print("\n=== FINAL STATUS ===")
    all_files = glob.glob("*.html")
    complete_esi = 0
    incomplete_esi = 0

    for filepath in all_files:
        if 'includes/' in filepath:
            continue
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if all(include in content for include in ['header.html', 'navbar.html', 'marquee.html', 'footer.html']):
                complete_esi += 1
            else:
                incomplete_esi += 1
                print(f"   Still incomplete: {filepath}")

    print(f"Files with complete ESI: {complete_esi}")
    print(f"Files with incomplete ESI: {incomplete_esi}")

if __name__ == "__main__":
    main()
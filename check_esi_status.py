#!/usr/bin/env python3
import glob
import re

def check_esi_status():
    html_files = glob.glob("*.html")
    complete_files = []
    incomplete_files = []

    print("ESI Integration Status Report")
    print("=" * 40)

    for file in sorted(html_files):
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                esi_count = len(re.findall(r'<esi:include', content))

                if esi_count >= 4:
                    complete_files.append(file)
                else:
                    incomplete_files.append((file, esi_count))
        except Exception as e:
            print(f"Error reading {file}: {e}")
            incomplete_files.append((file, 0))

    print(f"\nCOMPLETE FILES ({len(complete_files)} files - 4+ ESI includes):")
    print("-" * 50)
    for file in complete_files:
        print(f"[OK] {file}")

    print(f"\nINCOMPLETE FILES ({len(incomplete_files)} files):")
    print("-" * 40)
    for file, count in incomplete_files:
        print(f"[NO] {file} (has {count} ESI includes)")

    print(f"\nSUMMARY:")
    print(f"Complete: {len(complete_files)} files")
    print(f"Incomplete: {len(incomplete_files)} files")
    print(f"Total: {len(html_files)} files")

if __name__ == "__main__":
    check_esi_status()
import os
import re
from pathlib import Path

def fix_markdown_table_in_html(html_content):
    # Regex to find <p> tags that look like they contain markdown tables
    # Pattern: <p> followed by something starting with | and containing |---|
    p_tag_pattern = re.compile(r'<p>(.*?\|.*\|---.*\|.*)</p>', re.DOTALL)

    def replace_table(match):
        content = match.group(1).strip()
        
        # The rows were joined by spaces in the old convert_md.py: ' '.join(para_lines)
        # In the actual HTML, they appear as " | | "
        # We split by " | | " but we must be careful not to split inside cells
        # However, looking at the sample, the rows are clearly delimited by " | | "
        rows_raw = content.split(' | | ')
        
        if len(rows_raw) < 2:
            # Try splitting by "||" just in case
            rows_raw = content.split('||')
            if len(rows_raw) < 2:
                return match.group(0)

        processed_rows = []
        for row in rows_raw:
            row = row.strip()
            if not row:
                continue
            # Remove leading and trailing |
            if row.startswith('|'):
                row = row[1:]
            if row.endswith('|'):
                row = row[:-1]
            
            cells = [cell.strip() for cell in row.split('|')]
            processed_rows.append(cells)

        if len(processed_rows) < 2:
            return match.group(0)

        # Header is the first row
        header = processed_rows[0]
        # Separator is the second row
        separator = processed_rows[1]
        if not any('-' in cell for cell in separator):
            return match.group(0)

        # Build HTML table
        res = "<table>\n<thead>\n<tr>"
        for cell in header:
            res += f"<th>{cell}</th>"
        res += "</tr>\n</thead>\n<tbody>"
        
        # Data rows start from index 2
        for row in processed_rows[2:]:
            res += "\n<tr>"
            # Ensure we have the same number of cells as header
            for i in range(len(header)):
                cell = row[i] if i < len(row) else ""
                res += f"<td>{cell}</td>"
            res += "</tr>"
        res += "\n</tbody>\n</table>"
        
        return res

    return p_tag_pattern.sub(replace_table, html_content)

def main():
    thoughts_dir = Path('thoughts')
    if not thoughts_dir.exists():
        print("thoughts directory not found")
        return

    files_fixed = 0
    for html_file in thoughts_dir.glob('*.html'):
        content = html_file.read_text(encoding='utf-8')
        new_content = fix_markdown_table_in_html(content)
        if new_content != content:
            print(f"Fixing table in {html_file}")
            html_file.write_text(new_content, encoding='utf-8')
            files_fixed += 1
    
    print(f"Fixed {files_fixed} files.")

if __name__ == '__main__':
    main()

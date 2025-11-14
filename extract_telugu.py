import html
import re
import os

# Create directory for individual chapters
os.makedirs('src/irv-telugu-psalms', exist_ok=True)

# Read the HTML file
with open('src/IRV-Telugu Psalms.htm', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Extract all verses
verses = []
current_chapter = None

# Find all chapter numbers
chapter_pattern = r'<p class=c-ChapterNumber><span lang=EN-US style=\'font-size:10\.0pt\'>(\d+)<o:p></o:p></span></p>'
chapters = re.finditer(chapter_pattern, content)

chapter_positions = {}
for ch in chapters:
    chapter_num = int(ch.group(1))
    chapter_positions[chapter_num] = ch.end()

# Process each chapter
for chapter_num in sorted(chapter_positions.keys()):
    start_pos = chapter_positions[chapter_num]
    # Find the end position (next chapter or end of content)
    next_chapters = [pos for num, pos in chapter_positions.items() if num > chapter_num]
    end_pos = min(next_chapters) if next_chapters else len(content)
    
    chapter_content = content[start_pos:end_pos]
    
    # Create individual file for this chapter
    filename = f"src/irv-telugu-psalms/Psalm-{str(chapter_num).zfill(3)}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"కీర్తన {chapter_num}\n")
        f.write('='*60 + '\n\n')
        
        # Extract verses from this chapter
        verse_pattern = r'<span class=v-VerseNumber><span lang=EN-US[^>]*>(\d+)&nbsp;</span></span><span lang=TE[^>]*>(.*?)</span>'
        
        verses_in_chapter = re.finditer(verse_pattern, chapter_content, re.DOTALL)
        
        for verse_match in verses_in_chapter:
            verse_num = verse_match.group(1)
            verse_html = verse_match.group(2)
            
            # Decode HTML entities
            verse_text = html.unescape(verse_html)
            
            # Remove any remaining HTML tags
            verse_text = re.sub(r'<[^>]+>', '', verse_text)
            
            # Clean up extra whitespace
            verse_text = ' '.join(verse_text.split())
            
            f.write(f"{verse_num}. {verse_text}\n")

print("Extraction complete! Created individual files in src/irv-telugu-psalms/")
print(f"Total chapters processed: {len(chapter_positions)}")

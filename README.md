# Study Bible Generation Project

## Project Overview
This project aims to create a comprehensive Study Bible in Indian languages. We take Telugu as our test case. The project begins with English content as a prototype before translation to Telugu, targeting approximately 2,000 pages of accessible, clear biblical content.

## Target Audience
Indian Christian Community who need:
- Complete, clear sentences that are easy to understand
- Accessible theological explanations without academic jargon
- Practical biblical insights relevant to their context

## Project Structure

### Directories
- **`Notes/`** - Study notes for biblical books and chapters
  - **`archive/`** - Superseded versions of study notes
  - English notes (e.g., `John-001.md`, `Psalm-001.md`)
  - Telugu notes (e.g., `John-001-Telugu-expanded.md`, `Psalm-001-Telugu-v2.md`)
    - Files with `-v2` or `-expanded` suffixes are current versions
    - Earlier iterations are in the archive folder
- **`src/`** - Source texts and extraction tools
  - `irv-telugu-psalms/` - Individual Telugu IRV Psalm files (Psalm-001.txt through Psalm-150.txt)
  - `irv-telugu-john/` - John chapters in plain text (e.g., John-001.txt)
  - `IRV-Telugu-Psalms-Plain.txt` - Combined Telugu IRV Psalms text
  - `IRV (Psalms).htm` - Original HTML source file
- **`extract_telugu.py`** - Python script to extract Telugu text from HTML (located in project root)
- **`system-prompt.md`** - Complete project guidelines and formatting rules
- **`Study Bible Plan.md`** - Project planning document with content markers

### Key Files
- **`system-prompt.md`** - Master reference for all writing guidelines, including:
  - Content structure requirements
  - Writing style guidelines
  - Telugu-specific rules
  - Author's intent principles
  - Book and chapter introduction formats

## Content Guidelines

### Essential Content
- Book introductions (1 page maximum)
- Chapter introductions with outlines (integrated in study notes)
- Study notes for important verses
- Glossary, maps, and charts

### Writing Principles
1. **Clarity over complexity** - Write for understanding, not academic sophistication
2. **Complete sentences** - Avoid fragmented or abbreviated phrasing
3. **Active voice** - Make subjects and actions clear
4. **Author's intent** - Emphasize each book's primary purpose while maintaining orthodox interpretation
5. **Conciseness** - Keep within 2,000-page target

### Telugu-Specific Rules
- Use actual IRV (Indian Revised Version) text from source files
- Use "రూపరేఖలు" (plural) for outlines
- Avoid "మరియు" (and) and words for "or" in explanations
- Use active voice consistently
- Abbreviate Bible book names for space efficiency

## Bible Versions
- **English**: NASB (New American Standard Bible)
- **Telugu**: IRV (Indian Revised Version)

## Current Progress

### Completed
- System prompt with comprehensive guidelines
- Python extraction tool for Telugu IRV text
- Sample study notes:
  - Psalms 1, 23 (English and Telugu)
  - John 1 (English and Telugu with expanded version)

### Work Structure
Each chapter's study notes include:
1. **అధ్యాయ పరిచయం (Chapter Introduction)** - Brief overview (100-150 words)
2. **రూపరేఖలు (Outline)** - Numbered main sections
3. **అధ్యయన గమనికలు (Study Notes)** - Verse-by-verse explanations

## Study Notes Format

**[Verse number] [Key phrase from verse]**. [Complete sentence explanation with context] ([Cross-references]).

### Example (English)
**110:3 Your people will volunteer freely**. The Messiah's subjects will willingly submit themselves and serve Him with joyful hearts, offering themselves without compulsion (Jdg 5:2; 2Co 8:3).

### Example (Telugu)
**1 దుర్మార్గుల సలహా ప్రకారం నడుచుకోనివాడు**. ధన్యుడైన వ్యక్తి దుర్మార్గుల సలహా ప్రకారం నడుచుకోడు, పాపాత్ముల దారిలో నిలవడు, అల్లరి మూకలతో కూర్చోడు (కీర్తన 26:4-5; సామెతలు 4:14-15).

## Tools

### extract_telugu.py
Python script to extract Telugu text from IRV HTML files:
- Converts HTML entities to readable Telugu Unicode
- Creates individual chapter files
- Formats text with verse numbers and clean output

**Usage:**
```bash
python extract_telugu.py
```

## Getting Started

1. Review `system-prompt.md` for complete guidelines
2. Check `Study Bible Plan.md` for content type markers
3. Use existing notes in `notes/` folder as templates
4. Reference IRV Telugu text from `src/irv-telugu-psalms/`
5. Follow the three-section structure: Chapter Intro → Outline → Study Notes

## Project Goals
- Create accessible biblical study resources for the Indian Christian Community
- Maintain theological accuracy while prioritizing clarity
- Complete approximately 2,000 pages of study content
- Emphasize each biblical book's original author's intent
- Provide practical understanding for application

## Contributing
When creating new study notes:
1. Always consult `system-prompt.md` for current guidelines
2. Use actual source text (NASB for English, IRV for Telugu)
3. Maintain consistent formatting across all notes
4. Focus on clarity and practical application
5. Keep within length guidelines to meet page count goals

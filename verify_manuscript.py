import re
from pathlib import Path

def analyze_manuscript(filepath):
    text = Path(filepath).read_text(encoding='utf-8')
    
    # Split into sections
    # Find start of section 1
    match_start = re.search(r'^## 1\. Introduction', text, re.MULTILINE)
    match_end = re.search(r'^## References', text, re.MULTILINE)
    
    if not match_start:
        print("Could not find start of Section 1")
        return
    if not match_end:
        print("Could not find start of References")
        return
        
    start_pos = match_start.start()
    end_pos = match_end.start()
    
    body_text = text[start_pos:end_pos]
    
    # Count words
    words = re.findall(r'\b[A-Za-z0-9_\'-]+\b', body_text)
    total_words = len(words)
    
    print(f"Manuscript Body Word Count (Excluding Abstract, References, Appendices): {total_words}")
    
    # Check sections
    sections = re.findall(r'^## (\d+)\. (.*)', body_text, re.MULTILINE)
    print(f"Total Main Sections Found: {len(sections)}")
    for num, title in sections:
        sec_start = re.search(rf'^## {num}\. ', body_text, re.MULTILINE).start()
        # Find next section or end
        next_num = int(num) + 1
        next_sec = re.search(rf'^## {next_num}\. ', body_text, re.MULTILINE)
        if next_sec:
            sec_end = next_sec.start()
            sec_text = body_text[sec_start:sec_end]
        else:
            sec_text = body_text[sec_start:]
        sec_words = len(re.findall(r'\b[A-Za-z0-9_\'-]+\b', sec_text))
        print(f"  Section {num}: {title} -> {sec_words} words")

if __name__ == '__main__':
    analyze_manuscript("C:/Users/ismai/.gemini/antigravity/scratch/research/the-last-of-us-part-ii/14_FULL_RESEARCH_PAPER.md")

# Week 04 — Consolidated Revision Progress Report (Alt Style)

**Script:** `make_report_pdf_priyam_week04_altstyle.py`  
**Output:** `Weekly_Progress_Report_Priyam_Week04.pdf`  
**Name:** Priyam Kumar Mishra  

## What this script generates

A multi-page (4-page) PDF progress report for **Week 04** of the Python Internship.  
It uses a deep-violet + gold + coral colour palette and includes:

| Feature | Details |
|---------|---------|
| Cover / Header | Colour-block meta-bar (name, domain, week, date) |
| Learning Journey Timeline | Full-width table spanning Weeks 01–04 |
| Week-by-week recap | Weeks 01, 02, 03 topics + projects summarised |
| Project code samples | Quiz Game · Mini Calculator · NumPy+Pandas Analyser |
| Week 04 revision tracker | Activities table with status and confidence columns |
| Highlighted callout boxes | Gold-bordered tip/quote boxes |
| Dark code boxes | Dark-purple background with warm-cream monospaced text |

## Requirements

- Python 3.8 or above
- [reportlab](https://pypi.org/project/reportlab/)

## Installation

```bash
pip install reportlab
```

## Running the script

```bash
# From the repo root:
python reports/week04/make_report_pdf_priyam_week04_altstyle.py

# Or from inside the reports/week04/ directory:
cd reports/week04
python make_report_pdf_priyam_week04_altstyle.py
```

The PDF `Weekly_Progress_Report_Priyam_Week04.pdf` will be created in the
**current working directory** from which you run the script.

## Customising

| Variable | Location in script | Purpose |
|---------|--------------------|---------|
| `FILE_NAME` | `OUTPUT & REPORT METADATA` block at top of file | Change the output PDF name |
| `REPORTER_NAME` | `OUTPUT & REPORT METADATA` block at top of file | Update the reporter's full name |
| `DOMAIN` | `OUTPUT & REPORT METADATA` block at top of file | Change the internship/programme name |
| `WEEK_NUMBER` | `OUTPUT & REPORT METADATA` block at top of file | Change the week number shown in the report |
| `DATE_OF_SUBMISSION` | `OUTPUT & REPORT METADATA` block at top of file | Update the submission date |
| `C_ACCENT1` … `C_ACCENT4` | Colour palette block | Swap the colour theme |

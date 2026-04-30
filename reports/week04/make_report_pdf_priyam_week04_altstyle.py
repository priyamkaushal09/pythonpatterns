"""
Week 04 Consolidated Revision Progress Report — Alt Style
Name   : Priyam Kumar Mishra
Output : Weekly_Progress_Report_Priyam_Week04.pdf

Run:
    pip install reportlab
    python make_report_pdf_priyam_week04_altstyle.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, HRFlowable, PageBreak, KeepTogether,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

# ──────────────────────────────────────────────
# OUTPUT & REPORT METADATA  (edit these values)
# ──────────────────────────────────────────────
FILE_NAME          = "Weekly_Progress_Report_Priyam_Week04.pdf"
REPORTER_NAME      = "Priyam Kumar Mishra"
DOMAIN             = "Python Internship"
WEEK_NUMBER        = "04"
DATE_OF_SUBMISSION = "2026-04-30"   # update to match your actual submission date

# ──────────────────────────────────────────────
# COLOUR PALETTE  (deep-violet + gold + coral)
# ──────────────────────────────────────────────
C_TITLE    = colors.HexColor("#1A1035")   # deep violet (almost black-purple)
C_ACCENT1  = colors.HexColor("#6C3FC5")   # mid-violet
C_ACCENT2  = colors.HexColor("#F0A500")   # gold / amber
C_ACCENT3  = colors.HexColor("#E84855")   # coral / red
C_ACCENT4  = colors.HexColor("#2EC4B6")   # teal-green (highlight)
C_LIGHT_BG = colors.HexColor("#F5F0FF")   # very-light lavender
C_CODE_BG  = colors.HexColor("#1E1B2E")   # dark-purple for code boxes
C_CODE_FG  = colors.HexColor("#E8D5B7")   # warm-cream for code text
C_LINE     = colors.HexColor("#D4C8F0")   # soft divider
C_BODY     = colors.HexColor("#1C1C2E")   # near-black body text
C_MUTED    = colors.HexColor("#5B5670")   # muted gray-violet

# ──────────────────────────────────────────────
# PARAGRAPH STYLES
# ──────────────────────────────────────────────
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleAlt",
    parent=styles["Title"],
    fontSize=22,
    textColor=C_TITLE,
    spaceAfter=2,
    fontName="Helvetica-Bold",
)

subtitle_style = ParagraphStyle(
    "SubtitleAlt",
    parent=styles["BodyText"],
    fontSize=11.5,
    textColor=C_ACCENT1,
    spaceAfter=8,
    fontName="Helvetica-Oblique",
)

meta_style = ParagraphStyle(
    "MetaAlt",
    parent=styles["BodyText"],
    fontSize=10,
    textColor=colors.white,
    leading=12.5,
    fontName="Helvetica",
)

section_style = ParagraphStyle(
    "SectionAlt",
    parent=styles["Heading2"],
    fontSize=13,
    textColor=C_ACCENT1,
    spaceBefore=14,
    spaceAfter=6,
    fontName="Helvetica-Bold",
    borderPad=3,
)

subsection_style = ParagraphStyle(
    "SubsectionAlt",
    parent=styles["Heading3"],
    fontSize=11.5,
    textColor=C_ACCENT2,
    spaceBefore=8,
    spaceAfter=4,
    fontName="Helvetica-Bold",
)

body = ParagraphStyle(
    "BodyAlt",
    parent=styles["BodyText"],
    fontSize=10.8,
    leading=14.5,
    textColor=C_BODY,
    fontName="Helvetica",
)

muted = ParagraphStyle(
    "MutedAlt",
    parent=styles["BodyText"],
    fontSize=10.2,
    leading=13.2,
    textColor=C_MUTED,
    fontName="Helvetica",
)

code_style = ParagraphStyle(
    "CodeAlt",
    parent=styles["BodyText"],
    fontName="Courier",
    fontSize=9.8,
    leading=12.5,
    textColor=C_CODE_FG,
)

callout_style = ParagraphStyle(
    "CalloutAlt",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=13.5,
    textColor=C_TITLE,
    fontName="Helvetica-BoldOblique",
)

tbl_header_style = ParagraphStyle(
    "TblHeader",
    parent=styles["BodyText"],
    fontSize=10.2,
    textColor=colors.white,
    fontName="Helvetica-Bold",
    leading=12,
)

tbl_cell_style = ParagraphStyle(
    "TblCell",
    parent=styles["BodyText"],
    fontSize=10,
    textColor=C_BODY,
    fontName="Helvetica",
    leading=12.5,
)

# ──────────────────────────────────────────────
# HELPER UTILITIES
# ──────────────────────────────────────────────
PAGE_W = A4[0] - 3.4 * cm   # usable width (left 1.7 + right 1.7)

def section_divider():
    return HRFlowable(width="100%", thickness=0.6, color=C_LINE, spaceAfter=4)


def code_box(code_text: str) -> Table:
    """Dark-background code snippet box."""
    cell = Paragraph(code_text.replace("\n", "<br/>").replace(" ", "&nbsp;"), code_style)
    tbl = Table([[cell]], colWidths=[PAGE_W])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), C_CODE_BG),
        ("BOX",           (0, 0), (-1, -1), 1.2, C_ACCENT2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return tbl


def callout_box(text: str) -> Table:
    """Highlighted callout / tip box."""
    cell = Paragraph(text, callout_style)
    tbl = Table([[cell]], colWidths=[PAGE_W])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), colors.HexColor("#FFF8E6")),
        ("BOX",           (0, 0), (-1, -1), 1.2, C_ACCENT2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return tbl


def bullet_list(items: list) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(x, body)) for x in items],
        bulletType="bullet",
        leftIndent=18,
        bulletFontSize=10,
        bulletColor=C_ACCENT1,
    )


def numbered_list(items: list) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(x, body)) for x in items],
        bulletType="1",
        leftIndent=18,
    )


# ──────────────────────────────────────────────
# BUILD STORY
# ──────────────────────────────────────────────
doc = SimpleDocTemplate(
    FILE_NAME,
    pagesize=A4,
    leftMargin=1.7 * cm,
    rightMargin=1.7 * cm,
    topMargin=1.6 * cm,
    bottomMargin=1.6 * cm,
)

story = []

# ════════════════════════════════════════════
# PAGE 1 — COVER / HEADER
# ════════════════════════════════════════════

# Title block
story.append(Paragraph("Weekly Progress Report", title_style))
story.append(Paragraph("Week 04 · Consolidated Revision &amp; Overall Progress", subtitle_style))

# Meta bar (4-cell colourful header)
meta_data = [
    [
        Paragraph(f"<b>Name:</b><br/>{REPORTER_NAME}", meta_style),
        Paragraph(f"<b>Domain:</b><br/>{DOMAIN}", meta_style),
        Paragraph(f"<b>Week:</b><br/>{WEEK_NUMBER}", meta_style),
        Paragraph(f"<b>Date:</b><br/>{DATE_OF_SUBMISSION}", meta_style),
    ]
]
meta_tbl = Table(meta_data, colWidths=[5.0 * cm, 4.8 * cm, 2.0 * cm, 3.4 * cm])
meta_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (0, 0), C_ACCENT1),
    ("BACKGROUND",    (1, 0), (1, 0), C_ACCENT3),
    ("BACKGROUND",    (2, 0), (2, 0), C_ACCENT2),
    ("BACKGROUND",    (3, 0), (3, 0), C_ACCENT4),
    ("TEXTCOLOR",     (0, 0), (-1, -1), colors.white),
    ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ("TOPPADDING",    (0, 0), (-1, -1), 9),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ("ROUNDEDCORNERS",(0, 0), (-1, -1), 4),
]))
story.append(meta_tbl)
story.append(Spacer(1, 14))
story.append(section_divider())

# ─── I. Executive Summary ───────────────────
story.append(Paragraph("I. Executive Summary", section_style))
story.append(Paragraph(
    "Week 04 is a <b>full-revision week</b>. Rather than introducing new content, "
    "this report consolidates everything learned across Weeks 01–03: Python basics, "
    "control flow and functions, and data-analysis tools (NumPy &amp; Pandas). "
    "Three hands-on projects were planned or completed alongside the weekly topics, "
    "demonstrating how the concepts connect in real programs.",
    body,
))
story.append(Spacer(1, 6))
story.append(callout_box(
    "Goal of Week 04: Reinforce all prior learning, identify gaps, "
    "and ensure solid foundations before advancing to intermediate topics."
))
story.append(Spacer(1, 10))
story.append(section_divider())

# ─── II. Learning Journey Timeline ──────────
story.append(Paragraph("II. Learning Journey — Weeks 01 to 04 Timeline", section_style))
story.append(Paragraph(
    "The table below summarises the progression of topics and projects across all four weeks.",
    body,
))
story.append(Spacer(1, 8))

# ── TIMELINE TABLE ──────────────────────────
tl_header = [
    Paragraph("Week", tbl_header_style),
    Paragraph("Core Topics", tbl_header_style),
    Paragraph("Key Concepts", tbl_header_style),
    Paragraph("Project / Activity", tbl_header_style),
]
tl_rows = [
    [
        Paragraph("<b>01</b>", tbl_cell_style),
        Paragraph("Python Basics", tbl_cell_style),
        Paragraph("Variables, data types, operators, input/output, conditionals, loops", tbl_cell_style),
        Paragraph("Quiz Game (planning &amp; logic design)", tbl_cell_style),
    ],
    [
        Paragraph("<b>02</b>", tbl_cell_style),
        Paragraph("Functions &amp; Control Flow", tbl_cell_style),
        Paragraph("def, return, parameters, if/elif/else, for/while, break/continue", tbl_cell_style),
        Paragraph("Mini Calculator (function-based, multi-operation)", tbl_cell_style),
    ],
    [
        Paragraph("<b>03</b>", tbl_cell_style),
        Paragraph("NumPy &amp; Pandas", tbl_cell_style),
        Paragraph("Arrays, operators, DataFrames, Series, filtering, aggregation", tbl_cell_style),
        Paragraph("Expense / Student Marks Analyser (NumPy + Pandas)", tbl_cell_style),
    ],
    [
        Paragraph("<b>04</b>", tbl_cell_style),
        Paragraph("Overall Revision", tbl_cell_style),
        Paragraph("Full recap of all weeks; re-practice problems; end-to-end integration", tbl_cell_style),
        Paragraph("Integrated mini-projects review; identified areas for improvement", tbl_cell_style),
    ],
]

timeline_table = Table(
    [tl_header] + tl_rows,
    colWidths=[1.5 * cm, 3.5 * cm, 6.5 * cm, 4.7 * cm],
    repeatRows=1,
)
timeline_table.setStyle(TableStyle([
    # Header row
    ("BACKGROUND",    (0, 0), (-1, 0), C_ACCENT1),
    ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
    # Week-number column accent
    ("BACKGROUND",    (0, 1), (0, 1), colors.HexColor("#EDE7F6")),
    ("BACKGROUND",    (0, 2), (0, 2), colors.HexColor("#E8F5E9")),
    ("BACKGROUND",    (0, 3), (0, 3), colors.HexColor("#FFF3E0")),
    ("BACKGROUND",    (0, 4), (0, 4), colors.HexColor("#FCE4EC")),
    # Alternating row backgrounds
    ("ROWBACKGROUNDS", (1, 1), (-1, -1), [colors.white, C_LIGHT_BG]),
    # Grid
    ("GRID",          (0, 0), (-1, -1), 0.5, C_LINE),
    # Alignment
    ("ALIGN",         (0, 0), (0, -1), "CENTER"),
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    # Padding
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
]))
story.append(timeline_table)
story.append(Spacer(1, 12))
story.append(section_divider())

# ════════════════════════════════════════════
# PAGE 2 — WEEK-BY-WEEK RECAP
# ════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph("III. Week-by-Week Revision Recap", section_style))

# ─── Week 01 ────────────────────────────────
story.append(Paragraph("Week 01 — Python Fundamentals", subsection_style))
story.append(Paragraph(
    "The journey began with the essentials of Python programming, covering the building blocks "
    "used in every program.",
    body,
))
story.append(bullet_list([
    "<b>Variables &amp; Data Types:</b> int, float, str, bool — storing and manipulating values.",
    "<b>Operators:</b> arithmetic (+, -, *, /, //, %, **), comparison (==, !=, &gt;, &lt;), logical (and, or, not).",
    "<b>Input / Output:</b> input() for user data, print() for display, f-strings for formatting.",
    "<b>Conditionals:</b> if / elif / else blocks to make decisions.",
    "<b>Loops:</b> for and while loops; range(); break and continue statements.",
    "<b>Collections:</b> lists, tuples, and dictionaries — basic usage and iteration.",
]))
story.append(Spacer(1, 6))
story.append(Paragraph("<b>Project: Quiz Game (planning &amp; logic design)</b>", body))
story.append(Paragraph(
    "Designed a simple multiple-choice quiz program. The plan involved storing questions and "
    "answers in a list of dictionaries, looping through them, collecting user input, and "
    "maintaining a running score — directly applying conditionals and loops from Week 01.",
    muted,
))
story.append(Spacer(1, 10))

# ─── Week 02 ────────────────────────────────
story.append(Paragraph("Week 02 — Functions &amp; Control Flow", subsection_style))
story.append(Paragraph(
    "Week 02 introduced structured programming through functions, making code reusable and organised.",
    body,
))
story.append(bullet_list([
    "<b>Defining Functions:</b> def, return, parameters, default arguments.",
    "<b>Scope:</b> local vs. global variables inside functions.",
    "<b>Advanced Control Flow:</b> nested loops, while-else, list comprehensions.",
    "<b>String Methods:</b> .upper(), .lower(), .strip(), .split(), .join() for text manipulation.",
    "<b>Error Handling basics:</b> try / except to handle simple runtime errors.",
]))
story.append(Spacer(1, 6))
story.append(Paragraph("<b>Project: Mini Calculator</b>", body))
story.append(Paragraph(
    "Built a function-based calculator supporting addition, subtraction, multiplication, "
    "division, and modulus. Each operation was wrapped in its own function; a main() function "
    "handled the menu loop and user input — putting Week 02 functions and control flow into practice.",
    muted,
))
story.append(Spacer(1, 10))

# ─── Week 03 ────────────────────────────────
story.append(Paragraph("Week 03 — NumPy &amp; Pandas (Data Analysis)", subsection_style))
story.append(Paragraph(
    "Week 03 introduced the data-analysis ecosystem, enabling fast numeric computation and "
    "structured tabular data handling.",
    body,
))
story.append(bullet_list([
    "<b>NumPy Arrays:</b> creation, indexing, slicing, shape, 1D and 2D arrays.",
    "<b>NumPy Operators:</b> element-wise arithmetic, comparison operators, boolean arrays.",
    "<b>NumPy Functions:</b> sum(), mean(), min(), max(), reshape(), where().",
    "<b>Pandas Series &amp; DataFrames:</b> created from lists and dictionaries.",
    "<b>Pandas Operators:</b> column arithmetic, computed columns, filtering with df[condition].",
    "<b>Pandas Methods:</b> head(), describe(), sort_values(), value_counts(), to_csv().",
]))
story.append(Spacer(1, 6))
story.append(Paragraph("<b>Project: NumPy + Pandas Analysis (Expense / Student Marks)</b>", body))
story.append(Paragraph(
    "Applied NumPy for aggregation (total, average) and Pandas for table presentation and "
    "filtering. Results were exported to CSV — a complete mini data-pipeline from raw data to report.",
    muted,
))
story.append(Spacer(1, 10))
story.append(section_divider())

# ════════════════════════════════════════════
# PAGE 3 — PROJECTS + CODE SAMPLES
# ════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph("IV. Project Highlights &amp; Code Samples", section_style))

# ── Project 1: Quiz Game ─────────────────────
story.append(Paragraph("Project 1 — Quiz Game (Week 01)", subsection_style))
story.append(Paragraph(
    "A command-line multiple-choice quiz that loops through questions, captures answers, "
    "and displays a final score. This project reinforces conditionals, loops, and list-of-dict patterns.",
    body,
))
story.append(Spacer(1, 6))
story.append(code_box("""\
questions = [
    {"q": "What is 5 ** 2?",          "a": "25"},
    {"q": "Which keyword defines a function?", "a": "def"},
    {"q": "What does len([1,2,3]) return?",    "a": "3"},
]

score = 0
for item in questions:
    answer = input(item["q"] + "  Your answer: ").strip()
    if answer == item["a"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {item['a']}")

print(f"\\nFinal Score: {score}/{len(questions)}")"""))
story.append(Spacer(1, 10))

# ── Project 2: Mini Calculator ───────────────
story.append(Paragraph("Project 2 — Mini Calculator (Week 02)", subsection_style))
story.append(Paragraph(
    "A function-based calculator where each arithmetic operation is its own function, "
    "making the code modular, testable, and easy to extend.",
    body,
))
story.append(Spacer(1, 6))
story.append(code_box("""\
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):   return a / b if b != 0 else "Error: Division by zero"

def main():
    ops = {"1": add, "2": subtract, "3": multiply, "4": divide}
    labels = {"1": "Add", "2": "Subtract", "3": "Multiply", "4": "Divide"}
    print("Mini Calculator")
    for k, v in labels.items():
        print(f"  {k}. {v}")
    choice = input("Choose operation: ").strip()
    if choice in ops:
        x, y = float(input("Enter num 1: ")), float(input("Enter num 2: "))
        print(f"Result: {ops[choice](x, y)}")
    else:
        print("Invalid choice.")

main()"""))
story.append(Spacer(1, 10))

# ── Project 3: NumPy + Pandas Analysis ───────
story.append(Paragraph("Project 3 — NumPy + Pandas Analysis (Week 03)", subsection_style))
story.append(Paragraph(
    "Combines NumPy for fast numeric processing with Pandas for tabular presentation "
    "and conditional filtering — a simplified data-analysis pipeline.",
    body,
))
story.append(Spacer(1, 6))
story.append(code_box("""\
import numpy as np
import pandas as pd

students = ["Priyam", "Aman", "Riya", "Neha"]
math    = np.array([88, 72, 65, 91])
science = np.array([85, 78, 70, 88])
english = np.array([82, 68, 60, 94])

# NumPy operators — element-wise totals and averages
total = math + science + english
avg   = total / 3

df = pd.DataFrame({
    "Student": students,
    "Math": math, "Science": science, "English": english,
    "Total": total,
    "Average": avg.round(2),
})

# Pandas filtering operator
top = df[df["Average"] >= 80].sort_values("Average", ascending=False)

print(df.to_string(index=False))
print("\\nTop Students (Avg >= 80):")
print(top.to_string(index=False))

df.to_csv("student_analysis.csv", index=False)
print("\\nSaved: student_analysis.csv")"""))
story.append(Spacer(1, 10))
story.append(section_divider())

# ════════════════════════════════════════════
# PAGE 4 — WEEK 04 REVISION FOCUS
# ════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph("V. Week 04 — Revision Focus &amp; Activities", section_style))
story.append(Paragraph(
    "Week 04 is dedicated to revision, consolidation, and self-assessment. "
    "Rather than learning new topics, the focus is on revisiting past concepts with "
    "deeper understanding and fixing any weak areas.",
    body,
))
story.append(Spacer(1, 8))

# Revision activities table
story.append(Paragraph("Revision Activities Tracker", subsection_style))
ra_header = [
    Paragraph("Area", tbl_header_style),
    Paragraph("Activity", tbl_header_style),
    Paragraph("Status", tbl_header_style),
    Paragraph("Confidence", tbl_header_style),
]
ra_rows = [
    [
        Paragraph("Python Basics (Wk 01)", tbl_cell_style),
        Paragraph("Re-solve loop and conditional problems", tbl_cell_style),
        Paragraph("✔ Done", tbl_cell_style),
        Paragraph("High", tbl_cell_style),
    ],
    [
        Paragraph("Functions (Wk 02)", tbl_cell_style),
        Paragraph("Rewrite Mini Calculator with error handling", tbl_cell_style),
        Paragraph("✔ Done", tbl_cell_style),
        Paragraph("High", tbl_cell_style),
    ],
    [
        Paragraph("NumPy (Wk 03)", tbl_cell_style),
        Paragraph("Practice reshape(), where(), broadcasting", tbl_cell_style),
        Paragraph("In Progress", tbl_cell_style),
        Paragraph("Medium", tbl_cell_style),
    ],
    [
        Paragraph("Pandas (Wk 03)", tbl_cell_style),
        Paragraph("Practice groupby(), merge(), pivot basics", tbl_cell_style),
        Paragraph("Planned", tbl_cell_style),
        Paragraph("Medium", tbl_cell_style),
    ],
    [
        Paragraph("Integration", tbl_cell_style),
        Paragraph("Build small end-to-end script using all three topics", tbl_cell_style),
        Paragraph("Planned", tbl_cell_style),
        Paragraph("—", tbl_cell_style),
    ],
]
ra_table = Table(
    [ra_header] + ra_rows,
    colWidths=[4.2 * cm, 6.0 * cm, 2.8 * cm, 3.2 * cm],
    repeatRows=1,
)
ra_table.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), C_ACCENT3),
    ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C_LIGHT_BG]),
    ("GRID",          (0, 0), (-1, -1), 0.5, C_LINE),
    ("ALIGN",         (2, 0), (3, -1), "CENTER"),
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
]))
story.append(ra_table)
story.append(Spacer(1, 12))

# Key takeaways
story.append(Paragraph("Key Takeaways from Revision", subsection_style))
story.append(bullet_list([
    "Python's control structures (loops, conditionals) are the backbone of all programs — mastering them early pays off.",
    "Functions make code readable, reusable, and testable; a good habit to build early.",
    "NumPy array operators are significantly faster than Python list loops for numeric data.",
    "Pandas DataFrames are the standard way to handle structured/tabular data in Python.",
    "Combining NumPy + Pandas creates a powerful lightweight data pipeline without heavy frameworks.",
]))
story.append(Spacer(1, 10))
story.append(section_divider())

# ─── VI. Challenges ─────────────────────────
story.append(Paragraph("VI. Challenges Encountered", section_style))
story.append(bullet_list([
    "Remembering all Pandas method signatures (sort_values vs sort_index, axis parameters).",
    "NumPy broadcasting rules were initially confusing when operating on 2D arrays.",
    "Needed extra practice writing clean, reusable functions with good parameter design.",
    "Managing multiple project files and keeping code organised across weeks.",
]))
story.append(Spacer(1, 8))
story.append(section_divider())

# ─── VII. Learning Resources ────────────────
story.append(Paragraph("VII. Learning Resources Used", section_style))
story.append(bullet_list([
    "Python official documentation (docs.python.org) — data types, built-ins, functions.",
    "NumPy User Guide — array creation, indexing, universal functions.",
    "Pandas documentation — DataFrame / Series creation, filtering, groupby.",
    "Practice platforms — solved beginner-to-intermediate Python exercises for revision.",
    "Peer code review — compared solutions with peers to learn alternative approaches.",
]))
story.append(Spacer(1, 8))
story.append(section_divider())

# ─── VIII. Goals for Week 05 ─────────────────
story.append(Paragraph("VIII. Goals for Week 05", section_style))
story.append(numbered_list([
    "Data cleaning with Pandas: handle missing values, duplicates, and type conversion.",
    "Advanced NumPy: reshape(), where(), broadcasting with 2D arrays.",
    "File I/O: read/write CSV and JSON files using Pandas and the standard library.",
    "Begin Object-Oriented Programming (OOP): classes, objects, __init__, methods.",
    "Mini-project: Extend the Student Marks Analyser to read from CSV and output a formatted report.",
]))
story.append(Spacer(1, 10))
story.append(section_divider())

# ─── IX. Final Comments ──────────────────────
story.append(Paragraph("IX. Overall Comments", section_style))
story.append(Paragraph(
    "The four-week programme has been an excellent foundation. Starting from basic Python syntax, "
    "progressing through functions, and arriving at industry-standard data tools (NumPy &amp; Pandas) "
    "in just three weeks is a strong pace. Week 04's revision reinforced the importance of "
    "understanding 'why' each concept exists, not just memorising syntax.",
    body,
))
story.append(Spacer(1, 6))
story.append(callout_box(
    "\"Code is written once but read many times — write it clearly.\"\n"
    "— Personal revision note, Week 04"
))
story.append(Spacer(1, 14))

# Footer line
story.append(section_divider())
story.append(Paragraph(
    f"Report prepared by <b>{REPORTER_NAME}</b> · {DOMAIN} · Week {WEEK_NUMBER}",
    muted,
))

# ──────────────────────────────────────────────
# BUILD PDF
# ──────────────────────────────────────────────
doc.build(story)
print(f"✅  PDF created: {FILE_NAME}")

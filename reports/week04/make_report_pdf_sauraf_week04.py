"""
Week 04 Progress Report Generator – Sauraf Kumar
=================================================
Week 04 was an overall REVISION / RECAP week covering all topics and
projects from Weeks 01–03 (Python Basics, Conditional Statements,
NumPy + Pandas).

HOW TO RUN
----------
Step 1 – Install the required library (one-time):
    Windows :  py -m pip install reportlab
    Linux/Mac: pip install reportlab

Step 2 – Run this script:
    Windows :  py make_report_pdf_sauraf_week04.py
    Linux/Mac: python3 make_report_pdf_sauraf_week04.py

Output:  Weekly_Progress_Report_Sauraf_Week04.pdf  (in the same folder)
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

# ─────────────────────────── output file ───────────────────────────
FILE_NAME = "Weekly_Progress_Report_Sauraf_Week04.pdf"

# ─────────────────────────── colour palette ────────────────────────
NAVY      = colors.HexColor("#0B3D91")
TEAL      = colors.HexColor("#00796B")
ORANGE    = colors.HexColor("#E65100")
PURPLE    = colors.HexColor("#6A1B9A")
AMBER     = colors.HexColor("#F57F17")
LIGHTBLUE = colors.HexColor("#E3F2FD")
LIGHTGREY = colors.HexColor("#FAFAFA")
CODEBG    = colors.HexColor("#F1F8E9")
CODEBORD  = colors.HexColor("#558B2F")
DARKTEXT  = colors.HexColor("#263238")
SUBTEXT   = colors.HexColor("#37474F")

# ─────────────────────────── styles ────────────────────────────────
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    fontSize=20,
    textColor=NAVY,
    spaceAfter=6,
    leading=24,
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["BodyText"],
    fontSize=11,
    textColor=TEAL,
    spaceAfter=4,
    leading=14,
)

badge_style = ParagraphStyle(
    "BadgeStyle",
    parent=styles["BodyText"],
    fontSize=10.5,
    textColor=colors.white,
    leading=13,
)

h_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=13,
    textColor=NAVY,
    spaceBefore=12,
    spaceAfter=6,
    leading=16,
)

subh_style = ParagraphStyle(
    "SubHeadingStyle",
    parent=styles["Heading3"],
    fontSize=11.5,
    textColor=TEAL,
    spaceBefore=8,
    spaceAfter=4,
)

body = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=11,
    leading=14.5,
)

note_style = ParagraphStyle(
    "NoteStyle",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=13,
    textColor=SUBTEXT,
)

code_style = ParagraphStyle(
    "CodeStyle",
    parent=styles["BodyText"],
    fontSize=9.8,
    leading=12.5,
    fontName="Courier",
    textColor=DARKTEXT,
)

highlight_style = ParagraphStyle(
    "HighlightStyle",
    parent=styles["BodyText"],
    fontSize=11,
    leading=14,
    textColor=ORANGE,
)

# ─────────────────────────── helpers ───────────────────────────────

def code_box(code_text, bg=CODEBG, border=CODEBORD):
    """Wrap a code string in a styled single-cell table."""
    return Table(
        [[Paragraph(code_text.replace("\n", "<br/>"), code_style)]],
        colWidths=[16.2 * cm],
        style=TableStyle([
            ("BACKGROUND",    (0, 0), (-1, -1), bg),
            ("BOX",           (0, 0), (-1, -1), 0.8, border),
            ("LEFTPADDING",   (0, 0), (-1, -1), 10),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]),
    )


def bullet_list(items):
    return ListFlowable(
        [ListItem(Paragraph(x, body)) for x in items],
        bulletType="bullet",
        leftIndent=18,
    )


def numbered_list(items):
    return ListFlowable(
        [ListItem(Paragraph(x, body)) for x in items],
        bulletType="1",
        leftIndent=18,
    )


# ─────────────────────────── document ──────────────────────────────
doc = SimpleDocTemplate(
    FILE_NAME,
    pagesize=A4,
    leftMargin=2 * cm,
    rightMargin=2 * cm,
    topMargin=1.8 * cm,
    bottomMargin=1.8 * cm,
)

name              = "Sauraf Kumar"
domain            = "Python Internship"
date_of_submission = "2026-04-30"
week              = "04"
topic             = "Revision & Recap – Weeks 01, 02 & 03"

story = []

# ══════════════════════ PAGE 1 ══════════════════════════════════════

# Title
story.append(Paragraph("Weekly Progress Report (Week 04)", title_style))
story.append(Paragraph(
    "Focus: Overall Revision &amp; Recap of Weeks 01–03",
    subtitle_style,
))

# Badge bar
badge_tbl = Table(
    [[
        Paragraph(f"<b>Topic:</b> {topic}", badge_style),
        Paragraph(f"<b>Week:</b> {week}", badge_style),
        Paragraph(f"<b>Date:</b> {date_of_submission}", badge_style),
    ]],
    colWidths=[9.8 * cm, 3.2 * cm, 3.2 * cm],
)
badge_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, 0), NAVY),
    ("BACKGROUND", (1, 0), (1, 0), TEAL),
    ("BACKGROUND", (2, 0), (2, 0), PURPLE),
    ("TEXTCOLOR",  (0, 0), (-1, -1), colors.white),
    ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(badge_tbl)
story.append(Spacer(1, 10))

# Info table
info_tbl = Table(
    [
        ["Name",   name],
        ["Domain", domain],
        ["Week",   "04  (Revision Week)"],
        ["Date",   date_of_submission],
    ],
    colWidths=[4.2 * cm, 12.0 * cm],
)
info_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHTBLUE),
    ("TEXTCOLOR",  (0, 0), (0, -1), NAVY),
    ("FONTNAME",   (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE",   (0, 0), (-1, -1), 10.8),
    ("GRID",       (0, 0), (-1, -1), 0.6, colors.HexColor("#90A4AE")),
    ("ROWBACKGROUNDS", (1, 0), (1, -1), [colors.white, LIGHTGREY]),
    ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(info_tbl)
story.append(Spacer(1, 12))

# I. Overview / What Week 04 Was About
story.append(Paragraph("I. Overview – What Week 04 Was About", h_style))
story.append(Paragraph(
    "<b>Week 04 was a complete revision and recap week.</b> Instead of learning new topics, "
    "the entire week was dedicated to revisiting, practising, and consolidating everything "
    "covered in <b>Weeks 01, 02, and 03</b>. This included Python basics, conditional "
    "statements, NumPy, and Pandas — along with a review of all three mini-projects built "
    "during the internship so far.",
    body,
))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "The revision week gave an opportunity to fix gaps, strengthen understanding, and "
    "organise all learning before moving to advanced topics in Week 05.",
    body,
))
story.append(Spacer(1, 8))

# Revision summary table (three weeks at a glance)
story.append(Paragraph("II. Revision at a Glance – Weeks 01–03", h_style))

glance_data = [
    [
        Paragraph("<b>Week</b>", ParagraphStyle("th", parent=body, textColor=colors.white)),
        Paragraph("<b>Topics Revised</b>", ParagraphStyle("th", parent=body, textColor=colors.white)),
        Paragraph("<b>Project Revisited</b>", ParagraphStyle("th", parent=body, textColor=colors.white)),
    ],
    [
        Paragraph("Week 01", body),
        Paragraph("Python Basics – variables, data types, operators, input/output, strings", body),
        Paragraph("Quiz Game (planning &amp; logic design)", body),
    ],
    [
        Paragraph("Week 02", body),
        Paragraph("Conditional Statements – if, if-else, if-elif-else; comparison &amp; logical operators", body),
        Paragraph("Mini Calculator (if-elif-else logic)", body),
    ],
    [
        Paragraph("Week 03", body),
        Paragraph("NumPy (arrays, element-wise operators) &amp; Pandas (DataFrame, filtering, operators)", body),
        Paragraph("NumPy + Pandas Student Marks Analyser", body),
    ],
]
glance_tbl = Table(glance_data, colWidths=[2.5 * cm, 7.8 * cm, 5.9 * cm])
glance_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
    ("BACKGROUND", (0, 1), (-1, 1), LIGHTBLUE),
    ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#E8F5E9")),
    ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#FFF8E1")),
    ("GRID",       (0, 0), (-1, -1), 0.6, colors.HexColor("#90A4AE")),
    ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING",   (0, 0), (-1, -1), 6),
]))
story.append(glance_tbl)
story.append(Spacer(1, 12))

# III. Detailed Revision – Week 01
story.append(Paragraph("III. Detailed Revision – Week 01: Python Basics", h_style))
story.append(Paragraph(
    "Week 01 introduced the foundation of Python programming. During revision this week, "
    "the following concepts were reviewed and re-practised:",
    body,
))
story.append(bullet_list([
    "<b>Variables and Data Types</b> – int, float, str, bool; how Python stores values.",
    "<b>Basic Operators</b> – arithmetic (+, -, *, /, //, %, **), assignment (=, +=, -=), comparison.",
    "<b>Input / Output</b> – using <font face='Courier'>input()</font> and <font face='Courier'>print()</font> with f-strings and formatting.",
    "<b>Strings</b> – indexing, slicing, common methods (upper, lower, strip, replace, split).",
    "<b>Type Conversion</b> – int(), float(), str() to convert between types safely.",
]))
story.append(Spacer(1, 8))

story.append(Paragraph("Project Revisited: Quiz Game – Planning &amp; Logic Design", subh_style))
story.append(Paragraph(
    "The <b>Quiz Game</b> was planned and outlined during Week 01 as an ongoing internship project. "
    "This week the plan was reviewed and the overall game design was revisited:",
    body,
))
story.append(numbered_list([
    "Display a question to the user and collect their answer using <font face='Courier'>input()</font>.",
    "Compare the answer with the correct answer (string/int comparison).",
    "Keep a <b>score counter</b> (int variable) and update it for each correct answer.",
    "Display the final score at the end using <font face='Courier'>print()</font> with f-string formatting.",
    "Plan to add loops (Week 03) and conditions (Week 02) in later revisions.",
]))
story.append(Spacer(1, 6))
story.append(code_box(
    'score = 0\n'
    'question = "What is the capital of India?"\n'
    'answer = input(question + " ")\n\n'
    'if answer.strip().lower() == "new delhi":\n'
    '    score += 1\n'
    '    print("Correct! Score:", score)\n'
    'else:\n'
    '    print("Wrong! The answer is New Delhi. Score:", score)',
    bg=colors.HexColor("#E3F2FD"),
    border=NAVY,
))

# PAGE BREAK before Week 02 revision
story.append(PageBreak())

# ══════════════════════ PAGE 2 ══════════════════════════════════════

# IV. Detailed Revision – Week 02
story.append(Paragraph("IV. Detailed Revision – Week 02: Conditional Statements", h_style))
story.append(Paragraph(
    "Week 02 covered Python decision-making. During the revision week, all three forms of "
    "conditional statements were re-practised with fresh examples:",
    body,
))
story.append(bullet_list([
    "<b>if</b> – single condition check (example: is the number positive?).",
    "<b>if-else</b> – two-way branching (example: even or odd?).",
    "<b>if-elif-else</b> – multiple conditions in sequence (example: grade from marks).",
    "<b>Nested conditions</b> – an if inside another if for multi-rule decisions.",
    "<b>Logical operators</b> – <font face='Courier'>and</font>, <font face='Courier'>or</font>, <font face='Courier'>not</font> to combine conditions.",
]))
story.append(Spacer(1, 8))

story.append(Paragraph("Project Revisited: Mini Calculator", subh_style))
story.append(Paragraph(
    "The <b>Mini Calculator</b> was built in Week 02 as the first complete project using "
    "conditional statements. During revision, the code was re-read, re-tested, and "
    "improved. The calculator takes two numbers and an operator from the user, then uses "
    "<b>if-elif-else</b> to select the right operation:",
    body,
))
story.append(Spacer(1, 6))
story.append(numbered_list([
    "Take first number from the user (<font face='Courier'>float(input(...))</font>).",
    "Take second number from the user.",
    "Ask the user to choose an operation: +, -, *, /.",
    "Use if-elif-else to match the operation and calculate the result.",
    "Handle division by zero with a nested <font face='Courier'>if num2 == 0</font> check.",
    "Display an error message for invalid operations.",
]))
story.append(Spacer(1, 6))
story.append(code_box(
    'num1 = float(input("Enter first number: "))\n'
    'num2 = float(input("Enter second number: "))\n'
    'op   = input("Choose operation (+, -, *, /): ")\n\n'
    'if op == "+":\n'
    '    print("Result:", num1 + num2)\n'
    'elif op == "-":\n'
    '    print("Result:", num1 - num2)\n'
    'elif op == "*":\n'
    '    print("Result:", num1 * num2)\n'
    'elif op == "/":\n'
    '    if num2 == 0:\n'
    '        print("Error: Division by zero is not allowed")\n'
    '    else:\n'
    '        print("Result:", num1 / num2)\n'
    'else:\n'
    '    print("Invalid operation")',
    bg=colors.HexColor("#FFF3E0"),
    border=ORANGE,
))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>Revision insight:</b> The calculator correctly uses <font face='Courier'>if-elif-else</font> so only "
    "one branch runs. The nested <font face='Courier'>if</font> inside the division branch prevents a "
    "<font face='Courier'>ZeroDivisionError</font> runtime crash.",
    note_style,
))

story.append(PageBreak())

# ══════════════════════ PAGE 3 ══════════════════════════════════════

# V. Detailed Revision – Week 03
story.append(Paragraph("V. Detailed Revision – Week 03: NumPy &amp; Pandas", h_style))
story.append(Paragraph(
    "Week 03 introduced powerful data-science libraries. The revision covered NumPy arrays, "
    "element-wise operators, and Pandas DataFrames with filtering conditions.",
    body,
))

story.append(Paragraph("NumPy – Key Revision Points", subh_style))
story.append(bullet_list([
    "<b>Creating arrays</b> – <font face='Courier'>np.array([...])</font>, shape, dtype.",
    "<b>Element-wise operators</b> – +, -, *, /, //, %, ** applied to entire arrays at once.",
    "<b>Comparison operators</b> – produce boolean arrays (e.g. <font face='Courier'>arr &gt; 70</font>).",
    "<b>Aggregate functions</b> – <font face='Courier'>sum()</font>, <font face='Courier'>mean()</font>, <font face='Courier'>min()</font>, <font face='Courier'>max()</font>, <font face='Courier'>std()</font>.",
    "<b>Useful utilities</b> – <font face='Courier'>np.zeros()</font>, <font face='Courier'>np.ones()</font>, <font face='Courier'>np.arange()</font>, <font face='Courier'>np.reshape()</font>.",
]))

story.append(Paragraph("Pandas – Key Revision Points", subh_style))
story.append(bullet_list([
    "<b>Series and DataFrames</b> – creating from lists and dictionaries.",
    "<b>Column operators</b> – adding/subtracting columns to create new ones (e.g. Total = Math + Science).",
    "<b>Filtering</b> – <font face='Courier'>df[df['col'] &gt; value]</font> to select rows matching a condition.",
    "<b>Key methods</b> – <font face='Courier'>head()</font>, <font face='Courier'>info()</font>, <font face='Courier'>describe()</font>, <font face='Courier'>sort_values()</font>, <font face='Courier'>to_csv()</font>.",
]))

story.append(Spacer(1, 8))
story.append(Paragraph("Project Revisited: NumPy + Pandas Student Marks Analyser", subh_style))
story.append(Paragraph(
    "The <b>Student Marks Analyser</b> project from Week 03 was revisited, re-run, and "
    "extended during revision. The project stores student marks in NumPy arrays, calculates "
    "totals and averages using NumPy operators, then presents the data in a Pandas DataFrame "
    "with conditional filtering.",
    body,
))
story.append(Spacer(1, 6))
story.append(code_box(
    'import numpy as np\n'
    'import pandas as pd\n\n'
    'students = ["Aman", "Riya", "Neha", "Sauraf"]\n\n'
    'math    = np.array([78, 92, 65, 88])\n'
    'science = np.array([74, 90, 70, 85])\n'
    'english = np.array([80, 86, 60, 82])\n\n'
    '# NumPy element-wise operators\n'
    'total = math + science + english\n'
    'avg   = total / 3          # broadcasts over the array\n\n'
    '# Pandas DataFrame\n'
    'df = pd.DataFrame({\n'
    '    "Student": students, "Math": math,\n'
    '    "Science": science,  "English": english,\n'
    '    "Total": total,      "Average": avg\n'
    '})\n\n'
    '# Pandas filtering (Pandas condition operator)\n'
    'top = df[df["Average"] >= 70]\n\n'
    'print(df.to_string(index=False))\n'
    'print("\\nTop Students (Avg >= 70):\\n", top.to_string(index=False))\n'
    'df.to_csv("student_report.csv", index=False)',
))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>Revision insight:</b> NumPy operators work <i>element-wise</i> across the whole array "
    "in one line — no loops needed. Pandas filtering uses the same idea: applying a condition "
    "to a column returns a boolean Series, which then selects the matching rows.",
    note_style,
))

story.append(PageBreak())

# ══════════════════════ PAGE 4 ══════════════════════════════════════

# VI. Challenges During Revision
story.append(Paragraph("VI. Challenges Encountered During Revision", h_style))
story.append(bullet_list([
    "<b>Week 01 recap:</b> Remembered to always convert <font face='Courier'>input()</font> to the right type "
    "before arithmetic, since <font face='Courier'>input()</font> always returns a string.",
    "<b>Week 02 recap:</b> Re-traced logic errors caused by wrong condition order in "
    "<font face='Courier'>if-elif-else</font> chains — the first matching branch wins, so order matters.",
    "<b>Week 03 recap:</b> Refreshed memory on shape mismatches in NumPy and column-length "
    "mismatches when creating Pandas DataFrames.",
    "Organising all three weeks' notes and code into a single revision folder took extra effort "
    "but made the knowledge much clearer.",
]))

# VII. What Was Reinforced
story.append(Paragraph("VII. Key Takeaways Reinforced This Week", h_style))
story.append(bullet_list([
    "Python's basic building blocks (variables, types, operators, I/O) are used inside "
    "every project — getting them right is essential.",
    "Conditional statements (<font face='Courier'>if / elif / else</font>) are the core of decision-making "
    "and appear in both the Quiz Game and the Calculator.",
    "NumPy makes numerical operations on arrays fast and concise; Pandas makes tabular data "
    "easy to manipulate and filter.",
    "All three projects (Quiz Game, Mini Calculator, Marks Analyser) use multiple weeks' "
    "concepts together, showing how topics build on each other.",
]))

# VIII. Plan for Week 05
story.append(Paragraph("VIII. Plan for Week 05", h_style))
story.append(bullet_list([
    "Begin learning Python <b>loops</b> (for loop, while loop, range) and apply them to "
    "improve the Quiz Game (loop through all questions automatically).",
    "Add a <b>menu loop</b> to the Mini Calculator so the user can calculate multiple times "
    "without restarting the script.",
    "Practise more advanced NumPy functions (<font face='Courier'>np.where()</font>, "
    "<font face='Courier'>np.linspace()</font>) and Pandas data-cleaning operations "
    "(handling NaN values, removing duplicates).",
    "Start combining all learnt concepts in a single mid-internship consolidated project.",
]))

# IX. Learning Resources
story.append(Paragraph("IX. Learning Resources Used", h_style))
story.append(bullet_list([
    "Python official documentation – revision of data types, operators, and built-in functions.",
    "ReportLab documentation – for generating this PDF report.",
    "NumPy and Pandas beginner tutorials for operator and DataFrame revision.",
    "Personal notes and exercise files from Weeks 01–03.",
]))

# X. Remarks
story.append(Paragraph("X. Remarks", h_style))
story.append(Paragraph(
    "Week 04 was highly productive even though no new topic was introduced. Spending a full "
    "week on revision helped reinforce confidence in Python basics, conditional logic, and "
    "data-science fundamentals. All three mini-projects were reviewed and the code was "
    "cleaned up. This revision week has built a strong foundation before advancing to loops "
    "and more complex programs in Week 05.",
    body,
))

# ── build PDF ──────────────────────────────────────────────────────
doc.build(story)
print(f"PDF created successfully: {FILE_NAME}")
print("\nRun instructions:")
print("  1. Install reportlab (one-time):  pip install reportlab")
print(f"  2. Run this script           :  python3 make_report_pdf_sauraf_week04.py")
print(f"  3. Output file               :  {FILE_NAME}")

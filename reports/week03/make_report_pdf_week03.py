"""
make_report_pdf_week03.py
--------------------------
Generates Weekly_Progress_Report_Week03.pdf

Usage:
    pip install reportlab
    python make_report_pdf_week03.py

The PDF is written to the same directory as this script.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem,
    Table, TableStyle, HRFlowable,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ---------------------------------------------------------------------------
# Output file
# ---------------------------------------------------------------------------
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "Weekly_Progress_Report_Week03.pdf")

# ---------------------------------------------------------------------------
# Brand colours
# ---------------------------------------------------------------------------
DEEP_BLUE   = colors.HexColor("#1A3C6E")
LIGHT_BLUE  = colors.HexColor("#2E86C1")
ACCENT_TEAL = colors.HexColor("#1ABC9C")
BG_LIGHT    = colors.HexColor("#EAF4FB")
CODE_BG     = colors.HexColor("#1E1E2E")
CODE_FG     = colors.HexColor("#CDD6F4")
BADGE_GREEN = colors.HexColor("#28B463")
BADGE_ORANGE= colors.HexColor("#E67E22")
TEXT_DARK   = colors.HexColor("#1C1C1C")
TEXT_MID    = colors.HexColor("#2C3E50")
RULE_COLOR  = colors.HexColor("#AED6F1")

# ---------------------------------------------------------------------------
# Build custom paragraph styles
# ---------------------------------------------------------------------------
base_styles = getSampleStyleSheet()

def _ps(name, **kw):
    """Create a ParagraphStyle inheriting from BodyText."""
    return ParagraphStyle(name, parent=base_styles["BodyText"], **kw)

style_report_title = _ps(
    "ReportTitle",
    fontSize=24, textColor=colors.white, alignment=TA_CENTER,
    fontName="Helvetica-Bold", spaceAfter=2, leading=30,
)
style_subtitle = _ps(
    "SubTitle",
    fontSize=11, textColor=colors.HexColor("#D6EAF8"),
    alignment=TA_CENTER, fontName="Helvetica", spaceAfter=0, leading=15,
)
style_meta = _ps(
    "MetaText",
    fontSize=10.5, textColor=TEXT_MID, fontName="Helvetica",
    spaceAfter=3, leading=14,
)
style_section = _ps(
    "SectionHead",
    fontSize=13, textColor=colors.white, fontName="Helvetica-Bold",
    spaceAfter=4, spaceBefore=14, leading=18,
    backColor=LIGHT_BLUE, leftIndent=-4, rightIndent=-4,
    borderPad=5,
)
style_sub_head = _ps(
    "SubHead",
    fontSize=11.5, textColor=DEEP_BLUE, fontName="Helvetica-Bold",
    spaceAfter=3, spaceBefore=8, leading=15,
)
style_body = _ps(
    "Body",
    fontSize=10.5, textColor=TEXT_DARK, fontName="Helvetica",
    spaceAfter=3, leading=15,
)
style_code = _ps(
    "Code",
    fontSize=9, textColor=CODE_FG, fontName="Courier",
    backColor=CODE_BG, spaceAfter=2, leading=13,
    leftIndent=8, rightIndent=8, borderPad=6,
)
style_badge_green = _ps(
    "BadgeGreen",
    fontSize=9.5, textColor=colors.white, fontName="Helvetica-Bold",
    alignment=TA_CENTER, backColor=BADGE_GREEN,
    borderPad=4,
)
style_badge_orange = _ps(
    "BadgeOrange",
    fontSize=9.5, textColor=colors.white, fontName="Helvetica-Bold",
    alignment=TA_CENTER, backColor=BADGE_ORANGE,
    borderPad=4,
)


def bullet_list(items, style=style_body, indent=18):
    """Return a ListFlowable of bullet items."""
    return ListFlowable(
        [ListItem(Paragraph(item, style), bulletColor=ACCENT_TEAL, leftIndent=indent)
         for item in items],
        bulletType="bullet",
        leftIndent=indent,
        spaceBefore=2,
        spaceAfter=4,
    )


def section_heading(text):
    """Coloured section-heading paragraph with padding."""
    return Paragraph(f"&nbsp;&nbsp;{text}", style_section)


def rule():
    return HRFlowable(width="100%", thickness=1, color=RULE_COLOR, spaceAfter=6)


def badge_row(labels_styles):
    """
    Render a row of coloured badge pills in a single-row Table.
    labels_styles: list of (text, style) tuples.
    """
    cells = [Paragraph(lbl, sty) for lbl, sty in labels_styles]
    col_w = 14 * cm / len(cells)
    t = Table([cells], colWidths=[col_w] * len(cells))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("ROUNDEDCORNERS", [4]),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    return t


# ---------------------------------------------------------------------------
# Code snippet for the Student Marks Analyzer project
# ---------------------------------------------------------------------------
CODE_SNIPPET_LINES = [
    "import numpy as np",
    "import pandas as pd",
    "",
    "# ── NumPy: create marks array (5 students × 3 subjects) ──────────────",
    "marks = np.array([",
    "    [85, 90, 78],   # Alice",
    "    [72, 68, 80],   # Bob",
    "    [91, 95, 88],   # Carol",
    "    [60, 55, 62],   # Dave",
    "    [78, 82, 76],   # Eve",
    "])",
    "",
    "# ── NumPy operators ───────────────────────────────────────────────────",
    "totals  = marks.sum(axis=1)          # row-wise sum  (+)",
    "avg     = marks.mean(axis=1)         # row-wise mean",
    "maximum = marks.max(axis=1)          # row-wise max",
    "minimum = marks.min(axis=1)          # row-wise min",
    "percent = (totals / (3 * 100)) * 100 # percentage  (*  /)",
    "",
    "# ── Pandas: build DataFrame ───────────────────────────────────────────",
    "names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']",
    "df = pd.DataFrame(marks, columns=['Maths', 'Science', 'English'],",
    "                  index=names)",
    "",
    "# ── Pandas operators: add derived columns ─────────────────────────────",
    "df['Total']      = totals            # assignment operator",
    "df['Average']    = avg.round(2)",
    "df['Percentage'] = percent.round(2)",
    "df['Grade'] = df['Average'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')",
    "",
    "# ── Filter: students who passed ───────────────────────────────────────",
    "passed = df[df['Average'] >= 70]",
    "",
    "print(df.to_string())",
    "print('\\nPassed students:\\n', passed[['Total','Average','Grade']])",
    "",
    "# ── Export to CSV ─────────────────────────────────────────────────────",
    "df.to_csv('student_marks.csv')",
    "print('Exported to student_marks.csv')",
]


def code_block():
    """Return a list of Paragraph flowables that look like a highlighted code block."""
    items = []
    # Top label bar
    label_style = _ps(
        "CodeLabel",
        fontSize=8.5, textColor=colors.white, fontName="Helvetica-Bold",
        backColor=colors.HexColor("#11111B"), leading=12,
        leftIndent=6,
    )
    items.append(Paragraph("● student_marks_analyzer.py", label_style))
    for line in CODE_SNIPPET_LINES:
        safe = (line
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                or "&nbsp;")
        items.append(Paragraph(safe, style_code))
    return items


# ---------------------------------------------------------------------------
# Build the PDF story
# ---------------------------------------------------------------------------
def build_story():
    story = []
    page_w = A4[0] - 4 * cm   # usable width

    # ── Header banner ──────────────────────────────────────────────────────
    header_data = [[
        Paragraph("Weekly Progress Report", style_report_title),
    ]]
    header_table = Table(header_data, colWidths=[page_w])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), DEEP_BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(header_table)

    # Sub-header strip
    sub_data = [[Paragraph("Python Internship  |  Week 03  |  NumPy &amp; Pandas", style_subtitle)]]
    sub_table = Table(sub_data, colWidths=[page_w])
    sub_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LIGHT_BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(sub_table)
    story.append(Spacer(1, 10))

    # ── Meta-info row ──────────────────────────────────────────────────────
    meta = [
        ["<b>Name:</b> Priyam Kumar Mishra",   "<b>Domain:</b> Python Internship"],
        ["<b>Date of Submission:</b> 2026-04-21", "<b>Week Ending:</b> 03"],
    ]
    half = page_w / 2
    meta_table = Table(
        [[Paragraph(c, style_meta) for c in row] for row in meta],
        colWidths=[half, half],
    )
    meta_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BG_LIGHT),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("GRID",          (0, 0), (-1, -1), 0.4, RULE_COLOR),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    # ── I. Overview ────────────────────────────────────────────────────────
    story.append(section_heading("I.  Overview"))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "This week, the focus shifted to two of the most widely-used Python libraries for "
        "data analysis: <b>NumPy</b> and <b>Pandas</b>.  I explored NumPy arrays and "
        "mathematical operators, then moved on to Pandas Series, DataFrames, and data "
        "manipulation operators.  The week concluded with a hands-on mini-project — the "
        "<b>Student Marks Analyzer</b> — which tied both libraries together in a "
        "realistic, end-to-end scenario.",
        style_body,
    ))

    # ── II. Achievements ───────────────────────────────────────────────────
    story.append(Spacer(1, 6))
    story.append(section_heading("II.  Achievements"))
    story.append(Spacer(1, 4))

    # Badges
    story.append(badge_row([
        ("  NumPy  ", style_badge_green),
        ("  Pandas  ", style_badge_orange),
    ]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. NumPy — Arrays &amp; Operators", style_sub_head))
    story.append(bullet_list([
        "Created 1-D and 2-D NumPy arrays using <b>np.array()</b>, <b>np.zeros()</b>, "
        "and <b>np.arange()</b>.",
        "Practised element-wise arithmetic operators: <b>+</b>, <b>-</b>, <b>*</b>, <b>/</b>, "
        "<b>**</b> (power).",
        "Used aggregation functions: <b>sum()</b>, <b>mean()</b>, <b>min()</b>, <b>max()</b>, "
        "<b>std()</b> — both whole-array and along axes.",
        "Explored array slicing, indexing, and Boolean masking to filter elements.",
        "Applied <b>np.reshape()</b>, <b>np.transpose()</b>, and <b>np.concatenate()</b> "
        "for array manipulation.",
    ]))

    story.append(Paragraph("2. Pandas — DataFrame / Series &amp; Operators", style_sub_head))
    story.append(bullet_list([
        "Created <b>Series</b> (1-D labelled array) and <b>DataFrame</b> (2-D table) "
        "objects from lists, dicts, and NumPy arrays.",
        "Used Pandas operators: <b>+</b>, <b>-</b>, <b>*</b>, <b>/</b>, <b>//</b> "
        "(floor-div), <b>%</b> (modulo) on columns.",
        "Explored <b>df.loc[]</b> / <b>df.iloc[]</b> for label-based and integer-based "
        "row/column selection.",
        "Applied <b>df.apply()</b> and <b>lambda</b> functions to derive new columns.",
        "Used <b>df.sort_values()</b>, <b>df.groupby()</b>, and <b>df.describe()</b> "
        "for analysis.",
        "Exported DataFrames to CSV with <b>df.to_csv()</b>.",
    ]))

    # ── III. Project ───────────────────────────────────────────────────────
    story.append(Spacer(1, 6))
    story.append(section_heading("III.  Project — Student Marks Analyzer"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Description", style_sub_head))
    story.append(Paragraph(
        "A lightweight command-line tool that reads a class's subject marks, computes "
        "per-student statistics using <b>NumPy</b>, organises the results in a "
        "<b>Pandas DataFrame</b>, identifies passing/failing students, and exports the "
        "final report to a CSV file.",
        style_body,
    ))

    story.append(Paragraph("Steps", style_sub_head))
    story.append(bullet_list([
        "<b>Step 1 — Input data:</b> Define a 2-D NumPy array (students × subjects).",
        "<b>Step 2 — NumPy operators:</b> Compute total, average, max, min, and "
        "percentage per student using axis-wise operations.",
        "<b>Step 3 — Build DataFrame:</b> Convert the array to a Pandas DataFrame with "
        "proper student names and subject columns.",
        "<b>Step 4 — Pandas operators:</b> Assign derived columns (Total, Average, "
        "Percentage, Grade) using arithmetic and comparison operators.",
        "<b>Step 5 — Filter:</b> Use Boolean indexing to select students with average ≥ 70.",
        "<b>Step 6 — Export:</b> Save the full DataFrame to <i>student_marks.csv</i>.",
    ]))

    story.append(Paragraph("Sample Code", style_sub_head))
    story.extend(code_block())

    # ── IV. Challenges ─────────────────────────────────────────────────────
    story.append(Spacer(1, 8))
    story.append(section_heading("IV.  Challenges"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. NumPy Broadcasting", style_sub_head))
    story.append(bullet_list([
        "Understanding how NumPy automatically broadcasts arrays of different shapes "
        "took additional practice with simple examples.",
        "Resolved by reading the official NumPy broadcasting guide and running "
        "small experiments in a Jupyter notebook.",
    ]))

    story.append(Paragraph("2. Pandas Index Alignment", style_sub_head))
    story.append(bullet_list([
        "When combining two Series with different indices, unexpected NaN values "
        "appeared — this revealed the importance of aligned indexing.",
        "Used <b>df.reset_index()</b> and <b>df.fillna()</b> to handle mismatches "
        "cleanly.",
    ]))

    # ── V. Learning Resources ──────────────────────────────────────────────
    story.append(Spacer(1, 6))
    story.append(section_heading("V.  Learning Resources"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. NumPy Resources", style_sub_head))
    story.append(bullet_list([
        "Official NumPy documentation (numpy.org/doc) — array creation, indexing, "
        "mathematical functions.",
        "W3Schools NumPy tutorial for quick syntax reference.",
        "YouTube: 'NumPy in 1 Hour' for visual walkthroughs of array operations.",
    ]))

    story.append(Paragraph("2. Pandas Resources", style_sub_head))
    story.append(bullet_list([
        "Official Pandas 'Getting Started' tutorials (pandas.pydata.org).",
        "Kaggle Pandas micro-course — hands-on exercises with real datasets.",
        "Real Python article: 'The Pandas DataFrame: Make Working With Data Delightful'.",
    ]))

    # ── VI. Next Week's Goals ──────────────────────────────────────────────
    story.append(Spacer(1, 6))
    story.append(section_heading("VI.  Next Week's Goals"))
    story.append(Spacer(1, 4))

    story.append(Paragraph("1. Data Visualisation with Matplotlib &amp; Seaborn", style_sub_head))
    story.append(bullet_list([
        "Learn to create line plots, bar charts, histograms, and scatter plots "
        "using <b>Matplotlib</b>.",
        "Use <b>Seaborn</b> for statistical visualisations (heatmaps, pair plots).",
        "Visualise the Student Marks Analyzer results as a bar chart per student.",
    ]))

    story.append(Paragraph("2. Advanced Pandas Techniques", style_sub_head))
    story.append(bullet_list([
        "Explore <b>merge()</b>, <b>join()</b>, and <b>concat()</b> for combining "
        "multiple DataFrames.",
        "Practice <b>pivot_table()</b> and <b>groupby()</b> aggregation on a larger dataset.",
        "Handle missing data using <b>dropna()</b>, <b>fillna()</b>, and interpolation.",
    ]))

    # ── VII. Additional Comments ───────────────────────────────────────────
    story.append(Spacer(1, 6))
    story.append(section_heading("VII.  Additional Comments"))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Week 03 was a significant step forward — moving from pure Python to the "
        "powerful scientific-computing ecosystem.  NumPy and Pandas are cornerstones "
        "of data science in Python, and having a solid grasp of their operators and "
        "data structures will directly support upcoming topics like data visualisation "
        "and machine-learning preprocessing.  The Student Marks Analyzer project was "
        "especially valuable because it showed how NumPy efficiency and Pandas "
        "expressiveness complement each other in a real workflow.",
        style_body,
    ))

    # ── Footer rule ────────────────────────────────────────────────────────
    story.append(Spacer(1, 16))
    story.append(rule())
    story.append(Paragraph(
        "Python Internship — Weekly Progress Report &nbsp;|&nbsp; Week 03 &nbsp;|&nbsp; "
        "Priyam Kumar Mishra",
        _ps("Footer", fontSize=8.5, textColor=colors.grey, alignment=TA_CENTER),
    ))

    return story


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Weekly Progress Report – Week 03",
        author="Priyam Kumar Mishra",
        subject="Python Internship – NumPy & Pandas",
    )
    doc.build(build_story())
    print(f"✅  PDF created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

"""
Week 03 – Python Internship Weekly Progress Report PDF Generator
Topics  : NumPy, NumPy Operators, Pandas, Pandas Operators, Small Project
Name    : Priyam
Run     : py -m pip install reportlab
          py make_report_pdf_week03.py
Output  : Weekly_Progress_Report_Week03.pdf  (same folder)
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    ListFlowable, ListItem, Table, TableStyle, HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

# ── Output file ──────────────────────────────────────────────────────────────
FILE_NAME = "Weekly_Progress_Report_Week03.pdf"

# ── Color palette (teal / indigo / amber – distinct from Week 01–02 grey) ───
C_TITLE_BG   = colors.HexColor("#1B4F72")   # deep navy
C_TITLE_FG   = colors.white
C_BADGE_BG   = colors.HexColor("#1A7A8A")   # teal
C_BADGE_FG   = colors.white
C_ROW_LABEL  = colors.HexColor("#D6EAF8")   # light sky for label column
C_ROW_ALT    = colors.HexColor("#EBF5FB")   # very light blue alternating rows
C_HEADING    = colors.HexColor("#1B4F72")   # navy for section headings
C_SUBHEAD    = colors.HexColor("#1A7A8A")   # teal for sub-headings
C_HR         = colors.HexColor("#1A7A8A")
C_GRID       = colors.HexColor("#AED6F1")

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

title_style = ParagraphStyle(
    "W3Title",
    parent=base["Title"],
    fontSize=20,
    textColor=C_TITLE_FG,
    backColor=C_TITLE_BG,
    spaceAfter=0,
    spaceBefore=0,
    leading=28,
    leftIndent=12,
    rightIndent=12,
    borderPad=8,
)

badge_style = ParagraphStyle(
    "W3Badge",
    parent=base["Normal"],
    fontSize=10,
    textColor=C_BADGE_FG,
    backColor=C_BADGE_BG,
    spaceAfter=0,
    spaceBefore=0,
    leading=16,
    leftIndent=12,
    rightIndent=12,
    borderPad=5,
)

h_style = ParagraphStyle(
    "W3H",
    parent=base["Heading2"],
    fontSize=13,
    textColor=C_HEADING,
    spaceBefore=14,
    spaceAfter=5,
    leading=18,
)

subh_style = ParagraphStyle(
    "W3SubH",
    parent=base["Heading3"],
    fontSize=11.5,
    textColor=C_SUBHEAD,
    spaceBefore=8,
    spaceAfter=4,
    leading=16,
)

body = ParagraphStyle(
    "W3Body",
    parent=base["BodyText"],
    fontSize=10.5,
    leading=15,
    textColor=colors.HexColor("#1C1C1C"),
)

code_style = ParagraphStyle(
    "W3Code",
    parent=base["Code"],
    fontSize=9.5,
    leading=13,
    backColor=colors.HexColor("#EBF5FB"),
    leftIndent=10,
    rightIndent=10,
    borderPad=4,
)

# ── Document ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    FILE_NAME,
    pagesize=A4,
    leftMargin=2 * cm,
    rightMargin=2 * cm,
    topMargin=1.5 * cm,
    bottomMargin=2 * cm,
)

story = []

# ── Title block ──────────────────────────────────────────────────────────────
story.append(Paragraph("Weekly Progress Report", title_style))
story.append(Spacer(1, 2))
story.append(Paragraph("Python Internship  ·  Week 03", badge_style))
story.append(Spacer(1, 10))

# ── Info table ───────────────────────────────────────────────────────────────
info = [
    ["Name",              "Priyam"],
    ["Domain",            "Python Internship"],
    ["Date of Submission","2026-04-26"],
    ["Week Number",       "03"],
    ["Main Topics",       "NumPy · NumPy Operators · Pandas · Pandas Operators"],
]
info_tbl = Table(info, colWidths=[4.8 * cm, 11.4 * cm])
info_tbl.setStyle(TableStyle([
    # label column background
    ("BACKGROUND",   (0, 0), (0, -1), C_ROW_LABEL),
    # alternating value rows
    ("ROWBACKGROUNDS", (1, 0), (1, -1), [colors.white, C_ROW_ALT]),
    ("FONTNAME",     (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTNAME",     (1, 0), (1, -1), "Helvetica"),
    ("FONTSIZE",     (0, 0), (-1, -1), 10.5),
    ("GRID",         (0, 0), (-1, -1), 0.5, C_GRID),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",   (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 6),
    ("LEFTPADDING",  (0, 0), (-1, -1), 8),
]))
story.append(info_tbl)
story.append(Spacer(1, 14))
story.append(HRFlowable(width="100%", thickness=1.5, color=C_HR))
story.append(Spacer(1, 8))

# ════════════════════════════════════════════════════════════════════════════
# 1. WEEKLY SUMMARY
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("1) Weekly Summary", h_style))
story.append(Paragraph(
    "In Week 03, I explored two of the most important Python libraries used in data science and "
    "scientific computing: <b>NumPy</b> and <b>Pandas</b>. I learned how to create arrays, "
    "perform mathematical operations, work with tabular data, and filter/manipulate data using "
    "built-in operators. As a small project I built a <b>simple data calculator</b> that uses "
    "NumPy and Pandas to compute statistics on a set of numbers.",
    body,
))

# ════════════════════════════════════════════════════════════════════════════
# 2. KEY LEARNING
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("2) Key Learning / Tasks Completed", h_style))

# ── A. NumPy ─────────────────────────────────────────────────────────────────
story.append(Paragraph("A. NumPy – Introduction", subh_style))
story.append(Paragraph(
    "NumPy (Numerical Python) is a library that gives Python fast, memory-efficient "
    "multi-dimensional arrays called <b>ndarray</b>. It is the foundation of almost every "
    "data-science and machine-learning library in Python.",
    body,
))
story.append(Spacer(1, 4))
items_numpy = [
    "Installed NumPy: <b>py -m pip install numpy</b>",
    "Created 1-D and 2-D arrays using <b>np.array()</b>.",
    "Checked array properties: <b>shape</b>, <b>dtype</b>, <b>ndim</b>, <b>size</b>.",
    "Created special arrays: <b>np.zeros()</b>, <b>np.ones()</b>, <b>np.arange()</b>, <b>np.linspace()</b>.",
    "Used <b>np.reshape()</b> to change array shape without changing data.",
    "Accessed elements with indexing and slicing (same idea as Python lists, but multi-dimensional).",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=6) for x in items_numpy],
    bulletType="bullet", leftIndent=20,
))

# ── B. NumPy Operators ───────────────────────────────────────────────────────
story.append(Paragraph("B. NumPy Operators", subh_style))
story.append(Paragraph(
    "NumPy operators work <i>element-wise</i> on arrays, which is much faster than "
    "writing a Python loop.",
    body,
))
story.append(Spacer(1, 4))

numpy_ops = [
    ["Operator / Function", "What it does", "Example"],
    ["+  /  -  /  *  /  /", "Element-wise arithmetic", "a + b  →  each element added"],
    ["**",                   "Element-wise power",     "a ** 2  →  square every element"],
    ["np.sqrt()",            "Square root",            "np.sqrt(arr)"],
    ["np.sum()",             "Sum of all elements",    "np.sum(arr)"],
    ["np.mean()",            "Average",                "np.mean(arr)"],
    ["np.max() / np.min()", "Max / Min value",         "np.max(arr)"],
    ["np.dot()",             "Matrix dot product",     "np.dot(A, B)"],
    ["Boolean mask",         "Filter elements",        "arr[arr > 5]"],
]
ops_tbl = Table(numpy_ops, colWidths=[4.5 * cm, 5.5 * cm, 6.2 * cm])
ops_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), C_BADGE_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), colors.white),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE",     (0, 0), (-1, -1), 9.5),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C_ROW_ALT]),
    ("GRID",         (0, 0), (-1, -1), 0.4, C_GRID),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",   (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ("LEFTPADDING",  (0, 0), (-1, -1), 6),
]))
story.append(ops_tbl)
story.append(Spacer(1, 6))

# ── C. Pandas ────────────────────────────────────────────────────────────────
story.append(Paragraph("C. Pandas – Introduction", subh_style))
story.append(Paragraph(
    "Pandas is built on top of NumPy and provides two powerful data structures: "
    "<b>Series</b> (1-D labeled array) and <b>DataFrame</b> (2-D table, like a spreadsheet). "
    "It makes reading, cleaning, and analyzing data very straightforward.",
    body,
))
story.append(Spacer(1, 4))
items_pandas = [
    "Installed Pandas: <b>py -m pip install pandas</b>",
    "Created a <b>Series</b> from a list or dictionary.",
    "Created a <b>DataFrame</b> from a dictionary of lists (columns as keys).",
    "Read CSV files with <b>pd.read_csv()</b> and explored data with <b>df.head()</b>, "
    "<b>df.info()</b>, <b>df.describe()</b>.",
    "Selected columns with <b>df['column']</b> and multiple columns with "
    "<b>df[['col1','col2']]</b>.",
    "Filtered rows using conditions: <b>df[df['Age'] > 20]</b>.",
    "Added new columns and performed column-wise operations.",
    "Handled missing values with <b>df.dropna()</b> and <b>df.fillna()</b>.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=6) for x in items_pandas],
    bulletType="bullet", leftIndent=20,
))

# ── D. Pandas Operators ───────────────────────────────────────────────────────
story.append(Paragraph("D. Pandas Operators", subh_style))
pandas_ops = [
    ["Operation",            "Syntax / Method",              "Purpose"],
    ["Select column",        "df['col']",                    "Get one column as Series"],
    ["Select multiple cols", "df[['c1','c2']]",              "Get subset of columns"],
    ["Filter rows",          "df[df['col'] > value]",        "Keep rows matching condition"],
    ["Arithmetic ops",       "df['col'] + / - / * / /",      "Element-wise math on column"],
    ["Aggregate",            "df['col'].sum() / mean() …",   "Summary statistics"],
    ["Sort",                 "df.sort_values('col')",         "Sort by column"],
    ["Group by",             "df.groupby('col').mean()",      "Group and aggregate"],
    ["Apply function",       "df['col'].apply(func)",         "Custom transform per element"],
    ["Merge DataFrames",     "pd.merge(df1, df2, on='key')", "SQL-style join"],
]
pd_tbl = Table(pandas_ops, colWidths=[4.5 * cm, 5.8 * cm, 5.9 * cm])
pd_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, 0), C_TITLE_BG),
    ("TEXTCOLOR",    (0, 0), (-1, 0), colors.white),
    ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE",     (0, 0), (-1, -1), 9.5),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, C_ROW_ALT]),
    ("GRID",         (0, 0), (-1, -1), 0.4, C_GRID),
    ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",   (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
    ("LEFTPADDING",  (0, 0), (-1, -1), 6),
]))
story.append(pd_tbl)

# ════════════════════════════════════════════════════════════════════════════
# 3. SMALL PROJECT
# ════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=C_HR))
story.append(Paragraph("3) Small Project – NumPy &amp; Pandas Data Calculator", h_style))

story.append(Paragraph(
    "<b>Project Goal:</b> Build a simple console program that takes a list of numbers from "
    "the user and uses <b>NumPy</b> to calculate statistics (sum, mean, max, min, std dev) "
    "and <b>Pandas</b> to display the numbers in a neat table.",
    body,
))
story.append(Spacer(1, 6))

story.append(Paragraph("How it works (step by step):", subh_style))
steps = [
    "Ask the user to enter numbers separated by spaces.",
    "Convert the input into a NumPy array.",
    "Use NumPy to compute: sum, mean, maximum, minimum, and standard deviation.",
    "Create a Pandas DataFrame showing each number and its square.",
    "Print the statistics and the table to the console.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(f"<b>Step {i+1}:</b> {s}", body), leftIndent=6)
     for i, s in enumerate(steps)],
    bulletType="bullet", leftIndent=20,
))
story.append(Spacer(1, 8))

story.append(Paragraph("Project Code:", subh_style))

# Display code as monospaced table rows (avoids XML-escaping headaches)
code_lines = [
    "# data_calculator.py",
    "# Run: py -m pip install numpy pandas   then   py data_calculator.py",
    "",
    "import numpy as np",
    "import pandas as pd",
    "",
    "def main():",
    "    raw = input('Enter numbers separated by spaces: ')",
    "    numbers = np.array([float(x) for x in raw.split()])",
    "",
    "    print('\\n--- Statistics (NumPy) ---')",
    "    print(f'Count   : {len(numbers)}')",
    "    print(f'Sum     : {np.sum(numbers):.2f}')",
    "    print(f'Mean    : {np.mean(numbers):.2f}')",
    "    print(f'Max     : {np.max(numbers):.2f}')",
    "    print(f'Min     : {np.min(numbers):.2f}')",
    "    print(f'Std Dev : {np.std(numbers):.2f}')",
    "",
    "    df = pd.DataFrame({",
    "        'Number' : numbers,",
    "        'Square' : numbers ** 2,",
    "    })",
    "    print('\\n--- Data Table (Pandas) ---')",
    "    print(df.to_string(index=False))",
    "",
    "if __name__ == '__main__':",
    "    main()",
]

code_rows = [[line if line else " "] for line in code_lines]
code_tbl = Table(code_rows, colWidths=[16.4 * cm])
code_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, -1), colors.HexColor("#EBF5FB")),
    ("FONTNAME",     (0, 0), (-1, -1), "Courier"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
    ("LEADING",      (0, 0), (-1, -1), 13),
    ("LEFTPADDING",  (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING",   (0, 0), (-1, -1), 2),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 2),
    ("BOX",          (0, 0), (-1, -1), 0.8, C_GRID),
]))
story.append(code_tbl)
story.append(Spacer(1, 6))

story.append(Paragraph("Sample output (if user enters: 4 7 2 9 5 1):", subh_style))
sample_lines = [
    "--- Statistics (NumPy) ---",
    "Count   : 6",
    "Sum     : 28.00",
    "Mean    : 4.67",
    "Max     : 9.00",
    "Min     : 1.00",
    "Std Dev : 2.62",
    "",
    "--- Data Table (Pandas) ---",
    " Number  Square",
    "    4.0    16.0",
    "    7.0    49.0",
    "    2.0     4.0",
    "    9.0    81.0",
    "    5.0    25.0",
    "    1.0     1.0",
]
sample_rows = [[line if line else " "] for line in sample_lines]
sample_tbl = Table(sample_rows, colWidths=[16.4 * cm])
sample_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
    ("FONTNAME",     (0, 0), (-1, -1), "Courier"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
    ("LEADING",      (0, 0), (-1, -1), 13),
    ("LEFTPADDING",  (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING",   (0, 0), (-1, -1), 2),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 2),
    ("BOX",          (0, 0), (-1, -1), 0.8, C_GRID),
]))
story.append(sample_tbl)

# ════════════════════════════════════════════════════════════════════════════
# 4. CHALLENGES
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("4) Challenges Faced", h_style))
challenges = [
    "Understanding the difference between a NumPy array and a Python list (broadcasting rules).",
    "Getting used to Pandas DataFrame indexing — especially the difference between "
    "<b>.loc[]</b> (label-based) and <b>.iloc[]</b> (position-based).",
    "Handling shape mismatches when performing operations on arrays of different sizes.",
    "Learning when to use <b>groupby</b> effectively for aggregation tasks.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=6) for x in challenges],
    bulletType="bullet", leftIndent=20,
))

# ════════════════════════════════════════════════════════════════════════════
# 5. LEARNING RESOURCES
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("5) Learning Resources Used", h_style))
resources = [
    "Official NumPy documentation (numpy.org) for array operations and functions.",
    "Official Pandas documentation (pandas.pydata.org) for DataFrame methods.",
    "W3Schools Python NumPy and Pandas tutorials for quick examples.",
    "Practice exercises: creating arrays, filtering data, and summarising datasets.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=6) for x in resources],
    bulletType="bullet", leftIndent=20,
))

# ════════════════════════════════════════════════════════════════════════════
# 6. NEXT WEEK PLAN
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("6) Plan for Next Week", h_style))
next_week = [
    "Explore data visualisation with <b>Matplotlib</b> and <b>Seaborn</b> to plot graphs.",
    "Practice reading real-world CSV datasets with Pandas and cleaning messy data.",
    "Integrate NumPy/Pandas knowledge into the Quiz Game project (e.g., tracking scores "
    "across multiple rounds and computing statistics).",
    "Start exploring file handling (reading/writing CSV and JSON).",
]
story.append(ListFlowable(
    [ListItem(Paragraph(x, body), leftIndent=6) for x in next_week],
    bulletType="bullet", leftIndent=20,
))

# ════════════════════════════════════════════════════════════════════════════
# 7. REMARKS
# ════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("7) Remarks", h_style))
story.append(Paragraph(
    "Week 03 was a significant step forward. Learning NumPy and Pandas opened up a whole new "
    "dimension of Python — data handling and computation at scale. The small project reinforced "
    "these concepts in a practical way and made the learning feel rewarding. I am excited to "
    "continue building on this foundation next week.",
    body,
))

story.append(Spacer(1, 14))
story.append(HRFlowable(width="100%", thickness=1, color=C_HR))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<i>Generated by make_report_pdf_week03.py  ·  Python Internship  ·  Week 03</i>",
    ParagraphStyle("Footer", parent=body, fontSize=8.5,
                   textColor=colors.HexColor("#7F8C8D"), alignment=1),
))

# ── Build ────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF created: {FILE_NAME}")

"""
Week 03 Weekly Progress Report — Priyam Kumar Mishra
Python Internship | Topics: NumPy, NumPy Operators, Pandas, Pandas Operators

Run:
    pip install reportlab
    python generate_week03_report_priyam.py

Output: Weekly_Progress_Report_Priyam_Week03.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable,
    ListItem, Table, TableStyle, HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ── Output file ──────────────────────────────────────────────────────────────
OUTPUT_FILE = "Weekly_Progress_Report_Priyam_Week03.pdf"

# ── Colour palette (teal / slate / amber accent) ─────────────────────────────
C_HEADER_BG    = colors.HexColor("#1B4F72")   # deep navy (header banner)
C_HEADER_TEXT  = colors.white
C_ACCENT       = colors.HexColor("#1ABC9C")   # teal accent
C_SECTION_BG   = colors.HexColor("#EAF8F4")   # very light teal
C_SECTION_LINE = colors.HexColor("#1ABC9C")
C_LABEL_BG     = colors.HexColor("#D5F5E3")   # soft green for table labels
C_ALT_ROW      = colors.HexColor("#F2F3F4")   # alternating row
C_CODE_BG      = colors.HexColor("#F8F9FA")   # light grey for code block
C_CODE_BORDER  = colors.HexColor("#AEB6BF")
C_BODY_TEXT    = colors.HexColor("#1C2833")

# ── Page setup ───────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    leftMargin=1.8 * cm,
    rightMargin=1.8 * cm,
    topMargin=1.5 * cm,
    bottomMargin=1.8 * cm,
)
PAGE_W = A4[0] - 3.6 * cm   # usable width

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

BANNER_TITLE = ParagraphStyle(
    "BannerTitle",
    parent=base["Title"],
    fontSize=22,
    leading=28,
    textColor=C_HEADER_TEXT,
    alignment=TA_CENTER,
    fontName="Helvetica-Bold",
    spaceAfter=0,
)
BANNER_SUB = ParagraphStyle(
    "BannerSub",
    parent=base["Normal"],
    fontSize=11,
    leading=15,
    textColor=colors.HexColor("#A9CCE3"),
    alignment=TA_CENTER,
    fontName="Helvetica",
    spaceAfter=0,
)
SECTION_TITLE = ParagraphStyle(
    "SectionTitle",
    parent=base["Heading2"],
    fontSize=13,
    leading=16,
    textColor=C_HEADER_BG,
    fontName="Helvetica-Bold",
    spaceBefore=14,
    spaceAfter=6,
    leftIndent=8,
)
SUB_TITLE = ParagraphStyle(
    "SubTitle",
    parent=base["Heading3"],
    fontSize=11.5,
    leading=15,
    textColor=C_ACCENT,
    fontName="Helvetica-Bold",
    spaceBefore=8,
    spaceAfter=4,
    leftIndent=4,
)
BODY = ParagraphStyle(
    "Body",
    parent=base["BodyText"],
    fontSize=10.5,
    leading=15,
    textColor=C_BODY_TEXT,
    fontName="Helvetica",
    spaceAfter=4,
)
CODE_STYLE = ParagraphStyle(
    "Code",
    parent=base["Code"],
    fontSize=8.8,
    leading=13,
    fontName="Courier",
    textColor=colors.HexColor("#1A5276"),
    backColor=C_CODE_BG,
    leftIndent=6,
    rightIndent=6,
)
LABEL = ParagraphStyle(
    "Label",
    parent=base["Normal"],
    fontSize=10.5,
    fontName="Helvetica-Bold",
    textColor=C_HEADER_BG,
)
VALUE = ParagraphStyle(
    "Value",
    parent=base["Normal"],
    fontSize=10.5,
    fontName="Helvetica",
    textColor=C_BODY_TEXT,
)

# ── Helper functions ──────────────────────────────────────────────────────────

def section_header(text):
    """Return a teal-accented section header with a left border visual."""
    return [
        HRFlowable(width=PAGE_W, thickness=2, color=C_ACCENT, spaceAfter=2),
        Paragraph(text, SECTION_TITLE),
    ]


def bullet_list(items, style=BODY):
    return ListFlowable(
        [ListItem(Paragraph(it, style), leftIndent=14, bulletColor=C_ACCENT) for it in items],
        bulletType="bullet",
        leftIndent=18,
        bulletFontSize=9,
    )


def code_block(lines):
    """Render a code block as a table with a coloured border."""
    code_text = "<br/>".join(
        line.replace(" ", "&nbsp;").replace("<", "&lt;").replace(">", "&gt;")
        for line in lines
    )
    cell = Paragraph(code_text, CODE_STYLE)
    tbl = Table([[cell]], colWidths=[PAGE_W])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_CODE_BG),
        ("BOX",        (0, 0), (-1, -1), 1.2, C_CODE_BORDER),
        ("LEFTPADDING",  (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
    ]))
    return tbl


# ══════════════════════════════════════════════════════════════════════════════
# Build story
# ══════════════════════════════════════════════════════════════════════════════
story = []

# ── 1. Header banner ──────────────────────────────────────────────────────────
banner_data = [[
    Paragraph("Weekly Progress Report", BANNER_TITLE),
]]
banner_tbl = Table(banner_data, colWidths=[PAGE_W])
banner_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, -1), C_HEADER_BG),
    ("TOPPADDING",    (0, 0), (-1, -1), 16),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING",   (0, 0), (-1, -1), 14),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(banner_tbl)

sub_data = [[Paragraph("Python Internship  ·  Week 03  ·  NumPy &amp; Pandas", BANNER_SUB)]]
sub_tbl = Table(sub_data, colWidths=[PAGE_W])
sub_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, -1), colors.HexColor("#21618C")),
    ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ("LEFTPADDING",   (0, 0), (-1, -1), 14),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
]))
story.append(sub_tbl)
story.append(Spacer(1, 12))

# ── 2. Info table ─────────────────────────────────────────────────────────────
info_rows = [
    [Paragraph("Name",               LABEL), Paragraph("Priyam Kumar Mishra", VALUE)],
    [Paragraph("Domain",             LABEL), Paragraph("Python Internship",    VALUE)],
    [Paragraph("Date of Submission", LABEL), Paragraph("2026-04-26",           VALUE)],
    [Paragraph("Week",               LABEL), Paragraph("03",                   VALUE)],
    [Paragraph("Topics Covered",     LABEL), Paragraph(
        "NumPy, NumPy Operators, Pandas, Pandas Operators", VALUE)],
]
info_tbl = Table(info_rows, colWidths=[4.4 * cm, PAGE_W - 4.4 * cm])
info_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (0, -1), C_LABEL_BG),
    ("BACKGROUND",    (1, 0), (1, -1), colors.white),
    ("ROWBACKGROUNDS",(1, 0), (1, -1), [colors.white, C_ALT_ROW]),
    ("BOX",           (0, 0), (-1, -1), 1,   C_ACCENT),
    ("INNERGRID",     (0, 0), (-1, -1), 0.5, colors.HexColor("#BDC3C7")),
    ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING",   (0, 0), (-1, -1), 8),
]))
story.append(info_tbl)
story.append(Spacer(1, 14))

# ── 3. Overview ───────────────────────────────────────────────────────────────
story.extend(section_header("I. Overview"))
story.append(Paragraph(
    "Week 03 introduced me to two of the most powerful Python libraries for data handling: "
    "<b>NumPy</b> and <b>Pandas</b>. I learned how NumPy makes working with numbers and arrays "
    "fast and simple, and how Pandas lets me organize and analyse data using tables (DataFrames). "
    "I also applied both libraries in a hands-on mini project — <b>Monthly Sales Insights</b> — "
    "to see them working together in a real scenario.",
    BODY,
))

# ── 4. Achievements ──────────────────────────────────────────────────────────
story.extend(section_header("II. Achievements"))

# NumPy
story.append(Paragraph("A. NumPy — Basics", SUB_TITLE))
story.append(Paragraph(
    "NumPy (Numerical Python) is a library that provides fast, memory-efficient multi-dimensional "
    "arrays and a large collection of mathematical functions.", BODY))
story.append(bullet_list([
    "Understood what a NumPy array (ndarray) is and why it is faster than a Python list.",
    "Created 1-D and 2-D arrays using <b>np.array()</b>, <b>np.zeros()</b>, <b>np.ones()</b>, "
    "and <b>np.arange()</b>.",
    "Explored array attributes: <b>shape</b>, <b>dtype</b>, <b>ndim</b>, and <b>size</b>.",
    "Learned how to reshape and flatten arrays with <b>reshape()</b> and <b>flatten()</b>.",
    "Practised array indexing and slicing to access specific elements or rows/columns.",
]))

story.append(Spacer(1, 6))
story.append(Paragraph("B. NumPy Operators", SUB_TITLE))
story.append(Paragraph(
    "NumPy supports element-wise operations on entire arrays without writing loops.", BODY))
story.append(bullet_list([
    "<b>Arithmetic operators</b>: +, -, *, / applied element-by-element across arrays.",
    "<b>Aggregate functions</b>: <b>np.sum()</b>, <b>np.mean()</b>, <b>np.min()</b>, "
    "<b>np.max()</b>, <b>np.std()</b>.",
    "<b>Comparison operators</b>: ==, >, < produce boolean arrays (True/False per element).",
    "<b>Broadcasting</b>: adding a scalar or smaller array to a larger array automatically.",
    "<b>Universal functions (ufuncs)</b>: <b>np.sqrt()</b>, <b>np.abs()</b>, "
    "<b>np.log()</b>, <b>np.exp()</b>.",
]))

story.append(Spacer(1, 6))

# Pandas
story.append(Paragraph("C. Pandas — Basics", SUB_TITLE))
story.append(Paragraph(
    "Pandas is built on top of NumPy and is designed for working with labelled, structured data — "
    "similar to spreadsheets or SQL tables.", BODY))
story.append(bullet_list([
    "Understood the two core structures: <b>Series</b> (1-D labelled array) and "
    "<b>DataFrame</b> (2-D table with rows and columns).",
    "Created DataFrames from Python dictionaries and read data from CSV files with "
    "<b>pd.read_csv()</b>.",
    "Used <b>df.head()</b>, <b>df.tail()</b>, <b>df.info()</b>, and <b>df.describe()</b> "
    "for quick data exploration.",
    "Selected specific columns, filtered rows by condition, and handled missing values with "
    "<b>dropna()</b> and <b>fillna()</b>.",
    "Sorted data using <b>df.sort_values()</b> and reset the index with <b>reset_index()</b>.",
]))

story.append(Spacer(1, 6))
story.append(Paragraph("D. Pandas Operators", SUB_TITLE))
story.append(Paragraph(
    "Pandas provides rich operators for filtering, transforming, and aggregating data.", BODY))
story.append(bullet_list([
    "<b>Indexing operators</b>: <b>df['col']</b> (single column), <b>df[['c1','c2']]</b> "
    "(multiple), <b>df.loc[]</b> (label-based), <b>df.iloc[]</b> (position-based).",
    "<b>Comparison / Boolean filtering</b>: <b>df[df['Sales'] &gt; 500]</b> — returns only "
    "matching rows.",
    "<b>Arithmetic on columns</b>: adding, multiplying, or dividing entire columns in one line.",
    "<b>groupby + agg</b>: group rows by a category and calculate sum, mean, count, etc.",
    "<b>apply()</b>: run a custom function on every row or column.",
    "<b>merge() / concat()</b>: join two DataFrames together (like SQL JOIN or UNION).",
]))

# ── 5. Challenges ────────────────────────────────────────────────────────────
story.extend(section_header("III. Challenges Faced"))
story.append(bullet_list([
    "Understanding the difference between <b>loc</b> (label-based) and <b>iloc</b> "
    "(integer-position-based) indexing took extra practice.",
    "Broadcasting rules in NumPy — when shapes are compatible and when they raise errors — "
    "needed careful reading of examples.",
    "Handling missing / NaN values in Pandas correctly (when to drop vs. fill) required "
    "thinking about the data context.",
    "Reading the error messages from NumPy/Pandas and figuring out the right fix improved "
    "my debugging skills.",
]))

# ── 6. Learning Resources ────────────────────────────────────────────────────
story.extend(section_header("IV. Learning Resources"))
story.append(bullet_list([
    "Official NumPy documentation and quickstart tutorial.",
    "Official Pandas 'Getting started' guide and 10 Minutes to Pandas tutorial.",
    "Practical examples from YouTube walkthroughs on NumPy arrays and Pandas DataFrames.",
    "Solved exercises on small datasets to reinforce each concept before moving to the next.",
]))

# ── 7. Project Section ───────────────────────────────────────────────────────
story.extend(section_header("V. Mini Project — Monthly Sales Insights"))

story.append(Paragraph("What is this project?", SUB_TITLE))
story.append(Paragraph(
    "The <b>Monthly Sales Insights</b> project reads a small table of monthly product sales, "
    "uses <b>NumPy</b> to do quick number crunching, and uses <b>Pandas</b> to organise the data "
    "into a neat table and find the best/worst performing months.", BODY))

story.append(Paragraph("What the project does — step by step:", SUB_TITLE))
story.append(ListFlowable([
    ListItem(Paragraph(
        "<b>Step 1 — Create the data.</b>  We make a simple dictionary with three products "
        "(Widget A, Widget B, Widget C) and their sales figures for five months.", BODY),
        value=1, leftIndent=16, bulletColor=C_HEADER_BG),
    ListItem(Paragraph(
        "<b>Step 2 — Build a Pandas DataFrame.</b>  The dictionary becomes a table where each "
        "row is a month and each column is a product.", BODY),
        value=2, leftIndent=16, bulletColor=C_HEADER_BG),
    ListItem(Paragraph(
        "<b>Step 3 — NumPy calculations.</b>  We extract the sales numbers as a NumPy array "
        "and compute the total, monthly average, best month, and worst month.", BODY),
        value=3, leftIndent=16, bulletColor=C_HEADER_BG),
    ListItem(Paragraph(
        "<b>Step 4 — Pandas analysis.</b>  We add a 'Total' column, sort months by total "
        "sales, and print a readable summary.", BODY),
        value=4, leftIndent=16, bulletColor=C_HEADER_BG),
    ListItem(Paragraph(
        "<b>Step 5 — Print the report.</b>  The script prints all insights to the console "
        "in plain English so anyone can understand the output.", BODY),
        value=5, leftIndent=16, bulletColor=C_HEADER_BG),
], bulletType="1", leftIndent=20))

story.append(Spacer(1, 8))
story.append(Paragraph("Sample code snippet:", SUB_TITLE))

code_lines = [
    "import numpy as np",
    "import pandas as pd",
    "",
    "# Step 1 — Sales data (units sold per month)",
    "data = {",
    "    'Month':    ['Jan', 'Feb', 'Mar', 'Apr', 'May'],",
    "    'Widget_A': [320,   410,   390,   480,   520],",
    "    'Widget_B': [210,   190,   310,   275,   340],",
    "    'Widget_C': [150,   200,   170,   220,   260],",
    "}",
    "",
    "# Step 2 — Build DataFrame",
    "df = pd.DataFrame(data)",
    "",
    "# Step 3 — NumPy calculations on all sales values",
    "sales_array = np.array(df[['Widget_A', 'Widget_B', 'Widget_C']])",
    "monthly_totals = sales_array.sum(axis=1)   # sum across columns for each row",
    "overall_avg   = np.mean(monthly_totals)",
    "best_idx      = np.argmax(monthly_totals)",
    "worst_idx     = np.argmin(monthly_totals)",
    "",
    "# Step 4 — Pandas: add Total column and sort",
    "df['Total'] = monthly_totals",
    "df_sorted   = df.sort_values('Total', ascending=False).reset_index(drop=True)",
    "",
    "# Step 5 — Print insights",
    "print('=== Monthly Sales Insights ===')",
    "print(df_sorted.to_string(index=False))",
    "print(f'\\nOverall average monthly sales : {overall_avg:.1f} units')",
    "print(f'Best  month : {df[\"Month\"][best_idx]}  ({monthly_totals[best_idx]} units)')",
    "print(f'Worst month : {df[\"Month\"][worst_idx]} ({monthly_totals[worst_idx]} units)')",
]
story.append(code_block(code_lines))

story.append(Spacer(1, 8))
story.append(Paragraph("Expected output (sample):", SUB_TITLE))

output_lines = [
    "=== Monthly Sales Insights ===",
    " Month  Widget_A  Widget_B  Widget_C  Total",
    "   May       520       340       260   1120",
    "   Apr       480       275       220    975",
    "   Feb       410       190       200    800",
    "   Mar       390       310       170    870",
    "   Jan       320       210       150    680",
    "",
    "Overall average monthly sales : 889.0 units",
    "Best  month : May  (1120 units)",
    "Worst month : Jan  (680 units)",
]
story.append(code_block(output_lines))

# ── 8. Next Week Goals ────────────────────────────────────────────────────────
story.extend(section_header("VI. Plan for Next Week"))
story.append(bullet_list([
    "Dive deeper into Pandas: pivot tables, time-series indexing, and data visualisation "
    "with <b>Matplotlib</b>.",
    "Explore more NumPy features: matrix operations (<b>np.dot()</b>), random number "
    "generation (<b>np.random</b>), and linear algebra helpers.",
    "Extend the Monthly Sales Insights project to read data from a real CSV file and "
    "generate a bar chart of monthly totals.",
    "Practice combining what I have learned in small end-to-end data analysis exercises.",
]))

# ── 9. Remarks ────────────────────────────────────────────────────────────────
story.extend(section_header("VII. Remarks"))
story.append(Paragraph(
    "Week 03 was a significant step forward. NumPy and Pandas are core tools in Python data "
    "analysis, and getting comfortable with them early will make future topics much easier. "
    "The mini project helped me connect the theory to a practical use case, which made the "
    "concepts much clearer and more memorable.",
    BODY,
))

# ── Footer line ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 20))
story.append(HRFlowable(width=PAGE_W, thickness=1.5, color=C_ACCENT))
story.append(Spacer(1, 4))
footer_data = [[
    Paragraph("Priyam Kumar Mishra  |  Python Internship  |  Week 03", ParagraphStyle(
        "Footer", parent=base["Normal"], fontSize=8.5,
        textColor=colors.HexColor("#7F8C8D"), fontName="Helvetica",
        alignment=TA_CENTER,
    )),
]]
f_tbl = Table(footer_data, colWidths=[PAGE_W])
f_tbl.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
story.append(f_tbl)

# ── Build PDF ─────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF created successfully: {OUTPUT_FILE}")

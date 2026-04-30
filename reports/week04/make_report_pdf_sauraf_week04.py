"""
Week 04 Progress Report PDF Generator - Sauraf Kumar
=====================================================
Generates a multi-page, attractively styled PDF summarising
Weeks 01-03 learning and providing a Week 04 consolidated overview.

Usage:
    pip install reportlab
    python make_report_pdf_sauraf_week04.py

Output:
    Weekly_Progress_Report_Sauraf_Week04.pdf  (written to the same directory)
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, HRFlowable, PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

# ---------------------------------------------------------------------------
# Output file
# ---------------------------------------------------------------------------
OUTPUT_FILE = "Weekly_Progress_Report_Sauraf_Week04.pdf"

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------
DARK_NAVY   = colors.HexColor("#0D1B2A")
TEAL        = colors.HexColor("#17A589")
AMBER       = colors.HexColor("#F39C12")
SOFT_BLUE   = colors.HexColor("#D6EAF8")
SOFT_TEAL   = colors.HexColor("#D1F2EB")
SOFT_AMBER  = colors.HexColor("#FEF9E7")
GRAY_LIGHT  = colors.HexColor("#F2F3F4")
GRAY_MED    = colors.HexColor("#BFC9CA")
WHITE       = colors.white
TEXT_DARK   = colors.HexColor("#17202A")
TEXT_MUTED  = colors.HexColor("#566573")
CODE_BG     = colors.HexColor("#1E2D3D")
CODE_FG     = colors.HexColor("#E8F8F5")
ACCENT_RED  = colors.HexColor("#C0392B")
ACCENT_PUR  = colors.HexColor("#6C3483")

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
base = getSampleStyleSheet()

def _style(name, parent_name="BodyText", **kw):
    return ParagraphStyle(name, parent=base[parent_name], **kw)

COVER_TITLE = _style(
    "CoverTitle", "Title",
    fontSize=26, textColor=WHITE, leading=32, spaceAfter=4,
)
COVER_SUB = _style(
    "CoverSub", "BodyText",
    fontSize=13, textColor=colors.HexColor("#D5F5E3"),
    leading=18, spaceAfter=6,
)
SECTION_H = _style(
    "SectionH", "Heading1",
    fontSize=14, textColor=DARK_NAVY, spaceBefore=14, spaceAfter=6,
    borderPad=4,
)
SUB_H = _style(
    "SubH", "Heading2",
    fontSize=12, textColor=TEAL, spaceBefore=8, spaceAfter=4,
)
BODY = _style(
    "Body", "BodyText",
    fontSize=10.5, leading=15, textColor=TEXT_DARK,
)
BODY_MUTED = _style(
    "BodyMuted", "BodyText",
    fontSize=10, leading=14, textColor=TEXT_MUTED,
)
CODE_STYLE = _style(
    "Code", "BodyText",
    fontSize=9.5, leading=14, fontName="Courier",
    textColor=CODE_FG, backColor=CODE_BG,
)
CALLOUT = _style(
    "Callout", "BodyText",
    fontSize=10.5, leading=15, textColor=TEXT_DARK,
    leftIndent=8, rightIndent=8,
)
LABEL = _style(
    "Label", "BodyText",
    fontSize=10, textColor=DARK_NAVY, fontName="Helvetica-Bold",
)

# ---------------------------------------------------------------------------
# Helper builders
# ---------------------------------------------------------------------------

def divider(color=TEAL, thickness=1.2):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=4)


def section_header(text, story):
    story.append(divider())
    story.append(Paragraph(text, SECTION_H))


def callout_box(text, story, bg=SOFT_AMBER, border=AMBER, label=None):
    content = (f"<b>{label}</b><br/>" if label else "") + text
    tbl = Table(
        [[Paragraph(content, CALLOUT)]],
        colWidths=[16.6 * cm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), bg),
        ("BOX",           (0, 0), (-1, -1), 1.2, border),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 6))


def code_box(lines, story):
    code_text = "<br/>".join(lines)
    tbl = Table(
        [[Paragraph(code_text, CODE_STYLE)]],
        colWidths=[16.6 * cm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), CODE_BG),
        ("BOX",           (0, 0), (-1, -1), 1.0, TEAL),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 6))


def bullet_list(items, story, style=None):
    s = style or BODY
    story.append(ListFlowable(
        [ListItem(Paragraph(i, s), leftIndent=14, bulletColor=TEAL) for i in items],
        bulletType="bullet",
        leftIndent=18,
        spaceAfter=2,
    ))


def numbered_list(items, story, style=None):
    s = style or BODY
    story.append(ListFlowable(
        [ListItem(Paragraph(i, s), leftIndent=14) for i in items],
        bulletType="1",
        leftIndent=18,
        spaceAfter=2,
    ))

# ---------------------------------------------------------------------------
# Build story
# ---------------------------------------------------------------------------

def build_story():
    story = []

    # ------------------------------------------------------------------ #
    #  PAGE 1 – Cover / Header                                            #
    # ------------------------------------------------------------------ #

    # Coloured cover banner
    cover_data = [[
        Paragraph("Weekly Progress Report", COVER_TITLE),
        Paragraph(
            "<b>Name:</b> Sauraf Kumar<br/>"
            "<b>Domain:</b> Python Internship<br/>"
            "<b>Week:</b> 04 &nbsp;|&nbsp; <b>Date:</b> 2026-04-30<br/>"
            "<b>Mentor:</b> Priyam Kumar Mishra",
            COVER_SUB,
        ),
    ]]
    cover_tbl = Table(cover_data, colWidths=[9.5 * cm, 7.1 * cm])
    cover_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), DARK_NAVY),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 14),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(cover_tbl)
    story.append(Spacer(1, 10))

    # Badge row
    badges = [
        [Paragraph("<b>Week 01</b><br/>Python Basics", COVER_SUB),
         Paragraph("<b>Week 02</b><br/>Conditionals", COVER_SUB),
         Paragraph("<b>Week 03</b><br/>NumPy & Pandas", COVER_SUB),
         Paragraph("<b>Week 04</b><br/>Consolidation", COVER_SUB)],
    ]
    badge_tbl = Table(badges, colWidths=[4.0 * cm, 4.0 * cm, 4.0 * cm, 4.6 * cm])
    badge_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), colors.HexColor("#1A5276")),
        ("BACKGROUND",    (1, 0), (1, 0), colors.HexColor("#1E8449")),
        ("BACKGROUND",    (2, 0), (2, 0), colors.HexColor("#784212")),
        ("BACKGROUND",    (3, 0), (3, 0), TEAL),
        ("TEXTCOLOR",     (0, 0), (-1, -1), WHITE),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9.5),
        ("INNERGRID",     (0, 0), (-1, -1), 0.5, WHITE),
        ("BOX",           (0, 0), (-1, -1), 0.5, WHITE),
    ]))
    story.append(badge_tbl)
    story.append(Spacer(1, 14))

    # ------------------------------------------------------------------ #
    #  SECTION 1 – Executive Summary (Weeks 01-03 Recap)                 #
    # ------------------------------------------------------------------ #
    section_header("1. Executive Summary — Weeks 01–03 Recap", story)
    story.append(Paragraph(
        "Over the first three weeks of the Python internship, Sauraf Kumar progressed from a complete "
        "beginner to a developer capable of writing practical data-analysis scripts. Each week built "
        "directly on the last, establishing a solid foundation in core Python programming, decision-making "
        "logic, and scientific/data libraries.",
        BODY,
    ))
    story.append(Spacer(1, 8))

    callout_box(
        "By the end of Week 03, Sauraf had written three working programs: a Quiz Game prototype, "
        "a Mini Calculator, and a NumPy + Pandas data-analysis script — demonstrating real-world "
        "application of every concept covered so far.",
        story,
        bg=SOFT_TEAL,
        border=TEAL,
        label="Key Achievement",
    )

    story.append(Paragraph("<b>Week 01 – Python Introduction</b>", SUB_H))
    story.append(Paragraph(
        "The internship began with an exploration of Python fundamentals. Sauraf learned how to write and "
        "run Python scripts, understand data types (integers, floats, strings, booleans), read user input, "
        "and display output. The week also introduced variables, basic operators, and the concept of "
        "indentation-based code blocks. Alongside the theory, the project theme was finalised: a "
        "<b>Quiz Game</b> that would grow in complexity with each passing week.",
        BODY,
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Week 02 – Conditional Statements</b>", SUB_H))
    story.append(Paragraph(
        "Week 02 introduced the heart of program logic — conditional statements. Sauraf practised "
        "<b>if</b>, <b>if-else</b>, and <b>if-elif-else</b> chains, along with comparison operators "
        "(<code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, "
        "<code>&lt;=</code>) and logical operators (<code>and</code>, <code>or</code>, <code>not</code>). "
        "These skills were put into practice immediately through the <b>Mini Calculator</b> project, which "
        "accepts two numbers and an operator from the user and returns the correct result — including a "
        "guard against division by zero.",
        BODY,
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Week 03 – NumPy & Pandas with Operators</b>", SUB_H))
    story.append(Paragraph(
        "The third week levelled up the data-handling skills significantly. Sauraf was introduced to "
        "<b>NumPy</b> for numerical computing (arrays, element-wise operations, broadcasting, aggregation "
        "functions such as <code>mean</code>, <code>sum</code>, and <code>std</code>) and <b>Pandas</b> "
        "for tabular data (Series, DataFrames, filtering, groupby, and statistical operators). The week "
        "concluded with a combined <b>NumPy + Pandas Data Analyser</b> project that loads a sample "
        "dataset, computes descriptive statistics, and identifies outliers.",
        BODY,
    ))

    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  SECTION 2 – Skills Learned by Week (Timeline Table)               #
    # ------------------------------------------------------------------ #
    section_header("2. Skills Learned by Week", story)

    timeline_header = [
        Paragraph("<b>Week</b>",  LABEL),
        Paragraph("<b>Topic</b>", LABEL),
        Paragraph("<b>Key Skills Acquired</b>", LABEL),
        Paragraph("<b>Project</b>", LABEL),
    ]
    timeline_rows = [
        [
            Paragraph("Week 01", BODY),
            Paragraph("Python Intro", BODY),
            Paragraph(
                "Variables, data types, input/output,<br/>basic operators, indentation rules",
                BODY,
            ),
            Paragraph("Quiz Game (planning)", BODY),
        ],
        [
            Paragraph("Week 02", BODY),
            Paragraph("Conditional Statements", BODY),
            Paragraph(
                "if / if-else / if-elif-else,<br/>comparison &amp; logical operators,<br/>nested conditions",
                BODY,
            ),
            Paragraph("Mini Calculator", BODY),
        ],
        [
            Paragraph("Week 03", BODY),
            Paragraph("NumPy & Pandas", BODY),
            Paragraph(
                "Arrays, broadcasting, aggregation,<br/>DataFrame ops, filtering, groupby,<br/>operators on arrays/series",
                BODY,
            ),
            Paragraph("NumPy+Pandas Analyser", BODY),
        ],
        [
            Paragraph("Week 04", BODY),
            Paragraph("Consolidation", BODY),
            Paragraph(
                "Integration of all prior skills,<br/>code review, documentation,<br/>problem-solving strategies",
                BODY,
            ),
            Paragraph("Portfolio Review", BODY),
        ],
    ]

    timeline_data = [timeline_header] + timeline_rows
    col_w = [2.0 * cm, 3.8 * cm, 6.6 * cm, 4.2 * cm]
    tbl = Table(timeline_data, colWidths=col_w, repeatRows=1)
    tbl.setStyle(TableStyle([
        # Header row
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_NAVY),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 10),
        # Data rows alternating
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [GRAY_LIGHT, WHITE]),
        # Highlight week 04 row
        ("BACKGROUND",    (0, 4), (-1, 4), SOFT_TEAL),
        # Grid
        ("GRID",          (0, 0), (-1, -1), 0.5, GRAY_MED),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("FONTSIZE",      (0, 1), (-1, -1), 10),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 12))

    # ------------------------------------------------------------------ #
    #  SECTION 3 – Projects Completed                                     #
    # ------------------------------------------------------------------ #
    section_header("3. Projects Completed", story)

    # Project 3.1 – Quiz Game
    story.append(Paragraph("3.1  Quiz Game (Planning & Prototype)", SUB_H))
    story.append(Paragraph(
        "Conceived in Week 01 and progressively refined, the Quiz Game demonstrates understanding of "
        "variables, user interaction, and basic logic. The prototype flow is:",
        BODY,
    ))
    numbered_list([
        "Store a list of questions, choices, and correct answers.",
        "Display each question and all answer options to the user.",
        "Accept user input and compare against the correct answer.",
        "Increment score on correct answers.",
        "Display the final score and a grade message when all questions are done.",
    ], story)
    story.append(Spacer(1, 6))
    callout_box(
        "This project will be extended in future weeks to add loops, file I/O for saving scores, "
        "and eventually a graphical interface.",
        story,
        bg=SOFT_BLUE,
        border=colors.HexColor("#1A5276"),
        label="Future Roadmap",
    )

    # Project 3.2 – Mini Calculator
    story.append(Paragraph("3.2  Mini Calculator", SUB_H))
    story.append(Paragraph(
        "The Mini Calculator (Week 02) is the most tangible output so far. It applies "
        "<b>if-elif-else</b> in a real interactive program. The user enters two numbers, chooses an "
        "arithmetic operation, and receives an instant result. Division by zero is handled gracefully.",
        BODY,
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Highlighted Code Snippet — Mini Calculator</b>", BODY_MUTED))
    code_box([
        "# Mini Calculator — Sauraf Kumar (Week 02)",
        "num1 = float(input('Enter first number : '))",
        "num2 = float(input('Enter second number: '))",
        "op   = input('Choose operation (+  -  *  /)  : ')",
        "",
        "if op == '+':",
        "    print('Result:', num1 + num2)",
        "elif op == '-':",
        "    print('Result:', num1 - num2)",
        "elif op == '*':",
        "    print('Result:', num1 * num2)",
        "elif op == '/':",
        "    if num2 == 0:",
        "        print('Error: Division by zero is not allowed.')",
        "    else:",
        "        print('Result:', num1 / num2)",
        "else:",
        "    print('Invalid operation. Please use +  -  *  /')",
    ], story)

    # Project 3.3 – NumPy + Pandas Analyser
    story.append(Paragraph("3.3  NumPy + Pandas Data Analyser", SUB_H))
    story.append(Paragraph(
        "The Week 03 capstone project ties together both scientific libraries. Given a structured "
        "dataset (sales figures, student grades, or any CSV), the analyser:",
        BODY,
    ))
    numbered_list([
        "Loads data into a <b>Pandas DataFrame</b>.",
        "Uses <b>NumPy</b> to compute mean, median, standard deviation, and variance.",
        "Applies Pandas <b>groupby</b> to summarise data by category.",
        "Identifies outliers using the Z-score method (NumPy broadcasting).",
        "Prints a formatted summary report to the console.",
    ], story)
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Key Pandas Operators Practised</b>", BODY_MUTED))
    story.append(Spacer(1, 4))
    ops_data = [
        [Paragraph("<b>Operator / Method</b>", LABEL), Paragraph("<b>Purpose</b>", LABEL)],
        [Paragraph("df[col] > value",      BODY), Paragraph("Boolean filtering of rows", BODY)],
        [Paragraph("df.groupby(col).mean()", BODY), Paragraph("Average per group",         BODY)],
        [Paragraph("df.describe()",         BODY), Paragraph("Full descriptive stats",      BODY)],
        [Paragraph("np.mean / np.std",      BODY), Paragraph("Array-level aggregation",     BODY)],
        [Paragraph("np.where(condition)",   BODY), Paragraph("Vectorised if-else on array", BODY)],
    ]
    ops_tbl = Table(ops_data, colWidths=[7.0 * cm, 9.6 * cm])
    ops_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [SOFT_TEAL, WHITE]),
        ("GRID",          (0, 0), (-1, -1), 0.5, GRAY_MED),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("FONTSIZE",      (0, 0), (-1, -1), 10),
    ]))
    story.append(ops_tbl)
    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  PAGE BREAK before detailed sections                               #
    # ------------------------------------------------------------------ #
    story.append(PageBreak())

    # ------------------------------------------------------------------ #
    #  SECTION 4 – Key Outcomes                                          #
    # ------------------------------------------------------------------ #
    section_header("4. Key Outcomes", story)
    outcomes = [
        "<b>Python Fluency:</b> Comfortable writing scripts from scratch without references for all "
        "Week 01–02 concepts.",
        "<b>Data Literacy:</b> Able to load, inspect, and summarise real datasets using Pandas and NumPy.",
        "<b>Project Mindset:</b> Understands how to break a problem into smaller steps and iteratively "
        "build a working program.",
        "<b>Error Handling:</b> Implements basic guards (division by zero, invalid input) in interactive "
        "programs.",
        "<b>Code Readability:</b> Follows consistent naming conventions and adds inline comments to "
        "explain logic.",
        "<b>Library Usage:</b> Knows how to install third-party packages via <code>pip</code> and import "
        "them correctly.",
    ]
    bullet_list(outcomes, story)
    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  SECTION 5 – Challenges & Solutions                                #
    # ------------------------------------------------------------------ #
    section_header("5. Challenges & Solutions", story)
    challenges = [
        [
            Paragraph("<b>Challenge</b>", LABEL),
            Paragraph("<b>Solution Applied</b>", LABEL),
        ],
        [
            Paragraph("Indentation errors in nested conditions", BODY),
            Paragraph("Used a consistent 4-space indent; enabled a linter (Pylint) in the editor.", BODY),
        ],
        [
            Paragraph("Confusion between = (assignment) and == (comparison)", BODY),
            Paragraph("Created a personal cheat-sheet and practised with assertion tests.", BODY),
        ],
        [
            Paragraph("Understanding NumPy broadcasting rules", BODY),
            Paragraph("Worked through shape-mismatch examples step by step; drew shape diagrams.", BODY),
        ],
        [
            Paragraph("Pandas SettingWithCopyWarning on filtered slices", BODY),
            Paragraph("Learned to use .loc[] for explicit row/column selection.", BODY),
        ],
        [
            Paragraph("Choosing correct aggregation (mean vs median) for skewed data", BODY),
            Paragraph("Checked data distribution with df.describe() before deciding.", BODY),
        ],
    ]
    ch_tbl = Table(challenges, colWidths=[7.2 * cm, 9.4 * cm])
    ch_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), DARK_NAVY),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [SOFT_AMBER, WHITE]),
        ("GRID",          (0, 0), (-1, -1), 0.5, GRAY_MED),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("FONTSIZE",      (0, 0), (-1, -1), 10),
    ]))
    story.append(ch_tbl)
    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  SECTION 6 – Tools & Resources Used                                #
    # ------------------------------------------------------------------ #
    section_header("6. Tools & Resources Used", story)
    tools_data = [
        [Paragraph("<b>Tool / Resource</b>", LABEL), Paragraph("<b>Purpose</b>", LABEL)],
        [Paragraph("Python 3.x",              BODY), Paragraph("Primary programming language",         BODY)],
        [Paragraph("VS Code",                 BODY), Paragraph("Code editor with syntax highlighting", BODY)],
        [Paragraph("NumPy",                   BODY), Paragraph("Numerical arrays and operations",      BODY)],
        [Paragraph("Pandas",                  BODY), Paragraph("Tabular data manipulation",            BODY)],
        [Paragraph("ReportLab",               BODY), Paragraph("PDF generation (this report)",         BODY)],
        [Paragraph("pip",                     BODY), Paragraph("Package installation",                 BODY)],
        [Paragraph("Official Python Docs",    BODY), Paragraph("Syntax reference and tutorials",       BODY)],
        [Paragraph("Stack Overflow",          BODY), Paragraph("Troubleshooting and best practices",   BODY)],
    ]
    tools_tbl = Table(tools_data, colWidths=[5.0 * cm, 11.6 * cm])
    tools_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [GRAY_LIGHT, WHITE]),
        ("GRID",          (0, 0), (-1, -1), 0.5, GRAY_MED),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("FONTSIZE",      (0, 0), (-1, -1), 10),
    ]))
    story.append(tools_tbl)
    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  SECTION 7 – Week 04 Consolidated Overview                         #
    # ------------------------------------------------------------------ #
    section_header("7. Week 04 Consolidated Overview", story)
    story.append(Paragraph(
        "Week 04 is a dedicated <b>consolidation sprint</b>. Rather than introducing brand-new topics, "
        "the focus this week is on reviewing, refining, and integrating everything learned so far. "
        "Activities include:",
        BODY,
    ))
    bullet_list([
        "Re-reading and documenting all code written in Weeks 01–03.",
        "Refactoring the Mini Calculator to add a loop-based menu (user can calculate multiple times without restarting).",
        "Extending the NumPy + Pandas Analyser with a simple bar-chart using <code>matplotlib</code>.",
        "Writing a short self-assessment of strengths and areas for improvement.",
        "Preparing a single consolidated script that demonstrates all three projects in sequence.",
    ], story)
    story.append(Spacer(1, 8))

    callout_box(
        "Goal for Week 04: Every project from Weeks 01–03 should be clean, commented, and runnable "
        "without any errors on a fresh Python installation (after pip install of required packages).",
        story,
        bg=SOFT_TEAL,
        border=TEAL,
        label="Week 04 Goal",
    )

    # ------------------------------------------------------------------ #
    #  SECTION 8 – Next Steps                                            #
    # ------------------------------------------------------------------ #
    section_header("8. Next Steps (Week 05 Plan)", story)
    next_steps = [
        "<b>Loops (for / while):</b> Deep-dive into iteration, enabling the Quiz Game to loop through all "
        "questions automatically.",
        "<b>Functions:</b> Refactor the Mini Calculator and Analyser into well-named functions to improve "
        "modularity and reusability.",
        "<b>File I/O:</b> Learn to read from and write to text and CSV files — essential for a "
        "production-grade data pipeline.",
        "<b>Exception Handling (try/except):</b> Gracefully handle unexpected inputs and runtime errors.",
        "<b>Mini Project — Score Logger:</b> Combine loops, functions, and file I/O to build a quiz "
        "application that saves each player's score to a file.",
    ]
    numbered_list(next_steps, story)
    story.append(Spacer(1, 10))

    # ------------------------------------------------------------------ #
    #  SECTION 9 – Detailed Summary                                      #
    # ------------------------------------------------------------------ #
    section_header("9. Detailed Learning Summary", story)
    story.append(Paragraph(
        "This section provides an expanded narrative of the learning journey across all four weeks, "
        "suitable for mentor review and portfolio submission.",
        BODY_MUTED,
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Python as a Problem-Solving Tool", SUB_H))
    story.append(Paragraph(
        "From the very first session, the internship emphasised Python not just as a language but as a "
        "structured way to think about problems. Sauraf began with the simplest possible programs — "
        "printing a message, reading a number — and quickly discovered that even these tiny scripts "
        "contain the building blocks of every large application: state (variables), action (statements), "
        "and communication (input/output).",
        BODY,
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Conditional Logic — The Decision Engine", SUB_H))
    story.append(Paragraph(
        "The introduction of conditional statements in Week 02 was a turning point. Suddenly, programs "
        "could <i>make choices</i>. The Mini Calculator was deliberately chosen as the Week 02 project "
        "because it perfectly illustrates every form of branching: a four-way <code>if-elif-elif-else</code> "
        "for the operation, and a nested <code>if</code> inside the division branch to protect against "
        "division by zero. Sauraf also noticed that the order of <code>elif</code> clauses matters — a "
        "valuable debugging lesson that no tutorial can replace.",
        BODY,
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Entering the Data Science Space — NumPy & Pandas", SUB_H))
    story.append(Paragraph(
        "Week 03 introduced the two most important libraries for data work in Python. NumPy's ndarray "
        "changed how Sauraf thought about loops: instead of iterating over a list element by element, "
        "operations can be applied to the entire array at once — this is called <b>vectorisation</b>, and "
        "it is both faster and more readable. Pandas built on this concept by adding column names, "
        "row labels, and a rich API for reshaping and querying data tables.",
        BODY,
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "The Data Analyser project tied these together. Loading a CSV with "
        "<code>pd.read_csv()</code>, computing statistics with <code>df.describe()</code> and "
        "<code>np.std()</code>, and isolating outliers with boolean indexing — each step required "
        "combining knowledge from all three weeks. It was the first program where Sauraf could "
        "genuinely see the output and say: <i>'This is useful. I could give this to someone.'</i>",
        BODY,
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Reflection on the Internship So Far", SUB_H))
    story.append(Paragraph(
        "Four weeks in, the most important lesson has been that programming is iterative. No program is "
        "written correctly the first time. The process of writing, running, reading the error, fixing, "
        "and running again is not a sign of failure — it is the process. Sauraf has embraced this loop "
        "(pun intended) and approaches each new problem with curiosity rather than anxiety.",
        BODY,
    ))

    story.append(Spacer(1, 10))
    story.append(divider(color=AMBER))
    story.append(Paragraph(
        "<i>Report generated automatically by make_report_pdf_sauraf_week04.py using ReportLab.</i>",
        BODY_MUTED,
    ))

    return story


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title="Weekly Progress Report — Sauraf Kumar — Week 04",
        author="Sauraf Kumar",
        subject="Python Internship Week 04",
    )
    story = build_story()
    doc.build(story)
    print(f"✅  PDF created successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

# Week 03 — Progress Report PDF Generator

Generates **Weekly_Progress_Report_Week03.pdf** — a styled internship progress report covering **NumPy** and **Pandas**, including a mini-project (*Student Marks Analyzer*).

---

## Quick Start

### 1. Install the only dependency

```bash
pip install reportlab
```

### 2. Run the script

```bash
python make_report_pdf_week03.py
```

The PDF is saved **in the same folder** as the script:

```
reports/week03/Weekly_Progress_Report_Week03.pdf
```

---

## What's Inside the PDF

| Section | Content |
|---------|---------|
| **Header** | Coloured banner with name, domain, week, submission date |
| **I. Overview** | Week summary — NumPy & Pandas focus |
| **II. Achievements** | NumPy (arrays, operators) · Pandas (DataFrame/Series, operators) with colour badges |
| **III. Project** | Student Marks Analyzer — description, step-by-step plan, highlighted code block |
| **IV. Challenges** | NumPy broadcasting · Pandas index alignment |
| **V. Learning Resources** | Official docs, Kaggle, Real Python |
| **VI. Next Week's Goals** | Matplotlib/Seaborn · Advanced Pandas |
| **VII. Additional Comments** | Reflections on the week |

---

## Mini-Project: Student Marks Analyzer

- Create a **NumPy 2-D array** of student marks (5 students × 3 subjects).
- Use **NumPy operators** (`sum`, `mean`, `min`, `max`) along axes to compute per-student stats.
- Convert to a **Pandas DataFrame** with meaningful column and index labels.
- Add derived columns (Total, Average, Percentage, Grade) using **Pandas operators**.
- **Filter** students who passed (average ≥ 70) using Boolean indexing.
- **Export** the full report to `student_marks.csv` with `df.to_csv()`.

---

## Requirements

| Package | Version |
|---------|---------|
| reportlab | ≥ 3.6 |
| Python | ≥ 3.8 |

> **Note:** The script does *not* require NumPy or Pandas to be installed — the code snippet shown in the PDF is illustrative. If you want to actually *run* the analyzer code, install those packages separately:
> ```bash
> pip install numpy pandas
> ```

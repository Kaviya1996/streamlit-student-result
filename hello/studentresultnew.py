import streamlit as st
import os
import pandas as pd

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Student Report Card",
    page_icon="🎓",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── App background ── */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    min-height: 100vh;
}

/* ── Header banner ── */
.app-header {
    background: linear-gradient(90deg, #1d4ed8, #7c3aed);
    border-radius: 16px;
    padding: 2rem 2.5rem 1.5rem;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(124,58,237,0.3);
}
.app-header h1 {
    font-family: 'Playfair Display', serif;
    color: #ffffff;
    font-size: 2.4rem;
    margin: 0 0 0.25rem 0;
    letter-spacing: -0.5px;
}
.app-header p {
    color: #bfdbfe;
    font-size: 0.95rem;
    margin: 0;
}

/* ── Cards ── */
.card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.25rem;
    backdrop-filter: blur(8px);
}
.card-title {
    color: #93c5fd;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

/* ── Input labels ── */
label {
    color: #cbd5e1 !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}

/* ── Text inputs ── */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #f1f5f9 !important;
    font-family: 'DM Sans', sans-serif !important;
    padding: 0.55rem 0.9rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.25) !important;
}

/* ── Number inputs ── */
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #f1f5f9 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stNumberInput > div > div > input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.25) !important;
}
.stNumberInput button {
    background: rgba(255,255,255,0.08) !important;
    border: none !important;
    color: #94a3b8 !important;
}

/* ── Buttons ── */
.stButton > button {
    width: 100%;
    padding: 0.65rem 1.5rem;
    border-radius: 10px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    letter-spacing: 0.3px;
}
/* Primary button (first) */
.stButton:nth-of-type(1) > button {
    background: linear-gradient(90deg, #1d4ed8, #7c3aed);
    color: white;
    box-shadow: 0 4px 15px rgba(124,58,237,0.35);
}
.stButton:nth-of-type(1) > button:hover {
    box-shadow: 0 6px 20px rgba(124,58,237,0.55);
    transform: translateY(-1px);
}
/* Secondary button */
.stButton:nth-of-type(2) > button {
    background: rgba(255,255,255,0.07);
    color: #94a3b8;
    border: 1px solid rgba(255,255,255,0.12) !important;
}
.stButton:nth-of-type(2) > button:hover {
    background: rgba(255,255,255,0.12);
    color: #f1f5f9;
}

/* ── Result block ── */
.result-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.2rem 1.5rem;
    background: linear-gradient(90deg, rgba(29,78,216,0.3), rgba(124,58,237,0.3));
    border: 1px solid rgba(124,58,237,0.4);
    border-radius: 12px;
    margin-bottom: 1.25rem;
}
.result-header h3 {
    margin: 0;
    color: #f1f5f9;
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
}
.result-header small {
    color: #94a3b8;
    font-size: 0.82rem;
}

/* ── Grade badge ── */
.grade-badge {
    display: inline-block;
    padding: 0.35rem 1.1rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 1.1rem;
    letter-spacing: 0.5px;
}
.grade-A-plus  { background: rgba(34,197,94,0.2);  color: #4ade80; border: 1px solid rgba(74,222,128,0.4); }
.grade-A       { background: rgba(34,197,94,0.15); color: #86efac; border: 1px solid rgba(134,239,172,0.35); }
.grade-B       { background: rgba(59,130,246,0.2); color: #93c5fd; border: 1px solid rgba(147,197,253,0.4); }
.grade-C       { background: rgba(234,179,8,0.2);  color: #fde047; border: 1px solid rgba(253,224,71,0.4); }
.grade-D       { background: rgba(249,115,22,0.2); color: #fdba74; border: 1px solid rgba(253,186,116,0.4); }
.grade-Fail    { background: rgba(239,68,68,0.2);  color: #fca5a5; border: 1px solid rgba(252,165,165,0.4); }

/* ── Stats row ── */
.stats-row {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
}
.stat-box {
    flex: 1;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    text-align: center;
}
.stat-label {
    color: #64748b;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.stat-value {
    color: #f1f5f9;
    font-size: 1.4rem;
    font-weight: 700;
}

/* ── Table ── */
.stDataFrame {
    border-radius: 10px !important;
    overflow: hidden !important;
}
[data-testid="stDataFrame"] table {
    background: transparent !important;
}
[data-testid="stDataFrame"] th {
    background: rgba(124,58,237,0.25) !important;
    color: #c4b5fd !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
}
[data-testid="stDataFrame"] td {
    color: #e2e8f0 !important;
    background: rgba(255,255,255,0.03) !important;
}

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* ── Success / info messages ── */
.stSuccess, .element-container .stSuccess {
    background: rgba(34,197,94,0.1) !important;
    border: 1px solid rgba(74,222,128,0.3) !important;
    border-radius: 10px !important;
}
.stTextArea textarea {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    color: #cbd5e1 !important;
    font-family: 'DM Sans', monospace !important;
    font-size: 0.85rem !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>🎓 Student Report Card</h1>
    <p>Enter student details below to generate a result summary</p>
</div>
""", unsafe_allow_html=True)


# ── Helper: grade badge HTML ───────────────────────────────────────────────────
def grade_badge(grade: str) -> str:
    css_class = grade.replace("+", "-plus")
    return f'<span class="grade-badge grade-{css_class}">{grade}</span>'


# ── Core logic ─────────────────────────────────────────────────────────────────
def studentresult(student_name, roll_number, marks, subject, save_path):
    try:
        total = sum(marks)
        avg   = total / len(marks)

        if   avg >= 90: grade = "A+"
        elif avg >= 80: grade = "A"
        elif avg >= 70: grade = "B"
        elif avg >= 60: grade = "C"
        elif avg >= 50: grade = "D"
        else:           grade = "Fail"

        df = pd.DataFrame({"Subject": subject, "Marks": marks})
        df.index = range(1, len(df) + 1)
        df.index.name = "Sno"

        # ── Result card ──
        st.markdown(f"""
        <div class="result-header">
            <div>
                <h3>{student_name}</h3>
                <small>Roll No: {roll_number}</small>
            </div>
            <div style="margin-left:auto">{grade_badge(grade)}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="stats-row">'
            f'<div class="stat-box"><div class="stat-label">Total</div><div class="stat-value">{int(total)}<span style="font-size:0.8rem;color:#64748b">/500</span></div></div>'
            f'<div class="stat-box"><div class="stat-label">Average</div><div class="stat-value">{avg:.1f}</div></div>'
            f'<div class="stat-box"><div class="stat-label">Grade</div><div class="stat-value">{grade}</div></div>'
            '</div>', unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True)

        # ── Save to file ──
        if save_path.strip():
            mode = "a" if os.path.exists(save_path.strip()) else "x"
            try:
                with open(save_path.strip(), mode, encoding="utf-8") as f:
                    f.write("=" * 55 + "\n")
                    f.write(f"Student Name : {student_name}\n")
                    f.write(f"Roll Number  : {roll_number}\n")
                    f.write(df.to_string() + "\n")
                    f.write(f"Total        : {int(total)} / 500\n")
                    f.write(f"Average      : {avg:.2f}\n")
                    f.write(f"Grade        : {grade}\n\n")
                st.success("✅ Report saved to `" + save_path.strip() + "`")
            except Exception as e:
                st.warning(f"⚠️ Could not save file: {e}")

    except Exception as ex:
        st.error(f"❌ Please enter valid details.\n\n`{ex}`")


# ── Form ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">Student Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    student_name = st.text_input("Student Name", placeholder="e.g. Priya Sharma")
with col2:
    roll_number  = st.text_input("Roll Number",  placeholder="e.g. 2024CS042")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">Subject Marks  <span style="color:#475569;font-weight:400;text-transform:none;letter-spacing:0">(out of 100)</span></div>', unsafe_allow_html=True)
subjects = ["English", "Maths", "Computer Science", "Physics", "Chemistry"]
cols     = st.columns(len(subjects))
marks    = []
for col, sub in zip(cols, subjects):
    with col:
        m = st.number_input(sub, min_value=0.0, max_value=100.0, value=0.0, key=f"mark_{sub}", step=1.0)
        marks.append(m)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">Save Location (optional)</div>', unsafe_allow_html=True)
save_path = st.text_input(
    "File path for report_card.txt",
    value="report_card.txt",
    placeholder=r"e.g. C:\Users\YourName\Documents\report_card.txt",
    label_visibility="collapsed",
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

btn1, btn2 = st.columns(2)
with btn1:
    if st.button("Generate Result 🎯"):
        if not student_name.strip() or not roll_number.strip():
            st.warning("⚠️ Please fill in the student name and roll number.")
        else:
            studentresult(student_name, roll_number, marks, subjects, save_path)

with btn2:
    if st.button("View Saved Report 📋"):
        path = save_path.strip()
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            st.text_area("📄 Report Card File", content, height=350)
        else:
            st.info("ℹ️ No saved report found at the specified path.")

from fpdf import FPDF
from io import BytesIO

def sanitize_text(text):
    """Remove unsupported characters for Latin-1 encoding (used by FPDF)."""
    return text.encode("latin-1", errors="ignore").decode("latin-1")

def generate_task_pdf(parsed_data: dict, output_stream: BytesIO):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, sanitize_text("🧠 TaskUnpacker Report"), ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, sanitize_text(f"🎯 Goal: {parsed_data.get('goal_summary', 'N/A')}"), ln=1)
    pdf.ln(5)

    for category in parsed_data.get("categories", []):
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, sanitize_text(f"📂 {category['name']}"), ln=1)
        pdf.ln(1)

        for task in category.get("tasks", []):
            pdf.set_font("Arial", "B", 12)
            pdf.multi_cell(0, 10, sanitize_text(f"✅ Task: {task['task']}"))

            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, sanitize_text(f"Effort: {task['effort']} | Impact: {task['impact']}"))

            if task.get("depends_on"):
                depends = ", ".join(task["depends_on"])
                pdf.multi_cell(0, 8, sanitize_text(f"🔗 Depends on: {depends}"))

            if task.get("why_suggested"):
                pdf.multi_cell(0, 8, sanitize_text(f"💡 Why: {task['why_suggested']}"))

            pdf.ln(5)
        pdf.ln(10)

    # Export PDF to memory using `dest="S"` (returns string)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    output_stream.write(pdf_bytes)

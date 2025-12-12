from fpdf import FPDF

pdf = FPDF(orientation='Portrait', unit='mm', format='A4')

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, txt="Hello World!", ln=1, align="Center", border=1)
pdf.output("output.pdf")

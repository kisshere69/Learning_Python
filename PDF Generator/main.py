from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='Portrait', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=12, style="B")
    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align="L", border=0)
    pdf.line(10, 20, 200, 20)
pdf.output("output.pdf")
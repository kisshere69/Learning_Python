from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='Portrait', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() # Add a page for each topic
    pdf.set_font("Arial", size=12, style="B") # Set Arial Bold font for topic title
    pdf.set_text_color(0, 0, 255) # Set blue text color
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align="L", border=0, ) #Add the topic title
    pdf.line(10, 20, 200, 20) # Add a line under the topic title

pdf.output("output.pdf")
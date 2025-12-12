#---Importing libraries---
from fpdf import FPDF
import pandas as pd

#---Settings of the PDF---
pdf = FPDF(orientation='Portrait', unit='mm', format='A4')

df = pd.read_csv("topics.csv")

#---Creating a loop to populate pages with a content---
for index, row in df.iterrows():

    #---Adding pages---
    pdf.add_page()

    #---Styling---
    pdf.set_font("Arial", size=12, style="B") #Font settings
    pdf.set_text_color(0, 0, 255) #Text color
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align="L", border=0) #Topic
    pdf.line(10, 20, 200, 20) #Underline

    for i in range(row["Pages"] - 1):
        pdf.add_page()

#---Creating or overwriting the .pdf file---
pdf.output("output.pdf")
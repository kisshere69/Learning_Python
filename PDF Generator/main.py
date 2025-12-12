#---Importing libraries---
from fpdf import FPDF
import pandas as pd

#---Settings of the PDF---
pdf = FPDF(orientation='Portrait', unit='mm', format='A4')
pdf.set_auto_page_break(auto = False, margin = 0)

df = pd.read_csv("topics.csv")

#---Creating a loop to populate pages with a content---
for index, row in df.iterrows():

    #---Adding pages---
    pdf.add_page()

    #---Header styling for the main page---
    pdf.set_font("Arial", size=12, style="B") #Font settings
    pdf.set_text_color(0, 0, 255) #Text color
    pdf.cell(0, 10, txt=row["Topic"], ln=1, align="L", border=0)
    pdf.line(10, 20, 200, 20) #Underline

    #---Footer styling for the main page---
    pdf.ln(265)
    pdf.set_font("Arial", size=12, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=row["Topic"], align="R")

    #---Adding more pages and subtracting a 1 excessive page---
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #---Footer styling for other pages---
        pdf.ln(275)
        pdf.set_font("Arial", size=12, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row["Topic"], align="R")

#---Creating or overwriting the .pdf file---
pdf.output("output.pdf")

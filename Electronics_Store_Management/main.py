from fpdf import FPDF
import pandas

df = pandas.read_csv("articles.csv", dtype={"id":str})

class Article:

    """
    Create a new Article
    """

    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    """
    Decrease the stock by 1
    """

    def purchase(self):
        df.loc[df["id"] == self.id, "in stock"] -= 1
        df.to_csv("articles.csv", index = False)

    """
    Check if the article is available
    """

    def available(self):
        availability = df.loc[df["id"] == self.id, "in stock"].squeeze()
        if availability > 0:
            return True
        else:
            return False

class Receipt:

    """
    Create a new Receipt
    """

    def __init__(self, article):
        self.article = article

    """
    Generate a receipt
    """

    def generate_pdf(self):

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt No.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")

print("""
Welcome to the Electronics Store! Below is a list of our available articles:
"""'\n', df)

user_choice = input("\nEnter the article id you want to purchase: ")
article = Article(article_id = user_choice)


if article.available():
    receipt = Receipt(article)
    receipt.generate_pdf()
    article.purchase()
else:
    print("Sorry, the article that you've selected is currently not available.")
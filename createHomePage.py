from findTemperatureLive import findTemperatureLive
from sentence import sentence


def htmlDocType():
        return "<!DOCTYPE html>\n"

def initHTML():
        return "<html>\n"

def endHTML():
        return "</html>\n"

def initHead():
        return "<head>\n"

def endHead():
        return "</head>\n"

def title(content):
        return f"<title>{content}</title>\n"

def initBody():
        return "<body>\n"

def endBody():
        return "</body>\n"

def header1(content):
        return f"<h1>{content}</h1>\n"

def paragraph(content):
        return f"<p>\n{content}\n</p>\n"

def image(source, alt_text):
        return f"<img src=\"{source}\" alt=\"{alt_text}\" \n/>"




def createHomePage(emailuser, profile_pic):
        firstname, lastname = emailuser.split(".")
        file = open(f"{emailuser}.html", "w")
        file.write(htmlDocType())
        file.write(initHTML())
        file.write(initHead())
        file.write(title(f"{firstname}'s Home Page"))
        file.write(endHead())
        file.write(initBody())
        file.write(header1(f"Welcome to {firstname}'s Home Page"))
        file.write(paragraph(f"Hi! I am {firstname}. This is my home page! Here is my picture."))
        file.write(paragraph(f"{sentence()}"))
        file.write(image(profile_pic, f"Picture of a {firstname}"))
        temperature, town = findTemperatureLive('Natick', '01760')
        file.write(paragraph(f"The current temperature in {town} is {temperature} degrees."))
        file.write(endBody())
        file.write(endHTML())

if __name__ == "__main__":
        createHomePage("Stewart.Harvey", "stewface.jpg")
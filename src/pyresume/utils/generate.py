# <script src="https://kit.fontawesome.com/8a4fc1c9ce.js" crossorigin="anonymous"></script>
import dominate
from dominate.tags import *

from weasyprint import HTML
from pathlib import Path


def generate_cv(filename: str, css: str) -> str:
    doc = dominate.document(title="CV test")

    with doc.head:
        link(rel='stylesheet', href=css)
        script(type='text/javascript', src="https://kit.fontawesome.com/8a4fc1c9ce.js", crossorigin="anonymous")

    with doc:
        h1("header 1")
        p("This is some text. Wow.")

        with div(id="aside", cls="section level1"):
            h2("Contact Info")
            p("My contact info")

        print(doc)
    return str(doc)


def generate_resume(filename: str) -> str:
    pass


def generate(filename: str = "details.csv", output: str = "cv.pdf", css: str = 'src/pyresume/css/default.css',
             isCV: bool = True):
    # Go through slightly different generation processes for different document types.
    if isCV:
        doc = generate_cv(filename, css)
    else:
        doc = generate_resume(filename, css)

    dochtml = HTML(string=doc, base_url="")
    Path(output).write_bytes(dochtml.write_pdf())

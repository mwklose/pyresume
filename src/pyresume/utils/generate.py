# <script src="https://kit.fontawesome.com/8a4fc1c9ce.js" crossorigin="anonymous"></script>
import dominate
from dominate.tags import *


def generate_cv(filename: str):
    doc = dominate.document(title="CV test")

    with doc.head:
        link(rel='stylesheet', href='css/default.css')
        script(type='text/javascript', src="https://kit.fontawesome.com/8a4fc1c9ce.js", crossorigin="anonymous")

    with doc:
        h1("header 1")

    print(doc)


def generate_resume(filename: str):
    pass

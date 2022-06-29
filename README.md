# Aquilo Framework
 A Flutter-inspired, web development framework for python.
 
Build beautiful and responsive websites without ever needing to touch HTML, CSS, or JavaScript.
With Aquilo you can build a website entirely in python, and it will be blazing fast. 

You can choose to either host your website any cloud provider that supports WSGI specifications.
Or you can build the HTML and static files for your website
and host them wherever you want.

# Bugs & Roadmap 
- Fix issue with the imports (Aquilo, for now, only runs when I'm using PyCharm)
- Rewrite WSGI implementation (I tried deploying a test site to PythonAnywhere, but it didn't work)
- Add more HTML tags to the parser
- Add styling capabilities for easy customisation
- Make development server watch the project for changes and reload automatically
- Build a UI component library for Aquilo based on Material Design
- Make Aquilo opinionated about the structure of a project
- Create a CLI tool to help with repetitive tasks
- Add indepth documentation in docstrings for all the functions (I've just started learning Godot, and I really that you can find all the info you need about a function right in the docstring)

# Installation
- Clone the repository
- Open in PyCharm and run the `run.py` file in the example folder
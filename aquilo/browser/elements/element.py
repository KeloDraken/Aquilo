class Element:
    def __init__(self, etype: str, text: str, classList: list[str] = None, eid: str = None):
        self.etype = etype
        self.className: str = ""
        self.classList: list[str] = classList
        self.hidden: bool = False
        self.eid: str = eid
        self.innerHTML: str = text
        self.innerText: str = text
        self.tagName: str = etype.upper()
        self.title: str = ""

    def __call__(self, *args, **kwargs):
        self.className = " ".join(self.classList) if self.classList is not None else ""
        return f'<{self.etype} class="{self.className}">{self.innerHTML}</{self.etype}>'


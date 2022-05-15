class Element:
    def __init__(self, etype: str, text: str = None, classList: list[str] = None, eid: str = None):
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
        if self.classList is None:
            return f'<{self.etype}>{self.innerHTML}</{self.etype}>'
        else:
            self.className = " ".join(self.classList)
            return f'<{self.etype} class="{self.className}">{self.innerHTML}</{self.etype}>'

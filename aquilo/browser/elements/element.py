from typing import List


class Element:
    def __init__(self,
                 etype: str,
                 text: str = None,
                 eid: str = None,
                 class_list: List[str] = None):
        self.etype = etype
        self.hidden: bool = False
        self.eid: str = eid
        self.innerHTML: str = text
        self.innerText: str = text
        self.tagName: str = etype.upper()
        self.title: str = ""
        self.class_list: List[str] = class_list

    def __call__(self, *args, **kwargs):
        if self.class_list is not None:
            return f"<{self.etype} class=\"{' '.join(self.class_list)}\">{self.innerHTML}</{self.etype}>"
        return f"<{self.etype}>{self.innerHTML}</{self.etype}>"

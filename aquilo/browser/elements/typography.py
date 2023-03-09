from typing import List

from aquilo.browser.elements import Element


class Text(Element):
    def __init__(
        self,
        etype: str,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(etype, text, eid, class_list)


class h1(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class h2(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class h3(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class h4(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class h5(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class h6(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class p(Text):
    def __init__(
        self,
        text: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)


class a(Text):
    def __init__(
        self,
        text: str,
        href: str,
        eid: str = None,
        class_list: List[str] = None
    ):
        super().__init__(self.__class__.__name__, text, eid, class_list)
        self.href = href

    def __call__(self, *args, **kwargs):
        if self.class_list is not None:
            return f'<{self.etype} href="{self.href}" class=\"{" ".join(self.class_list)}\">{self.innerHTML}</{self.etype}>'
        return f'<{self.etype} href="{self.href}">{self.innerHTML}</{self.etype}>'

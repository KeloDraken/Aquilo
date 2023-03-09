from aquilo.browser.elements.typography import h1


class H1(h1):
    def __init__(
        self,
        text: str
    ):
        super().__init__(
            text,
            class_list=["text-5xl", "mt-16", "mb-0", "font-bold"]
        )

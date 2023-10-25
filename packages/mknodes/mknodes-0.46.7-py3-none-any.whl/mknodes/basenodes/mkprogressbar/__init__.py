from __future__ import annotations

from typing import Any, Literal

from mknodes.basenodes import mknode
from mknodes.utils import log, reprhelpers, resources


logger = log.get_logger(__name__)


class MkProgressBar(mknode.MkNode):
    """Node to display a CSS-based progress bar."""

    REQUIRED_EXTENSIONS = [resources.Extension("pymdownx.progressbar")]
    ICON = "fontawesome/solid/bars-progress"
    CSS = [resources.CSSFile("progressbar.css")]
    ATTR_LIST_SEPARATOR = ""

    def __init__(
        self,
        percentage: int,
        title: str | None | Literal[True] = True,
        style: Literal["thin", "candystripe", "candystripe_animated"] | None = None,
        **kwargs: Any,
    ):
        """Constructor.

        Arguments:
            percentage: Percentage value for the progress bar
            title: Title to display on top of progress bar
            style: Progress bar style
            kwargs: Keyword arguments passed to parent
        """
        super().__init__(**kwargs)
        self.title = title
        self.percentage = percentage
        self.style = style
        match self.style:
            case "thin":
                self.add_css_class("thin")
            case "candystripe":
                self.add_css_class("candystripe")
            case "candystripe_animated":
                self.add_css_class("candystripe")
                self.add_css_class("candystripe-animate")

    def __repr__(self):
        return reprhelpers.get_repr(
            self,
            percentage=self.percentage,
            title=self.title,
            style=self.style,
        )

    def _to_markdown(self) -> str:
        match self.title:
            case str():
                title = self.title.format(percentage=self.percentage)
            case True:
                title = f"{self.percentage}%"
            case _:
                title = ""
        return rf'[={self.percentage}% "{title}"]'

    @classmethod
    def create_example_page(cls, page):
        import mknodes as mk

        node = MkProgressBar(60)
        page += mk.MkReprRawRendered(node, header="### Regular")
        node = MkProgressBar(60, style="thin")
        page += mk.MkReprRawRendered(node, header="### Thin")
        node = MkProgressBar(70, style="candystripe", title="We reached {percentage}!")
        page += mk.MkReprRawRendered(node, header="### Candystripe")
        node = MkProgressBar(80, style="candystripe_animated")
        page += mk.MkReprRawRendered(node, header="### Animated")


if __name__ == "__main__":
    bar = MkProgressBar(percentage=30, title=None)
    print(bar)

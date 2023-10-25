from collections.abc import Iterator
from typing import NamedTuple

from citation_utils import CountedCitation  # type: ignore
from statute_utils import CountedStatute  # type: ignore

from .block import Block, fn_pattern
from .utils import Annex, Footnote


class Segment(NamedTuple):
    id: str
    order: int
    decision_id: str
    opinion_id: str
    material_path: str
    text: str
    footnotes: list[Footnote]
    category: str | None = None

    def __repr__(self) -> str:
        return f"<Segment {self.material_path}: fn {len(self.footnotes)}>"  # noqa: E501

    @property
    def proper(self) -> str:
        from .utils import clear_markdown

        values = []
        for footnote in self.footnotes:
            values.append(footnote.value)
        text = clear_markdown(fn_pattern.sub("", self.text))
        if not values:
            return text
        return text + "\n\n\n\n" + "\n\n".join(values)

    @property
    def as_row(self):
        data = self._asdict()
        data.pop("footnotes")
        data["text"] = self.proper
        data["char_count"] = len(data["text"])
        return data


class Opinion(NamedTuple):
    """Whether the opinion is the main opinion of the decision
    or a separate one, it will contain common fields and associated
    records based on the content.
    """

    id: str
    decision_id: str
    content: str
    justice_id: int | None = None
    is_main: bool = True
    label: str = "Opinion"
    file_statutes: str | None = None
    file_citations: str | None = None

    def __repr__(self) -> str:
        return f"<Opinion {self.id}>"

    @property
    def row(self):
        return {"opinion_id": self.id, "decision_id": self.decision_id}

    @property
    def index(self):
        return Annex.lookup_index(self.content)

    @property
    def body(self) -> str:
        return self.content[: self.index] if self.index else self.content

    @property
    def annex(self) -> str | None:
        return self.content[self.index :] if self.index else None

    @property
    def footnotes(self) -> list[Footnote]:
        return list(Footnote.gather(self.annex)) if self.annex else []

    @property
    def blocks(self) -> list[Block]:
        return list(Block(body=self.body).blocks)

    def get_segments(
        self,
        with_footnotes_only: bool = False,
        only_ruling_chunks: bool = False,
    ) -> Iterator[Segment]:
        """Hierarchical content:

        - `Opinion` - may consist of a body and an Annex
            - `Block` - a body division based on a _natural_ or _artificial_ header
                - `Chunk` - a formula-based division of a block (e.g. include blockquotes)
                    - `Passage` - a chunk divided into "sentences which end in footnotes"

        Construction of a `Segment`
        - The `Annex` contains a list of `Footnote`s.
        - Each `Passage` will contain a footnote reference.
        - A segment consists of a passage and a list of sliced footnotes relevant to the passage.
        - This makes it possible to match passages with their referenced footnotes.

        Args:
            with_footnotes_only (bool, optional): If True, will only gather passages with footnotes detected. Defaults to False.
            only_ruling_chunks (bool, optional): If True, will only gather passages part of the ruling block. Defaults to False.

        Yields:
            Iterator[Segment]: Gathered segments found in the body, matched with their footnotes.
        """  # noqa: E501
        counter = 1
        for block in self.blocks:
            for chunk in block.chunks:
                if only_ruling_chunks and chunk.category != "ruling":
                    continue

                for passage in chunk.passages:
                    if with_footnotes_only and not passage.footnotes:
                        continue

                    yield Segment(
                        id=f"{self.id}-{passage.material_path}",
                        decision_id=self.decision_id,
                        opinion_id=self.id,
                        material_path=passage.material_path,
                        text=passage.text,
                        footnotes=passage.get_footnotes(sourcenotes=self.footnotes),
                        category=chunk.category,
                        order=counter,
                    )
                    counter += 1

    @property
    def segments_list(self) -> list[Segment]:
        return list(self.get_segments(only_ruling_chunks=True)) or list(
            self.get_segments()
        )

    @property
    def segments(self) -> list[dict]:
        """Will be used as part of a decision's collection."""
        return [seg.as_row for seg in self.segments_list if seg.as_row["char_count"]]

    @property
    def headings(self) -> list[dict]:
        """Will be used as part of a decision's collection."""
        res = []
        for blk in self.blocks:
            if blk.title:
                data = {}
                data["id"] = f"{self.id}-{blk.material_path}"
                data |= blk._asdict()
                data |= self.row
                data["category"] = data.pop("inherited_category")
                data.pop("body")
                res.append(data)
        return res

    @property
    def statutes(self) -> list[dict]:
        """Will be used as part of a decision's collection."""
        res = []
        if self.file_statutes:
            objs = CountedStatute.from_repr_format(self.file_statutes.split("; "))
            for obj in objs:
                data = {"cat": obj.cat, "num": obj.num, "mentions": obj.mentions}
                data |= self.row
                res.append(data)
        return res

    @property
    def citations(self) -> list[dict]:
        """Will be used as part of a decision's collection."""
        res = []
        if self.file_citations:
            objs = CountedCitation.from_repr_format(self.file_citations.split("; "))
            for obj in objs:
                data = obj.model_dump()
                data |= self.row
                res.append(data)
        return res

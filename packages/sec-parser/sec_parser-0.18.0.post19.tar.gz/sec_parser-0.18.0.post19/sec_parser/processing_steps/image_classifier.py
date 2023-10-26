from __future__ import annotations

from typing import TYPE_CHECKING

from sec_parser.processing_steps.abstract_elementwise_processing_step import (
    AbstractElementwiseProcessingStep,
    ElementwiseProcessingContext,
)
from sec_parser.semantic_elements.semantic_elements import ImageElement

if TYPE_CHECKING:  # pragma: no cover
    from sec_parser.semantic_elements.abstract_semantic_element import (
        AbstractSemanticElement,
    )


class ImageClassifier(AbstractElementwiseProcessingStep):
    """
    ImageClassifier class for converting elements into ImageElement instances.

    This step scans through a list of semantic elements and changes it,
    primarily by replacing suitable candidates with ImageElement instances.
    """

    def _process_element(
        self,
        element: AbstractSemanticElement,
        _: ElementwiseProcessingContext,
    ) -> AbstractSemanticElement:
        is_unary = element.html_tag.is_unary_tree()
        contains_image = element.html_tag.contains_tag("img", include_self=True)
        if is_unary and contains_image:
            return ImageElement.create_from_element(element)

        return element

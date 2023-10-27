from __future__ import annotations

from typing import Any, Dict, List, Union

from nextpy.constants import EventTriggers
from nextpy.components.component import Component, NoSSRComponent
from nextpy.core.vars import Var


class FramerMotion(Component):
    """A component that wraps all the framer motion components."""

    library = "framer-motion"

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_CLICK: lambda: [],
            EventTriggers.ON_MOUSE_ENTER: lambda: [],
            EventTriggers.ON_MOUSE_MOVE: lambda: [],
            EventTriggers.ON_MOUSE_LEAVE: lambda: [],
        }

#The class that defines all the class attributes
class MotionAttributes:
    animate: Var[Any]
    initial: Var[Any]
    transformTemplate: Var[str]
    exit: Var[Dict[str, Any]]
    transition: Var[Dict[str, Any]]
    variant: Var[Dict[Any, Any]]
    layout: Var[Any]
    layoutId: Var[str]
    layoutDependency: Var[Any]
    layoutScroll: Var[bool]
    inherit: Var[bool]
    whileHover: Var[Dict[str, Any]]
    whileTap: Var[Dict[str, Any]]
    whileFocus: Var[Dict[str, Any]]
    drag: Var[bool | str]
    whileDrag: Var[Any]
    dragConstraints: Var[Any]
    dragSnapToOrigin: Var[bool]
    dragElastic: Var[int]
    dragMomentum: Var[bool]
    dragTransition: Var[Dict[str, Any]]
    dragPropagation: Var[bool]
    dragControls: Var[Any]
    dragListener: Var[bool]
    whileInView: Var[Any]

#The base class that inherits the FramerMotion class
class MotionBase(FramerMotion):
    """A component that wraps Framer Motion"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = None
        self.is_default = False
        self.motion_attributes = MotionAttributes()

    # rest of the properties...

    # rest of the code...


# The classes that inherits the MotionBase class and each of these classes denote a html element used with "motion." suffix to use as a motion component
class MotionA(MotionBase):
    """A framer motion component that wraps motion.a element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.a"

class MotionArticle(MotionBase):
    """A framer motion component that wraps motion.Article element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.article"

class MotionAside(MotionBase):
    """A framer motion component that wraps motion.aside element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.aside"

class MotionButton(MotionBase):
    """A framer motion component that wraps motion.button element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.button"

class MotionDiv(MotionBase):
    """A framer motion component that wraps motion.div element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.div"

class MotionFieldset(MotionBase):
    """A framer motion component that wraps motion.fieldset element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.fieldset"

class MotionFooter(MotionBase):
    """A framer motion component that wraps motion.footer element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.footer"

class MotionForm(MotionBase):
    """A framer motion component that wraps motion.form element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.form"

class MotionH1(MotionBase):
    """A framer motion component that wraps motion.h1 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h1"

class MotionH2(MotionBase):
    """A framer motion component that wraps motion.h2 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h2"

class MotionH3(MotionBase):
    """A framer motion component that wraps motion.h3 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h3"

class MotionH4(MotionBase):
    """A framer motion component that wraps motion.h4 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h4"

class MotionH5(MotionBase):
    """A framer motion component that wraps motion.h5 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h5"

class MotionH6(MotionBase):
    """A framer motion component that wraps motion.h6 element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h6"

class MotionHeader(MotionBase):
    """A framer motion component that wraps motion.header element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.header"

class MotionImg(MotionBase): 
    """A framer motion component that wraps motion.img element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.img"


class MotionInput(MotionBase):
    """A framer motion component that wraps motion.input element"""
    tag = "motion.input"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.h6"
    
    @property
    def animate(self):
        return {"x": self.x, "y": self.y, "z": self.z}
        
class MotionLabel(MotionBase):
    """A framer motion component that wraps motion.label element"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.label"

class MotionLi(MotionBase):
    """A framer motion component that wraps motion.li element"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.li"

class MotionMain(MotionBase):
    """A framer motion component that wraps motion.main element"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.main"

class MotionNav(MotionBase):
    """A framer motion component that wraps motion.nav element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.nav"

class MotionOl(MotionBase):
    """A framer motion component that wraps motion.ol element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.ol"

class MotionOption(MotionBase):
    """A framer motion component that wraps motion.option element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.option"

class MotionP(MotionBase):
    """A framer motion component that wraps motion.p element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.p"

class MotionSection(MotionBase):
    """A framer motion component that wraps motion.section element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.section"

class MotionSelect(MotionBase):
    """A framer motion component that wraps motion.select element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.select"

class MotionSpan(MotionBase):
    """A framer motion component that wraps motion.span element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.span"

class MotionTable(MotionBase):
    """A framer motion component that wraps motion.table element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.table"

class MotionTd(MotionBase):
    """A framer motion component that wraps motion.td element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.td"

class MotionTextArea(MotionBase):
    """A framer motion component that wraps motion.textarea element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.textarea"

class MotionTh(MotionBase):
    """A framer motion component that wraps motion.th element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.th"

class MotionTr(MotionBase):
    """A framer motion component that wraps motion.tr element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.tr"

class MotionUl(MotionBase):
    """A framer motion component that wraps motion.ul element"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag = "motion.ul"


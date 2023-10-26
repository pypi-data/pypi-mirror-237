"""
The basic sprite ("DesignerObject") and subclass sprites (image, circle, rectangle, text, various widgest, etc.).
"""

from designer.objects.designer_object import DesignerObject
from designer.objects.arc import arc
from designer.objects.circle import circle
from designer.objects.ellipse import ellipse
from designer.objects.group import group
from designer.objects.image import image
from designer.objects.line import line
from designer.objects.rectangle import rectangle
from designer.objects.shape import shape, lines
from designer.objects.text import text, get_text, set_text
from designer.objects.emoji import emoji, get_emoji_name, set_emoji_name
from designer.objects.pen import pen
from designer.objects.pixels import get_pixels, get_pixels2d

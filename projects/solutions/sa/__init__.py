"""
Gentle Hands-On Introduction to Python: course project
"""

import sys

if not "-m" in sys.argv:
    from .distance import align, edit_distance, needleman_wunsch
    from .assemble import assemble, score

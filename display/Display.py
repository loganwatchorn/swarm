from space import Vector

from .DisplayVariant import DisplayVariant
from .StandardDisplay import StandardDisplay
from .ScannerDisplay import ScannerDisplay

class Display:
    def __new__(cls, variant, debug):
        if variant == DisplayVariant.scanners:
            display_class = ScannerDisplay
        else:
            display_class = StandardDisplay

        display = super().__new__(display_class)
        display.debug = debug
        return display

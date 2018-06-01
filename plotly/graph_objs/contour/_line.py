from plotly.basedatatypes import BaseTraceHierarchyType


class Line(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the contour level. Has no effect if
        `contours.coloring` is set to *lines*.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # dash
    # ----
    @property
    def dash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
        *longdashdot*) or a dash length list in px (eg
        *5px,10px,2px,2px*).
    
        The 'dash' property is a string and must be specified as:
          - One of the following strings:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot',
                'longdashdot']
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['dash']

    @dash.setter
    def dash(self, val):
        self['dash'] = val

    # smoothing
    # ---------
    @property
    def smoothing(self):
        """
        Sets the amount of smoothing for the contour lines, where *0*
        corresponds to no smoothing.
    
        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self['smoothing']

    @smoothing.setter
    def smoothing(self, val):
        self['smoothing'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the line width (in px).
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'contour'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the contour level. Has no effect if
            `contours.coloring` is set to *lines*.
        dash
            Sets the dash style of lines. Set to a dash type string
            (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
            *longdashdot*) or a dash length list in px (eg
            *5px,10px,2px,2px*).
        smoothing
            Sets the amount of smoothing for the contour lines,
            where *0* corresponds to no smoothing.
        width
            Sets the line width (in px).
        """

    def __init__(
        self, color=None, dash=None, smoothing=None, width=None, **kwargs
    ):
        """
        Construct a new Line object
        
        Parameters
        ----------
        color
            Sets the color of the contour level. Has no effect if
            `contours.coloring` is set to *lines*.
        dash
            Sets the dash style of lines. Set to a dash type string
            (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
            *longdashdot*) or a dash length list in px (eg
            *5px,10px,2px,2px*).
        smoothing
            Sets the amount of smoothing for the contour lines,
            where *0* corresponds to no smoothing.
        width
            Sets the line width (in px).

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

        # Import validators
        # -----------------
        from plotly.validators.contour import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_line.ColorValidator()
        self._validators['dash'] = v_line.DashValidator()
        self._validators['smoothing'] = v_line.SmoothingValidator()
        self._validators['width'] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.dash = dash
        self.smoothing = smoothing
        self.width = width

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
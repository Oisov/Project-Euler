(TeX-add-style-hook
 "piechart"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "datapie"
    "xcolor"))
 :latex)


(TeX-add-style-hook
 "standalonefile"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8")))
   (TeX-run-style-hooks
    "latex2e"
    "test"
    "standalone"
    "standalone10"
    "inputenc"
    "pgfplots"
    "tikz"))
 :latex)


(TeX-add-style-hook
 "ProjectEuler"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "english") ("xcolor" "dvpipsnames*" "svgnames") ("mdframed" "framemethod=TikZ") ("cleveref" "nameinlink") ("natbib" "numbers")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "fontenc"
    "lmodern"
    "inputenc"
    "babel"
    "booktabs"
    "csquotes"
    "mathtools"
    "amsfonts"
    "amssymb"
    "amsthm"
    "subcaption"
    "caption"
    "siunitx"
    "textcomp"
    "xcolor"
    "tikz"
    "mdframed"
    "listings"
    "geometry"
    "hyperref"
    "cleveref"
    "natbib"
    "chapterbib"
    "multicol")
   (TeX-add-symbols
    "link")
   (LaTeX-add-labels
    "PE-#2")
   (LaTeX-add-environments
    '("ProjectEuler" LaTeX-env-args ["argument"] 1)
    "lemma"
    "proposition"
    "definition"))
 :latex)


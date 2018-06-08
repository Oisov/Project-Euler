(TeX-add-style-hook
 "ProjectEuler"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "english") ("xcolor" "dvpipsnames*" "svgnames") ("mdframed" "framemethod=TikZ") ("cleveref" "nameinlink") ("natbib" "numbers")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "frontpage"
    "preface"
    "Problems/PE-002"
    "Problems/PE-014"
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
    "chngcntr"
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
    '("ProjectEuler" LaTeX-env-args ["argument"] 1))
   (LaTeX-add-amsthm-newtheorems
    "lemma"
    "proposition"
    "definition")
   (LaTeX-add-caption-DeclareCaptions
    '("\\DeclareCaptionFormat{listing}" "Format" "listing")))
 :latex)


(TeX-add-style-hook
 "Project-Euler"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "english") ("xcolor" "dvipsnames*" "		svgnames") ("mdframed" "framemethod=TikZ") ("cleveref" "nameinlink") ("natbib" "numbers")))
   (add-to-list 'LaTeX-verbatim-environments-local "pythoncode*")
   (add-to-list 'LaTeX-verbatim-environments-local "pythoncode")
   (add-to-list 'LaTeX-verbatim-environments-local "minted")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "Preface"
    "1-100/Project-Euler-001"
    "1-100/Project-Euler-002"
    "1-100/Project-Euler-003"
    "1-100/Project-Euler-004"
    "1-100/Project-Euler-005"
    "1-100/Project-Euler-006"
    "1-100/Project-Euler-007"
    "1-100/Project-Euler-008"
    "1-100/Project-Euler-009"
    "1-100/Project-Euler-010"
    "1-100/Project-Euler-013"
    "article"
    "art10"
    "fontenc"
    "lmodern"
    "inputenc"
    "babel"
    "lipsum"
    "booktabs"
    "csquotes"
    "amsmath"
    "amsfonts"
    "amssymb"
    "amsthm"
    "imakeidx"
    "xcolor"
    "graphicx"
    "tikz"
    "caption"
    "subcaption"
    "fullpage"
    "siunitx"
    "textcomp"
    "minted"
    "mdframed"
    "hyperref"
    "cleveref"
    "natbib"
    "chapterbib"
    "multicol")
   (TeX-add-symbols
    "lcm"
    "kortlinje"
    "link"
    "figureautorefname"
    "tableautorefname"
    "equationautorefname")
   (LaTeX-add-labels
    "PE-#2")
   (LaTeX-add-environments
    '("pythoncode*" LaTeX-env-args (TeX-arg-key-val LaTeX-minted-key-val-options-local))
    '("pythoncode")
    '("ProjectEuler" LaTeX-env-args ["argument"] 1))
   (LaTeX-add-amsthm-newtheorems
    "lemma"
    "proposition"
    "definition"))
 :latex)


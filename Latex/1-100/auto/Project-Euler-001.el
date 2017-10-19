(TeX-add-style-hook
 "Project-Euler-001"
 (lambda ()
   (LaTeX-add-labels
    "fig:PE1-venn-2"
    "fig:PE1-venn-3")
   (LaTeX-add-environments
    '("ProjectEuler" LaTeX-env-args ["argument"] 1)))
 :latex)


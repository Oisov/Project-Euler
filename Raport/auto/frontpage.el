(TeX-add-style-hook
 "frontpage"
 (lambda ()
   (LaTeX-add-environments
    '("ProjectEuler" LaTeX-env-args ["argument"] 1)))
 :latex)


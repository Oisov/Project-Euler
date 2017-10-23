(TeX-add-style-hook
 "PE-002"
 (lambda ()
   (LaTeX-add-environments
    '("ProjectEuler" LaTeX-env-args ["argument"] 1)))
 :latex)


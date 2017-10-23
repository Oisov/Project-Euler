(TeX-add-style-hook
 "preface"
 (lambda ()
   (LaTeX-add-environments
    '("ProjectEuler" LaTeX-env-args ["argument"] 1)))
 :latex)


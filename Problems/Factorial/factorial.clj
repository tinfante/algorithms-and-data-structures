(ns factorial)


(defn factorial
  "Typical recursive solution, causes stackoverflow. Notice *' for BigInteger."
  [n]
  (if (= n 0) 
    1
    (*' n (factorial (- n 1)))
    )
  )

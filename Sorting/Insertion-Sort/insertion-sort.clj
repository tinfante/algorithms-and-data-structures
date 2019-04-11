(ns insertion-sort
  (:gen-class)
  )


(defn insert
  [elem result]
  (if (empty? result)
    (list elem)
    (if (< elem (last result))
      (concat (insert elem (butlast result)) (list (last result)))
      (concat result (list elem))
    )))


(defn insertion-sort
  ([-seq]
   (if (< (count -seq) 2)
     -seq
     (insertion-sort (rest -seq) (list (first -seq)))
     ))
  ([-seq result]
   (if (empty? -seq)
     result
     (recur (rest -seq) (insert (first -seq) result))
     )))

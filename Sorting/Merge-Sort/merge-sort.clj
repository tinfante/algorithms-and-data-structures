(ns merge-sort
  (:gen-class)
  )


(defn -merge [seq1 seq2]
  (loop [s1 seq1
         s2 seq2
         merged []]
    (if (or (empty? s1) (empty? s2))
      (concat merged (or (seq s1) (seq s2)))
      (if (< (first s1) (first s2))
        (recur (rest s1) s2 (conj merged (first s1)))
        (recur s1 (rest s2) (conj merged (first s2)))
        ))))


(defn merge-sort [seqnc]
  (if (< (count seqnc) 2)
    seqnc
    (let [middle (int (/ (count seqnc) 2))
          [left right] (split-at middle seqnc)]
      (-merge (merge-sort left) (merge-sort right))
      )))

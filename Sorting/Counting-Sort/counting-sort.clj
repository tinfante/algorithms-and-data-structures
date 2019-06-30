(ns counting-sort)


(defn counting-sort-1 [a mn mx]
  (let [freqs (frequencies a)]
    (apply concat (for [j (range mn (inc mx))
                        :when (contains? freqs j)
                        ]
                    (repeat (get freqs j) j)
                    ))))


(defn counting-sort-2 [a mn mx]
  (let [c (frequencies a)
        f #(if (contains? c %2)
             (apply conj %1 (repeat (get c %2) %2))
             %1
             )]
    (reduce f [] (range mn (inc mx)))
    ))

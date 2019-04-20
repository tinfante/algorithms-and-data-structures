(ns priority-queue
    (:gen-class)
    )


(defn swap [v i1 i2]
  "Given two indexes, swaps the elements in a vector."
  (assoc v i2 (v i1) i1 (v i2)))


(defn choose-min-node [v i]
  "Given a vector and an index (1-based), where the index is a parent node in
  a heap, returns the index of either the parent node, its left child or right
  child, whichever has the largest value. Since indexing logic is 1-based
  the vector's first element (which should be nil) is ignored."
  (reduce #(if (>= %2 (count v))
             %1
             (if (<= (v %1) (v %2)) %1 %2)
             )
          [i (* i 2) (inc (* i 2))]
          ))


(defn min-heapify [v i]
  (let [min-node (choose-min-node v i)]
    (if (= min-node i)
      v
      (min-heapify (swap v min-node i) min-node)
      )))


(defn build-min-heap [v]
  (loop [i (int (/ (dec (count v)) 2))
         h v]
    (if (< i 1)
      h
      (recur (dec i) (min-heapify h i))
      )))

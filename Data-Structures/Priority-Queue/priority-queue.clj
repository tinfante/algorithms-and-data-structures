(ns priority-queue
    (:gen-class))


(defn swap-nodes [v i1 i2]
  "Given a vector and two indexes, swaps the elements at those indexes."
  (assoc v i2 (v i1) i1 (v i2)))


(defn choose-node [v i f]
  "Given a vector, an index (1-based), where the index is a parent node in
  a heap, and a comparison function, returns the index of either the parent
  node, its left child or right child. Whichever has the largest/smallest
  value according to the comparison function. Since indexing logic is 1-based
  the vector's first element (which should be nil) is ignored."
  (reduce #(if (>= %2 (count v))
             %1
             (if (f (v %1) (v %2)) %1 %2)
             )
          [i (* i 2) (inc (* i 2))]
          ))


(defn heapify [v i f]
  "Given a vector and an index, swaps node at index i with its left or
  right child node if either of them is considered larger/smaller by
  choose-node function. This function also needs to receive the comparison
  function, which is passed on to choose-node."
  (let [chosen-one (choose-node v i f)]
    (if (= chosen-one i)
      v
      (recur (swap-nodes v chosen-one i) chosen-one f)
      )))


(defn build-heap [v & r]
  "Given an unordered vector, creates a heap. By default it creates a min
  heap, but another comparison function can be passed as an optional second
  argument. e.g. >= to make a max heap or a function to deal with a data type
  other than int."
  (let [f (if (nil? r) <= (first r))]
    (loop [i (int (/ (dec (count v)) 2))
           h v]
      (if (< i 1)
        h
        (recur (dec i) (heapify h i f))
        ))))


(defn enqueue [e v & r]
  "Given an element e and a vector v, removes the first item from the vector
  and then prepends [nil e] to the vector. Due to the 1-based indexing logic
  the first item of the vector should be nil, so this is equivalent to
  prepending e to the heap vector representation (but it actually inserts e
  at index 1 of v). It then runs heapify function to guarantee that the heap
  property is maintained after insertion. A third optional argument is the
  comparison function (the default is <=) used by the heapify function."
  (let [f (if (nil? r) <= (first r))]
    (heapify (into [nil e] (rest v)) 1 f)
    ))


(defn dequeue [v & r]
  "Given a vector removes its first two elements, the first of which should be
  nil and the second the heap's first element. It then preprends nil back into
  the vector and calls heapify on it. Like build-heap and enqueue functions,
  accepts a comparison function as a second optional argument. Returns a list
  with the item that was removed from the heap/priority queue and the modified
  heap/vector."
  (let [f (if (nil? r) <= (first r))]
    (list (v 1)  (heapify (into [nil] (subvec v 2)) 1 f))
    ))

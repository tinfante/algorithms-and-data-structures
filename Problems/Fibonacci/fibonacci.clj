(ns fibonacci)


(defn fib [n]
  "Basic recursive solution. Causes stack overflow."
  (if (< n 2)
    n
    (+ (fib (dec n)) (fib (- n 2)))
    ))


;Same as above but memoized.
(def fib-memo
  (memoize fib))


(defn fib-tail-1 [n]
  "Tail-recursive solution. No stack overflow."
  (if (< n 2)
    n
    (loop [x 1 f 0 s 1]
      (if (< x n)
        (recur (inc x) s (+' f s))
        s
        ))))


(defn fib-tail-2
  "Another tail-recursive solution using a multi-arity function."
  ([n]
   (if (< n 2)
     n
     (fib-tail-2 n 1 0 1))
   )
  ([n r f s]  ; r=num recursions, f=first value, s=second value
   (if (< r n)
     (recur n (inc r) s (+' f s))
     s
     )))

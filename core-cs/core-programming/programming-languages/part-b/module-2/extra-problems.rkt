#lang racket

; Problem 1: Binary Trees

(struct btree-leaf () #:transparent)
(struct btree-node (value left right) #:transparent)

(define (tree-height tree)
  (cond
    [(btree-leaf? tree) 0]
    [(btree-node? tree)
     (+ 1 (max (tree-height (btree-node-left tree))
               (tree-height (btree-node-right tree))))]))


(define (sum-tree tree)
  (cond
    [(btree-leaf? tree) 0]
    [(btree-node? tree)
     (+ (btree-node-value tree)
        (sum-tree (btree-node-left tree))
        (sum-tree (btree-node-right tree)))]))


(define (prune-at-v tree v)
  (cond
    [(btree-leaf? tree) tree]
    [(btree-node? tree)
     (if (equal? (btree-node-value tree) v)
         (btree-leaf)
         (btree-node (btree-node-value tree)
                     (prune-at-v (btree-node-left tree) v)
                     (prune-at-v (btree-node-right tree) v)))]))


(define (well-formed-tree? tree)
  (cond
    [(btree-leaf? tree) #t]
    [(btree-node? tree)
     (and (number? (btree-node-value tree))
          (well-formed-tree? (btree-node-left tree))
          (well-formed-tree? (btree-node-right tree)))]))


(define (fold-tree f acc tree)
  (cond
    [(btree-leaf? tree) acc]
    [(btree-node? tree)
     (fold-tree f
                (f (btree-node-value tree)
                   (fold-tree f acc (btree-node-left tree)))
                (btree-node-right tree))]))


(define (fold-tree-c f)
  (lambda (acc tree)
    (cond
      [(btree-leaf? tree) acc]
      [(btree-node? tree)
       (fold-tree-c f
                    (f (btree-node-value tree)
                       (fold-tree-c f acc (btree-node-left tree)))
                    (btree-node-right tree))])))


; Problem 2: Crazy Sum

(define (crazy-sum lst)
  (let loop ((lst lst)
             (op '+)
             (result 0))
    (cond
      [(null? lst) result]
      [(procedure? (car lst))
       (loop (cdr lst) (car lst) result)]
      [else
       (loop (cdr lst) op (op result (car lst)))])))


; Problem 3: Either Fold

(define (either-fold f acc lst-or-tree)
  (cond
    [(list? lst-or-tree)
     (foldl f acc lst-or-tree)]
    [(or (btree-leaf? lst-or-tree) (btree-node? lst-or-tree))
     (fold-tree f acc lst-or-tree)]
    [else
     (error "Invalid input, not a list or binary tree")]))

; Problem 4: Flatten

(define (flatten lst)
  (cond
    [(null? lst) '()]
    [(list? (car lst))
     (append (flatten (car lst)) (flatten (cdr lst)))]
    [else
     (cons (car lst) (flatten (cdr lst)))]))


; Problem 5: Remove Lets and Pairs

(define (remove-lets expr)
  (cond
    [(pair? expr)
     (case (car expr)
       [(mlet) (remove-lets (call (fun #f (list (cadr expr) (caddr expr))) (cadddr expr)))]
       [(apair) (remove-lets (fun #f "_f" (call (call (var "_f") (cadr expr)) (caddr expr))))])
    [(list? expr) (map remove-lets expr)]
    [else expr]])) ; Use #t instead of else


; Problem 6: MUPL Functions

(define mupl-all
  (fun #f "lst"
       (ifgreater (var "lst")
                  (int 0)
                  (int 1)
                  (ifgreater (call (var "lst") (int 0))
                             (int 0)
                             (int 1)
                             (call-curried (var "mupl-all")
                                           (list (call (var "lst") (int 0))
                                                 (call (var "lst") (int 1))))))))


(define mupl-append
  (fun #f "lst1"
       (fun #f "lst2"
            (call-curried (var "mupl-list") (list (call (var "lst1") (int 0))
                                                   (call (var "lst2") (int 0)))))))


(define mupl-zip
  (fun #f "lst1"
       (fun #f "lst2"
            (ifgreater (var "lst1")
                       (int 0)
                       (int 1)
                       (ifgreater (var "lst2")
                                  (int 0)
                                  (int 1)
                                  (call-curried (var "mupl-list")
                                                (list (call (var "mupl-pair") (int 0) (int 0))
                                                      (call (var "mupl-zip") (call (var "lst1") (int 1)) (call (var "lst2") (int 1))))))))))


(define mupl-curry
  (fun #f "f"
       (fun #f "x"
            (fun #f "y"
                 (call (var "f") (call (var "mupl-pair") (var "x") (var "y")))))))


(define mupl-uncurry
  (fun #f "f"
       (fun #f "p"
            (call (var "f") (fst (var "p")) (snd (var "p"))))))


; Problem 7: MUPL Macros

(define-syntax if-greater3
  (syntax-rules ()
    [(if-greater3 a b c d e)
     (ifgreater a b
                (ifgreater b c
                           d
                           e)
                e)]))

(define-syntax call-curried
  (syntax-rules ()
    [(call-curried f args)
     (foldl (lambda (arg acc) (call acc arg)) f args)]))


; Example usage
(define lst1 (list 1 2 3 4 5))
(define lst2 (list 6 7 8 9 10))
(define tree (btree-node 4 (btree-node 5 (btree-leaf) (btree-leaf)) (btree-leaf)))

(displayln (tree-height tree)) ; Output: 2
(displayln (sum-tree tree))    ; Output:

#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;1
(define (sequence low high stride)
    (if (> low high)
        null
        (cons low (sequence (+ low stride) high stride))))
;2
(define (string-append-map xs suffix)
    (map (lambda (i) (string-append i suffix)) xs))
;3
(define (list-nth-mod xs n)
    (cond [(< n 0) (error "list-nth-mod: negative number")]
          [(null? xs) (error "list-nth-mod: empty list")]
          [#t (car (list-tail xs (remainder n (length xs))))]))
;4
(define (stream-for-n-steps s n)
    (if (= n 0)
        null
        (cons (car (s)) (stream-for-n-steps (cdr (s)) (- n 1)))))
;5
(define funny-number-stream
    (letrec ([f (lambda (x)
                (if (zero? (remainder x 5))
                (cons (* -1 x) (lambda () (f (+ x 1))))
                (cons x (lambda () (f (+ x 1))))))])
    (lambda () (f 1))))
;6
(define dan-then-dog
    (letrec ([f (lambda (x)
                (if (string=? x "dan.jpg")
                (cons "dan.jpg" (lambda () (f "dog.jpg")))
                (cons "dog.jpg" (lambda () (f "dan.jpg")))))])
    (lambda () (f "dan.jpg"))))
;7
(define (stream-add-zero s)
    (lambda () (cons (cons 0 (car (s))) (stream-add-zero (cdr (s))))))
;8
(define (cycle-lists xs ys)
    (letrec ([f (lambda (n1 n2) (cons (cons  (list-nth-mod xs n1) (list-nth-mod ys n2)) (lambda () (f (+ n1 1) (+ n2 1)))))])
    (lambda () (f 0 0))))
;9
(define (vector-assoc v vec)
    (letrec ([f (lambda (n)
                (cond [(= n (vector-length vec)) #f]
                      [(not (pair? (vector-ref vec n))) (f (+ n 1))]
                      [(equal? (car (vector-ref vec n)) v) (vector-ref vec n)]
                      [#t (f (+ n 1))])
             )])
    (f 0) ))
;10
(define (cached-assoc xs n)
    (letrec([track-next 0]
            [cache-vector (make-vector n #f)]
            [f (lambda (v)
                (let ([ans (vector-assoc v cache-vector)])
                    (if ans
                        ans
                        (let ([new-ans (assoc v xs)])
                            (if new-ans
                                (begin
                                ;(print cache-vector)
                                (vector-set! cache-vector track-next new-ans)
                                (set! track-next (remainder (+ track-next 1) n))
                                new-ans)
                                #f
                            )
                        )
                    ))
                    )])
    f))

;; Problem 11: while-less macro
(define-syntax (while-less stx)
  (syntax-case stx ()
    ((_ e1 do e2)
     (let ((temp (gensym)))
       #'(let loop ()
           (define temp e1)
           (if (< e2 temp)
               (begin
                 e2
                 (loop))
               #t))))))
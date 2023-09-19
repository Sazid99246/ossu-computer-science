#lang racket

(define empty-stream '())

(define (palindromic lst)
  (define (helper lst1 lst2)
    (if (null? lst1)
        '()
        (cons (+ (car lst1) (car lst2))
              (helper (cdr lst1) (reverse (cdr lst2))))))
  (helper lst lst))

(define fibonacci
  (letrec ((fib-stream (cons 0
                          (cons 1
                                (stream-map + fib-stream (cdr fib-stream))))))
    fib-stream))

(define (stream-until f s)
  (if (f (car s))
      (car s)
      (stream-until f (cdr s))))

(define (stream-map f s)
  (if (equal? s empty-stream)
      s
      (cons (f (car s))
            (stream-map f (cdr s)))))

(define (stream-zip s1 s2)
  (if (equal? s1 empty-stream)
      s1
      (cons (cons (car s1) (car s2))
                   (stream-zip (cdr s1) (cdr s2)))))

(define (interleave streams)
  (define (interleave-helper current-streams)
    (if (not (ormap equal? current-streams))
        empty-stream
        (stream-append (map car current-streams))))
  (apply stream-append (map list->stream streams)))

(define (pack n s)
  (define (pack-helper k lst)
    (if (null? lst)
        empty-stream
        (cons-stream (take lst n)
                     (pack-helper k (drop lst n)))))
  (stream-map (lambda (x) (if (list? x) x (list x))) (pack-helper n s)))

(define (sqrt-stream n)
  (define (sqrt-helper x)
    (cons-stream x (sqrt-helper (/ (+ x (/ n x)) 2))))
  (sqrt-helper n))

(define (approx-sqrt n e)
  (define sqrt (sqrt-stream n))
  (define (close-enough? x)
    (<= (abs (- (* x x) n)) e))
  (stream-until close-enough? sqrt))

(define-syntax (perform stx)
  (syntax-case stx ()
    ((_ e1 if e2)
     (syntax (if (not e2) e1 e2)))
    ((_ e1 unless e2)
     (syntax (if e2 e2 e1)))))

#lang racket

(provide (all-defined-out))

(define xs (list 4 5 6));
(define ys (list (list 4 (list 5 0)) 6 7 (list 8) 9 2 3 (list 0 1)))

(define (sum1 xs)
  (if (null? xs)
      0
      (if (number? (car xs))
          (+ (car xs) (sum1 (cdr xs)))
          (+ (sum1 (car xs)) (sum1 (cdr xs))))))

(define (sum2 xs)
  (if (null? xs)
      0
      (if (number? (car xs))
          (+ (car xs) (sum2 (cdr xs)))
          (if (list? (car xs))
              (+ (sum2 (car xs)) (sum2 (cdr xs)))
              (sum2 (cdr xs))))))

(define (sum3 xs)
  (if (or (null? xs) (not (list? xs)))
      0
      (if (number? (car xs))
          (+ (car xs) (sum3 (cdr xs)))
          (if (list? (car xs))
              (+ (sum3 (car xs)) (sum3 (cdr xs)))
              (sum3 (cdr xs))))))

#lang racket

(provide (all-defined-out))

(define (sum4 xs)
  (cond [(null? xs) 0]
        [(number? (car xs)) (+ (car xs) (sum4 (cdr xs)))]
        [#t (+ (sum4 (car xs)) (sum4 (cdr xs)))]))

(define (sum5 xs)
  (cond [(null? xs) 0]
        [(number? (car xs)) (+ (car xs) (sum5 (cdr xs)))]
        [(list? (car xs)) (+ (sum5 (car xs)) (sum5 (cdr xs)))]
        [#t (sum5 (cdr xs))]))

(define (sum6 xs)
  (cond [(or (null? xs) (not (list? xs))) 0]
        [(number? (car xs)) (+ (car xs) (sum6 (cdr xs)))]
        [(list? (car xs)) (+ (sum6 (car xs)) (sum6 (cdr xs)))]
        [#t (sum6 (cdr xs))]))

(define (count-falses xs)
  (cond [(null? xs) 0]
        [(car xs) (count-falses (cdr xs))]
        [#t (+ 1 (count-falses (cdr xs)))]))

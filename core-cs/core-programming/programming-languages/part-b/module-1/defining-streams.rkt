#lang racket

(define ones (lambda () (cons 1 ones)))

(define (f x) (cons x (lambda () (f (+ x 1)))))

(define nats
  (letrec ([f (lambda (x) (cons x (lambda () (f (+ x 1)))))])
    (lambda () (f 1))))

(define powers-of-two
  (letrec ([f (lambda (x) (cons x (lambda () (f (* x 2)))))])
    (lambda () (f 1))))

;(define (stream-maker fn arg) ...)
;(define nats (stream-maker + 1))
;(define powers-of-two (stream-maker * 2))
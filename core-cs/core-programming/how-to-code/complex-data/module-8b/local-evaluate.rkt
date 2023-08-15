;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname local-evaluate) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define b 1)

(+ b
   (local [(define b 2)]
     (* b b))
   b)

(+ 1
   (local [(define b 2)]
     (* b b))
   b)

(define b_0 2)

(+ 1
   (* b_0 b_0)
   b)

(+ 1
   (* 2 2)
   b)

(+ 1
   4
   b)

(+ 1
   4
   1)
6
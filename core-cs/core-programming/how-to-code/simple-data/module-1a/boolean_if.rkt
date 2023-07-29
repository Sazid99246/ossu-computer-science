;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname boolean_if) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;(define WIDTH 100)
;(define HEIGHT 100)
;
;(> HEIGHT WIDTH)
;(>= HEIGHT WIDTH)
;
;(= 1 2)
;(= 1 1)
;(= 3 9)

;(string=? "foo" "bar")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

(and (> (image-height I1) (image-height I2))
     (< (image-width I1) (image-width I2)))
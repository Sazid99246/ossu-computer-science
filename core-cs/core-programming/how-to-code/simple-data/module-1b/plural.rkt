;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname plural) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; String -> String - Signature
;; Adds a "s" to the last of a word - Purpose

;; Examples
(check-expect (pluralize "pen") "pens")
(check-expect (pluralize "laptop") "laptops")

;; (define (pluralize s) "") ;; Stub

;; Template
;;(define (pluralize s)
  ;; ... s)

(define (pluralize s)
   (string-append s "s"))

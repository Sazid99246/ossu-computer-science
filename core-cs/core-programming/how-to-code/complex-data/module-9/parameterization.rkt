;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname parameterization) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; parameterization-starter.rkt

(define (area r)
  (* pi (sqr r)))

(area 4) ;area of circle radius 4
(area 6) ;area of circle radius 6


;; ====================

;; ListOfString -> Boolean
;; produce #true if los includes "UBC"
(check-expect (contains-ubc? empty) #false)
(check-expect (contains-ubc? (cons "McGill" empty)) #false)
(check-expect (contains-ubc? (cons "UBC" empty)) #true)
(check-expect (contains-ubc? (cons "McGill" (cons "UBC" empty))) #true)

;(define (contains-ubc? los) #false) ;stub

;<template from ListOfString>

(define (contains-ubc? los) (contains? "UBC" los))

;; ListOfString -> Boolean
;; produce #true if los includes "McGill"
(check-expect (contains-mcgill? empty) #false)
(check-expect (contains-mcgill? (cons "UBC" empty)) #false)
(check-expect (contains-mcgill? (cons "McGill" empty)) #true)
(check-expect (contains-mcgill? (cons "UBC" (cons "McGill" empty))) #true)

;(define (contains-mcgill? los) #false) ;stub

;<template from ListOfString>

(define (contains-mcgill? los) (contains? "McGill" los))

;; String (listof String) -> Boolean
;; produce #true if los includes s
(check-expect (contains? "UBC" empty) #false)
(check-expect (contains? "UBC" (cons "McGill" empty)) #false)
(check-expect (contains? "UBC" (cons "UBC" empty)) #true)
(check-expect (contains? "UBC" (cons "McGill" (cons "UBC" empty))) #true)
(check-expect (contains? "UBC" (cons "UBC" (cons "McGill" empty))) #true)
(check-expect (contains? "Torronto" (cons "UBC" (cons "McGill" empty))) #false)

(define (contains? s los)
  (cond [(empty? los) #false]
        [else
         (if (string=? (first los) s)
             #true
             (contains? s (rest los)))]))

;; ====================

;; ListOfNumber -> ListOfNumber
;; produce list of sqr of every number in lon
(check-expect (squares empty) empty)
(check-expect (squares (list 3 4)) (list 9 16))

;(define (squares lon) empty) ;stub

;<template from ListOfNumber>

(define (squares lon)
  (map2 sqr lon))

;; ListOfNumber -> ListOfNumber
;; produce list of sqrt of every number in lon
(check-expect (square-roots empty) empty)
(check-expect (square-roots (list 9 16)) (list 3 4))

;(define (square-roots lon) empty) ;stub

;<template from ListOfNumber>

(define (square-roots lon)
  (map2 sqrt lon))

;; given fn and (list n0 n1 n2...) produce (list (fn n0) (fn n1) (fn n2)...)
(check-expect (map2 sqr empty) empty)
(check-expect (map2 sqr (list 3 4)) (list 9 16))
(check-expect (map2 sqrt (list 9 16)) (list 3 4))
(check-expect (map2 abs (list 2 -3 4)) (list 2 3 4))
(check-expect (map2 string-length (list "a"  "bc" "def")) (list 1 2 3))

;; (X -> Y)  (listof X) -> (listof Y)
(define (map2 fn lon)
  (cond [(empty? lon) empty]
        [else
         (cons (fn (first lon))
               (map2 fn (rest lon)))]))

;; ====================

;; ListOfNumber -> ListOfNumber
;; produce list with only positive? elements of lon
(check-expect (positive-only empty) empty)
(check-expect (positive-only (list 1 -2 3 -4)) (list 1 3))

;(define (positive-only lon) empty) ;stub

;<template from ListOfNumber>

(define (positive-only lon)
  (filter-two positive? lon))


;; ListOfNumber -> ListOfNumber
;; produce list with only negative? elements of lon
(check-expect (negative-only empty) empty)
(check-expect (negative-only (list 1 -2 3 -4)) (list -2 -4))

;(define (negative-only lon) empty) ;stub

;<template from ListOfNumber>

(define (negative-only lon)
  (filter-two negative? lon))

;; filter list to contain only those elements for which pred produces #true
(check-expect (filter-two positive? empty) empty)
(check-expect (filter-two positive? (list 1 -2 3 -4)) (list 1 3))
(check-expect (filter-two negative? (list 1 -2 3 -4)) (list -2 -4))

;; (X -> Boolean) (Listof X) -> (Listof Y)
(define (filter-two pred lon)
  (cond [(empty? lon) empty]
        [else
         (if (pred (first lon))
             (cons (first lon)
                   (filter-two pred (rest lon)))
             (filter-two pred (rest lon)))]))

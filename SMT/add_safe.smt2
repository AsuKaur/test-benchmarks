(set-logic QF_FP)

(declare-fun a () (_ FloatingPoint 8 24))
(declare-fun b () (_ FloatingPoint 8 24))

; a >= 0.0 & a <= 1.0
; b >= 0.0 & b <= 1.0
(assert (and (fp.geq a ((_ to_fp 8 24) RNE 0.0))
             (fp.leq a ((_ to_fp 8 24) RNE 1.0))
             (fp.geq b ((_ to_fp 8 24) RNE 0.0))
             (fp.leq b ((_ to_fp 8 24) RNE 1.0))))

; sum = a + b
(define-fun sum () (_ FloatingPoint 8 24)
  (fp.add RNE a b))

; SAFE: sum <= 2.0
(assert (fp.leq sum ((_ to_fp 8 24) RNE 2.0)))

(check-sat)
(get-model)

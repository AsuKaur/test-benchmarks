(set-logic QF_FP)

(declare-fun a () (_ FloatingPoint 8 24))
(declare-fun b () (_ FloatingPoint 8 24))
(declare-fun z () (_ FloatingPoint 8 24))

(define-fun zero () (_ FloatingPoint 8 24) ((_ to_fp 8 24) RNE 0.0))

; a >= 0.0 & a <= 1.0
; b >= 0.0 & b <= 1.0
(assert (and (fp.geq a ((_ to_fp 8 24) RNE 0.0))
             (fp.leq a ((_ to_fp 8 24) RNE 1.0))
             (fp.geq b ((_ to_fp 8 24) RNE 0.0))
             (fp.leq b ((_ to_fp 8 24) RNE 1.0))))


; Z = ReLU(A - B)
(assert (= z (ite (fp.gt (fp.sub RNE a b) zero) (fp.sub RNE a b) zero)))

; UNSAFE: Z > 1.0 
(assert (fp.gt z ((_ to_fp 8 24) RNE 1.0)))

(check-sat)
(get-model)

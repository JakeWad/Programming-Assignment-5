(define (reverse-list lst)
  (if (null? lst)
      '()
      (append (reverse-list (cdr lst)) (list (car lst)))))

(define x '(1 2 3 4 5))

(reverse-list x)

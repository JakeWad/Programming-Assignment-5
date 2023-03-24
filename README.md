Lewis University SP23-CPSC-46000-LT1-Programming Languages

Programming-Assignment-5


	1.Write a Scheme (Using Dr. Racket) program to perform binary search.
 
		Sample Data Pattern:

			(define alist ‘(1 3 7 9 12 18 20 23 25 37 46))

			Test -2, 9, 16, 37

 		Sample Output :

			> (binary alist -2)

			-1

			> (binary alist 9)

			3

			> (binary alist 16)

			-1

			> (binary alist 37)

			9

	2.Write a Scheme program which can reverse a list
 
		Sample List :

			(define x '(1 2 3 4 5))

			(reverse x)

 		Sample Output :

			'(5 4 3 2 1)

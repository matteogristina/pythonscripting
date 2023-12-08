reverse_list(Xs,Ys) :- reverse_list(Xs,[],Ys).

reverse_list([],A,A).
reverse_list([H|T],R,A) :- reverse_list(T,[H|R],A).

main :- read(Input),
	reverse_list(Input, Result),
	write(Result).
    
%read mickey.png and stores it in matrix A
A = imread('mickey.png');

%changes 2D matrix A to 1D matrix B (1 row, 256^2 col)
B = reshape(A, [1, 65536]);

%writes 1D matrix to input.txt, delimiter places spaces in between each argument
dlmwrite('input.txt', B, 'delimiter', ' ');

imshow(A);

%closes matlab
exit;
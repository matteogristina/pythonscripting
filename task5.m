%read c output txt to 1D string martix data
orig = imread('mickey.png');
cdata = importdata('c_output.txt');
haskdata = importdata('haskell_output.txt');
proldata = importdata('prolog_output.txt');


%change strings to nums
%change from nums to unsigned ints

%reshape 1d array to 2d array
cout = reshape(cdata, [256, 256]);
haskout = reshape(haskdata, [256, 256]);
prolout = reshape(proldata, [256, 256]);


cunsigned = uint8(cout);
haskunsigned = uint8(haskout);
prolunsigned = uint8(prolout);

%https://www.mathworks.com/help/matlab/creating_plots/combine-multiple-plots.html
tiledlayout(2,2)

%show the image for debugging
nexttile
imshow(orig);
title('Original')
nexttile
imshow(cunsigned);
title('Threshold')
nexttile
imshow(haskunsigned);
title('Inverted')
nexttile
imshow(prolunsigned);
title('Flipped')

%pause
%closes matlab
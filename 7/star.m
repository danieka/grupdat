clf
x = rand(10,1)*100;
y = rand(10,1)*100;
r = rand(10,1);


hold on
for i = 1:size(x,1)
    fillcircle(x(i), y(i), r(i), 'r')
end
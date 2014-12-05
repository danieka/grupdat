function fillcircle(xc, yc, r, col, n)
if nargin == 4
    n = 100;
end
fi = linspace(0,2*pi,n);

x = xc + r*cos(fi);
y = yc + r*sin(fi);
fill(x, y, col)
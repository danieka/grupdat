function res = polygonsidor(x, y)

xs = [x x(1)];
ys = [y y(1)];

dx = diff(xs);
dy = diff(ys);

res = sqrt(dx.^2 + dy.^2);

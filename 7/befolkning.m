clc
clear all

filename = 'befolkning.csv';
b = csvread(filename);

out = [zeros(9, 1)]

for i=1:length(b)
    elm = b(i);
    %digit = floor(elm / 10^(floor(log10(elm))));
    digit = (floor(log10(elm)));
    out(digit) = out(digit) + elm;
end

plot(x, out(2:end));

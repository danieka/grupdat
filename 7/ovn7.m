filename = 'befolkning.csv';
b = csvread(filename);

out = zeros(9,1);
for i=1:length(b)
    elm = b(i);
    digit = floor(log10(elm));
    out(digit) = out(digit) +elm;
end

plot(out)
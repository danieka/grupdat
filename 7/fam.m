ages = [0 4 6 34];

ages = ages + 1;

for i = 1:50
    if isprime(ages)
        disp(ages)
    end
    ages = ages +2;
end
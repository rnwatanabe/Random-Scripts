% Compares two floats with the precision epsilon
%
% written by: Renato Naville Watanabe
%
%   equal = comp(x, y, epsilon)
%
% Inputs: 
%
%   x and y: floats, the two numbers that you want to verify if are equal.
%   
%   epsilon: float, precision to consider x and y equal.  good number is
%   1e-6.
%
% Outputs:
%
%   equal: boolean, 1 if equal and 0 if not equal.



function equal = comp(x, y, epsilon)
    if (x >= y - epsilon  && x <= y + epsilon)
        equal = 1;
    else
        equal = 0;
    end
end

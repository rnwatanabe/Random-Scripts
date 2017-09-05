%% Implements the basic Matched Filter algorithm
% by Renato Naville Watanabe
% Inputs:
%   - st is a vector with the template of the signal to be found.
%   - x is vector with the signal to be analised.
%   - Rv is a covariance matrix with of the noise present in the signal x.
% If you have no information about Rv, use an identity matrix.
%   - threshold is a real scalar with the tg=hreshold to identify the
%   template.
% Outputs:
%   - matchedSignal is a vector of the same size of x with the identified 
% signals similar to the template st.
%   - y is a vector of the same size of x with the projection of st in x 
% at each instant 

function [matchedSignal, y] = matchedFilter(st, x, Rv, threshold)


y = zeros(size(x));
matchedSignal = zeros(size(x));

h = 2/length(st)*(Rv\st);

begin = 1;
for i = begin:length(x)-length(st)+begin
   y(i) = h'*x(i-begin+1:i+length(st)-begin);
end

[pks,locs] = findpeaks(y,'MinPeakHeight',threshold*max(y));
locs
for i = 1:length(locs)
   matchedSignal(locs(i):locs(i)+length(st)-1)= st; 
end

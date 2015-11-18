%% compute the Moving Average of a signal
% x is a vector with the signal you want to compute moving average
% window is an integer with the number of samples to be considered during
%the moving average
% y is the move averaged signal 

function y = ma(x, window)
    y = zeros(size(x));
    for i = 1:length(x);
        y(i) = mean(x(max(1,i-round(window/2)):min(length(x),i+round(window/2))));
    end
end
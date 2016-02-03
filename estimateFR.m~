% Estimates the firing rate along time, in Hz, of a firing process. It
% convolves a gaussian with a Dirac's delta train of the firing isntants.
%
% written by: Renato Naville Watanabe
%
%   [FR, t] = estimateFR(spikeTimes, dt, gaussianSD, tf)
%
% Inputs:
%
%   spikeTimes: vector of floats, instants of time, in s, that the a process has
%   fired.
%
%   dt: float, time step to build the firing rate signal, in s.
%
%   gaussianSD: float, standard deviation of the gaussian.
%
%   tf: float, time to end the FR signal.
%
% Outputs:
%
%   FR: vector of floats, signal of the firing rate, in Hz.
%
%   t: vector of floats, time values correspondent to the FR signal.


function [FR, t] = estimateFR(spikeTimes, dt, gaussianSD, tf)
    t = 0:dt:tf; 
    S = zeros(size(t));
    j = 1;
    for i = 1:length(S)
        if comp(t(i), spikeTimes(j), dt/2);
           S(i) = 1;
           if (j < length(spikeTimes))
                j = j + 1;
           end
        end
    end
    spikeTrain = (S./dt);
    bin = dt;
    edges = -3*gaussianSD:bin:3*gaussianSD;
    gaussKernel = normpdf(edges, 0, gaussianSD)*bin;
    FR = filtfilt(gaussKernel,1,[zeros(1,round(3*gaussianSD/bin)) spikeTrain zeros(1, round(3*gaussianSD/bin))]);
    FR = FR(round(3*gaussianSD/bin):length(FR)- round(3*gaussianSD/bin) - 1);
end
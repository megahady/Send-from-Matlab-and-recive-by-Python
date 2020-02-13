%% Matlab as a Data Client 
% This code is running on a second copy of MATLAB.
% Create a waveform and visualize it.

theta=linspace(0,2*pi,200);
data = sin(theta);

%Create a client interface and open it.

t = tcpip('192.168.1.3', 1234, 'NetworkRole', 'client');
fopen(t)
% Int16 is a signed 2 byte 
data=int16(floor(interp1([-1,1],[-255,255],data))) 
% Write the waveform to the server session.
try
    fwrite(t, data,'int16')  % Data type is very important
catch
     fclose(t)
end
pause(0.53) % time delay is unnecessary  
plot(data)
fclose(t)
disp("Ok ============= Ok")

function ecRecta( x1,x2,y1,y2 )

m = y2 - y1 ;
b = y2 - m * x2

x = -10:10 ;
fx = m * x + b ;

figure
plot(x,fx) ; grid on ; ylabel('y'); xlabel('x'); hold on ;


end


clc , clear all , close all ;
%%
% operacion de vectores

a = 1 ; b = 2 ; 
c = 3 ; d = -1 ;

vectA = [a ; b] ;  vectB = [c ; d] ; 

opcion = 2 ;


if (opcion == 1)  % suma
    vectSuma = [ vectA(1,1) + vectB(1,1) ; vectA(2,1)+ vectB(2,1) ] 
    
    plotv(vectA,'-'); grid on ; hold on  ; plotv(vectB,'-'); plotv(vectSuma,'-');

elseif (opcion == 2)
    vectResta = [ vectA(1,1) - vectB(1,1) ; vectA(2,1)- vectB(2,1) ] 
    plotv(vectA,'-'); grid on ; hold on  ; plotv(vectB,'-'); plotv(vectResta,'-');

elseif (opcion == 3)
    vectMulti = [ vectA(1,1) * vectB(1,1) ; vectA(2,1) * vectB(2,1) ] 
    plotv(vectA,'-'); grid on ; hold on  ; plotv(vectB,'-'); plotv(vectMulti,'-');
    
end

%%

o = [0 0 0];  % Origen
a = [1 2 0];  %
b = [3 -1 0];  % 
c = a+b;      %
arrowStarts = [o; a; o];        %# Starting points for arrows
arrowEnds = [a; c; c];          %# Ending points for arrows
(arrowStarts,arrowEnds);   %# Plot arrows

%%
% https://rstopup.com/como-dibujar-los-vectores-fisica-2d-3d-vectores-en-matlab.html
% metodo paralelogramo
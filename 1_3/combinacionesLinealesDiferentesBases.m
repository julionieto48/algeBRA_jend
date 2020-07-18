clc , clear all , close all ;
%%
% * Combinacion Lineal*

% hacer funcion de ecuacion de la recta


origen = [0 ; 0] ;                            % coordenada de origen

%%
% cambio en los vectores base
% esta e suna version de combinacion lineales, en el que se aplican
% transformaciones comunes

opcionUnitarios = 4;

if (opcionUnitarios == 1)
    unitario_i = [1 ; 0] ; unitario_j = [0 ; 1] ;
elseif (opcionUnitarios == 2) % entrada del usuario de bases
    aa = -2 ; bb = 1 ; cc = -2 ; dd = 1 ;
    unitario_i = [aa ; bb] ; unitario_j = [cc ; dd] ;
elseif (opcionUnitarios == 3) %rotacion 90 grados antireloj
    unitario_i = [0 ; 1] ; unitario_j = [-1 ; 0] ;
elseif (opcionUnitarios == 4) %sheer
    unitario_i = [1 ; 0] ; unitario_j = [1 ; 1] ;

end
    

%%
figure;
plotv(unitario_i,'-'); grid on ; hold on  ; plotv(unitario_j,'-');


% ecRecta(origen(1),origen(2),unitario_i(1),unitario_i(2) ) %% reemplazar la funcion plotv

%%
% x y y son dos puntos cualquiera de un vector
x = 1 ; y = 1 ; % esta es la transformacion lineal
input = [x ;  y] ; 

a = unitario_i(1,1) ; c = unitario_i(2,1) ;   % i
b = unitario_j(1,1) ; d = unitario_j(2,1) ;   % j
X = input(1,1)      ; Y = input(2,1)      ;

vect = [a*X + b*Y ; c*X + d*Y] ;

plotv(vect,'-');
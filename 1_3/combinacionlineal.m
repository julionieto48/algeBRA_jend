clc , clear all , close all ;
%%
% * Combinacion Lineal *

% hacer funcion de ecuacion de la recta


origen = [0 ; 0 ] ;                            % coordenada de origen

unitario_i = [1 ; 0 ] ; unitario_j = [0 ; 1 ] ;    % coordenadas de vect unitarios

figure;
plotv(unitario_i,'-'); grid on ; hold on  ; plotv(unitario_j,'-'); % se determinan las bases de forma standard
plotv(unitario_k,'-');



%%
x = 5 ; y = 7 ;  % esta es la transformacion lineal
input = [x ;  y] ; 

% hay 2 corrdenadas donde quedaran las bases
a = unitario_i(1,1) ; c = unitario_i(2,1) ;   % i  a = 1   c = 0
b = unitario_j(1,1) ; d = unitario_j(2,1) ;   % j b = 0    d = 1
X = input(1,1)      ; Y = input(2,1)      ;

vect = [a*X + b*Y ; c*X + d*Y] ; % vector transformado

plotv(vect,'-');
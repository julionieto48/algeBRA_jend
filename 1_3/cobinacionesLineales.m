clc , clear all , close all ;
%%
% * Combinacion Lineal en 3- D*

% hacer funcion de ecuacion de la recta


origen = [0 ; 0] ;                            % coordenada de origen

unitario_i = [1 ; 0 ; 0 ] ; unitario_j = [0 ; 1 ; 0] ; unitario_k = [0 ; 0 ; 1] ;     % coordenadas de vect unitarios

figure;
plot3( [unitario_i(1,1,1),unitario_i(2,1,1),unitario_i(3,1,1)])
% plot3(first(:,1), first(:,2), first(:,3), 'k*-', second(:,1), second(:,2), second(:,3), 'b^-', third(:,1), third(:,2), third(:,3), 'g>-');
%legend(('first', 'second', 'third'})
% plot3([0 0 0; vector_1(:,1), vector_2(:,1), vector_3(:,1)], [0 0 0; vector_1(:,2), vector_2(:,2), vector_3(:,2)])
% ecRecta(origen(1),origen(2),unitario_i(1),unitario_i(2) ) %% reemplazar la funcion plotv

%%
x = 5 ; y = 7 ; z = 2 ; % esta es la transformacion lineal
input = [x ;  y ; z] ; 

% hay 2 corrdenadas donde quedaran las bases
a = unitario_i(1,1,1) ; b = unitario_i(2,1,1) ; c = unitario_i(3,1,1) ;  % i  a = 1  b = 0  c = 0
d = unitario_j(1,1,1) ;  e = unitario_j(2,1,1) ; f = unitario_j(3,1,1) ; % j  a = 0  b = 1  c = 0 
g = unitario_k(1,1,1) ;  h = unitario_k(2,1,1) ; i = unitario_k(3,1,1) ; % k  a = 0  b = 0  c = 1
X = input(1,1,1)        ; Y = input(2,1,1)      ; Z = input(3,1,1)      ;

vect = [a*X + b*Y + c*Z ; d*X + e*Y + f*Z ; g*X + h*Y + i*Z] ; % vector transformado

plot3(vect(1,1,1),vect(2,1,1),vect(3,1,1));




% https://www.tutorialspoint.com/matlab/matlab_matrics.htm
% hacer en 3 dimensiones , crear mi propia funcion plot v , genralizar las
% transformaciones en una funcion
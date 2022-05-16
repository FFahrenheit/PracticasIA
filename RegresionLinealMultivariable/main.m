clear all;
close all;
clc;

% Lectura de datos
datos = load("dataset_RegresionLinealMultivariable.txt");
x = datos(:,1:2);
y = datos(:,3);

[m, n]= size(x);

%Gráfica de datos
figure(1);
plot3(x(:,1), x(:,2), y, 'ok', 'MarkerFaceColor', 'y');
xlabel('x1');
ylabel('x2');
zlabel('y');
hold on;

% Normalización y gráfica
x_norm = zeros(m, n);
mu = mean(x);
sigma = std(x, 1);

for i=1:n
    x_norm(:,i) = (x(:,i) - mu(i))/sigma(i);
end

figure(2);
plot3(x_norm(:,1), x_norm(:,2), y, 'ok', 'MarkerFaceColor', 'y');
xlabel('x1');
ylabel('x2');
zlabel('y');
hold on;

% Parámetros del algoritmo
x = x_norm;
x = [ones(m,1), x];
n = n + 1;

a = zeros(n, 1);
beta = 0.023;
iterMax = 200;
iter = 1;

% Cálculo de hipótesis
for i=1:m
    h(i,1) = a'*x(i,:)';
end
J = (1/(2*m))*sum((h - y).^2);

%plot(x, h, 'r');

while (iter < iterMax)
    convergencia(iter) = J;

    for j=1:n
        a(j) = a(j) - beta*(1/n)*sum(h-y).*x(:,j);
    end
    
    for i=1:m
        h(i,1) = a'*x(i,:)';
    end

    J = (1/(2*m))*sum((h - y).^2);
    iter = iter + 1;
end

plot(convergencia, '*');

datoEntrada = [1 0.75 1.12];
%figure(1);
hDatoEntrada = a'*datoEntrada';
%plot(datoEntrada, hDatoEntrada, 'ok', 'MarkerFaceColor', 'm');

%fprintf("J = %d\t a0 = %d\t a1 = %d\n", J, a0, a1);
%fprintf("x = %d\t y = 7.5435\t h = %d\n", datoEntrada, hDatoEntrada);
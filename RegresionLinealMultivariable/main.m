clear all;
close all;
clc;

%  Lectura de datos
datos = load("dataset_RegresionLinealMultivariable.txt");
x = datos(:,1:2);
xDatos = x;
y = datos(:,3);

[m, n]= size(x);

% Gráfica de datos
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
beta = 0.8;
iterMax = 600;
iter = 1;

%Cálculo de hipótesis
for i=1:m
    h(i,1) = a'*x(i,:)';
end
disp(size(h));
J = (1/(2*m))*sum((h - y).^2);

while (iter < iterMax)
    convergencia(iter) = J;

    for j=1:n
        a(j) = a(j) - beta*(1/m)*sum((h-y).*x(:,j));
    end
    
    for i=1:m
        h(i,1) = a'*x(i,:)';
    end

    J = (1/(2*m))*sum((h - y).^2);
    iter = iter + 1;
end

figure(3);
plot(convergencia);
hold on;

fprintf("J = %0.4f\ta0 = %0.4f\ta1 = %0.4f\ta2 = %0.4f\n", J, a(1), a(2), a(3));

% Datos de prueba
prueba = 1;
for i=5:7
    fprintf("Dato de prueba %d\tx1 = %d\tx2 = %d\tSalida correcta y = %d\tPrediccion h = %0.4f\n", prueba, xDatos(i,1), xDatos(i,2), y(i), h(i));
    prueba = prueba + 1;
end
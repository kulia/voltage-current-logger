
s = [
792600 66 539
793468 97 525
794340 155 515
795252 244 505
796164 373 491
797084 479 487
798004 595 477
798916 684 481
799832 759 479
800740 821 490
801652 863 497
802564 871 510
803476 845 523
804388 779 533
805300 689 545
806212 562 560
807124 449 562
808040 338 573
808948 251 570
809860 174 569
810772 112 559
811684 78 551
812548 67 539
813420 89 527
814284 147 517
815200 243 503
816108 359 494
817020 473 487
817932 584 478
818844 677 480
819756 753 479
820668 813 489
821580 859 496
822484 871 507
823392 846 522
824300 784 532
825212 695 543
];

t = (s(:, 1) - s(1, 1)) ./ 1000; % ms

figure(1)
clf(1)
hold on
i = (s(:, 3) - mean(s(:, 3)));
v = s(:, 2) - mean(s(:, 2));

plot(t, 5.* i, 'b')
plot(t, v, 'r')

plot(t, 5.* i, 'b*')
plot(t, v, 'r*')

title('Blue: Current | Red: Voltage')
xlabel('Time [ms]')

disp(['Presition for i: ' num2str(max(i)-min(i))])
disp(['Presition for v: ' num2str(max(v)-min(v))])

figure(2)
clf(2)

L = length(i);
I_f = fft(i);
I_f = abs(I_f/L);
I_f = I_f(1:L/2+1);
I_f(2:end-1) = 2*I_f(2:end-1);

subplot(2, 1, 1), semilogx((I_f))
title('Single-Sided Amplitude Spectrum of the current')
xlabel('f')
ylabel('|I(f)|')

L = length(v);
V_f = fft(v);
V_f = abs(V_f/L);
V_f = V_f(1:L/2+1);
V_f(2:end-1) = 2*V_f(2:end-1);

subplot(2, 1, 2), semilogx((V_f))
title('Single-Sided Amplitude Spectrum of the voltage')
xlabel('f')
ylabel('|V(f)|')
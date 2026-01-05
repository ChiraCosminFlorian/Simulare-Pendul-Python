import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.fft import fft, fftfreq
import csv
plt.style.use('seaborn-v0_8-muted') # Sau 'ggplot' pentru un aspect profesional
# ==========================================================
# 1. DEFINIREA MODELULUI FIZIC
# ==========================================================
def model_pendul(y, t, b, m, g, L):
    """
    Ecuația diferențială a pendulului cu frecare (amortizat).
    y[0] = unghiul (theta), y[1] = viteza unghiulară (omega)
    """
    theta, omega = y
    dydt = [omega, - (b/m)*omega - (g/L)*np.sin(theta)]
    return dydt

# ==========================================================
# 2. PARAMETRII INITIALI SI CONFIGURARE
# ==========================================================
# Constante fizice
g = 9.81  # accelerația gravitațională
L = 2.0   # lungimea firului (metri)
m = 1.0   # masa (kg)
t_max = 30
fps = 100
t = np.linspace(0, t_max, t_max * fps)

# Condiții inițiale: unghi de 45 grade (transformat în radiani) și viteză 0
y0 = [np.pi/4, 0.0]

# Regimuri de testat (coeficienți de frecare diferiți)
coeficienti_frecare = [0.1, 0.5, 2.0, 5.0]
culori = ['blue', 'green', 'orange', 'red']
etichete = ['Amortizare mică', 'Amortizare medie', 'Amortizare critică', 'Supra-amortizat']

# ==========================================================
# 3. PROCESARE SI CALCUL
# ==========================================================
rezultate = []

print("Se inițializează simularea...")

for b in coeficienti_frecare:
    # Rezolvarea ecuației diferențiale cu SciPy
    solutie = odeint(model_pendul, y0, t, args=(b, m, g, L))
    unghi = solutie[:, 0]
    viteza = solutie[:, 1]
    rezultate.append((unghi, viteza))

# Calculăm FFT (Transformata Fourier) pentru primul regim (cel cu oscilații)
# Aceasta ne arată frecvența dominantă a sistemului
semnal = rezultate[0][0]
n = len(t)
yf = fft(semnal)
xf = fftfreq(n, 1/fps)[:n//2]
amplitudine_fft = 2.0/n * np.abs(yf[0:n//2])

print("Calcule finalizate. Se generează raportul grafic...")

# ==========================================================
# 4. VIZUALIZARE AVANSATĂ (MATPLOTLIB)
# ==========================================================
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Raport Analiză Sistem Dinamic: Pendul Amortizat', fontsize=20)

# Graficul 1: Evoluția în timp (Unghi)
for i in range(len(coeficienti_frecare)):
    axs[0, 0].plot(t, rezultate[i][0], color=culori[i], label=etichete[i])
axs[0, 0].set_title('Evoluția Unghiului în Timp')
axs[0, 0].set_xlabel('Timp [s]')
axs[0, 0].set_ylabel('Unghi [rad]')
axs[0, 0].grid(True, linestyle='--')
axs[0, 0].legend()

# Graficul 2: Portretul de Fază (Unghi vs Viteză)
# Arată cum "starea" sistemului converge spre zero (punctul de echilibru)
for i in range(len(coeficienti_frecare)):
    axs[0, 1].plot(rezultate[i][0], rezultate[i][1], color=culori[i])
axs[0, 1].set_title('Portret de Fază (Viteză vs Poziție)')
axs[0, 1].set_xlabel('Unghi [rad]')
axs[0, 1].set_ylabel('Viteză unghiulară [rad/s]')
axs[0, 1].grid(True)

# Graficul 3: Analiza Spectrală (FFT)
axs[1, 0].plot(xf, amplitudine_fft, color='purple')
axs[1, 0].set_title('Analiza Frecvenței (FFT) - Regim Sub-amortizat')
axs[1, 0].set_xlabel('Frecvență [Hz]')
axs[1, 0].set_ylabel('Amplitudine')
axs[1, 0].set_xlim(0, 2) # Ne concentrăm pe frecvențele joase
axs[1, 0].grid(True)

# Graficul 4: Energia Sistemului (Cinetică + Potențială)
# Calculăm energia pentru primul caz
unghi_ref = rezultate[0][0]
viteza_ref = rezultate[0][1]
E_pot = m * g * L * (1 - np.cos(unghi_ref))
E_cin = 0.5 * m * (L * viteza_ref)**2
E_tot = E_pot + E_cin

axs[1, 1].fill_between(t, E_pot, label='Energie Potențială', alpha=0.5)
axs[1, 1].fill_between(t, E_cin, label='Energie Cinetică', alpha=0.5)
axs[1, 1].plot(t, E_tot, 'k--', label='Energie Totală')
axs[1, 1].set_title('Conservarea și Disiparea Energiei')
axs[1, 1].set_xlabel('Timp [s]')
axs[1, 1].set_ylabel('Energie [J]')
axs[1, 1].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ==========================================================
# 5. EXPORT DATE IN CSV
# ==========================================================
nume_fisier = "date_pendul.csv"
with open(nume_fisier, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timp', 'Unghi_SubAmortizat', 'Viteza_SubAmortizat'])
    for i in range(len(t)):
        writer.writerow([t[i], rezultate[0][0][i], rezultate[0][1][i]])

print(f"Succes! Datele au fost salvate în {nume_fisier}.")
plt.show()
# Analiza și Simularea Sistemelor Dinamice: Pendulul Amortizat

Acest proiect reprezintă o simulare numerică avansată a mișcării unui pendul gravitațional, luând în considerare forțele de frecare (amortizarea). Proiectul utilizează bibliotecile fundamentale de Python pentru calcul științific și vizualizarea datelor.

## 🚀 Funcționalități
- **Simulare Fizică**: Rezolvarea numerică a ecuației diferențiale de ordinul II a mișcării folosind `scipy.integrate`.
- **Studiu Comparativ**: Analiza celor patru regimuri de amortizare (mică, medie, critică și supra-amortizare).
- **Analiză Spectrală**: Aplicarea Transformatei Fourier Rapide (FFT) pentru a determina frecvența dominantă a sistemului.
- **Analiza Energetică**: Monitorizarea disipării energiei mecanice (cinetică + potențială) în timp.
- **Export Date**: Salvarea rezultatelor simulării în format `CSV` pentru procesare ulterioară.

## 🛠️ Librării Utilizate
* **NumPy**: Pentru gestionarea vectorilor de date și calcule trigonometrice.
* **SciPy**: Pentru rezolvarea ecuațiilor diferențiale (`odeint`) și procesarea semnalului (`fft`).
* **Matplotlib**: Pentru generarea raportului grafic (4 sub-grafice profesionale).
* **CSV**: Pentru stocarea datelor brute.

## 📊 Rezultate Vizuale
Proiectul generează un dashboard interactiv cu 4 secțiuni:
1. **Evoluția Unghiului**: Cum scade amplitudinea oscilației în funcție de coeficientul de frecare.
2. **Portretul de Fază**: Relația dintre poziție și viteză, evidențiind convergența spre punctul de echilibru.
3. **Analiza FFT**: Vizualizarea componentelor de frecvență ale semnalului.
4. **Graficul Energiei**: Demonstrarea legii conservării și disipării energiei în sisteme disipative.

## 💻 Cum se rulează
1. Asigurați-vă că aveți Python instalat.
2. Instalați dependențele:
   ```bash
   pip install numpy scipy matplotlib

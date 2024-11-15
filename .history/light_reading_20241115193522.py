# Zakładam, że jesteś w katalogu projektu
import os
import venv

# Utwórz środowisko wirtualne
venv_dir = os.path.join(os.getcwd(), 'venv')
venv.create(venv_dir, with_pip=True)

# Aktywuj środowisko wirtualne
activate_script = os.path.join(venv_dir, 'Scripts', 'activate')
os.system(f'"{activate_script}"')

# Zainstaluj wymagane biblioteki
os.system('pip install pandas matplotlib')

# Wczytaj dane i stwórz wizualizacje
import pandas as pd
import matplotlib.pyplot as plt

csv_file = input("Podaj pełną ścieżkę do pliku CSV z danymi: ")
data = pd.read_csv(csv_file)
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['Light_Level_lx'])
plt.xlabel('Znacznik czasu')
plt.ylabel('Natężenie światła (lx)')
plt.title('Natężenie światła w czasie')
plt.grid()
plt.savefig('light_intensity_plot.png')

plt.figure(figsize=(8, 6))
plt.hist(data['Light_Level_lx'], bins=20)
plt.xlabel('Natężenie światła (lx)')
plt.ylabel('Częstość')
plt.title('Rozkład natężenia światła')
plt.savefig('light_intensity_histogram.png')

print('Wizualizacje zapisano jako light_intensity_plot.png i light_intensity_histogram.png')
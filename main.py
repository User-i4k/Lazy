import os
import sys
import subprocess
import time

# --- Kütüphane Kontrol ve Kurulum Bloğu ---
def install_dependencies():
    required_libraries = ['pyautogui', 'keyboard', 'pyperclip']
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f">>> Eksik kütüphane bulundu: {lib}. Kuruluyor...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Kodu çalıştırmadan önce bağımlılıkları yükle
install_dependencies()

# Kütüphaneleri kurduktan sonra içe aktar
import pyautogui
import keyboard
import pyperclip

# --- Yapılandırma ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILE = os.path.join(BASE_DIR, "text.txt")

def start_typing():
    if not os.path.exists(SOURCE_FILE):
        print(f"\n[HATA] '{os.path.basename(SOURCE_FILE)}' dosyası bulunamadı!")
        return

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n[BAŞLADI] 3 saniye içinde yazım başlıyor...")
    time.sleep(3)
    pyautogui.PAUSE = 0 

    for char in content:
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.02) 

        if char in ['\n', '{', '}']:
            time.sleep(0.02)
    
    print("\n[BİTTİ] Yazma işlemi tamamlandı.")

def show_welcome_screen():
    print("====================================================")
    print("                OTOMATİK KOD YAZICI                 ")
    print("====================================================")
    print(f"1. Yazılacak metni şu dosyaya kaydedin: {os.path.basename(SOURCE_FILE)}")
    print("\n2. ÖNEMLİ: Eğer kodları PDF'ten kopyalıyorsanız ve bozuk")
    print("   görünüyorsa (ör: RJUHQFL), metni önce ChatGPT veya")
    print("   Gemini'ye yapıştırıp 'Bu kodu düzelt' deyin.")
    print("   Düzeltilen metni text.txt dosyasına yapıştırın.")
    print("\n3. Yazılacak alanı seçin (imleci oraya tıklayın).")
    print("\n4. Başlatmak için: CTRL + ALT + . (Nokta)")
    print("================================================================================")
    print("NOT: Bu programın temel amacı, text.txt dosyasındaki içeriği hızlıca yazmaktır.")
    print("================================================================================")
    print("\n====================================================")
    print("Program dinlemede... Kısayol bekliyor.")

# Kısayol: Ctrl + Alt + .
keyboard.add_hotkey("ctrl+alt+.", start_typing)

if __name__ == "__main__":
    show_welcome_screen()
    keyboard.wait()
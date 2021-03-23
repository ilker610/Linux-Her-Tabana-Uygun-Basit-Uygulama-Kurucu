import os

print('Uygulama Kurucunun OpenSuse Sürümüne Hoş Geldiniz!')
soru = input('Hangi Uygulama Kurulsun ? (opera,discord,woeusb,neofetch,chrome) ')
bileşen = input('Uygulamanın Çalışması İçin Gerekli Programlar Kurulsun mu ? ')
snap1 = ('sudo zypper addrepo --refresh https://download.opensuse.org/repositories/system:/snappy/openSUSE_Leap_15.2 snappy')
snap2 = ('sudo zypper --gpg-auto-import-keys refresh')
snap3 = ('sudo zypper dup --from snappy')
snap4 = ('sudo zypper install snapd')
snap5 = ('sudo systemctl enable --now snapd')
snap6 = ('sudo systemctl enable --now snapd.apparmor')
discord = ('sudo snap install discord')
neofetch = ('sudo zypper install neofetch')
opera = ('sudo snap install opera')
woeusb1 = ('sudo snap install woe-usb --edge')
chrome1 = ('sudo zypper addrepo http://dl.google.com/linux/chrome/rpm/stable/x86_64 Google-Chrome')
chrome2 = ('sudo zypper refresh')
chrome3 = ('wget https://dl.google.com/linux/linux_signing_key.pub')
chrome4 = ('sudo rpm --import linux_signing_key.pub')
chrome5 = ('sudo zypper install --no-confirm google-chrome-stable')

if bileşen == 'evet':
    print('Önemli Bileşenler Kuruluyor !')
    os.system(snap1)
    os.system(snap2)
    os.system(snap3)
    os.system(snap4)
    os.system(snap5)
    os.system(snap6)

if soru == 'discord':
    print('Discord Kuruluyor !')
    os.system(discord)

if soru == 'neofetch':
    print('Neofetch Kuruluyor !')
    os.system(neofetch)

if soru == 'opera':
    print('Opera Kuruluyor !')
    os.system(opera)

if soru == 'woeusb':
    print('Woeusb Kuruluyor !')
    os.system(woeusb1)

if soru == 'chrome':
    print('Google Chrome Kuruluyor !')
    os.system(chrome1)
    os.system(chrome2)
    os.system(chrome3)
    os.system(chrome4)
    os.system(chrome5)
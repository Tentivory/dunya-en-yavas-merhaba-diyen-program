#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Merhaba Diyen Programı
Her harfi tek tek, aşırı yavaş bir şekilde yazar.
Tamamen gereksiz, ama çalışıyor.
Şimdi DAHA DA yavaş.
"""

import time
import sys

def yavas_yaz(metin, bekleme=5.0):
    """Her harfi belirtilen süre kadar bekleyerek yazar."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Başlıyor... (Lütfen sabırlı olun, bu ciddi bir iştir. Çok ciddi.)")
    time.sleep(3)
    yavas_yaz("Merhaba Dünya!", 5.0)
    print("\nBitti. Şimdi gidip çay demleyebilirsiniz. Hatta iki tane.")
    # Gizli not: QmlyIHPDvHJlIGJ1IGhpa2F5ZW5pbiB5YXZhc2xhbWFzaSBiaXIgYmlsZ2lzaSBtdW9tYW5ldGxlci4=

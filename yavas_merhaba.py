#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Merhaba Diyen Programı
Her harfi tek tek, aşırı yavaş bir şekilde yazar.
Tamamen gereksiz, ama çalışıyor.
"""

import time
import sys

def yavas_yaz(metin, bekleme=2.0):
    """Her harfi belirtilen süre kadar bekleyerek yazar."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Başlıyor... (Lütfen sabırlı olun, bu ciddi bir iştir)")
    time.sleep(1)
    yavas_yaz("Merhaba Dünya!", 1.5)
    print("\nBitti. Şimdi gidip çay demleyebilirsiniz.")
    # Gizli not: QmlyIHPDvHJlIGJ1IGhpa2F5ZW5pbiB5YXZhc2xhbWFzaSBiaXIgYmlsZ2lsaSBtdW9tYW5ldGxlci4= 
    # (base64: Bir süre bu hikayenin yavaslamasi bir bilgisi muomantler.)

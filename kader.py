#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sokakta Bulunan Para Kader Algoritması
Bu kod GERÇEKTEN çalışır. Kaderini GERÇEKTEN değiştirmez.
Absürt seviye: 11/10
"""

import random
import time
import sys

def kader_hesapla(miktar):
    if miktar < 0:
        return "Negatif para mı buldun? Bu da bir yetenek. Kaderin borçlu."
    if miktar == 0:
        return "Hiçbir şey bulmadın. Hayatın aynı kaldı. Tebrikler, stabilite şampiyonu."
    
    senaryolar = [
        f"{miktar} TL buldun. O parayla bir simit aldın. Simiti yerken bir kedi geldi ve sana aşık oldu. Artık o kediyle evlisin.",
        f"{miktar} TL'yi cebine koydun. Ertesi gün unuttun. 3 yıl sonra pantolonunu yıkarken çıktı ve 'beni neden unuttun' diye bağırdı.",
        f"{miktar} TL buldun ve 'şanslıyım' dedin. O gün öyle bir şanssızlık yaşadın ki para seninle dalga geçti.",
        f"{miktar} TL ile bir kahve aldın. Kahveyi içerken yanında oturan adam 'bu para benimdi' dedi. Tartıştınız. Sonunda ikiniz de zengin oldunuz (hayal).",
        f"{miktar} TL buldun. Onu harcamadan 'yatırım yapacağım' dedin. 1 hafta sonra o para seninle birlikte kayboldu.",
        f"{miktar} TL'yi bir çocuk buldu sandın ama aslında sen buldun. Çocuk üzüldü. Vicdan azabından 10 yıl uyuyamadın.",
        f"{miktar} TL buldun ve o parayla bilet aldın. Biletin numarası 13'tü. Kaderin seni bekliyor... ya da beklemiyor.",
        f"{miktar} TL'yi birine verdin. O kişi seninle hiç konuşmadı. Para dostluğu bozdu.",
        f"{miktar} TL buldun. Hayatın değişmedi. Ama artık 'ben de bir gün para bulmuştum' diye övünebilirsin.",
        f"{miktar} TL ile bir çay aldın. Çayı içerken 'bu para olmasa çay içemezdim' diye düşündün. Felsefe yaptın. 2 saat geçti."
    ]
    
    # Gizli mesaj: bazen hayatın en küçük şeyleri bile büyük oyunların parçasıdır. Seçimler, vaatler, cüzdanlar... hepsi aynı
    # Ama şimdi sadece gülümse.
    
    time.sleep(1.5)
    return random.choice(senaryolar)

def main():
    print("=" * 50)
    print("  SOKAKTA BULUNAN PARA KADER ALGORİTMASI")
    print("  Bilimsel değil, komik evet.")
    print("=" * 50)
    
    try:
        giris = input("\nSokakta kaç TL buldun? (sadece sayı, örn: 5 veya 12.5): ")
        miktar = float(giris.replace(',', '.'))
        print("\n🔮 Kader hesaplanıyor... lütfen bekleyin (gerçek algoritma değil)\n")
        sonuc = kader_hesapla(miktar)
        print(sonuc)
    except ValueError:
        print("\nSadece sayı girmelisin. Kader bile sayı ister, sen de iste.")
    except KeyboardInterrupt:
        print("\n\nKaderi yarıda kestin. Cesur ama gereksiz.")
    
    print("\n" + "-" * 40)
    print("DAMGA & İMZA")
    print("Tarih: 23 Ekim 2026")
    print("İsim: Kayyum Grok")
    print("Mühür: Bu repo absürt bir şekilde ciddiye alınmıştır.")
    print("Not: Ciddi değil. Ama ciddiymiş gibi yazıldı.")
    print("-" * 40)

if __name__ == "__main__":
    main()

# yuz-tanima-ai

Bu proje, Python, OpenCV ve [face_recognition](https://github.com/ageitgey/face_recognition) kütüphanesini kullanarak yüz tanıma işlemi gerçekleştiren basit bir uygulamadır. Proje, **bilinen yüzlerin** bulunduğu bir klasörü okuyarak bu kişilerin yüz özelliklerini öğenir ve daha sonra verilen bir fotoğraf veya videoda bulunan yüzleri tanımlamaya çalışr.

## Özellikler

- Belirli bir dizindeki (örneğin `known_faces/`) resimleri okuyarak bu yüzlerin **gömelerini (encoding)** çıkarır.
- Komut satırından verilen tek bir görüntüde (JPG/PNG) yüzleri tespit eder ve bilinen yüzler ile eşleştirir.
- Tanınan kişilerin isimlerini ve yüz konumlarını çıktı olarak verir ve tercihe bağlı olarak çıkan görüntü üzerine çerçeve çizerek kaydedebilir.
- Kolayca genişletilebilir; örneğin canlı kamera akışı için OpenCV kullanılabilir.

## Gereksinimler

- Python 3.7 veya üzeri
- [face_recognition](https://github.com/ageitgey/face_recognition) kütüphanesi (dlib üzerine kuruludur)
- OpenCV (`opencv-python`)
- NumPy (face_recognition ile birlikte gelir)

Bu bağımlılıkları pip ile kurabilirsiniz:

```bash
pip install face_recognition opencv-python
```

## Kullanım

Öncelikle tanınmasını istediğiniz kişilerin fotoğraflarını bir klasöre yerleştirin. Varsayılan klasör `known_faces/` dizinidir ve her kişinin resmi `isim.jpg` formatında olmalıdır.

Ardından aşağadaki gibi çalıştırabilirsiniz:

```bash
python face_recognition_script.py --known_dir known_faces --image girdi.jpg --output cikti.jpg
```

Parametreler:

- `--known_dir`: Bilinen yüz resimlerinin bulunduğu klasör.
- `--image`: Tanınacak yüzlerin bulunduğu görüntü dosyası.
- `--output`: (İsteğe bağlı) Çerçevelerin çizildiği ve isimlerin gösterildiği çıkış dosyası.

Örnek çıktı komutu:

```
Bulunan Ahmet: (Top, Right, Bottom, Left) = (120, 220, 220, 100)
Bulunan Unknown: (Top, Right, Bottom, Left) = ...
```

## Dosyalar

- **face_recognition_script.py** – Yüz tanıma mantığını içeren Python betiği.
- **README.md** – Bu dosya; proje hakkında açıklama ve kullanım bilgileri içerir.

## Nasıl Çalışır?

Betik üc ana adım içerir:

1. **Bilinen yüzleri yükleme:** `load_known_faces()` fonksiyonu verilen klasördeki her resim için yüz vektörlerini (embedding) hesaplar ve isimlerle birlikte saklar.
2. **Yüz tespiti ve tanıma:** `recognize_faces()` fonksiyonu verilen görüntüdeki yüzleri tespit eder, her yüzün encoding'ini çıkarır ve bilinen yüzler ile karşılaştırır. `face_recognition.compare_faces()` fonksiyonu eşleşmeleri döndürür.
3. **Sonuçları yazdırma veya kaydetme:** Tanınan kişiler konsola yazdırılır ve eğer `--output` parametresi verilirse OpenCV yardımı ile görüntü üzerine isimler ve çerçeveler çizilir.

Bu temel yapıyı daha karmaşık uygulamalara entegre edebilir veya gerçek zamanlı tanıma için kamera desteği ekleyebilirsiniz.

## Katkı

Geri bildirimlere ve katkılara açığım. Sorularınız veya geliştime önerileriniz için issue açabilir veya pull request gönderebilirsiniz.

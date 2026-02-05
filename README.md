# 📊 Telekomünikasyon Sektöründe Müşteri Kaybı (Churn) Tahmini

Bu çalışma, telekomünikasyon sektöründe müşteri kaybının (churn) önceden tahmin edilmesine yönelik **uçtan uca makine öğrenmesi tabanlı** bir karar destek sistemi uygulamasıdır. Kırıkkale Üniversitesi Bilgisayar Mühendisliği Bölümü kapsamında bir dönem projesi olarak geliştirilmiştir.

## 🚀 Proje Hakkında
Telekomünikasyon sektörü gibi rekabetçi pazarlarda mevcut müşteriyi elde tutmak, yeni bir müşteri kazanmaktan çok daha düşük maliyetlidir. Bu projede, müşteri davranışlarını yansıtan demografik bilgiler, abonelik türleri ve kullanım alışkanlıklarını içeren **Telco Customer Churn** veri seti kullanılarak, hangi müşterilerin hizmeti terk etme eğiliminde olduğu önceden tespit edilmektedir.

## 📁 Proje Yapısı
* **`api/`**: Modelin servis edildiği FastAPI kodları ve Jinja2 şablon motoru ile hazırlanan kullanıcı arayüzü.
* **`notebooks/`**: Veri analizi (EDA), özellik mühendisliği ve model eğitim süreçlerini içeren Jupyter defterleri.
* **`ui/`**: Projenin görsel arayüz dosyaları ve stil şablonları.

## ⚙️ Uygulanan Metotlar
* **Veri Ön İşleme:** Eksik değerlerin (TotalCharges) doldurulması, sayısal verilerin `StandardScaler` ile ölçeklendirilmesi ve kategorik verilerin `One-Hot Encoding` ile dönüştürülmesi işlemleri uygulanmıştır.
* **Algoritmalar:** Lojistik Regresyon, Rastgele Orman ve XGBoost algoritmaları eğitilerek performansları karşılaştırılmıştır.
* **Güven Aralığı:** Tahmin sonuçlarının belirsizliğini ifade etmek amacıyla **Bootstrap** yeniden örnekleme yöntemi kullanılarak %95 güven aralığı hesaplanmıştır.
* **Model Servis Etme:** Eğitilen en iyi model, **FastAPI** kullanılarak bir web servisi haline getirilmiş ve gerçek zamanlı tahmin üretecek şekilde tasarlanmıştır.


## 📊 Model Performans Sonuçları
Müşteri kaybını yakalama başarısını ifade eden **Duyarlılık (Recall)** değerinin kritik olması sebebiyle, bu alanda en yüksek skoru üreten **XGBoost** nihai model olarak seçilmiştir.

| Algoritma | Doğruluk (Acc) | Duyarlılık (Recall) | F1-Skoru | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: |
| Lojistik Regresyon | 0.74 | 0.77 | 0.61 | 0.83 |
| Rastgele Orman | 0.77 | 0.76 | 0.64 | 0.84 |
| **XGBoost (Seçilen)** | **0.75** | **0.80** | **0.63** | **0.84** |

## 🔍 Önemli Özellikler (Feature Importance)
Modelin karar verme sürecinde müşteri kaybını en güçlü şekilde açıklayan değişkenler şunlardır:
1. **Sözleşme Türü (Aydan aya):** Kısa süreli taahhütlü müşterilerin churn riski belirgin şekilde daha yüksektir.
2. **İnternet Hizmeti (Fiber Optik):** Fiber optik altyapısı kullanan müşteriler modelde yüksek risk grubu olarak öne çıkmaktadır.
3. **Müşteri Süresi (Tenure):** Şirketle olan abonelik süresi arttıkça churn olasılığı azalmaktadır.


## 🛠️ Kurulum ve Çalıştırma

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/yakupaydogan/telco-customer-churn-prediction.git](https://github.com/yakupaydogan/telco-customer-churn-prediction.git)
   cd telco-customer-churn-prediction
   ```
2. **Gerekli paketleri yükleyin:** 
    ```bash
    pip install -r requirements.txt
    ```

3. **Uygulamayı başlatın:**
    ```
    cd api
    uvicorn main:app --reload
    ```
    
Uygulama arayüzüne `http://127.0.0.1:8000` adresinden erişebilirsiniz.

---

**Hazırlayan:** Yakup Aydoğan  

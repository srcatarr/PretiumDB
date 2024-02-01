# PretiumDB
**Google SpreadSheet'i veri tabanına dönüştürün.**<br>
Google SpreadSheet tablosunu bir veri tabanı olarak kullanabilmek için geliştirilmiş Google Apps Script tabanlı bir JSON API'dır.
<br><br>
PretiumDB'nin sağladığı özellikler şunlardır:
- [x] Okuma
- [x] Oluşturma
- [x] Güncelleme
- [x] Silme

## Tabloya Bağlanmak
PretiumDB daha güvenli olması açısından kendi sistemini kullanmak yerine, Google Apps Script'i kullanarak bir ara eleman görevi görür. Bu yüzden herhangi bir API anahtarı vermez ve çalışmak için SpreadSheet tablonuzun kimliğine ihtiyaç duyar.<br>

Google SpreadSheet tablosunu açtığınızda `https://docs.google.com/spreadsheets/d/abcdef0123456789/...` şeklinde bir adresi olur. Bu adreste, `abcdef0123456789` kısmında SpreadSheet tablonuzun kimliği bulunur. Sunucuya istekleri atmak için rota `/api/abcdef0123456789/...` şeklinde olmalıdır.

## Veri Gizliliği
Önceki başlıkta denildiği gibi, PretiumDB daha güvenli olması açısından kendi sistemini kullanmak yerine, Google Apps Script'i kullanarak bir ara eleman görevi görür *(Kendi sistemimiz yazmaya üşendiğimizden değil...)*. Bu yüzden herhangi bir veriyi kaydetme ihtiyacına sahip değildir, bir günlük de kaydetmez. İsterseniz Github üzerinden kaynak kodunu inceleyebilirsiniz.

## Okumak
`/api/abcdef0123456789` rotasına bir `GET` isteğinde bulunduğunuzda, tablonun ilk sayfasındaki verileri JSON türünde geri döndürür. Örnek olarak Python'da kullanım şöyledir;
```python
import requests

response = requests.get(
    "https://.../api/abcdef0123456789"
)
```
Özel bir sayfanın verisini çekmek için `/api/abcdef0123456789/Sayfa_Adı` rotasına bir `GET` isteğinde bulunduğunuzda, tablonun `Sayfa_Adı` isimli sayfasındaki verileri JSON türünde geri döndürür.

```python
import requests

response = requests.get(
    "https://.../api/abcdef0123456789/Sayfa_Adı"
)
```

## Oluşturmak
`/api/abcdef0123456789` rotasına bir `POST` isteğinde bulunduğunuzda, tablonun ilk sayfasına yeni bir satır ekler.
```python
import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = [
    {
        "username": "deneme",
        "password": "12345"
    }
]

response = requests.post(
    "https://.../api/abcdef0123456789/",
    headers=headers,
    data=json.dumps(data)
)
```
Özel bir sayfanın verisini yenilemek için `/api/abcdef0123456789/Sayfa_Adı` rotasına bir `POST` isteğinde bulunduğunuzda, tablonun `Sayfa_Adı` isimli sayfasına yeni bir satır ekler.
```python
import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = [
    {
        "username": "deneme",
        "password": "12345"
    }
]

response = requests.post(
    "https://.../api/abcdef0123456789/Sayfa_Adı",
    headers=headers,
    data=json.dumps(data)
)
```

## Güncellemek
`/api/abcdef0123456789` rotasına bir `PATCH` isteğinde bulunduğunuzda, tablonun belirlenen satırında bulunan verileri günceller.
```python
import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = [
    1,
    {
        "username": "yasir",
        "password": "54321"
    }
]

response = requests.patch(
    "https://.../api/abcdef0123456789/",
    headers=headers,
    data=json.dumps(data)
)
```
`data` listesinin birinci elemanı güncellenecek satır numarasıdır. Özel bir sayfanın verisini yenilemek için `/api/abcdef0123456789/Sayfa_Adı` rotasına bir `PATCH` isteğinde bulunduğunuzda, tablonun `Sayfa_Adı` isimli sayfasının belirlenen satırında bulunan verileri günceller.
```python
import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = [
    1,
    {
        "username": "yasir",
        "password": "54321"
    }
]

response = requests.patch(
    "https://.../api/abcdef0123456789/Sayfa_Adı",
    headers=headers,
    data=json.dumps(data)
)
```
Aynı şekilde, `data` listesinin birinci elemanı satır numarasıdır.

**NOT: Satır numarası `data` listesinin birinci elemanının bir numara fazlasıdır. Örnek:**

| Satır Numarası | A Sütunu | B Sütun |
|--|--|--|
| 1 | username | password |
| 2 | yasir | 12345 |
| 3 | utku | 67890 |

Eğer `data` listesinin birinci elemanı `1` ise `2` iki numaralı satırı baz alır.


## Silmek
`/api/abcdef0123456789` rotasına bir `DELETE` isteğinde bulunduğunuzda, tablonun ilk sayfasının belirlenen satırını siler.

```python
import requests, json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = [1]

response = requests.delete(
    "https://.../api/abcdef0123456789/",
    headers=headers,
    data=json.dumps(data)
)
```
Özel bir sayfanın verisini yenilemek için `/api/abcdef0123456789/Sayfa_Adı` rotasına bir `DELETE` isteğinde bulunduğunuzda, tablonun `Sayfa_Adı` sayfasından belirlenen satırını siler.

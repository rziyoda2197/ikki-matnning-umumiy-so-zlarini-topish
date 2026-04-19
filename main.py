def umumiy_sozlar(matn1, matn2):
    sozlar1 = set(matn1.split())
    sozlar2 = set(matn2.split())
    umumiy_sozlar = sozlar1 & sozlar2
    return umumiy_sozlar

matn1 = "Men Google va Meta tajribasiga ega arxitektor-dasturchi"
matn2 = "Men Google va Meta tajribasiga ega arxitektor-dasturchi"

print(umumiy_sozlar(matn1, matn2))
```

```python
def umumiy_sozlar(matn1, matn2):
    sozlar1 = set(matn1.lower().split())
    sozlar2 = set(matn2.lower().split())
    umumiy_sozlar = sozlar1 & sozlar2
    return umumiy_sozlar

matn1 = "Men Google va Meta tajribasiga ega arxitektor-dasturchi"
matn2 = "Men Google va Meta tajribasiga ega arxitektor-dasturchi"

print(umumiy_sozlar(matn1, matn2))
```

Ikkita matnning umumiy so'zlarni topish uchun ikkita matnni so'zlariga ajratib, so'zlarni setga aylantirib, keyin ikkita setni birlashtib oladi. Natija sifatida umumiy so'zlarni qaytaradi.

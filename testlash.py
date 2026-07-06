# assert (tasdiqlash) — Python-ning ichida tayyor keladigan eng sodda tekshirish operatori. Uning mantiqi shunday: "Men kutgan natija mana bu, agar unday boʻlmasa, dasturni xatolik bilan toʻxtat!"
def yoshni_tekshir(yosh):
    return yosh >= 18


# TESTLASH:
# Agar yosh 20 bo'lsa, True qaytishi kerak. Buni tasdiqlaymiz:
assert yoshni_tekshir(20) == True

# Agar yosh 15 bo'lsa, False qaytishi kerak.
assert yoshni_tekshir(15) == False

# Keling, ataylab xato shart beramiz (Test yiqilishi uchun):
assert yoshni_tekshir(16) == True, "Xatolik: 16 yoshdagilar o'ta olmaydi!"

print("Hamma testlar muvaffaqiyatli o'tdi!")






# pip install pytest



# Test yoziladigan fayl nomi majburiy ravishda test_ bilan boshlanishi kerak (masalan: test_auth.py).

# Ichidagi test funksiyalari ham test_ bilan boshlanishi kerak (masalan: def test_calculator():).





# auth.py:

# def parol_yaroqlimi(parol: str) -> bool:
#     """Parol kamida 8 ta belgidan iborat bo'lishi kerak"""
#     if len(parol) >= 8:
#         return True
#     return False





# test_auth.py:
# from auth import parol_yaroqlimi


# def test_togri_parol():
#     # 8 ta belgidan uzun parol True qaytarishi kerak
#     assert parol_yaroqlimi("super_secret_123") is True


# def test_kaltka_parol():
#     # 5 ta belgili parol False qaytarishi kerak
#     assert parol_yaroqlimi("12345") is False


# def test_chegara_holat():
#     # Aynan 8 ta belgili parol ham True qaytarishi kerak
#     assert parol_yaroqlimi("abcdefgh") is True





# Agar test fayllari kopayib ketsa, alohida tests degan papka ochiladi.




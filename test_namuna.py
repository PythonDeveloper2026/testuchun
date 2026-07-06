
# 1. Xatoliklar (Exceptions) ni testlash
# utils.py:
# def boʻlish(a: float, b: float) -> float:
#     if b == 0:
#         raise ZeroDivisionError("Sonni nolga bo'lish mumkin emas!")
#     return a / b



# test_utils.py:
# import pytest
# from utils import boʻlish


# def test_normal_bolish():
#     assert boʻlish(10, 2) == 5.0


# def test_nolga_bolish_xatoligi():
#     # Faqat xatolik chiqishini tekshiradi, matniga qaramaydi
#     with pytest.raises(ZeroDivisionError):
#         boʻlish(10, 0)


# chiqqan xatolik matnini to'g'riligini ham tekshirsak boladi:
# import pytest
# from utils import boʻlish


# def test_normal_bolish():
#     assert boʻlish(10, 2) == 5.0


# def test_nolga_bolish_xatoligi():
#     # Pytest-ga ushbu blok ichida aynan shu xatolik chiqishini kutayotganimizni aytamiz
#     with pytest.raises(ZeroDivisionError) as exc_info:
#         boʻlish(10, 0)

#     # Chiqqan xatolik matni to'g'riligini ham tekshirish mumkin
#     assert str(exc_info.value) == "Sonni nolga bo'lish mumkin emas!"




# 2. Bir nechta maʼlumot bilan testlash (Parametrizatsiya)
# # Bitta funksiyani 10 xil maʼlumot bilan tekshirish uchun 10 ta alohida funksiya yozilmaydi. Buning uchun @pytest.mark.parametrize ishlatiladi.

# validator.py:
# def email_yaroqlimi(email: str) -> bool:
#     # Sodda email tekshiruvi
#     return "@" in email and email.endswith(".com")


# test_validator.py:
# import pytest
# from validator import email_yaroqlimi

# # (kiruvchi_qiymat, kutilayotgan_natija) juftliklari ro'yxati
# @pytest.mark.parametrize(
#     "test_email, expected",
#     [
#         ("abror@gmail.com", True),
#         ("info@loyiha.com", True),
#         ("notogri-email", False),
#         ("user@domain.", False),
#         ("@missing-user.com", True),  # Funksiyamizdagi cheklov bo'yicha True
#     ],
# )
# def test_email_turlari(test_email, expected):
#     assert email_yaroqlimi(test_email) == expected

# # Terminalda pytest yurgizilganda, bu xuddi 5 ta alohida testdek ishlaydi va qaysi birida xato bo'lsa, o'shani aniq ko'rsatadi.






# 3 Bir nechta assertlar bilan ishlash
# models.py:
# def student_yarat(ism: str, yosh: int):
#     # Yangi o'quvchi obyektini (yoki lug'atini) qaytaradi
#     return {
#         "name": ism.strip().title(),  # Ismning bosh harfini katta qiladi
#         "age": yosh,
#         "status": "active",
#         "role": "student",
#     }



# test_models.py:
# from models import student_yarat


# def test_student_yaratish_xususiyatlari():
#     # Funksiyani chaqiramiz
#     natija = student_yarat("  abror  ", 22)

#     # Bir nechta assert yordamida barcha maydonlarni tekshiramiz:
#     assert natija["name"] == "Abror"  # Bo'sh joylar olingan va Katta harf bo'lgan
#     assert natija["age"] == 22  # Yosh to'g'ri yozilgan
#     assert natija["status"] == "active"  # Defolt status to'g'ri
#     assert natija["role"] == "student"  # Rol to'g'ri biriktirilgan


# Ketma-ket yozilgan assertlarda agar eng birinchisi xato boʻlib yiqilsa, Python undan keyingi assertlarni oʻqib oʻtirmaydi, test oʻsha joyning oʻzidayoq toʻxtaydi.
    # assert natija["name"] == "Abror" xato boʻlsa, yosh yoki status toʻgʻrimi-yoʻqmi Git buni tekshirib koʻrmaydi. Shuning uchun bitta test ichiga bir-biriga mutlaqo aloqasi boʻlmagan narsalarni tiqishtirmaslik, faqat bitta mantiqiy obyektga tegishli narsalarnigina tekshirish kerak.






# # 4. listlar bilan ishlash:
# groups.py:
# def guruhga_qosh(guruh: list, yangi_talaba: str):
#     if yangi_talaba not in guruh:
#         guruh.append(yangi_talaba)
#     return guruh


# test_groups.py:
# from groups import guruhga_qosh


# def test_guruhga_qoshish_oqimlari():
#     bosh_guruh = ["Ali", "Vali"]

#     # Yangi odam qo'shamiz
#     yangilangan_guruh = guruhga_qosh(bosh_guruh, "Olim")

#     # 1-assert: Ro'yxat uzunligi 3 ta bo'lishi kerak
#     assert len(yangilangan_guruh) == 3

#     # 2-assert: Olim ro'yxat ichida borligini tekshiramiz
#     assert "Olim" in yangilangan_guruh

#     # 3-assert: Ro'yxatning oxirgi elementi aynan Olim ekanini tekshiramiz
#     assert yangilangan_guruh[-1] == "Olim"
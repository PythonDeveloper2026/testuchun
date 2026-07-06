# pip install python-dotenv
# .gitignore fayli yaratiladi

# .env kodlari:
# DB_HOST=localhost
# DB_PORT=5432
# DB_NAME=my_database
# DB_USER=postgres
# DB_PASSWORD=secret_password_123



# gitignore fayliga .env deb yoziladi


# import os
# import psycopg2
# from dotenv import load_dotenv

# # .env faylidagi ma'lumotlarni muhitga (os.environ) yuklash
# load_dotenv()

# # Ma'lumotlarni o'qib olish
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")


# def connect_to_db():
#     try:
#         # Postgresql ga ulanish
#         connection = psycopg2.connect(
#             host=DB_HOST,
#             port=DB_PORT,
#             database=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#         )
#         print("PostgreSQL-ga muvaffaqiyatli ulandik!")
#         return connection

#     except Exception as error:
#         print(f"Ulanishda xatolik yuz berdi: {error}")


# if __name__ == "__main__":
#     conn = connect_to_db()
#     if conn:
#         conn.close()






# .env.example fayli:
# DB_HOST=your_host_here
# DB_PORT=5432
# DB_NAME=your_db_name
# DB_USER=your_user
# DB_PASSWORD=your_password






# .gitignore fayli ga yana masalan, venv, pycache larni yozish mumkin:
# venv/
# __pycache__/

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
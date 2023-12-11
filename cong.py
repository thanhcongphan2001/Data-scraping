import psycopg2

# Thay thế các giá trị dưới đây bằng thông tin kết nối của bạn
database_name = 'postgres'
user = 'postgres'
password = '12345678'
host = 'localhost'
port = 5432

# Kết nối đến cơ sở dữ liệu
connection = psycopg2.connect(
    database=database_name,
    user=user,
    password=password,
    host=host,
    port=port
)


cursor = connection.cursor()

# Thực hiện truy vấn SQL
cursor.execute("SELECT * FROM tablequan1")

# Lấy kết quả
result = cursor.fetchall()
print(result)

# Đóng cursor và kết nối
cursor.close()
connection.close()

# 從模組 import 特定函式
from myModule import after_discount, FileEditor

# 簡單斷句
if __name__ == "__main__":

    # after_discount(4500)

    """
    file = FileEditor("../Module2/2-1.py")
    texts = file.get_text()
    print(texts)
    """

    # 建立物件
    file = FileEditor("./test.txt")
    file.insert_text("Hello World!!\n")

    data = file.get_text()
    print(data)


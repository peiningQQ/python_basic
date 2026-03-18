class FileEditor:

    # 建構函式 -> 在物件建立的時候 要給我 file_path
    def __init__(self, file_path):
        self.file_path = file_path

    # 定義 Method
    def get_text(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            texts = f.read()

        return texts

    def insert_text(self, text):
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(text)


# 折扣後金額
def after_discount(total, threshold=2000, discount=200):
    if total <= 0:
        return 0
    
    if total >= threshold:
        # 需要折幾個 200
        total -= discount * (total//threshold)
    
    print(f"折扣後: {total} 元")
    return total

# print(f"myModule 的 __name__ : {__name__}")

if __name__ == "__main__":

    # 測試模組
    after_discount(3000)


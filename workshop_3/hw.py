"""

int("7") -> 7 (რიცხვი)
int("13") -> 13 (რიცხვი)
int("1A3") -> Error
რა ხდება როცა რიცხვი გადაგყავთ bool -ში

1 byte - 8 bit
A - 65
|0|0|0|0|0|0|0|1|
5 - bool(5)   -> True 
0 - bool(0)   -> False
-1 - bool(-1) -> True

გატესეთ რამდენიმე რიცხვი რომ სტრინგში გადაიყვანოთ
5 -> str(5) ?

სტრინგი bool-ში
bool("") -> False
bool(" ")
bool("A")
bool("0")

bool -> int
int(True)  -> 1
int(False) -> 0
"""
print(int(True))
print(int(False))

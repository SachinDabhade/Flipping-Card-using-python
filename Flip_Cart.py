# ************************* Flipping card assignment ***************************

# This is the Practice problem to solve the following problem statement
"""
20 random cards are placed in a row all faces down. A turn consists of taking two adjacent
card where the left 1 is faced up and the right one can be faced up or faced down and flipping
them both. Show that this process can be terminate.(With all the cards facing up)
"""

def transform(data):
    for i in range(len(data) - 1):
        if data[i] == '0' or data[i] == '1':
            if data[i] == '1':
                data[i] = '0'
                if data[i + 1] == '1':
                    data[i + 1] = '0'
                else:
                    data[i + 1] = '1'
        else:
            return "none"
    return str(data)

if __name__ == '__main__':
    while True:
        try:
            data = list(input("Enter the number ( Only 1 and 0 are acceptable) : "))
        except Exception as E:
            print("Something went wrong...!")
        else:
            if transform(data=data) != "none":
                print(f"This is the processed number: {transform(data=data)}")
            else:
                print("Only 1 and 0 numbers are allowed..!")
        continue

from src.day3 import Part2

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    ob = Part2(file_name=file_name)
    print(ob.sum_part_numbers())
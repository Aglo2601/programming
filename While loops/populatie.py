# 1200 / 3 = 400 nieuwe lama’s geboren. Maar er zijn ook 1200 / 4 = 300

# n/4 lamas overlijden
# n/3 lamas geboren
# n/4-n/3 + n=e
# start: =n
def calculate_years(start_size, end_size,):
    # overgebleven = n / 4 - n/3 + n

    years = 0
    n = start_size
    while n < end_size:
        n = n - n/4 + n/3
        years += 1

    return years

if __name__ == '__main__':

    start_size = int(input("Startgrootte: "))
    while start_size <=8:
        start_size = int(input("Startgrootte: "))

    end_size = int(input("Eindgrootte: "))
    while end_size <= start_size:
        end_size = int(input("Eindgrootte: "))
    jaren = calculate_years(start_size, end_size)
    print(f"Jaren: {jaren}")

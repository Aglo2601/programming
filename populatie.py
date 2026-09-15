def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    """

    years = 0
    n = start_size
    while n < end_size:
        born = n // 3
        dead = n // 4
        n = n + born - dead
        years += 1
    return years

if __name__ == '__main__':
   # Vraag startgrootte (>= 9)
   while True:
       s = input("Startgrootte: ").strip()
       if not s.isdigit():
           continue
       start = int(s)
       if start >= 9:
           break

   # Vraag eindgrootte (> start)
   while True:
       s = input("Eindgrootte: ").strip()
       if not s.isdigit():
           continue
       end = int(s)
       if end > start:
           break

   jaren = calculate_years(start, end)
   print(f"Jaren: {jaren}")

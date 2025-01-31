print("Convert human years to dog years: how old is your dog?")
human_years = int(input())
dog_years = 0

if human_years < 0:
    print("Error: Age cannot be negative")
else:
    if human_years <= 2:
        dog_years = 10.5 * human_years
        print("Your dog is {} years old in dog years.".format(dog_years))
    else:
        dog_years = int(10.5 * 2) + 4 * (human_years - 2)
        print("Your dog is {} years old in dog years.".format(dog_years))
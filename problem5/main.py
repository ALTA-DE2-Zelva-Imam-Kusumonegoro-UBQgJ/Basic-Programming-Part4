def mean_median(angka):
    if len(angka) == 0:
        return None
    
    mean = sum(angka) / len(angka)
    
    sort_angka = sorted(angka)
    if len(angka) % 2 == 0:
        median = (sort_angka[int(len(angka)*0.5 - 1)] + sort_angka[int(len(angka)*0.5)]) / 2
    else:
        median = sort_angka[len(angka)//2]
    
    # Return a tuple containing mean and median
    return round(mean, 1), round(median, 1)


if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)
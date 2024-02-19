def draw_xyz(N):
    result =""
    for i in range(1, N*N + 1):
        if i % 3 == 0:
            result +="X "
        elif i % 2 != 0:
            result +="Y "
        else:
            result +="Z "
        if i % N == 0:
            result += "\n"
    return result



if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
  
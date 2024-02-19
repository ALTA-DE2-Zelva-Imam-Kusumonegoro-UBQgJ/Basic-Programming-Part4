
def play_with_asterisk(n):
    result = ""
    for i in range(n):
        for j in range(n - i -1):
            result +=" " 
        for k in range(i + 1):
            result += "* "
        result += "\n"
    return result

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """

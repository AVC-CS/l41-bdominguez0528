def main():

    N = int(input('Enter the number N: '))
    result = []
    
    for i in range(N + 1):
        print(2 ** i)
        result.append(2 ** i)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

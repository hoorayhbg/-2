try:
    somefile = open("C:\\Users\\Александр\\Desktop\\где я")
    try:
        somefile.write("где танки?")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)




    FILENAME = "messages.txt"

    messages = list()

    for i in range(4):
        message = input("эм " + str(i + 1) + ": ")
        messages.append(message + "\n")


    with open(FILENAME, "a") as file:
        for message in messages:
            file.write(message)


    print("эм 2.0")
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end="?")
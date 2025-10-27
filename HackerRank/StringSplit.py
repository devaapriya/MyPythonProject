num=int(input())
if 1<=num<=10 :
    for i in range(num):
        ip_string = input()
        if 2<=len(ip_string)<=10000 :
            odd_indexed = ""
            even_indexed = ""
            for i in range(len(ip_string)):
                # print(i, ip_string[i])
                if i%2 == 0 :
                    even_indexed += ip_string[i]
                else :
                    odd_indexed += ip_string[i]
            print(even_indexed, odd_indexed)
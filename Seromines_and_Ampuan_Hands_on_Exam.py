name1 = "Ralph Joshua Seromines"
name2 = "Ayyah Ampuan"
print("By:", name1,"and", name2)

decimal_number = eval(input("Please enter a decimal number: "))
print("[1] Decimal number to Binary number\n[2] Decimal number to Octal\n[3] Decimal number to Hexadecimal")
the_conversion_choice = int(input("Select 1,2 or 3:"))


if the_conversion_choice == 1:
    result = format(decimal_number, 'b')
    print("Decimal", decimal_number, "Converted to Binary Number is", result)
elif the_conversion_choice == 2:
    result = format(decimal_number, 'o')
    print("If the Decimal", decimal_number, "Converted to Octal Number is", result)
elif the_conversion_choice == 3:
    result = format(decimal_number, 'x')
    print("If the Decimal", decimal_number, "Converted to Hexadecimal Number is", result)
else:
    result = "Bugok ka?!!! 1 ,2 og 3 raman sa selection. BOBO!!, Undang Skwela uii uli dadto!!"
    print(result)





def vitamins():
    total = 0
    vitamin_name = []
    price = []
    money =[]
    amount_of_vitamins =[]
    while True:
        print("""List Vitamin\n
        1. Blackmores Koala Kids Body Shield                    \t : 200000 
        2. Stimuno Syrup                                        \t : 45000
        3. Holisticare Ester C Kids                             \t : 43000
        4. Vidoran Gummy Multivitamin                           \t : 15000
        5. Imboost Kids Syrup                                   \t : 75000
        6. Weliness Multi Teen                                  \t : 150000
        7. Pharmaton Formula                                    \t : 60000
        8. ABC Plus Vitamin                                     \t : 130000
        9. Cerebrovit X-cel                                     \t : 25000
        10. Natures Plus POW TEEN                               \t : 400000
        11. Neurobiun Fore                                      \t : 40000
        12. Redoxon Triple                                      \t : 35000
        13. Blackmores Vitamin D3                               \t : 15000
        14. Curcuma Plus Grow Emulsiun                          \t : 40000
        15. Vitamin C Ipi                                       \t : 40000
        16. Viostin Kaplet                                      \t : 34000
        17. Enervon C kaplet                                    \t : 40000
        18. Sangobion Vito-Tonik                                \t : 40000
        19. Kirklan Mature Multi                                \t : 300000
        20. Ester c Holisticare                                 \t : 50000
        21. Femmy Trimune and Femmy Vitamin D3                  \t : 65000
        22. Realfood Royal Wellness                             \t : 37000
        23. Nature's Way                                        \t : 43000
        24. Healthy Care ulta Premium Propolis                  \t : 78000
        25. Enervon-C Multivitamin                              \t : 50000
        26. Nutrimax Complete Plus                              \t : 33000
        27. Fruit 18                                            \t : 74000
        28. Vegeblend for Adults                                \t : 60000
        29. Stimuno Forte                                       \t : 55000
        30. Imboost Force                                       \t : 77000
        31. Blackmores Vitamin C                                \t : 60000
        32. Holisticare Ester C                                 \t : 54000
        33. Redoxon Fortimun EFF                                \t : 75000
        34. Zevit Grow                                          \t : 70000
        35. Puritan's Pride Biotin                              \t : 89000
        36. CDR                                                 \t : 100000
        37. Youvit                                              \t : 91000
        38. Blackmores Multivitamin                             \t : 92000
        39. Renovit                                             \t : 86000
        40. Fatigon                                             \t : 56000
        41. Pharmaton Formula                                   \t : 56000
        42. Natural Factors                                     \t : 43000
        43. Wellness Echinacea                                  \t : 64000
        44. Phytogreen Adults                                   \t : 60000
        45. Antioxidants                                        \t : 70000
        46. Hemaviton Stamina Plus                              \t : 75000
        47. Enervon C Active                                    \t : 55000
        48. Gummy Multivitamin                                  \t : 130000
        49. Cerebrovit X-cel                                    \t : 66000
        50. Stimuno Forte                                       \t : 100000
            
        """)
        
        kode = int(input("Enter your item number : "))
        if kode == 1:
            vitamin_name.append('Blackmores Koala Kids Body Shield')
            price.append(200000)
            total += 200000
            
        elif kode == 2:
            vitamin_name.append('Stimuno Syrup')
            price.append(45000)
            total += 45000
            
        elif kode == 3:
            vitamin_name.append('Holisticare Ester C Kids')
            price.append(43000)
            total += 43000
            
        elif kode == 4:
            vitamin_name.append('Vidoran Gummy Multivitamin')
            price.append(15000)
            total += 15000
            
        elif kode == 5:
            vitamin_name.append('Imboost Kids Syrup')
            price.append(75000)
            total += 75000
            
        elif kode == 6:
            vitamin_name.append('Weliness Multi Teen')
            price.append(15000)
            total += 15000
            
        elif kode == 7:
            vitamin_name.append('Pharmaton Formula')
            price.append(60000)
            total += 60000
            
        elif kode == 8:
            vitamin_name.append('ABC Plus Vitamin')
            price.append(130000)
            total += 130000
            
        elif kode == 9:
            vitamin_name.append('Cerebrovit X-cel')
            price.append(25000)
            total += 25000
            
        elif kode == 10:
            vitamin_name.append('Natures Plus POW TEEN')
            price.append(400000)
            total += 400000
            
        elif kode == 11:
            vitamin_name.append('Neurobiun Fore')
            price.append(40000)
            total += 40000
            
        elif kode == 12:
            vitamin_name.append('Redoxon Triple')
            price.append(35000)
            total += 35000
        
        elif kode == 13:
            vitamin_name.append('Blackmores Vitamin D3')
            price.append(15000)
            total += 15000
            
        elif kode == 14:
            vitamin_name.append('Curcuma Plus Grow Emulsiun')
            price.append(40000)
            total += 40000
            
        elif kode == 15:
            vitamin_name.append('Vitamin C Ipi')
            price.append(40000)
            total += 40000
            
        elif kode == 16:
            vitamin_name.append('Viostin Kaplet')
            price.append(34000)
            total += 34000
            
        elif kode == 17:
            vitamin_name.append('Enervon C Kaplet')
            price.append(40000)
            total += 40000
            
        elif kode == 18:
            vitamin_name.append('Sangobion Vito-Tonik')
            price.append(40000)
            total += 40000
            
        elif kode == 19:
            vitamin_name.append('Kirklan Mature Multi')
            price.append(300000)
            total += 300000
            
        elif kode == 20:
            vitamin_name.append('Ester c Holisticare')
            price.append(50000)
            total += 50000
        
        elif kode == 21:
            vitamin_name.append('Femmy Trimune and Femmy Vitamin D3')
            price.append(65000)
            total += 65000
            
        elif kode == 22:
            vitamin_name.append('Realfood Royal Wellness')
            price.append(37000)
            total += 37000
        
        elif kode == 23:
            vitamin_name.append("Nature's Way")
            price.append(43000)
            total += 43000
        
        elif kode == 24:
            vitamin_name.append('Healthy Care ulta Premium Propolis')
            price.append(78000)
            total += 78000
        
        elif kode == 25:
            vitamin_name.append('Enervon-C Multivitamin')
            price.append(50000)
            total += 50000
        
        elif kode == 26:
            vitamin_name.append('Nutrimax Complete Plus')
            price.append(33000)
            total += 33000
        
        elif kode == 27:
            vitamin_name.append('Fruit 18')
            price.append(74000)
            total += 74000
        
        elif kode == 28:
            vitamin_name.append('Vegeblend for Adults')
            price.append(60000)
            total += 60000
        
        elif kode == 29:
            vitamin_name.append('Stimuno Forte')
            price.append(55000)
            total += 55000
            
        elif kode == 30:
            vitamin_name.append('Imboost Force')
            price.append(77000)
            total += 77000
        
        elif kode == 31:
            vitamin_name.append('Blackmores Vitamin C')
            price.append(60000)
            total += 60000
            
        elif kode == 32:
            vitamin_name.append('Holisticare Ester C')
            price.append(54000)
            total += 54000
        
        elif kode == 33:
            vitamin_name.append('Redoxon Fortimun EFF')
            price.append(75000)
            total += 75000
        
        elif kode == 34:
            vitamin_name.append('Zevit Grow')
            price.append(70000)
            total += 70000
        
        elif kode == 35:
            vitamin_name.append("Puritan's Pride Biotin")
            price.append(89000)
            total += 89000
        
        elif kode == 36:
            vitamin_name.append('CDR')
            price.append(100000)
            total += 100000
        
        elif kode == 37:
            vitamin_name.append('Youvit')
            price.append(91000)
            total += 91000
        
        elif kode == 38:
            vitamin_name.append('Blackmores Multivitamin')
            price.append(92000)
            total += 92000
        
        elif kode == 39:
            vitamin_name.append('Renovit')
            price.append(86000)
            total += 86000
        
        elif kode == 40:
            vitamin_name.append('Fatigon')
            price.append(56000)
            total += 56000
        
        elif kode == 41:
            vitamin_name.append('Pharmaton Formula')
            price.append(56000)
            total += 56000
        
        elif kode == 42:
            vitamin_name.append('Natural Factors')
            price.append(43000)
            total += 43000
        
        elif kode == 43:
            vitamin_name.append('Wellness Echinacea')
            price.append(64000)
            total += 64000
        
        elif kode == 44:
            vitamin_name.append('Phytogreen Adults')
            price.append(60000)
            total += 60000
        
        elif kode == 45:
            vitamin_name.append('Antioxidants')
            price.append(70000)
            total += 70000
        
        elif kode == 46:
            vitamin_name.append('Hemaviton Stamina Plus')
            price.append(75000)
            total += 75000
        
        elif kode == 47:
            vitamin_name.append('Enervon C Active')
            price.append(55000)
            total += 55000
        
        elif kode == 48:
            vitamin_name.append('Gummy Multivitamin')
            price.append(130000)
            total += 130000
        
        elif kode == 49:
            vitamin_name.append('Cerebrovit X-cel')
            price.append(66000)
            total += 66000
        
        elif kode == 50:
            vitamin_name.append('Stimuno Forte')
            price.append(100000)
            total += 100000
            
        else:
            print('The code is not found')
            
        lanjut = input('do you want to continue shopping (yes/no) : ')
        if lanjut == 'no':
            print("")
            break
        
    print('Name of items purchased : ', vitamin_name)
    print('price of all items : ', price)
    print('total price of vitamins : ', total, '\n')

    money = int(input('enter payment money : '))
    if money > total:
        print('Money changes : ', money - total)
    elif money == total:
        print('No change')
    else:
        print('You need ', total - money)
    print("Thank you for your purchase")
def left_join(ht, ht1):
    result = []
    for key in ht:
        if key in ht1:
            value = ht1[key]
        else:
            value = 'NULL'
        result.append([key, ht[key], value])
    return result

if __name__ == "__main__":
    ht = {'fond':'enamored','wrath':'anger','diligent':'employed','outift':'garb','guide':'usher'}
    ht1 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    print(left_join(ht, ht1))
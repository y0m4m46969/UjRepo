szoveg=""
try:
    with open("scifi_input_v2.txt", encoding='utf-8') as fajl:
        szoveg=fajl.read()
except IOError as ex:
    print(f"fajl megnyitas hiba: {ex}")
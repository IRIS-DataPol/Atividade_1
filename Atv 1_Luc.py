import pandas as pd


def load_position_data():
    xlsx_path = "Arquivos/Posicoes.xlsx"
    df = pd.read_excel(xlsx_path, engine='openpyxl')
    return pd.read_excel(xlsx_path, engine='openpyxl', header=4, usecols="A,B,T,AG,AS,AX,BM,CA,CK,CO",
                         names=['UF', 'Cidade', df.iloc[0][19], df.iloc[0][32], df.iloc[0][44], df.iloc[0][49],
                                df.iloc[0][64], df.iloc[0][78], df.iloc[0][88], df.iloc[2][92]])


def list_of_items(data):
    lst = list(data.items())
    lst = list(lst[0])
    lst = list(lst[1])
    lst = lst[2:]
    return lst


def create_dataset_list(lst):
    data = []
    for col in columns:
        column = pd.DataFrame(lst, columns=[col])
        column_data = list_of_items(column)
        for idx, item in enumerate(column_data):
            if len(data) <= idx:
                data.append([item])
            else:
                data[idx].append(item)
    for city in data:
        city.append(sum(city[2:]))
    return data


def handling_input(col, data):
    print("Coloque uma cidade para ver seus índices")
    print("Ou o nome de um índice para ver a cidade que mais se destaca nele")
    print("(Enter para sair)")
    entry = input()
    if entry == "Top":
        print("As cidades com melhores índices são:")
        data.sort(key=lambda x: x[-1])
        for i in range(5):
            print(data[i][1])
        print()
        return True
    try:
        idx = col.index(entry)
        data.sort(key=lambda x: x[idx])
        print("O top 5 de cidades com melhor ", entry, ":", sep='')
        for i in range(5):
            print(data[i][1], "em:", data[i][idx], "Lugar")
        print()
        return True
    except ValueError:
        for i, city in enumerate(data):
            if entry == city[1]:
                for index, cl in enumerate(col):
                    print(cl, ":", sep='', end=' ')
                    print(city[index])
                print()
                return True
        if entry == '':
            return False
        print("Input inválido!!!")
        print()
        return True


if __name__ == '__main__':
    cities = load_position_data()
    columns = list(cities)
    all_data = create_dataset_list(cities)
    while handling_input(columns, all_data):
        pass

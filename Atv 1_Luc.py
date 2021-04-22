import pandas as pd


def list_of_items(data):
    lst = list(data.items())
    lst = list(lst[0])
    lst = list(lst[1])
    lst = lst[2:]
    return lst


def create_dataset_list():
    data = []
    for col in columns:
        column = pd.DataFrame(file, columns=[col])
        column_data = list_of_items(column)
        for idx, item in enumerate(column_data):
            if len(data) <= idx:
                data.append([item])
            else:
                data[idx].append(item)
    return data


def handle_input(col, data):
    print("Coloque uma cidade para ver seus índices")
    print("Ou o nome de um índice para ver a cidade que mais se destaca nele")
    print("(Enter para sair)")
    entry = input()
    try:
        idx = col.index(entry)
        data.sort(key=lambda x: x[idx], reverse=True)
        print("O top 5 de cidades com melhor ", entry, ":", sep='')
        for i in range(5):
            print(data[i][1], "com:", data[i][idx])
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
    file = pd.read_excel(r'Arquivos/Posicoes.xlsx')
    columns = list(file)
    all_data = create_dataset_list()
    while handle_input(columns, all_data):
        pass





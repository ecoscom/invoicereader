import tabula



def nota_Inter(tables):
    ordens = tables[2]
    #print(ordens)
    
    ordens.columns = ['Praça', 'C/V - Tipo mercado', 'Título', 'Obs.', 'Quantidade', 'Preço liquidação', 'Compra/Venda', 'D/C']
    for index, row in ordens.iterrows(): 
        if row[0] != '1-Bovespa':
            ordens.drop(index, inplace=True)
        else:
            celula = str(row[1]).split(' ')
            row[1] = celula[0] 
    ordens.dropna(axis=1, how='all', inplace=True)
    save_and_open_file(ordens)


def get_nota_date(cabecalho):
    cabecalho.columns = cabecalho.columns.str.replace('\r', ':')
    print(cabecalho.columns[2])

def nota_BTG(file):
    
    tables = tabula.read_pdf(file, pages="all")
    get_nota_date(tables[0])
    resumo_negocios = tables[3]
    valor = str(resumo_negocios.iat[0,0]).split('\r')
    for dado in valor:
        print(dado)
    
    #ordens = tables[2]
    #save_and_open_file(ordens)

def save_and_open_file(ordens):
    with open('table.html', 'w') as fd:
        fd.write(ordens.to_html())
        webbrowser.open_new_tab("table.html")





if __name__ == "__main__":
    tables = tabula.read_pdf("notaBTG3.pdf", pages="all")


    #for table in tables:
        #print(table.to_html())
    nota_BTG(tables)







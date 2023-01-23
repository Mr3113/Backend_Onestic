"""
@author: Mario Marcos
"""

import pandas as pd

orders = pd.read_csv("orders.csv")
products = pd.read_csv('products.csv')
costumers = pd.read_csv('costumers.csv')

report = int(input('Reporte 1: total de cada pedido\nReporte 2: que clientes han comprado cada producto\nReporte 3: todos los pedidos ordenados descendentemente por el total en euros\n\nElige un número de reporte: '))

if report == 1:
    list_total = []
    for i in orders['products']:
        tot = 0    
        for x in i.split():
            tot += products['cost'][int(x)]
        list_total.append(tot)
    
    datos = {'id': orders['id'],
             'total': list_total}
    columns = ['id', 'total']
    df = pd.DataFrame(datos, columns=columns)
    df = df.set_index('id')
    df.to_csv('order_prices.csv')

if report==2:
    list_prod = []
    for i in products['id']:
        cust = ''
        for r in range(len(orders)):
            if str(i) in orders['products'][r].split():
                cust += str(orders['customer'][r]) + ' '
        list_prod.append(cust.strip())
    
    datos = {'id': products['id'],
             'customer_ids': list_prod}
    columns = ['id', 'customer_ids']
    df = pd.DataFrame(datos, columns=columns)
    df = df.set_index('id')
    df.to_csv('product_costumers.csv')

if report==3:
    list_total = []
    for c in costumers['id']:
        tot = 0
        for o in range(len(orders)):
            if c == orders['customer'][o]:
                prod = orders['products'][o]
                for x in prod.split():
                    tot += products['cost'][int(x)]
        list_total.append(tot)
    
    datos = {'id': costumers['id'],
             'name': costumers['firstname'],
             'lastname': costumers['lastname'],
             'total': list_total}
    columns = ['id','name','lastname','total']
    df = pd.DataFrame(datos, columns=columns)
    df = df.set_index('id')
    dford = df.sort_values('total',ascending=False)
    dford.to_csv('costumer_ranking.csv')
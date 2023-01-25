# Prueba técnica developer junior engineer - backend
#### Realizada por Mario Marcos Ramón

Para realizar esta prueba técnica, he descargado los 3 csvs ([customers.csv](customers.csv), [products.csv](products.csv) y [orders.csv](orders.csv)) y he creado el código necesario en jupyter notebook ([testing.ipynb](testing.ipynb)) para la ejecución de los 3 reportes solicitados y así poder realizar un testing con más detalle y comprobar que el código funcionara bien. Tras esto, he pasado este código a un archivo .py ([prueba_tecnica_backend.py](prueba_tecnica_backend.py)) en el cual se selecciona el número de reporte a ejecutar y devuelve un archivo .csv con la información solicitada:
- Para el **Reporte 1: total de cada pedido** devuelve [order_prices.csv](order_prices.csv)
- Para el **Reporte 2: que clientes han comprado cada producto** devuelve [product_customers.csv](product_customers.csv)
- Para el **Reporte 3: todos los pedidos ordenados descendentemente por el total en euros** devuelve [customer_ranking.csv](customer_ranking.csv)

## Explicación código:
En primer lugar, se importan las librerias necesarias y se guardan en variables cada uno de los csvs proporcionados. Seguidamente, se crea una variable por la cual se le pide un número al usuario, correspondiente al número del reporte que se quiera ejecutar:
### Reporte 1: total de cada pedido
Se recorren los productos de [orders.csv](orders.csv) para cada uno de los pedidos y para cada uno de los productos se accede a su coste guardado en [products.csv](products.csv). Tras esto, se va sumando este coste hasta obtener el total del coste para cada uno de los pedidos que se añade a una lista. Con los ids de los pedidos y esta lista se crea [order_prices.csv](order_prices.csv)
### Reporte 2: que clientes han comprado cada producto
Se recorren los ids de [products.csv](products.csv), se comprueba que coincidan con algún elemento del listado de productos en [orders.csv](orders.csv) para cada uno de los pedidos y de ahí se obtiene id del cliente, que se va almacenando en una lista de clientes que han comprado un producto con ese id. Esta lista y los ids de los productos se guardan en un csv llamado [product_customers.csv](product_customers.csv)
### Reporte 3: todos los pedidos ordenados descendentemente por el total en euros 
Se recorren los ids de [customers.csv](customers.csv), y cuando uno de estos costumers haga un pedido con ciertos productos, se recorre cada uno de los productos y se accede a su coste guardado en [products.csv](products.csv). Obtenemos el total de todos los productos para un cliente haciendo un sumatorio del coste de cada uno de los productos comprados por dicho cliente y esto, junto con el id, el nombre y los apellidos del cliente se alamcena en [customer_ranking.csv](customer_ranking.csv)

## Frontend:
Con todo lo anterior realizado, probé a crear una página web en la cual se pudiera seleccionar uno de los tres reportes y, tras apretar el botón de descargar, se generara un el archivo .csv correspondiente al reporte elegido. 
Todo lo necesario para crear la página web está incluido dentro de la carpeta [frontend](frontend)

## Documentación:
- Para borrar el índice que se genera a la hora de guardar el csv resultante para cada uno de los reportes, he accedido a la página web de https://www.delftstack.com/es/howto/python-pandas/pandas-remove-index/
- Para quitar el espacio en blanco que se generaba al final de la columna costumers_ids para el segundo reporte he consultado en el siguiente enlace: https://j2logo.com/eliminar-espacios-en-blanco-string-strip-python/
- Por último, para ordenar el dataFrame en el caso del último reporte, he entrado en este enlace: https://www.analyticslane.com/2019/04/29/diferentes-formas-de-ordenar-dataframes-en-pandas/

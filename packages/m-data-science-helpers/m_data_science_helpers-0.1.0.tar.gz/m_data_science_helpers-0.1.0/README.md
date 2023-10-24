# Data Science Helpers

## AWS Handler

AWSHandler es un wrapper para funcionalidades de aws. Autentica automaticamente tomando las credenciales desde el clipboard (solo tienen que copiarlas desde Get credentials --> Command Line or Programatic Access --> Copy Credentials) y luego borra el clipboard

## Instalacion

```python
!pip install m-data-science-helpers
```

## Ejemplo de uso

```python
from m_data_science_helpers.aws_utils import AWSHandler

# Con las credenciales en clipboard, crear una instancia de AWSHandler (podes obtenerlas desde desde Command Line or Programatic Access)
aws_handler = AWSHandler()
```
### Consultar datos usando Athena
```python
sql = "SELECT * FROM mi_base_de_datos.mi_tabla LIMIT 10"
database = "mi_base_de_datos"
result_df = aws_handler.query(sql, database)
print(result_df)
```
### Listar tablas y vistas en una base de datos
```python
database_info = aws_handler.list_tables("mi_base_de_datos")
print(database_info)
```
### Listar todas las bases de datos
```python
databases = aws_handler.list_data_sources()
print(databases)
```
### Guardar un DataFrame en S3
```python
aws_handler.save_df(df, 'mi_bucket', 'filename.parquet', file_format='parquet')
```
### Cargar un DataFrame desde S3
```python
loaded_df = aws_handler.load_df('mi_bucket', 'filename.parquet')
print(loaded_df)
```
### Listar todos los buckets disponibles
```python
aws_handler.list_all_buckets()
```
### Listar objetos en una carpeta específica de un bucket de S3
```python
aws_handler.list_bucket("mi_bucket", "prefijo_carpeta/")
```

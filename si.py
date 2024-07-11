import pandas as pd
import os
#muchos errores perdon xd
def cargar_productos(file_path):
    try:
        productos_df = pd.read_csv(file_path)
        print(f"Archivo {file_path} cargado exitosamente.")
        return productos_df
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except pd.errors.EmptyDataError:
        print("Error: El archivo está vacío.")
    except pd.errors.ParserError:
        print("Error: Error al analizar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

def calcular_precio_promedio(df):
    if df is not None and 'precio' in df.columns:
        return df['precio'].mean()
    else:
        print("Error: DataFrame no válido o columna 'precio' no encontrada.")
        return None

def aplicar_descuento(df, descuento):
    if df is not None and 'precio' in df.columns:
        df['precio_con_descuento'] = df['precio'].apply(lambda x: x * (1 - descuento))
    else:
        print("Error: DataFrame no válido o columna 'precio' no encontrada.")
    return df

def main():
    # ruta
    script_dir = os.path.dirname(__file__)  # Directorio del script actual
    file_path = os.path.join(script_dir, 'productos.csv')
    
    
    if not os.path.isfile(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return

    #productos desde el archivo
    productos_df = cargar_productos(file_path)
    
    #contenido del DataFrame
    if productos_df is not None:
        print("Contenido del DataFrame:")
        print(productos_df.head())
    
    #precio promedio de los productos
    precio_promedio = calcular_precio_promedio(productos_df)
    if precio_promedio is not None:
        print(f"Precio promedio: {precio_promedio}")

    
    descuento = 0.10  # descuento del 10%
    productos_df_con_descuento = aplicar_descuento(productos_df, descuento)

    if productos_df_con_descuento is not None:
        print(productos_df_con_descuento)

if __name__ == "__main__":
    main()

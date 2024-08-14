import pandas as pd

def test_read_simple_csv():
    try:
        df = pd.read_csv('curso_temp.csv')
        print("CSV simple leído correctamente:")
        print(df.head())
    except Exception as e:
        print(f"Error al leer el CSV simple: {e}")

if __name__ == "__main__":
    test_read_simple_csv()

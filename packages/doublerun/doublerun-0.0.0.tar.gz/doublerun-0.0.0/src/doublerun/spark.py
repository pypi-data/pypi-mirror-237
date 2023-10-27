import pyspark
from typing import List, Tuple
import sys

def comparison_count(df1: pyspark.sql.DataFrame, df2: pyspark.sql.DataFrame):
    print("COMPARAISON DU NOMBRE DE LIGNES".center(80, "*"))

    df1_count = df1.count()
    df2_count = df2.count()

    if df1_count!=df2_count:
        print(
            f"""
    Le nombre de lignes des deux DataFrames ne sont pas égaux :
        - Pour le DataFrame 1 on a {df1_count} lignes.
        - Pour le DataFrame 2 on a {df2_count} lignes
            """)
    else:
        print(
            f"""
    Le nombre de lignes des deux DataFrames sont égaux: {df1_count}.
            """)

        
def comparison_schema(df1: pyspark.sql.DataFrame, df2: pyspark.sql.DataFrame):
    print("COMPARAISON DU SCHEMA".center(80, "*"))
    
    if df1.schema!=df2.schema:
        print(
            f"""
    Les schémas ne sont pas équivalents.
    Dans le DataFrame 1 il y a ces colonnes manquantes par rapport au DataFrame 2:
        {[i for i in df2.columns if i not in df1.columns]}
    
    Dans le DataFrame 2 il y a ces colonnes manquantes par rapport au DataFrame 1:
        {[i for i in df1.columns if i not in df2.columns]}
            
            """)

def comparison_columns(df1: pyspark.sql.DataFrame, df2: pyspark.sql.DataFrame) -> List[str]:
    print("COMPARAISON DES COLONNES".center(80, "*"))
    
    colonnes_communes = [i for i in df2.columns if i in df1.columns]

    col_diff = len(df1.columns) - len(df2.columns)

    if col_diff:

        larger_df = 1 if len(df1.columns) > len(df2.columns) else 2
        smaller_df = 2 if len(df1.columns) > len(df2.columns) else 1
        print(
        f"""
        Le nombre de colonnes du DataFrame {larger_df} est supérieur à celui du DataFrame {smaller_df}.
            Nombre de colonnes communes entre les deux DataFrames: {len(colonnes_communes)}
            Colonnes communes entre les deux DataFrames:
                {colonnes_communes}
        """)
    
    else:
        print(
            f"""
        Le nombre de colonnes est identiques entre les deux DataFrames.
            Nombre de colonnes communes entre les deux DataFrames: {len(colonnes_communes)}
            Colonnes communes du dataframe csv et de la bdd : 
                {colonnes_communes}
        """)

    return colonnes_communes

def comparison_records(df1: pyspark.sql.DataFrame, df2: pyspark.sql.DataFrame) -> Tuple[pyspark.sql.DataFrame, pyspark.sql.DataFrame, pyspark.sql.DataFrame]:
    print("COMPARAISON DES DONNÉES ENTRE LES DEUX DATAFRAMES".center(80, '*'))

    colonnes_communes = [i for i in df2.columns if i in df1.columns]

    # Lignes présentes dans df1 pas présentes dans df2 (et vice-versa)
    left_diff = df1.select(*colonnes_communes).subtract(df2.select(*colonnes_communes))
    right_diff = df2.select(*colonnes_communes).subtract(df1.select(*colonnes_communes))

    common = df1.select(*colonnes_communes).subtract(left_diff)

    if left_diff.count()!=0 or right_diff.count()!=0:
        print(f"""
        Certaines lignes ne sont pas présentes dans les deux DataFrames:
              {left_diff.count()} lignes sont uniquement dans le DataFrame 1.
              
              {right_diff.count()} lignes sont uniquement dans le DataFrame 2.
              
              {common.count()} lignes sont présentes dans les deux DataFrames.
        """)
        
    else:
        print("Toutes les lignes du DataFrame 1 sont présentes dans le DataFrame 2.")

    
    return common, left_diff, right_diff

 
import pandas as pd


def read_table_file(filepath):
    if '.xlsx' in filepath:
        df = pd.read_excel(filepath, index_col=0)
    if '.txt' in filepath:
        df = pd.read_csv(filepath, sep='\t', index_col=0)
        df.columns = df.index
    return df


def get_matrix(df):
    out = df.set_index(['target1', 'target2'])['value'].unstack()
    out.columns.name = None
    out.index.name = None

    return out


def loadGImapTableHorlbeck_et_al(datasets_path):
    """Read GI map data.py from Horlbeck et al, _Cell_ (2018) 'Mapping the Genetic Landscape of Human Cells'
    https://doi.org/10.1016/j.cell.2018.06.010
    Table S5
    """
    filepath = f'{datasets_path}/Horlbeck_et_al_Cell_2018/mmc5.xlsx'

    tabs = pd.ExcelFile(filepath).sheet_names

    print("Load Table S5 from Horlbeck et al, _Cell_ (2018)")
    print("https://doi.org/10.1016/j.cell.2018.06.010\n")

    print("Sheet Names:\n")
    for i, t in enumerate(tabs): print(f'{i + 1}. {t}')

    sheet_name = 'gene GI scores and correlations'
    print(f'\nload "{sheet_name}" ...')

    data = pd.read_excel(filepath, index_col=[0, 1], header=[0, 1, 2], sheet_name=sheet_name)

    return data


def annGImapTable(df):
    """annotate targets in GImap table
    col 1: target 1
    col 2: target 2
    col 3: GI score
    """
    df.insert(0, 'targetType', '')

    df.loc[(df.target1.eq('non-targeting') & df.target2.eq('non-targeting')), df.columns.isin(
        ['targetType'])] = 'ctrl-ctrl'
    df.loc[(df.target1.eq('non-targeting') & ~df.target2.eq('non-targeting')), df.columns.isin(
        ['targetType'])] = 'ctrl-geneB'
    df.loc[(~df.target1.eq('non-targeting') & df.target2.eq('non-targeting')), df.columns.isin(
        ['targetType'])] = 'geneA-ctrl'
    df.loc[
        (~df.target1.eq('non-targeting') & ~df.target2.eq('non-targeting')) &
        (df.target1 == df.target2),
        df.columns.isin(['targetType'])
    ] = 'gene-gene'
    df.loc[
        (~df.target1.eq('non-targeting') & ~df.target2.eq('non-targeting')) &
        (df.target1 != df.target2),
        df.columns.isin(['targetType'])
    ] = 'geneA-geneB'

    return df

def see(df, n=3, nulls=False):
    """
    Visualizer for pandas DataFrames.  Uses missingno to 
    display the location of NANs.

    https://github.com/ResidentMario/missingno
    """
    from missingno import matrix

    print(f'shape: {df.shape}\n')
    if nulls:
        print(df.head(n))
        return matrix(df)
    else:
        return df.head(n)

def make_geodf(df, lat_col_name='latitude', lon_col_name='longitude'):
    """
    Take a dataframe with latitude and longitude columns, and turn
    it into a geopandas df.
    """
    from geopandas import GeoDataFrame
    from geopandas import points_from_xy
    df = df.copy()
    lat = df['latitude']
    lon = df['longitude']
    return GeoDataFrame(df, geometry=points_from_xy(lon, lat))

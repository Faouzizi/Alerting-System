def traiter_valeurs_extremes_continues(df, variable):
    ###############################################################
    # Cette fonction vous permettra de traiter les valeurs extrèmes
    # les valeurs extrèmes seront remplacé par moyenne dans ce cas
    ###############################################################
    q1 = df[variable].quantile([0.25]).values[0]
    q3 = df[variable].quantile([0.75]).values[0]
    IC_valeur_non_aberantes = [q1 - 2*(q3-q1), q3 + 2*(q3-q1)]
    df.loc[df[variable]<IC_valeur_non_aberantes[0], variable] = df[variable].mean()
    df.loc[df[variable]>IC_valeur_non_aberantes[1], variable] = df[variable].mean()
    return(df[variable])
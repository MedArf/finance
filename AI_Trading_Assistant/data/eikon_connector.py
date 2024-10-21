import eikon as ek

ek.set_app_key('c5859a4da1204b7cb109bdef864737b47e9f5013')


df, err = ek.get_data(['GOOG.O', 'MSFT.O', 'FB.O', 'AMZN.O', 'TWTR.K'],['TR.Revenue.date','TR.Revenue','TR.GrossProfit'],{'Scale': 6, 'SDate': 0, 'EDate': -2, 'FRQ': 'FY', 'Curn': 'EUR'})

print(df)

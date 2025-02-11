import yfinance as yf
import pandas as pd

# Définir le ticker pour l'or. Le ticker pour l'or sur Yahoo Finance est "GC=F"
ticker = "GC=F"

# Télécharger les données historiques
def get_historical_data(ticker, period, interval):
    data = yf.download(ticker, period=period, interval=interval)
    return data

# Données mensuelles pour les 10 dernières années
monthly_data = get_historical_data(ticker, period="10y", interval="1mo")
print("Monthly Data:")
print(monthly_data)

# Données hebdomadaires pour les 5 dernières années
weekly_data = get_historical_data(ticker, period="5y", interval="1wk")
print("\nWeekly Data:")
print(weekly_data)

# Données journalières pour les 2 dernières années
daily_data = get_historical_data(ticker, period="2y", interval="1d")
print("\nDaily Data:")
print(daily_data)

# Sauvegarder les données dans des fichiers CSV
monthly_data.to_csv("gold_monthly_data.csv")
weekly_data.to_csv("gold_weekly_data.csv")
daily_data.to_csv("gold_daily_data.csv")

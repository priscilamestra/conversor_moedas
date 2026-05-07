import requests

API_URL = "https://api.frankfurter.dev/v1/latest"

SUPPORTED = {"USD", "EUR", "GBP", "CHF"}


def get_rates(base: str = "BRL") -> dict:
   """
    Busca cotações em tempo real.
    Retorna um dict tipo: {"USD": 0.20, "EUR": 0.18, ...}
    significando: 1 BRL = X USD, X EUR, etc.

   """
   params = {
       "base": base,
       "symbols": ",".join(SUPPORTED)
   }
   resp = requests.get(API_URL, params=params, timeout=10)
   resp.raise_for_status() # se der 4xx/5xx, explode aqui com um erro claro

   data = resp.json()

   # Segurança extra: se por algum motivo não vier "rates"
   if "rates" not in data:
       raise RuntimeError(f"Resposta inesperada da API: {data}")
   return data["rates"]

def brl_to(currency: str, brl_value: float) -> float:
    currency = currency.upper().strip()

    if currency not in SUPPORTED:
        raise ValueError(f"Moeda não suportada: {currency}. Use: {', '.join(sorted(SUPPORTED))}")

    rates = get_rates(base="BRL")
    rate = rates[currency] # pode KeyError, mas isso é um bug se acontecer, pois já validei anterioremente
    
    # Como a API devolve 1 BRL = rate USD, então:
    return brl_value * rate
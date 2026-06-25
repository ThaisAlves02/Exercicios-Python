class Pagamento:
    def __init__(self, valor):
        self.valor = valor
    
class FormasPagamento(Pagamento):
    def __init__(self, valor):
        super().__init__(valor)

    def pagamento_pix(self):
        print(f"Seu pix no valor de {valor:.2f} foi realizado com sucesso!")
            
    def pagamento_cartao(self):
        print(f"Pagamento de {valor:.2f} aprovado no cartão de crédito.")
    
    def pagamento_boleto(self):
        print(f"Boleto de {valor:.2f} gerado com sucesso.")


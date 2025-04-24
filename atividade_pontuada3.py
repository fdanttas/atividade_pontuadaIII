import os
os.system("cls || clear")

matricula = input("Digite seu login: ")
senha = input("Digite sua senha: ")
salario = float(input("Digite seu salário: "))
vale_transporte = input("Deseja receber vale transporte? (s/n): ").strip().lower()
vale_refeicao = float(input("Digite o valor do vr: "))
plano_saude = float(input("Digite quantas pessoas tem no plano de saúde: "))

def desconto_inss():

    if salario <= 1320.00:
        desconto = salario * 0.075

    if salario >= 1320.01 <= 2571.29:
        desconto = salario * 0.09
   
    if salario >= 2571.30 <= 3856.94:
        desconto = salario * 0.12

    if salario >= 3856.95 <= 7507.49:
        desconto = salario * 0.14
      
    return desconto
descontos_inss = desconto_inss()


def imposto_renda():
    if salario >= 2112.01 <= 2826.65:
        desconto = salario * 0.075
     
    if salario >= 2826.66 <= 3544.00:
        desconto = salario * 0.15
       
    if salario >= 3544.01 <= 4256.00:
        desconto = salario * 0.225
    
    if salario > 4526.00:
        desconto = salario * 0.275
        
    return desconto
desconto_imposto_renda = imposto_renda()




quantidade_ps = plano_saude * 150
desconto_ps = quantidade_ps

desconto_vt = 0.06 * salario if vale_transporte == 's' else 0  
desconto_vr = 0.2 * vale_refeicao  

desconto_governo = desconto_imposto_renda + descontos_inss
desconto_clt = desconto_vt + desconto_ps + desconto_vr

salario_pos_governo = salario - desconto_governo
salario_liquido = salario_pos_governo - desconto_clt    

print("\n--- Folha de Pagamento ---")
print(f"Matrícula: {matricula}")
print(f"Salário Base: R$ {salario:.2f}")
print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
print(f"Desconto após imposto de renda: {desconto_imposto_renda}")
print(f"Desconto do inss: {descontos_inss}")
print(f"Desconto do plano de saúde: {desconto_ps:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")




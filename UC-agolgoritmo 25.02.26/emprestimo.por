progrma {
inicio ()
real valorImovel, salario, prestacaoMensal, limitePrestacao
        inteiro anos, meses

        escreva("Digite o valor da casa: ")
        leia(valorImovel)
        escreva("Digite o salário do comprador: ")
        leia(salario)
        escreva("Quantos anos irá pagar? ")
        leia(anos)

        meses = anos * 12
        prestacaoMensal = valorImovel / meses
        limitePrestacao = salario * 0.30

        escreva("Para pagar uma casa de R$", valorImovel, " em", anos, " anos, ")
        
        se (prestacaoMensal <= limitePrestacao) {
            escreva ("Empréstimo APROVADO!")
        } senao {
            escreva("Empréstimo negado. A prestação excede 30% do salário.")
        }

}
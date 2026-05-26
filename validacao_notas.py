# Validação de Notas de uma Turma

alunos = [
    "Ana Silva", "Bruno Souza", "Carlos Lima", "Diana Pereira", "Eduardo Costa",
    "Fernanda Rocha", "Gabriel Santos", "Helena Martins", "Igor Oliveira", "Julia Ferreira"
]

print("=" * 45)
print("   VALIDAÇÃO DE NOTAS DA TURMA")
print("=" * 45)

for aluno in alunos:
    print(f"\nAluno: {aluno}")
    print("-" * 45)
    notas = []

    for i in range(1, 4):
        nota = float(input(f"  Digite a nota {i}: "))

        while nota < 0 or nota > 10:
            print("  ⚠️  Nota inválida! Digite um valor entre 0 e 10.")
            nota = float(input(f"  Digite a nota {i} novamente: "))

        notas.append(nota)
        print(f"  Nota {i} registrada: {nota:.1f}")

    media = sum(notas) / len(notas)
    print(f"\n  📊 Média de {aluno}: {media:.1f}")
    if media >= 7:
        print(f"  ✅ Situação: Aprovado")
    elif media >= 5:
        print(f"  ⚠️  Situação: Recuperação")
    else:
        print(f"  ❌ Situação: Reprovado")

print("\n" + "=" * 45)
print("  Todas as notas foram lançadas.")
print("=" * 45)

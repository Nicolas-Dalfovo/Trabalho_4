# Sistema de Registro de Usuários com Singleton e Relatórios com Decorator

import threading

# Padrão Singleton: Registro de Usuários
class RegistroUsuarios:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # Garantir que apenas uma instância seja criada
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super().__new__(cls)
                cls._usuarios = []
        return cls._instancia

    def registrar_usuario(self, nome):
        # Adicionar um novo usuário
        self._usuarios.append(nome)
        print(f"Usuário '{nome}' registrado.")

    def listar_usuarios(self):
        # Retornar a lista de usuários
        return self._usuarios

# Padrão Decorator: Geração de Relatórios
# Classe base
class Relatorio:
    def gerar(self):
        return "Relatório base"

# Decorador base
class RelatorioDecorator(Relatorio):
    def __init__(self, relatorio):
        self._relatorio = relatorio

    def gerar(self):
        return self._relatorio.gerar()

# Decorador para bordas
class BordasDecorator(RelatorioDecorator):
    def gerar(self):
        return f"{'*' * 30}\n{self._relatorio.gerar()}\n{'*' * 30}"

# Decorador para cabeçalho
class CabecalhoDecorator(RelatorioDecorator):
    def __init__(self, relatorio, titulo):
        super().__init__(relatorio)
        self._titulo = titulo

    def gerar(self):
        return f"{self._titulo}\n{'-' * len(self._titulo)}\n{self._relatorio.gerar()}"

# Decorador para cor
class CorDecorator(RelatorioDecorator):
    def __init__(self, relatorio, cor):
        super().__init__(relatorio)
        self._cor = cor

    def gerar(self):
        return f"[{self._cor}] {self._relatorio.gerar()} [{self._cor}]"

# Menu do Sistema
def main():
    print("Sistema de Registro de Usuários")
    print("Desenvolvido por: [Nicolas Marquez Dalfovo]\n")

    registro = RegistroUsuarios()

    while True:
        print("\nMenu:")
        print("1. Registrar usuário")
        print("2. Listar usuários")
        print("3. Gerar relatório")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            registro.registrar_usuario(nome)
        elif opcao == "2":
            usuarios = registro.listar_usuarios()
            print(f"Usuários registrados: {', '.join(usuarios)}")
        elif opcao == "3":
            relatorio = Relatorio()
            titulo = "Relatório de Usuários"
            relatorio_decorado = BordasDecorator(CabecalhoDecorator(relatorio, titulo))
            print("\n" + relatorio_decorado.gerar())
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

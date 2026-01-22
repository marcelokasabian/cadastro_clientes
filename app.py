from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from arquivo import salvar_atendimento, carregar_atendimentos
from busca import buscar
from pontuacao import calcular_pontos_periodo, PONTOS
from periodo import obter_periodo_atual, formatar_data, calcular_prazos
from formatacao import normalizar_data, formatar_telefone

from datetime import datetime


class Tela(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.menu()

    def limpar(self):
        self.clear_widgets()

    # ---------------- MENU ----------------
    def menu(self):
        self.limpar()

        self.add_widget(Label(text="SISTEMA DE ATENDIMENTOS", font_size=22))

        self.add_widget(Button(text="Cadastrar atendimento", on_press=self.tela_cadastro))
        self.add_widget(Button(text="Buscar atendimento", on_press=self.tela_busca))
        self.add_widget(Button(text="Pontuação do período", on_press=self.pontos))
        self.add_widget(Button(text="Prazos 30 dias", on_press=self.prazos))
        self.add_widget(Button(text="Sair", on_press=self.sair))

        self.resultado = Label(text="", size_hint_y=None)
        self.resultado.bind(texture_size=self.resultado.setter("size"))

        scroll = ScrollView()
        scroll.add_widget(self.resultado)
        self.add_widget(scroll)

    # ---------------- CADASTRO ----------------
    def tela_cadastro(self, instance):
        self.limpar()

        self.data = TextInput(hint_text="Data (010125 ou 01/01/25)")
        self.nome = TextInput(hint_text="Nome")
        self.endereco = TextInput(hint_text="Endereço")
        self.tipo = TextInput(hint_text="Tipo (reparo ou instalacao)")
        self.telefone = TextInput(hint_text="Telefone")
        self.obs = TextInput(hint_text="Observações")

        for campo in [self.data, self.nome, self.endereco, self.tipo, self.telefone, self.obs]:
            self.add_widget(campo)

        self.add_widget(Button(text="Salvar", on_press=self.salvar))
        self.add_widget(Button(text="Voltar", on_press=lambda x: self.menu()))

    def salvar(self, instance):
        data = normalizar_data(self.data.text)
        telefone = formatar_telefone(self.telefone.text)
        tipo = self.tipo.text.lower()

        if not data:
            self.menu()
            self.resultado.text = "❌ Data inválida."
            return

        if not telefone:
            self.menu()
            self.resultado.text = "❌ Telefone inválido."
            return

        pontos = PONTOS.get(tipo, 0)

        atendimento = {
            "data": data,
            "nome": self.nome.text,
            "endereco": self.endereco.text,
            "tipo": tipo,
            "telefone": telefone,
            "observacoes": self.obs.text,
            "pontos": pontos
        }

        salvar_atendimento(atendimento)
        self.menu()
        self.resultado.text = "✅ Atendimento salvo com sucesso."

    # ---------------- BUSCA ----------------
    def tela_busca(self, instance):
        self.limpar()

        self.campo = TextInput(hint_text="Digite para buscar")
        self.add_widget(self.campo)
        self.add_widget(Button(text="Buscar", on_press=self.buscar))
        self.add_widget(Button(text="Voltar", on_press=lambda x: self.menu()))

        self.resultado = Label(text="", size_hint_y=None)
        self.resultado.bind(texture_size=self.resultado.setter("size"))

        scroll = ScrollView()
        scroll.add_widget(self.resultado)
        self.add_widget(scroll)

    def buscar(self, instance):
        termo = self.campo.text
        dados = carregar_atendimentos()
        resultados = buscar(dados, termo)

        if not resultados:
            self.resultado.text = "Nenhum resultado encontrado."
            return

        texto = ""
        for a in resultados:
            texto += (
                f"Cliente: {a['nome']}\n"
                f"Data: {a['data']}\n"
                f"Tipo: {a['tipo']}\n"
                f"Telefone: {a['telefone']}\n"
                f"Observações: {a['observacoes']}\n"
                f"Pontos: {a['pontos']}\n"
                "--------------------------\n"
            )

        self.resultado.text = texto

    # ---------------- PONTOS ----------------
    def pontos(self, instance):
        total, reparo, instalacao = calcular_pontos_periodo()
        inicio, fim = obter_periodo_atual()

        self.resultado.text = (
            f"Período: {formatar_data(inicio)} até {formatar_data(fim)}\n\n"
            f"Reparo: {reparo:.2f}\n"
            f"Instalação: {instalacao:.2f}\n"
            f"Total: {total:.2f}"
        )

    # ---------------- PRAZOS ----------------
    def prazos(self, instance):
        dados = carregar_atendimentos()
        self.resultado.text = calcular_prazos(dados)

    # ---------------- SAIR ----------------
    def sair(self, instance):
        App.get_running_app().stop()


class AppCadastro(App):
    def build(self):
        return Tela()


if __name__ == "__main__":
    AppCadastro().run()

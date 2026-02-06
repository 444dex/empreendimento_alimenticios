import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from db import conectar 


# APP PRINCIPAL

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🍽 Sistema de Empreendimento Alimentício")
        self.geometry("950x650")
        
        # Controle de Tema 
        self.tema_escuro = False
        self.style = ttk.Style(self)
        self.definir_tema_claro()

        #  Frame principal para gerenciamento de telas 
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        #  Telas 
        self.frames = {}
        telas = {
            "BoasVindas": TelaBoasVindas,
            "Login": TelaLogin,
            "Cadastro": TelaCadastro,
            "Dashboard": TelaDashboard,
            "Produtos": TelaProdutos,
            "Relatorios": TelaRelatorios,
            "Configuracoes": TelaConfiguracoes
        }

        for nome, Tela in telas.items():
            frame = Tela(self.container, self)
            self.frames[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("BoasVindas")

    def mostrar_tela(self, nome):
        frame = self.frames[nome]
        frame.tkraise()
        self.aplicar_tema_global()

    #  TEMAS 
    def definir_tema_claro(self):
        self.tema_escuro = False
        self.configure(bg="#f5f5f5")
        self.style.theme_use("clam")

        # tema claro
        self.style.configure("TFrame", background="#f5f5f5")
        self.style.configure("TLabel", font=("Segoe UI", 12), background="#f5f5f5", foreground="black")
        self.style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"), foreground="#333")
        self.style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=10, relief="flat")
        self.style.configure("TEntry", fieldbackground="white", foreground="black")

        self.style.map("TButton",
                       background=[("active", "#3700b3")],
                       foreground=[("active", "white")])

        self.style.configure("Primary.TButton", background="#6200ee", foreground="white")
        self.style.configure("Success.TButton", background="#03dac6", foreground="black")
        self.style.configure("Danger.TButton", background="#ff0266", foreground="white")
        self.style.configure("Secondary.TButton", background="#cccccc", foreground="black")
        
        # Treeview (tabela)
        self.style.configure("Treeview", 
                            background="white",
                            foreground="black",
                            fieldbackground="white")
        self.style.configure("Treeview.Heading",
                            background="#e0e0e0",
                            foreground="black",
                            relief="flat")
        self.style.map("Treeview",
                      background=[("selected", "#3700b3")],
                      foreground=[("selected", "white")])

    def definir_tema_escuro(self):
        self.tema_escuro = True
        self.configure(bg="#121212")
        self.style.theme_use("clam")

        # tema escuro
        self.style.configure("TFrame", background="#121212")
        self.style.configure("TLabel", font=("Segoe UI", 12), background="#121212", foreground="white")
        self.style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"), foreground="white")
        self.style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=10, relief="flat")
        self.style.configure("TEntry", fieldbackground="#333333", foreground="white")

        self.style.map("TButton",
                       background=[("active", "#BB86FC")],
                       foreground=[("active", "black")])

        self.style.configure("Primary.TButton", background="#BB86FC", foreground="black")
        self.style.configure("Success.TButton", background="#03dac6", foreground="black")
        self.style.configure("Danger.TButton", background="#ff0266", foreground="white")
        self.style.configure("Secondary.TButton", background="#333333", foreground="white")
        
        # Treeview (tabela)
        self.style.configure("Treeview", 
                            background="#1e1e1e",
                            foreground="white",
                            fieldbackground="#1e1e1e")
        self.style.configure("Treeview.Heading",
                            background="#333333",
                            foreground="white",
                            relief="flat")
        self.style.map("Treeview",
                      background=[("selected", "#BB86FC")],
                      foreground=[("selected", "black")])

    def alternar_tema(self):
        if self.tema_escuro:
            self.definir_tema_claro()
        else:
            self.definir_tema_escuro()
        
        
        self.aplicar_tema_global()

    def aplicar_tema_global(self):
        """Aplica o tema atual a toda a aplicação"""
        bg_color = "#121212" if self.tema_escuro else "#f5f5f5"
        fg_color = "white" if self.tema_escuro else "black"
        
        
        self.container.config(bg=bg_color)
        
        
        for nome, frame in self.frames.items():
            self.aplicar_tema_frame(frame, bg_color, fg_color)

    def aplicar_tema_frame(self, frame, bg_color, fg_color):
        """Aplica o tema a um frame específico e seus widgets"""
        try:
            if hasattr(frame, 'config'):
                try:
                    frame.config(bg=bg_color)
                except:
                    pass

            def aplicar_widget(widget):
                try:
                    widget_type = widget.winfo_class()
                    if widget_type in ['Frame', 'Labelframe']:
                        widget.config(bg=bg_color)
                    elif widget_type == 'Label':
                        widget.config(bg=bg_color, fg=fg_color)
                    elif widget_type == 'Entry':
                        widget.config(bg="#333333" if self.tema_escuro else "white",
                                     fg=fg_color,
                                     insertbackground=fg_color)
                except:
                    pass
                for child in widget.winfo_children():
                    aplicar_widget(child)
            
            aplicar_widget(frame)
            
        except Exception as e:
            print(f"Erro ao aplicar tema: {e}")




def carregar_imagem(caminho, largura, altura):
    try:
        img = Image.open(caminho)
        img = img.resize((largura, altura), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None


# TELAS 

class TelaBoasVindas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        logo = carregar_imagem("logo.png", 180, 180)
        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")
        if logo:
            tk.Label(container, image=logo).pack(pady=10)
            self.logo = logo
        ttk.Label(container, text="Bem-vindo!", style="Title.TLabel").pack(pady=10)
        ttk.Button(container, text="Entrar", style="Primary.TButton",
                   command=lambda: controller.mostrar_tela("Login")).pack(pady=10)


class TelaLogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        container = tk.Frame(self, bd=1, relief="solid")
        container.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)
        ttk.Label(container, text="Login", style="Title.TLabel").pack(pady=15)
        ttk.Label(container, text="Email:").pack(anchor="w", padx=30, pady=5)
        self.entry_email = ttk.Entry(container, width=30)
        self.entry_email.pack(pady=5)
        ttk.Label(container, text="Senha:").pack(anchor="w", padx=30, pady=5)
        self.entry_senha = ttk.Entry(container, show="*", width=30)
        self.entry_senha.pack(pady=5)
        ttk.Button(container, text="Entrar", style="Success.TButton", command=self.login).pack(pady=10)
        ttk.Button(container, text="Cadastrar Novo Usuário", style="Primary.TButton",
                   command=lambda: controller.mostrar_tela("Cadastro")).pack()

    def login(self):
        email, senha = self.entry_email.get(), self.entry_senha.get()
        try:
            conn = conectar()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
            user = cursor.fetchone()
            conn.close()
            if user:
                messagebox.showinfo("Bem-vindo", f"Login bem-sucedido: {user['nome']}")
                self.controller.mostrar_tela("Dashboard")
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar no banco: {e}")


class TelaCadastro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        container = tk.Frame(self, bd=1, relief="solid")
        container.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)
        ttk.Label(container, text="Cadastro de Usuário", style="Title.TLabel").pack(pady=15)
        ttk.Label(container, text="Nome:").pack(anchor="w", padx=30, pady=5)
        self.entry_nome = ttk.Entry(container, width=30)
        self.entry_nome.pack(pady=5)
        ttk.Label(container, text="Email:").pack(anchor="w", padx=30, pady=5)
        self.entry_email = ttk.Entry(container, width=30)
        self.entry_email.pack(pady=5)
        ttk.Label(container, text="Senha:").pack(anchor="w", padx=30, pady=5)
        self.entry_senha = ttk.Entry(container, show="*", width=30)
        self.entry_senha.pack(pady=5)
        ttk.Button(container, text="Registrar", style="Success.TButton",
                   command=self.cadastrar_usuario).pack(pady=10)
        ttk.Button(container, text="Voltar", style="Secondary.TButton",
                   command=lambda: self.controller.mostrar_tela("Login")).pack()

    def cadastrar_usuario(self):
        nome, email, senha = self.entry_nome.get(), self.entry_email.get(), self.entry_senha.get()
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)",
                           (nome, email, senha, "cliente"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.controller.mostrar_tela("Login")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")


class TelaDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="📊 Dashboard", style="Title.TLabel").pack(pady=20)
        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.4, anchor="center")
        ttk.Button(container, text="📦 Produtos", style="Primary.TButton",
                   command=lambda: controller.mostrar_tela("Produtos")).grid(row=0, column=0, padx=20, pady=20, ipadx=10, ipady=20)
        ttk.Button(container, text="📑 Relatórios", style="Success.TButton",
                   command=lambda: controller.mostrar_tela("Relatorios")).grid(row=0, column=1, padx=20, pady=20, ipadx=10, ipady=20)
        ttk.Button(container, text="⚙ Configurações", style="Secondary.TButton",
                   command=lambda: controller.mostrar_tela("Configuracoes")).grid(row=0, column=2, padx=20, pady=20, ipadx=10, ipady=20)


class TelaProdutos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Gerenciar Produtos", style="Title.TLabel").pack(pady=15)

        colunas = ("ID", "Nome", "Preço", "Estoque")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings", height=10)
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=120)
        self.tabela.pack(pady=10, fill="x", padx=20)

        botoes = tk.Frame(self)
        botoes.pack(pady=10)
        ttk.Button(botoes, text="➕ Adicionar", style="Success.TButton",
                   command=self.abrir_janela_add).grid(row=0, column=0, padx=5)
        ttk.Button(botoes, text="❌ Remover", style="Danger.TButton",
                   command=self.remover_produto).grid(row=0, column=1, padx=5)
        ttk.Button(botoes, text="⬅ Voltar", style="Secondary.TButton",
                   command=lambda: controller.mostrar_tela("Dashboard")).grid(row=0, column=2, padx=5)

        self.carregar_produtos()

    def carregar_produtos(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
            for row in cursor.fetchall():
                self.tabela.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar produtos: {e}")

    
    def abrir_janela_add(self):
        janela = tk.Toplevel(self)
        janela.title("Adicionar Produto")
        janela.geometry("400x400")

        ttk.Label(janela, text="Cadastro de Produto", style="Title.TLabel").pack(pady=15)

        # Campos
        ttk.Label(janela, text="Nome:").pack(anchor="w", padx=20, pady=5)
        entry_nome = ttk.Entry(janela, width=30)
        entry_nome.pack(pady=5)

        ttk.Label(janela, text="Preço:").pack(anchor="w", padx=20, pady=5)
        entry_preco = ttk.Entry(janela, width=30)
        entry_preco.pack(pady=5)

        ttk.Label(janela, text="Estoque:").pack(anchor="w", padx=20, pady=5)
        entry_estoque = ttk.Entry(janela, width=30)
        entry_estoque.pack(pady=5)

        # Combobox 
        ttk.Label(janela, text="Categoria:").pack(anchor="w", padx=20, pady=5)
        categorias = []
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM categorias")
            categorias = cursor.fetchall()  
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar categorias: {e}")

        
        categoria_dict = {nome: id for id, nome in categorias}
        combo_categoria = ttk.Combobox(janela, values=list(categoria_dict.keys()), state="readonly", width=28)
        combo_categoria.pack(pady=5)

        def salvar():
            nome = entry_nome.get()
            preco = entry_preco.get()
            estoque = entry_estoque.get()
            categoria_nome = combo_categoria.get()

            if not nome or not preco or not estoque or not categoria_nome:
                messagebox.showwarning("Aviso", "Preencha todos os campos!")
                return

            categoria_id = categoria_dict[categoria_nome]

            try:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO produtos (nome, preco, estoque, categoria_id) VALUES (%s, %s, %s, %s)",
                    (nome, preco, estoque, categoria_id)
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
                janela.destroy()
                self.carregar_produtos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")

        ttk.Button(janela, text="Salvar", style="Success.TButton", command=salvar).pack(pady=10)
        ttk.Button(janela, text="Cancelar", style="Secondary.TButton", command=janela.destroy).pack()
    
    def remover_produto(self):
        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto para remover.")
            return
        produto_id = self.tabela.item(item, "values")[0]
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id=%s", (produto_id,))
            conn.commit()
            conn.close()
            self.carregar_produtos()
            messagebox.showinfo("Sucesso", "Produto removido!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao remover produto: {e}")

class TelaRelatorios(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="📑 Relatórios", style="Title.TLabel").pack(pady=20)
        container = tk.Frame(self)
        container.pack(pady=20, fill="both", expand=True)
        colunas = ("Nome", "Preço", "Estoque")
        self.tabela = ttk.Treeview(container, columns=colunas, show="headings", height=10)
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=150)
        self.tabela.pack(pady=10, fill="x")
        ttk.Button(self, text="⬅ Voltar", style="Secondary.TButton",
                   command=lambda: controller.mostrar_tela("Dashboard")).pack(pady=20)
        self.carregar_relatorios()

    def carregar_relatorios(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT nome, preco, estoque FROM produtos ORDER BY preco DESC LIMIT 5")
            for row in cursor.fetchall():
                self.tabela.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar relatórios: {e}")


class TelaConfiguracoes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.4, anchor="center")
        ttk.Label(container, text="⚙ Configurações", style="Title.TLabel").pack(pady=20)
        ttk.Button(container, text="🔄 Alterar usuário",
                   command=lambda: controller.mostrar_tela("Login")).pack(pady=10)
        ttk.Button(container, text="🌙/☀ Alternar Tema",
                   command=controller.alternar_tema).pack(pady=10)
        ttk.Button(container, text="🚪 Sair", command=controller.quit).pack(pady=10)
        ttk.Button(container, text="⬅ Voltar",
                   command=lambda: controller.mostrar_tela("Dashboard")).pack(pady=10)




if __name__ == "__main__":
    app = App()
    app.mainloop()

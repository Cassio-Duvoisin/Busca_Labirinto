class TreeNode:
    def __init__(self, data):
        self.data = data  # O dado armazenado no nó (tupla coordenada)
        self.previous = None # Referência ao antecessor
        self.branch1 = None  # Referência ao filho 1
        self.branch2 = None  # Referência ao filho 2
        self.branch3 = None  # Referência ao filho 3

# Função para inserir um novo nó na árvore binária
def insert(self, new_data):
        # Verificar quantos ramos estão vazios
        empty_branches = [branch for branch in [self.branch1, self.branch2, self.branch3] if branch is None]
        
        # Se todos os ramos estiverem cheios, não podemos adicionar o novo nó
        if not empty_branches:
            return False

        # Criar um novo nó com os dados fornecidos e adicioná-lo ao branch com o menor número
        new_node = TreeNode(new_data)
        new_node.previous = self  # Configurar a referência ao antecessor

        if self.branch1==None:
            self.branch1=new_node
        if self.branch2==None:
            self.branch2=new_node
        else: self.branch3=new_node
        
        return True
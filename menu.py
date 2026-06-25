import pygame
import sys
import os
import subprocess
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

# ==========================================
# CONFIGURAÇÕES DA JANELA E CONSTANTES
# ==========================================
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pi Game - Menu")

clock = pygame.time.Clock()

# Cores
FUNDO = (10, 12, 25)
AZUL = (40, 70, 140)
AZUL_HOVER = (80, 120, 220)
BRANCO = (240, 240, 240)
VERMELHO_BLOQUEADO = (120, 50, 50)
LARANJA = (255, 140, 60)
ROSA = (255, 90, 120)
AMARELO = (255, 220, 100)

# Controle de Estado Inicial do Menu
estado = "menu"

# ==========================================
# FUNÇÕES DE CARREGAMENTO SEGURO E AUXILIARES
# ==========================================
def carregar_fonte(tamanho):
    caminho = os.path.join(BASE_DIR, "assets", "fonts", "Press_Start_2P.ttf")
    if os.path.exists(caminho):
        return pygame.font.Font(caminho, tamanho)
    return pygame.font.SysFont("consolas", tamanho, bold=True)

fonte_titulo = carregar_fonte(36)
fonte = carregar_fonte(20)

def obter_fase_maxima():
    """Lê o arquivo de save gerado pelo main.py para saber quais fases liberar."""
    caminho_save = os.path.join(BASE_DIR, "save.json")
    if os.path.exists(caminho_save):
        try:
            with open(caminho_save, "r") as f:
                dados = json.load(f)
                return dados.get("fase_maxima", 1)
        except:
            return 1  # Se der erro, assume fase 1
    return 1  # Se não houver arquivo, assume fase 1

def carregar_fundo():
    caminho = os.path.join(BASE_DIR, "assets", "background", "fundo_menu.jpg")
    if os.path.exists(caminho):
        try:
            img = pygame.image.load(caminho)
            return pygame.transform.scale(img, (LARGURA, ALTURA))
        except:
            pass
    return None

def lancar_jogo(fase_id):
    """Para a música do menu e invoca o motor principal passando a fase de forma segura."""
    pygame.mixer.music.stop()
    pygame.quit()
    
    # Descobre o caminho absoluto exato até o arquivo main.py baseado na pasta do menu
    caminho_main = os.path.join(BASE_DIR, "main.py")
    
    # Executa o main.py passando o caminho completo e o número da fase
    subprocess.Popen([sys.executable, caminho_main, str(fase_id)])
    sys.exit()

fundo = carregar_fundo()

# Inicialização segura da Música
try:
    caminho_musica = os.path.join(BASE_DIR, "assets", "music", "menu_theme.mp3")
    if os.path.exists(caminho_musica):
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
except Exception as e:
    print(f"[AVISO] Música do menu não carregada: {e}")

# ==========================================
# INTERFACE DE BOTÕES INTERATIVOS
# ==========================================
class Botao:
    def __init__(self, x, y, w, h, texto, bloqueado=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.texto = texto
        self.bloqueado = bloqueado
        self.surf = pygame.Surface((w, h), pygame.SRCALPHA)

    def desenhar(self):
        mouse = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse)

        # Efeito de sombra/brilho traseiro
        sombra = pygame.Surface((self.rect.w + 10, self.rect.h + 10), pygame.SRCALPHA)
        pygame.draw.rect(sombra, (255, 255, 255, 40), sombra.get_rect(), border_radius=14)
        tela.blit(sombra, (self.rect.x - 5, self.rect.y - 5))

        # Determinação de cores baseado no estado do botão
        if self.bloqueado:
            cor = VERMELHO_BLOQUEADO
        else:
            cor = AZUL_HOVER if hover else AZUL

        self.surf.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, (*cor, 200), self.surf.get_rect(), border_radius=12)
        tela.blit(self.surf, self.rect.topleft)

        txt = fonte.render(self.texto, True, BRANCO)
        tela.blit(txt, (self.rect.centerx - txt.get_width() // 2, self.rect.centery - txt.get_height() // 2))

    def clicado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos)
        )

# ==========================================
# INSTANCIAÇÃO DOS ELEMENTOS DO MENU
# ==========================================
btn_jogar = Botao(500, 300, 280, 60, "JOGAR")
btn_sair = Botao(500, 390, 280, 60, "SAIR")
btn_voltar = Botao(20, 20, 160, 50, "VOLTAR")

# Buscamos a fase máxima real do arquivo antes de criar os botões das fases
fase_desbloqueada_max = obter_fase_maxima()

# Criamos os botões aplicando a trava dinamicamente logo na inicialização do script
btn_fase1 = Botao(400, 220, 480, 60, "FASE 1", bloqueado=False)

btn_fase2 = Botao(
    400, 320, 480, 60, 
    "FASE 2" if fase_desbloqueada_max >= 2 else "FASE 2 - BLOQUEADA", 
    bloqueado=(fase_desbloqueada_max < 2)
)

btn_fase3 = Botao(
    400, 420, 480, 60, 
    "FASE 3" if fase_desbloqueada_max >= 3 else "FASE 3 - BLOQUEADA", 
    bloqueado=(fase_desbloqueada_max < 3)
)

# ==========================================
# LOOP DE EXECUÇÃO PRINCIPAL
# ==========================================
while True:
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gerenciar os cliques do menu principal
        if estado == "menu":
            if btn_jogar.clicado(e):
                # Recarrega o progresso atualizado antes de exibir as fases
                fase_desbloqueada_max = obter_fase_maxima()
                
                # Aplica as travas e textos correspondentes
                btn_fase2.bloqueado = (fase_desbloqueada_max < 2)
                btn_fase2.texto = "FASE 2" if fase_desbloqueada_max >= 2 else "FASE 2 - BLOQUEADA"
                
                btn_fase3.bloqueado = (fase_desbloqueada_max < 3)
                btn_fase3.texto = "FASE 3" if fase_desbloqueada_max >= 3 else "FASE 3 - BLOQUEADA"
                
                estado = "fases"

            if btn_sair.clicado(e):
                pygame.quit()
                sys.exit()

        elif estado == "fases":
            if btn_voltar.clicado(e):
                estado = "menu"

            if btn_fase1.clicado(e):
                lancar_jogo(1)

            if btn_fase2.clicado(e):
                if not btn_fase2.bloqueado:
                    lancar_jogo(2)
                else:
                    print("Complete a Fase 1 primeiro!")

            if btn_fase3.clicado(e):
                if not btn_fase3.bloqueado:
                    lancar_jogo(3)
                else:
                    print("Complete a Fase 2 primeiro!")

    # Renderização Visual do Fundo
    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(FUNDO)

    # Renderização Estilizada do Título do Jogo
    texto_titulo = "TREASURE HUNTERS"
    sombra = fonte_titulo.render(texto_titulo, True, (20, 20, 20))
    titulo_rosa = fonte_titulo.render(texto_titulo, True, ROSA)
    titulo_laranja = fonte_titulo.render(texto_titulo, True, LARANJA)
    titulo_amarelo = fonte_titulo.render(texto_titulo, True, AMARELO)

    pos_x_tit = LARGURA // 2 - titulo_rosa.get_width() // 2
    tela.blit(sombra, (pos_x_tit + 5, 85))
    tela.blit(titulo_rosa, (pos_x_tit, 80))
    tela.blit(titulo_laranja, (pos_x_tit, 78))
    tela.blit(titulo_amarelo, (pos_x_tit, 76))

    # Renderização Condicional dos Botões
    if estado == "menu":
        btn_jogar.desenhar()
        btn_sair.desenhar()
    elif estado == "fases":
        btn_fase1.desenhar()
        btn_fase2.desenhar()
        btn_fase3.desenhar()
        btn_voltar.desenhar()

    pygame.display.flip()
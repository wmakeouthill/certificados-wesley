# Case — Gerador de Crachás (Supermercados Rio Sul)

**Tipo:** Freelance (cliente: Supermercados Rio Sul)
**Papel:** Desenvolvedor (autoria completa)
**Status:** Entregue e em uso
**Stack:** Python (Pillow), servidor de preview HTTP local, PyInstaller (distribuição .exe), HTML/JS (preview interativo)

## Contexto e problema

O RH do supermercado gerava crachás de funcionários manualmente em editor gráfico: posicionar foto, nome e cargo um a um, com resultado inconsistente e horas gastas a cada leva de contratações.

## Solução

Ferramenta de geração de crachás em lote: o RH coloca as fotos em uma pasta, ajusta posições uma única vez em um **preview interativo no navegador** (servidor local que renderiza o layout em tempo real e salva as coordenadas em `positions.json`) e gera todos os crachás padronizados de uma vez.

## Decisões técnicas

- **Distribuição como executável Windows (PyInstaller)** com script de build (`criar_exe.bat`) — o cliente não precisa ter Python instalado; incluí também roteiro "como usar sem Python"
- **Configuração visual, não por código**: preview HTML com ajuste de posições persistido em JSON — o RH calibra o template sozinho quando o layout do crachá muda
- **Processamento em lote com Pillow**: fotos normalizadas e compostas sobre o template com tipografia consistente

## Resultados e impacto

- Geração de crachás caiu de tarefa manual por funcionário para processamento em lote de uma pasta inteira
- Ferramenta autônoma para usuário não-técnico: sem instalação, sem dependências, calibração visual

## Destaques para entrevista (STAR resumido)

- **S/T:** RH gastava horas montando crachás um a um em editor gráfico. **A:** entreguei ferramenta Python empacotada em .exe com preview interativo no navegador para calibrar o layout e geração em lote. **R:** processo reduzido a "colocar fotos na pasta e clicar", operável por usuário sem conhecimento técnico.

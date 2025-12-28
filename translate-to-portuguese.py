#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para traduzir arquivos HTML do repositorio ferramentas-html de Chinês para Português (Brasil)
Uso: python translate-to-portuguese.py
"""

import os
import re

# Dicionário de traduções
translations = {
    # Metadados e títulos
    'lang="zh-CN"': 'lang="pt-BR"',
    'JustHTMLs - 开源 HTML 工具集': 'Ferramentas HTML - Código Aberto',
    '开源 HTML 工具集平台': 'Plataforma de Ferramentas HTML de Código Aberto',
    '轻量级 HTML 工具集合': 'Conjunto Leve de Ferramentas HTML',
    
    # Interface
    '工具数量': 'Ferramentas',
    '分类数量': 'Categorias',
    '今日 PV/UV': 'PV/UV Hoje',
    '总 PV/UV': 'Total PV/UV',
    '开源免费': '100% Código Aberto',
    
    # Botões e ações
    '问题反馈': 'Feedback',
    '工具排行': 'Ranking de Ferramentas',
    '提交需求': 'Sugerir Ferramenta',
    '贡献工具': 'Contribuir Ferramenta',
    '搜索工具名称、描述或标签...': 'Buscar ferramentas por nome, descrição ou tags...',
    '全部': 'Todas',
    '工具列表': 'Lista de Ferramentas',
    '加载中...': 'Carregando...',
    '加载工具列表...': 'Carregando lista de ferramentas...',
    '加载工具列表失败，请刷新页面重试。': 'Falha ao carregar ferramentas, por favor atualize a página.',
    '共': 'Total',
    '个工具': 'ferramentas',
    '未找到匹配的工具': 'Nenhuma ferramenta encontrada',
    '更新时间：新 → 旧': 'Atualizado: Novo → Antigo',
    '更新时间：旧 → 新': 'Atualizado: Antigo → Novo',
    
    # Rodapé
    '关于 JustHTMLs': 'Sobre Ferramentas HTML',
    '快速链接': 'Links Rápidos',
    '设计理念': 'Filosofia de Design',
    '设计文档': 'Documentação de Design',
    '单文件 HTML，内联 CSS/JS': 'HTML de Arquivo Único, CSS/JS Integrado',
    '无需构建，复制即用': 'Sem Build, Copiar e Usar',
    '数据本地处理，保护隐私': 'Processamento Local, Privacidade Protegida',
    '贡献指南': 'Guia de Contribuição',
    '报告问题': 'Reportar Problema',
    'GitHub 组织': 'Organização GitHub',
    '网站仓库': 'Repositório do Site',
    '© 2025 JustHTMLs. 基于 MIT 许可证开源。': '© 2025 Ferramentas HTML. Código Aberto sob Licença MIT.',
}

def translate_file(filepath):
    """Traduz um arquivo HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for chinese, portuguese in translations.items():
        content = content.replace(chinese, portuguese)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Traduz todos os arquivos HTML"""
    html_files = ['index.html', 'reference.html', 'tools-rank.html']
    
    print('Traduzindo arquivos HTML para Português (Brasil)...')
    
    for filename in html_files:
        if os.path.exists(filename):
            if translate_file(filename):
                print(f'✓ {filename} traduzido com sucesso')
            else:
                print(f'- {filename} já estava em português')
        else:
            print(f'✗ {filename} não encontrado')
    
    print('\nTraduçãoconcluída!')
    print('Não esqueça de fazer commit e push das mudanças:')
    print('  git add .')
    print('  git commit -m "Traduzir HTML para português (PT-BR)"')
    print('  git push')

if __name__ == '__main__':
    main()

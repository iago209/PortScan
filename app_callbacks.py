import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from data_manipulation import*

# Estilos para os botões Obs: migrar para o arquivo styles.css
botao_estilo = {
    'margin-right': '10px',
    'padding': '8px 16px',
    'border-radius': '5px',
    'font-size': '14px'
}

def register_callbacks(app):
    @app.callback(
        Output('tabs-content', 'children'),
        [Input('tabs', 'value')]
    )
    def render_content(tab):
        if tab == 'tab-vdc-sesup':
            return html.Div([
                # Estrutura para a primeira aba (VDC - SESUP)
                dcc.Tabs(id='sub-tabs-vdc-sesup', value='sub-tab-dmz192', children=[
                    dcc.Tab(label='DMZ - REDE 192', value='sub-tab-dmz192'),
                    dcc.Tab(label='DMZ - REDE 141', value='sub-tab-dmz141'),
                    dcc.Tab(label='PESQUISA - REDE 149', value='sub-tab-pesquisa'),
                    dcc.Tab(label='HPC - REDE 223', value='sub-tab-hpc223'),
                    dcc.Tab(label='HPC - REDE 222', value='sub-tab-hpc222'),
                    dcc.Tab(label='OPERACIONAL - REDE 147', value='sub-tab-operacional'),
                ]),
                html.Div(id='sub-tabs-content-vdc-sesup')
            ])
        elif tab == 'tab-vdc-coids':
            return html.Div([
                # Estrutura para a segunda aba (VDC - COIDS)
                dcc.Tabs(id='sub-tabs-vdc-coids', value='sub-tab-dmz', children=[
                    dcc.Tab(label='DMZ - REDE 218', value='sub-tab-dmz'),
                    dcc.Tab(label='PESQUISA - REDE 214', value='sub-tab-pesquisa'),
                    dcc.Tab(label='HPC - REDE 216', value='sub-tab-hpc'),
                    dcc.Tab(label='OPERACIONAL - REDE 212', value='sub-tab-operacional'),
                ]),
                html.Div(id='sub-tabs-content-vdc-coids')
            ])
        
        return ''
    '''
    O bloco de código a seguir define uma função de retorno de chamada (callback) que atualiza o conteúdo exibido em uma Div 
    com o identificador 'sub-tabs-content-vdc-sesup' ou 'sub-tabs-content-vdc-coids' 
    com base no valor selecionado em uma barra de abas.
    '''
    # VDC - SESUP

    @app.callback(
        Output('sub-tabs-content-vdc-sesup', 'children'),
        [Input('sub-tabs-vdc-sesup', 'value')]
    )
    def render_sub_content_vdc_sesup(sub_tab):
        if sub_tab == 'sub-tab-dmz192':
            # Calcula o número de hosts com portas abertas e fechadas
            num_hosts_com_portas_dmz192 = len(df_dmz_192_sesup[df_dmz_192_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_dmz192 = len(df_dmz_192_sesup[df_dmz_192_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            # Cria o gráfico de pizza
            labels_dmz192 = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_dmz192 = [num_hosts_com_portas_dmz192, num_hosts_sem_portas_dmz192]
            fig_pizza_dmz192 = go.Figure(data=[go.Pie(labels=labels_dmz192, values=values_dmz192)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_dmz192, id='grafico-pizza-dmz192'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-dmz192', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-dmz192', style=botao_estilo),
                    dcc.Input(id='input-filtro-dmz192', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-dmz192')
                ])
            ])
        
        elif sub_tab == 'sub-tab-dmz141':
    
            num_hosts_com_portas_dmz141 = len(df_dmz_141_sesup[df_dmz_141_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_dmz141 = len(df_dmz_141_sesup[df_dmz_141_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_dmz141 = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_dmz141 = [num_hosts_com_portas_dmz141, num_hosts_sem_portas_dmz141]
            fig_pizza_dmz141 = go.Figure(data=[go.Pie(labels=labels_dmz141, values=values_dmz141)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_dmz141, id='grafico-pizza-dmz141'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-dmz141', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-dmz141', style=botao_estilo),
                    dcc.Input(id='input-filtro-dmz141', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-dmz141')
                ])
            ])
            
        elif sub_tab == 'sub-tab-pesquisa':
            
            num_hosts_com_portas_pesquisa = len(df_pesquisa_sesup[df_pesquisa_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_pesquisa = len(df_pesquisa_sesup[df_pesquisa_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_pesquisa = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_pesquisa = [num_hosts_com_portas_pesquisa, num_hosts_sem_portas_pesquisa]
            fig_pizza_pesquisa = go.Figure(data=[go.Pie(labels=labels_pesquisa, values=values_pesquisa)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_pesquisa, id='grafico-pizza-pesquisa'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-pesquisa', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-pesquisa', style=botao_estilo),
                    dcc.Input(id='input-filtro-pesquisa', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-pesquisa')
                ])
            ])

        elif sub_tab == 'sub-tab-operacional':

            num_hosts_com_portas_operacional = len(df_operacional_sesup[df_operacional_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_operacional = len(df_operacional_sesup[df_operacional_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_operacional = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_operacional = [num_hosts_com_portas_operacional, num_hosts_sem_portas_operacional]
            fig_pizza_operacional = go.Figure(data=[go.Pie(labels=labels_operacional, values=values_operacional)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_operacional, id='grafico-pizza-operacional'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-operacional', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-operacional', style=botao_estilo),
                    dcc.Input(id='input-filtro-operacional', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-operacional')
                ])
            ])
        
        return ''
    '''  
Os próximos blocos de códigos definem uma função de retorno de chamada (callback) para atualizar os conteúdos exibidos em cada uma das div
com o identificadores, exemplo: 'tabela-container-dmz192' com base em interações do usuário. 
Ele responde a três eventos de entrada: cliques nos botões 'botao-tabela1-dmz192' e 'botao-tabela2-dmz192', 
e digitação de texto no campo 'input-filtro-dmz192'
    '''
    @app.callback(
        Output('tabela-container-dmz192', 'children'),
        [Input('botao-tabela1-dmz192', 'n_clicks'),
        Input('botao-tabela2-dmz192', 'n_clicks'),
        Input('input-filtro-dmz192', 'value')]
    )
    def display_table_dmz192(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-dmz192':
            filtered_data = df_dmz_192_sesup[df_dmz_192_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas DMZ REDE-192 SESUP"
        elif button_id == 'botao-tabela2-dmz192':
            filtered_data = df_dmz_192_sesup[df_dmz_192_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas DMZ REDE-192 SESUP"
        else:
            filtered_data = df_dmz_192_sesup
            titulo = "Dados do DataFrame - Todos os Hosts DMZ REDE-192 SESUP"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-dmz192',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    @app.callback(
        Output('tabela-container-dmz141', 'children'),
        [Input('botao-tabela1-dmz141', 'n_clicks'),
        Input('botao-tabela2-dmz141', 'n_clicks'),
        Input('input-filtro-dmz141', 'value')]
    )
    def display_table_dmz141(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-dmz141':
            filtered_data = df_dmz_141_sesup[df_dmz_141_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas DMZ REDE-141 SESUP"
        elif button_id == 'botao-tabela2-dmz141':
            filtered_data = df_dmz_141_sesup[df_dmz_141_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas DMZ REDE-141 SESUP"
        else:
            filtered_data = df_dmz_141_sesup
            titulo = "Dados do DataFrame - Todos os Hosts DMZ REDE-141 SESUP"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-dmz141',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    @app.callback(
        Output('tabela-container-pesquisa', 'children'),
        [Input('botao-tabela1-pesquisa', 'n_clicks'),
        Input('botao-tabela2-pesquisa', 'n_clicks'),
        Input('input-filtro-pesquisa', 'value')]
    )
    def display_table_pesquisa(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-pesquisa':
            filtered_data = df_pesquisa_sesup[df_pesquisa_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas PESQUISA SESUP"
        elif button_id == 'botao-tabela2-pesquisa':
            filtered_data = df_pesquisa_sesup[df_pesquisa_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas PESQUISA SESUP"
        else:
            filtered_data = df_pesquisa_sesup
            titulo = "Dados do DataFrame - Todos os Hosts PESQUISA SESUP"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-pesquisa',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    @app.callback(
        Output('tabela-container-operacional', 'children'),
        [Input('botao-tabela1-operacional', 'n_clicks'),
        Input('botao-tabela2-operacional', 'n_clicks'),
        Input('input-filtro-operacional', 'value')]
    )

    def display_table_operacional(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-operacional':
            filtered_data = df_operacional_sesup[df_operacional_sesup['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas OPERACIONAL SESUP"
        elif button_id == 'botao-tabela2-operacional':
            filtered_data = df_operacional_sesup[df_operacional_sesup['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas OPERACIONAL SESUP"
        else:
            filtered_data = df_operacional_sesup
            titulo = "Dados do DataFrame - Todos os Hosts OPERACIONAL SESUP"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-operacional',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    # VDC - COIDS 

    @app.callback(
        Output('sub-tabs-content-vdc-coids', 'children'),
        [Input('sub-tabs-vdc-coids', 'value')]
    )
    def render_sub_content_vdc_coids(sub_tab):
        if sub_tab == 'sub-tab-dmz':
     
            num_hosts_com_portas_dmz = len(df_dmz_coids[df_dmz_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_dmz = len(df_dmz_coids[df_dmz_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_dmz = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_dmz = [num_hosts_com_portas_dmz, num_hosts_sem_portas_dmz]
            fig_pizza_dmz = go.Figure(data=[go.Pie(labels=labels_dmz, values=values_dmz)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_dmz, id='grafico-pizza-dmz'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-dmz', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-dmz', style=botao_estilo),
                    dcc.Input(id='input-filtro-dmz', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-dmz')
                ])
            ])

        elif sub_tab == 'sub-tab-pesquisa':
            
            num_hosts_com_portas_pesquisa = len(df_pesquisa_coids[df_pesquisa_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_pesquisa = len(df_pesquisa_coids[df_pesquisa_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_pesquisa = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_pesquisa = [num_hosts_com_portas_pesquisa, num_hosts_sem_portas_pesquisa]
            fig_pizza_pesquisa = go.Figure(data=[go.Pie(labels=labels_pesquisa, values=values_pesquisa)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_pesquisa, id='grafico-pizza-pesquisa'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-pesquisa', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-pesquisa', style=botao_estilo),
                    dcc.Input(id='input-filtro-pesquisa', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-pesquisa-coids')
                ])
            ])
            
        elif sub_tab == 'sub-tab-operacional':
           
            num_hosts_com_portas_operacional = len(df_operacional_coids[df_operacional_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada'])
            num_hosts_sem_portas_operacional = len(df_operacional_coids[df_operacional_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada'])

            labels_operacional = ['Com Portas Abertas', 'Sem Portas Abertas']
            values_operacional = [num_hosts_com_portas_operacional, num_hosts_sem_portas_operacional]
            fig_pizza_operacional = go.Figure(data=[go.Pie(labels=labels_operacional, values=values_operacional)])

            return html.Div([
                dcc.Graph(figure=fig_pizza_operacional, id='grafico-pizza-operacional'),
                html.Div([
                    html.Button('Hosts com Portas Abertas', id='botao-tabela1-operacional', style=botao_estilo),
                    html.Button('Hosts com Portas Fechadas', id='botao-tabela2-operacional', style=botao_estilo),
                    dcc.Input(id='input-filtro-operacional', placeholder='Filtrar por Host...', type='text'),
                    html.Div(id='tabela-container-operacional_coids')
                ])
            ])
        
        return ''

    @app.callback(
        Output('tabela-container-dmz', 'children'),
        [Input('botao-tabela1-dmz', 'n_clicks'),
        Input('botao-tabela2-dmz', 'n_clicks'),
        Input('input-filtro-dmz', 'value')]
    )
    def display_table_dmz(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-dmz':
            filtered_data = df_dmz_coids[df_dmz_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas DMZ COIDS"
        elif button_id == 'botao-tabela2-dmz':
            filtered_data = df_dmz_coids[df_dmz_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas DMZ COIDS"
        else:
            filtered_data = df_dmz_coids
            titulo = "Dados do DataFrame - Todos os Hosts DMZ COIDS"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-dmz',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    @app.callback(
        Output('tabela-container-pesquisa-coids', 'children'),
        [Input('botao-tabela1-pesquisa', 'n_clicks'),
        Input('botao-tabela2-pesquisa', 'n_clicks'),
        Input('input-filtro-pesquisa', 'value')]
    )

    def display_table_pesquisa(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-pesquisa':
            filtered_data = df_pesquisa_coids[df_pesquisa_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas PESQUISA COIDS"
        elif button_id == 'botao-tabela2-pesquisa':
            filtered_data = df_pesquisa_coids[df_pesquisa_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas PESQUISA COIDS"
        else:
            filtered_data = df_pesquisa_coids
            titulo = "Dados do DataFrame - Todos os Hosts PESQUISA COIDS"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-pesquisa',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])

    @app.callback(
        Output('tabela-container-operacional_coids', 'children'),
        [Input('botao-tabela1-operacional', 'n_clicks'),
        Input('botao-tabela2-operacional', 'n_clicks'),
        Input('input-filtro-operacional', 'value')]
    )

    def display_table_operacional(n_clicks1, n_clicks2, filtro_host):
        ctx = dash.callback_context
        if not ctx.triggered:
            return ''
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if button_id == 'botao-tabela1-operacional':
            filtered_data = df_operacional_coids[df_operacional_coids['Portas abertas'] != 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Abertas OPERACIONAL COIDS"
        elif button_id == 'botao-tabela2-operacional':
            filtered_data = df_operacional_coids[df_operacional_coids['Portas abertas'] == 'Nenhuma porta aberta encontrada']
            titulo = "Dados do DataFrame - Hosts com Portas Fechadas OPERACIONAL COIDS"
        else:
            filtered_data = df_operacional_coids
            titulo = "Dados do DataFrame - Todos os Hosts OPERACIONAL COIDS"
        
        if filtro_host:
            filtered_data = filtered_data[filtered_data['Host'].str.contains(filtro_host, case=False, na=False)]
        
        return html.Div([
            html.H3(titulo),
            dash_table.DataTable(
                id='tabela-operacional',
                columns=[{'name': col, 'id': col} for col in filtered_data.columns],
                data=filtered_data.to_dict('records'),
                style_table={'className': 'tabela_estilo'},
                filter_action='native',
                page_size=10  
            )
        ])
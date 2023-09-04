'''
Este bloco de código define o layout principal da aplicação Dash. 
Ele cria um componente de guias (Tabs) com duas guias (Tabs) nomeadas 'VDC - SESUP' e 'VDC - COIDS'. 
As guias têm cores de fundo diferentes e texto em branco para personalização visual. 
O conteúdo das guias é definido para ser exibido em uma div com um identificador 'tabs-content'. 
Este layout será retornado e usado para construir a interface do aplicativo Dash.
'''
import dash
from dash import dcc, html
import plotly.graph_objs as go

def criar_layout():
    layout = html.Div([
        dcc.Tabs(id='tabs', value='tab-vdc-sesup', children=[
            #dcc.Tab(label='VDC - SESUP', value='tab-vdc-sesup', style={'className': 'tab-estilo-sesup'}),
            #dcc.Tab(label='VDC - COIDS', value='tab-vdc-coids', style={'className': 'tab-estilo-coids'}),
            dcc.Tab(label='VDC - SESUP', value='tab-vdc-sesup', style={'background-color': '#1976D2', 'color': 'white'}), #Migrar style.css
            dcc.Tab(label='VDC - COIDS', value='tab-vdc-coids', style={'background-color': '#388E3C', 'color': 'white'}), #Migrar style.css
        ]),
        html.Div(id='tabs-content')
    ])
    return layout

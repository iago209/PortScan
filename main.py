'''
Esse bloco de código cria uma aplicação Dash, configura o layout e os callbacks da aplicação,
e inicia o servidor web para executar a aplicação na URL 'http://150.163.190.30:8050/' com depuração ativada.
As linhas comentadas sugerem diferentes maneiras de configurar estilos externos para a aplicação, mas atualmente estão desabilitadas.
'''
import dash
from app.app_layout import criar_layout
from app.app_callbacks import register_callbacks

# Configuração dos estilos externos
#external_stylesheets=['C:\\Users\\Bolsista\\Downloads\\PortScan\\app\\styles.css']

app = dash.Dash(__name__, suppress_callback_exceptions=True)

#app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
#external_stylesheets=['C:/Users/Bolsista/Downloads/PortScan/app/styles.css']
#external_stylesheets=['C:\\Users\\Bolsista\\Downloads\\PortScan\\app\\styles.css']
#external_stylesheets = [r'C:\Users\Bolsista\Downloads\PortScan\app\styles.css']

app.layout = criar_layout()
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(host='150.163.190.30', port=8050, debug=True)
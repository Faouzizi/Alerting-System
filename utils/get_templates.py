###############################################################################################
########### Import python packages
###############################################################################################
from string import Template
import base64

###############################################################################################
############# Build the email content using html
###############################################################################################
def get_html_template(type_alert):
    # Import of time series plots
    data24h_uri = base64.b64encode(open('./plots/plot_24h.png', 'rb').read()).decode('utf-8')
    data48h_uri = base64.b64encode(open('./plots/plot_48h.png', 'rb').read()).decode('utf-8')
    img24h_tag = '<img src="data:image/png;base64,{0}">'.format(data24h_uri)
    img48h_tag = '<img src="data:image/png;base64,{0}" height="auto"> '.format(data48h_uri)
    # Choice of the email color, orange for low sales and blue for high sales
    if type_alert=='Low':
        color = '#F7F8E0'
    else:
        color = '#33E3FF'
    # Html email contents
    message = """
    <!DOCTYPE html>
      <html>
    
        <head>
          <title>Volume Alert</title>
        </head>
    
    
    
        <body  style="background-color: #F7F8E0">
    
    
          <header style="background-color: """+color+"""">
            <h1 >"""+type_alert+""" Sales Volume</h1>
          </header>
    
          <div style="background-color: """+color+""";">
            <br>
            <div style="position: relative; top: 20px; left: 30px;">
              """+img24h_tag+"""
            </div>
            <h2>Last 24 hours</h2>
          </div>
    
    
          <div style="background-color: """+color+""";">
            <br>
            <div style="position: relative; top: 20px; left: 30px;">
              """+img48h_tag+"""
            </div>
            <h2>Last 48 hours</h2>
          </div>
    
    
    
          <footer style="background-color: gray;">
            <p style="text-align: center;">Contact us on : <a href="mailto:haaply.apps@gmail.com">haaply.apps@gmail.com</a></p>
          </footer
        </body>
    
    
    
      </html>
    """
    return(Template(message))

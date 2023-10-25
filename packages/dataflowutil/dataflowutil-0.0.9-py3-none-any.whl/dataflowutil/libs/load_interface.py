from dash import Dash, html, Input, Output, ctx, callback, dcc, State, dependencies, dash_table
import dash_bootstrap_components as dbc
import sys
import yaml
from io import StringIO
import os
import pandas as pd

assets_path = os.getcwd() +'/assets'

class LoadInterface():
    def __init__(self,main):
        self.app = Dash(__name__,external_stylesheets=[dbc.themes.COSMO],suppress_callback_exceptions=True,assets_folder=assets_path)
        self.title_tab_new,self.title_info,self.markdown= {},{},{}
        self.icon_theme = None
        self.color_theme = None
        self.title_general = None
        self.color_df_header = None
        
        self.main = main
        
        self.df = None

        self.loading_df()

        self.app.callback([dependencies.Output('console-output', 'children'),dependencies.Output('df_edit','data'),],
              dependencies.Input('run_process', 'n_clicks'),State('tabs-inline', 'value'),State('df_edit', 'data'),
                State('df_edit', 'columns'))(self.run_process_button)

        self.app.callback(dependencies.Output('tabs-example-content-1', 'children'),
              dependencies.Input('tabs-inline', 'value'))(self.render_content)
    

    def loading_df(self):
        self.df = pd.DataFrame(self.main.get_app().get_load_data_sheet()).T.reset_index()
        self.df.rename(columns={"index":"tags / db_name"},inplace=True)
        self.df = self.df[["tags / db_name","update_bucket","update_bigquery"]]
        self.df["update_bucket"] =  self.df["update_bucket"].astype(int)
        self.df["update_bigquery"] =  self.df["update_bigquery"].astype(int)

    def reloading_df(self):
        self.main.get_app().reload_data_sheet()
        self.loading_df()

    def load_interface(self,yaml_archive):
        with open(yaml_archive, 'r') as file:
            load_yml = yaml.safe_load(file)
        
        self.title_tab_new,self.title_info,self.markdown= {},{},{}
        self.icon_theme = None
        self.color_theme = None
        self.title_general = None
        self.color_df_header = None

        for key,value in load_yml.items():
            if "config_general" in  key:
                self.title_general = value["title_general"]
                self.icon_theme = value["icon"]
                self.color_theme = value["color"]
                self.color_df_header = value["color_header_df"]
            else:
                self.title_tab_new[key] = value["title_tab_new"]
                self.title_info[key] = value["title_info"]
                self.markdown[key] = value["descrip_tab_page"]


        self.load_process()

    def load_process(self):
        tabs_styles = {
            'height': '44px'
        }

        tab_style = {
            'padding': '10px',
            'fontWeight': 'bold',
            "color":"#9E9E9E",
        }

        tab_selected_style = {
            'borderBottom': f'3px solid {self.color_theme}',
            'padding': '10px',
            'fontWeight': 'bold',
            "background": "white",
            "color": f"{self.color_theme}",
        }


        elements_tab = [
            dcc.Tab(label=f'{value}', value=f'{key}', style=tab_style, selected_style=tab_selected_style)
            for key,value in self.title_tab_new.items()
        ]
        
        self.app.layout = dbc.Container([

            dbc.Row(
                [
                    dbc.Col(html.Img(src=self.app.get_asset_url(self.icon_theme),style={"width":"65px","margin-left":"20px"}), width=3,style={"background-color": self.color_theme,"padding": "17px"}),
                    dbc.Col(
                        html.H1(self.title_general,style={"color":"white","margin-left":"20px"}
                    ), width=9,style={"background-color": self.color_theme,"padding": "15px"})
                ],
            ),

            dcc.Tabs(id='tabs-inline', value=list(self.title_tab_new.keys())[0], children=elements_tab,style=tabs_styles,colors={
                "background": "white"
            }),
            
            html.Div(style={'margin': '40px'}),
            html.Div(id='tabs-example-content-1'),
            dcc.Loading(
                    id="loading-output",
                    type="circle",  # También puedes probar con "default", "circle", "dot", "default", "pacman"
                    children=[html.Div(id="console-output",style={'textAlign': 'center'})],fullscreen=True,
                ) ,
            
        ],fluid=True)


    def render_content(self,tab):
        get_title = self.title_info[tab]

        df_graph = None

        className="d-grid gap-3 col-8 mx-auto"


        if tab in list(self.title_tab_new.keys())[0]:
            df_graph = dbc.Col(
                        dash_table.DataTable(self.df.to_dict('records'), [{"name": i, "id": i} for i in self.df.columns],
                                    id='df_edit',
                                    editable=True,
                                    page_current= 0,
                                    style_table={'width': '100%', 'overflowX': 'auto'},
                                    style_cell={'height': 'auto', 'font_family': 'Georgia','whiteSpace': 'normal','border': '1px solid grey',"color":"#232323",'textAlign': 'center'},
                                    style_header={'height': 'auto','fontWeight': 'bold',"background-color":self.color_df_header,'border': '1px solid grey','textAlign': 'center'},
                                    style_data={'height': 'auto','whiteSpace': 'normal','lineHeight': '15px'},
                                    page_size= 9),
                    width=8,style={"padding": "15px", "display":"block"})

            className="d-grid gap-3 col-10 mx-auto"


            descrip = dbc.Col(
                        dbc.Row(
                        [
                            dbc.Col( dcc.Markdown(self.markdown[tab]) ,width= 12,className="d-flex justify-content-center"),
                            dbc.Col( dbc.Button("Run Process",id="run_process", style={"background-color":"00377b"}),width= 12,className="d-flex justify-content-center"),
                        ])
           , width=4,style={"padding": "17px", "display":"block"})
        else:

            df_graph = dbc.Col(
                        dash_table.DataTable(self.df.to_dict('records'), [{"name": i, "id": i} for i in self.df.columns],
                                    id='df_edit',
                                    editable=True,
                                    page_current= 0,
                                    #style_table={'width': '100%', 'overflowX': 'auto'},
                                    #style_cell={'height': 'auto', 'whiteSpace': 'normal'},
                                    #style_header={'height': 'auto'},
                                    #style_data={'height': 'auto','whiteSpace': 'normal','lineHeight': '15px'},

                                    style_table={'width': '100%', 'overflowX': 'auto'},
                                    style_cell={'height': 'auto', 'font_family': 'Georgia','whiteSpace': 'normal','border': '1px solid grey',"color":"#232323",'textAlign': 'center'},
                                    style_header={'height': 'auto','fontWeight': 'bold',"background-color":self.color_df_header,'border': '1px solid grey','textAlign': 'center'},
                                    style_data={'height': 'auto','whiteSpace': 'normal','lineHeight': '15px'},



                                    page_size= 9),
                    width=8,style={"padding": "15px","display":"None"})

            className="d-grid gap-3 col-8 mx-auto"
            
            descrip = dbc.Col(
                        dbc.Row(
                        [
                            dbc.Col( dcc.Markdown(self.markdown[tab]) ,width= 12,className="d-flex justify-content-center"),
                            dbc.Col( dbc.Button("Run Process",id="run_process", style={"background-color":"00377b"}),width= 12,className="d-flex justify-content-center"),
                        ])
            , width=12,style={"padding": "17px","display":"block"})
            

        
        get_render =  html.Div([

            dbc.Row(
            [
                html.H1(get_title, style={'textAlign': 'center'}),
                html.Div(style={'margin': '7px'}),


                descrip,

                df_graph,

            ]),
            
        ],className=className)


        return get_render

    def run_process_button(self,n_clicks,state,rows,columns):
        if n_clicks is not None:
            # Redirect stdout to a variable
            sys.stdout = mystdout = StringIO()

            if state in list(self.title_tab_new.keys())[0]:
                df_new = pd.DataFrame(rows, columns=[c['name'] for c in columns])
                df_new["update_bucket"] =  df_new["update_bucket"].astype(int)
                df_new["update_bigquery"] =  df_new["update_bigquery"].astype(int)

                comparacion_bucket = df_new['update_bucket'].eq(self.df['update_bucket'])
                comparacion_bigquery = df_new['update_bigquery'].eq(self.df['update_bigquery'])

                index_bucket = comparacion_bucket.index[~comparacion_bucket].tolist()
                values_bucket = df_new.loc[index_bucket,"update_bucket"]

                index_bigquery = comparacion_bigquery.index[~comparacion_bigquery].tolist()
                values_bigquery = df_new.loc[index_bigquery,"update_bigquery"]

                for idx, value in zip(index_bucket, values_bucket):
                    self.main.get_app().upload_spreadsheets("10R6KIbBS3Z-wedIoo5I_C1cLG3MxKRzRwX-0erZAIvE","CONFIG_DATA",f"F{idx+2}",value)
        
                for idx, value in zip(index_bigquery, values_bigquery):
                    self.main.get_app().upload_spreadsheets("10R6KIbBS3Z-wedIoo5I_C1cLG3MxKRzRwX-0erZAIvE","CONFIG_DATA",f"G{idx+2}",value)

                #self.df["update_bucket"] = df_new["update_bucket"]
                #self.df["update_bigquery"] = df_new["update_bigquery"]

            self.main.load(state)

            # Get the output
            sys.stdout = sys.__stdout__
            output = mystdout.getvalue()
            
            self.reloading_df()
            return (html.Pre(output),self.df.to_dict("records"))
        else:
            return(html.Pre(""),self.df.to_dict('records'))
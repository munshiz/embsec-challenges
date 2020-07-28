def define_color_blocks():
    
    style = """
    <style>
        div.intro { 
            background-color: #e3f5ff; 
            border-color: #dFb5b4; 
            border-bottom: 5px solid rgb(2,48,79); 
            border-top: 12px solid rgb(2,48,79); 
            padding: 0.5em;
        }
        </style>
    <style>
        div.first_level { 
            background-color: rgb(2,48,79); 
            border-color: #dFb5b4; 
            border-bottom: 5px solid rgb(232,200,93); 
            border-top: 12px solid rgb(232,200,93); 
            padding: 0.5em;
        }
    </style>
     <style>
        div.third_level { 
            background-color: #e3f5ff; 
            border-color: #dFb5b4; 
            border-bottom: 0px solid rgb(232,200,93); 
            border-top: 0px solid rgb(2,48,79); 
            padding: 0.5em;
        }
    </style>
    """
    return style
